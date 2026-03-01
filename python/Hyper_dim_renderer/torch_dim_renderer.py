from math import sin, cos, sqrt
import torch, pygame, moderngl, numpy

def find_edges(points):
    diff_pos = points.unsqueeze(1) != points.unsqueeze(0)
    diff_counts = diff_pos.sum(dim = 2)
    edge_mat = torch.triu(diff_counts == 1)
    edge_idx = torch.nonzero(edge_mat)
    return edge_idx

def fast_find_edges(dim):
    edges = []
    n_points = 2**dim
    for x in range(n_points):
        for bit in range(dim):
            y = x ^ (1 << bit)
            if x < y:
                edges.append((x, y))
    return edges

def project_to_2d(points, camera_distance=None):
    projected = points.clone()

    if camera_distance is None:
        camera_distance = sqrt(points.shape[1]) + 1.0

    while projected.shape[1] > 2:
        z = projected[:, -1:] 
        scale = camera_distance / (camera_distance - z)
        projected = projected[:, :-1] * scale
        max_val = torch.max(torch.abs(projected))
        projected /= max_val
    return projected

def create_master(dim, angle, device):
    rot_mats = []
    for x in range(dim):
        angle *= 1 + (1 / (x + 1))
        c = cos(angle)
        s = sin(angle)
        for y in range(x + 1, dim):
            current = torch.eye(dim)
            current[x, x] = c
            current[x, y] = s
            current[y, x] = -s
            current[y, y] = c
            rot_mats.append(current)
    return torch.linalg.multi_dot(rot_mats).to(device)
        


pygame.init()


dim = 7

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Running on: {device}")


screen_width, screen_height = 800, 600
screen_center = torch.tensor([screen_width / 2, screen_height / 2]).to(device)
screen = pygame.display.set_mode((screen_width, screen_height), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption(f"{dim}D Hardware-Accelerated Engine")
clock = pygame.time.Clock()

ctx = moderngl.create_context()

shader_program = ctx.program(
    vertex_shader = f'''
        #version 330
        in vec2 in_position;
        void main() {{
            gl_Position = vec4(in_position.x * {(screen_height / screen_width)}, in_position.y, 0.0, 1.0);
        }}
    ''',
    fragment_shader = f'''
        #version 330
        out vec4 fragColor;
        void main() {{
            fragColor = vec4(1.0, 1.0, 1.0, 1.0); // Cyan color (R, G, B, Alpha)
        }}
    '''
)

scale = 250
values = torch.tensor([-1.0, 1.0])
base_points = torch.cartesian_prod(*[values for _ in range(dim)]).to(device)
rot_points = base_points.clone()
#edges = find_edges(base_points)
edges = fast_find_edges(dim)
angle = 0
angle_diff = 0.05 / dim**1.5
master_mat = create_master(dim, angle, device)

edge_data = numpy.array(edges, dtype='i4').tobytes()
ibo = ctx.buffer(edge_data)
vbo = ctx.buffer(reserve=len(base_points) * 2 * 4, dynamic=True)
vao = ctx.vertex_array(shader_program, [(vbo, '2f', 'in_position')], index_buffer=ibo)

print(f"{len(base_points)} Vertices, {len(edges)} Edges.")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    master_mat = create_master(dim, angle, device)
    rot_points = (base_points @ master_mat)
    projected_2d = project_to_2d(rot_points)
    vertex_bytes = projected_2d.cpu().numpy().astype('f4').tobytes()

    vbo.write(vertex_bytes)
    ctx.clear(0.04, 0.04, 0.06)
    vao.render(moderngl.LINES)

    pygame.display.flip()
    clock.tick(60)

    angle += angle_diff
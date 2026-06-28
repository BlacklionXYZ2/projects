import pygame
import moderngl
import numpy as np

pygame.init()
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)

ctx = moderngl.create_context()

vertex_shader = """
#version 330
in vec2 in_vert;
void main() {
    gl_Position = vec4(in_vert, 0.0, 1.0);
}
"""
fragment_shader = """
#version 330
out vec4 f_color;
void main() {
    f_color = vec4(1.0, 0.5, 0.2, 1.0);
}
"""
prog = ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

vertices = np.array([0.0, 0.8, -0.6, -0.8, 0.6, -0.8], dtype='f4')
vbo = ctx.buffer(vertices.tobytes())
vao = ctx.vertex_array(prog, [(vbo, '2f', 'in_vert')])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ctx.clear(0.1, 0.1, 0.1)
    vao.render()
    pygame.display.flip()

pygame.quit()
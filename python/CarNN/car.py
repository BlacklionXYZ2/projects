import numpy as np
rng = np.random.default_rng()
screenx = 1000
screeny = 1000
center = np.array([int(screenx/2), int(screeny/2)])
r = np.array([int(screenx/4), int(screeny/4)])

class carNN:
    def __init__(self, n_iters, shape, save_path = 'python/CarNN/save.txt'):
        self.w1 = np.random.randn(n_iters, shape[1], 64) * np.sqrt(1.0 / shape[1])
        self.b1 = np.zeros((n_iters, 1, 64)) + 0.01
        self.w2 = np.random.randn(n_iters, 64, 4) * np.sqrt(2.0 / (64 + 4))
        self.b2 = np.zeros((n_iters, 1, 4)) + 0.01
        self.save_path = save_path

    def load_weights(self):
        with open(self.save_path, 'r') as file:
            params = file.read.split('\n')
            self.w1 = params[0]
            self.b1 = params[1]
            self.w2 = params[2]
            self.b2 = params[3]
            file.close()

    def save_weights(self):
        with open(self.save_path, 'w') as file:
            file = f'{self.w1}\n{self.b1}\n{self.w2}\n{self.b2}'
            file.close()

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    
    def forward_pass(self, x):
        mask_dead = self.is_alive == 1
        living = x[mask_dead]
        if living.shape[0] == 0:
            return np.zeros((x.shape[0], self.w2.shape[2]))
        
        z1 = (living.reshape((50, 1, 6)) @ self.w1) + self.b1 # 1st layer
        a1 = np.tanh(z1)
        z2 = (a1 @ self.w2) + self.b2 # 2nd layer

        out = self.sigmoid(z2)
        output = np.zeros((x.shape[0], self.w2.shape[2]))
        output[mask_dead] = out.squeeze()
        return self.sigmoid(z2) # output


class car(carNN):
    def __init__(self, n_iters, start_pos = center):
        self.att_mat = np.zeros((n_iters, 6, 1))
        self.pop_size = n_iters
        super().__init__(n_iters, self.att_mat.shape)

        self.start_pos = np.array(start_pos)
        self.pos = self.start_pos.copy()
        self.pos = np.tile(self.pos, (50, 1))
        self.vel = np.zeros((n_iters, 2))
        self.force = np.zeros(n_iters)
        self.angle = np.zeros(n_iters)
        self.is_alive = np.ones(n_iters)
        self.col = (255, 0, 0)

        self.scores = np.zeros(n_iters)
        self.acc_score = np.zeros(n_iters)
        self.vel_score = np.zeros(n_iters)

        self.controls = {'w': self.att_mat[:, 0], 's': self.att_mat[:, 1], 'a': self.att_mat[:, 2], 'd': self.att_mat[:, 3]}


    def forward(self):
        controls = self.forward_pass(self.att_mat) # calculate new controls
        controls = controls.squeeze()
        self.controls['w'] = controls[:, 0]
        self.controls['s'] = controls[:, 1]
        self.controls['a'] = controls[:, 2]
        self.controls['d'] = controls[:, 3]

        mask_vel = self.controls['w'] + self.controls['s'] == 2
        self.controls['w'][mask_vel] = 0
        self.controls['s'][mask_vel] = 0

        mask_vel = self.controls['a'] + self.controls['d'] == 2
        self.controls['a'][mask_vel] = 0
        self.controls['d'][mask_vel] = 0


    def update_scores(self, center):
        dist_from_track = np.abs(np.linalg.norm(self.pos - center) / np.linalg.norm(1.25 * center))
        self.acc_score += np.clip(1 - dist_from_track, 0, 1)

        speeds = np.sum(self.vel, axis = 1)
        non_zero_speeds = speeds > 0
        max_speed = np.max(speeds)
        if max_speed > 0:
            self.vel_score[non_zero_speeds] += speeds[non_zero_speeds] / np.max(speeds)

    
    def update_pos(self, dt):
        angle = np.radians(self.angle)
        cosine, sine = np.cos(angle), np.sin(angle)

        self.vel[:, 0] += self.force * 5 * cosine * dt
        self.vel[:, 1] += self.force * 5 * sine * dt
        self.vel -= self.vel * 0.15 * dt

        self.pos += self.vel.reshape(-1, 2) * dt
        

    def find_best(self):
        self.scores = self.acc_score + self.vel_score
        threshold = np.quantile(self.scores, 0.9)
        indexes = np.where(self.scores > threshold)
        
        return list(self.w1[indexes])
    

    def cross_and_mutate(self):
        parentA, parentB = self.w1[rng.integers(0, self.pop_size)], self.w1[rng.integers(0, self.pop_size)]

        cross_mask = np.random.rand(*parentA.shape) > 0.5
        child_w1 = np.empty_like(parentA)
        child_w1[cross_mask] = parentA[cross_mask]
        child_w1[~cross_mask] = parentB[~cross_mask]

        mutation_rate = 0.05
        mutation_strength = 0.1
        mutation_mask = np.random.rand(*child_w1.shape) < mutation_rate
        noise = np.random.randn(*child_w1.shape) * mutation_strength
        child_w1[mutation_mask] += noise[mutation_mask]
        return child_w1
    

    def reset_atts(self):
        self.pos[:] = self.start_pos
        self.vel[:] = 0
        self.force[:] = 0
        self.angle[:] = 0
        self.is_alive[:] = 1
        self.scores[:] = 0
        self.acc_score[:] = 0
        self.vel_score[:] = 0


    def next_generation(self):
        best = self.find_best() # the top 10% of the population is passed unaffected into the next generation
        new = list(self.cross_and_mutate() for _ in range(int(self.pop_size * 0.9)))
        self.w1 = np.concatenate((best, new), axis = 0)


    def check_alive(self):
        pos_mask_min = np.abs(self.pos) < np.min(r)
        pos_mask_max = np.abs(self.pos) > np.min(center)
        self.alive[pos_mask_min] = 0
        self.alive[pos_mask_max] = 0
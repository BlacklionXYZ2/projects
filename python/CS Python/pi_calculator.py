import pygame, time, threading
from decimal import Decimal, getcontext

thread_speed = 10
screen_speed = 240


class ChudnovskyState:
    def __init__(self, max_digits):
        self.max_digits = max_digits
        
        self.C = 426880 * Decimal(10005).sqrt()
        self.K = 6
        self.M = 1
        self.X = 1
        self.L = 13591409
        self.S = Decimal(13591409)
        self.i = 1 
        self.current_pi_str = str(self.C / self.S)[:-2]

        self.is_playing = True
        self.app_running = True

        self.math_thread = threading.Thread(target=self._calculation_loop, daemon=True)
        self.math_thread.start()

    def _calculation_loop(self):
        getcontext().prec = self.max_digits + 2

        thread_clock = pygame.time.Clock()

        while self.app_running:
            if self.is_playing and (self.i * 14) <= self.max_digits:
                self._step_math()
            else:
                time.sleep(0.05)
            thread_clock.tick(thread_speed)

    def _step_math(self):
        self.M = (self.K ** 3 - 16 * self.K) * self.M // self.i ** 3 
        self.L += 545140134
        self.X *= -262537412640768000
        self.S += Decimal(self.M * self.L) / self.X
        self.K += 12
        self.i += 1
        self.current_pi_str = str(self.C / self.S)[:-2]

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pi Calculator")

font = pygame.font.SysFont("consolas", 18)
status_font = pygame.font.SysFont("consolas", 24, bold=True)

bg_color = (30, 30, 30)
text_color = (0, 255, 100)
pause_color = (255, 50, 50)
header_bg_color = (20, 20, 20)

MAX_LIMIT = 10000
pi_state = ChudnovskyState(MAX_LIMIT)

clock = pygame.time.Clock()
scroll_y = 0

while pi_state.app_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pi_state.app_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pi_state.is_playing = not pi_state.is_playing
        elif event.type == pygame.MOUSEWHEEL:
            scroll_y += event.y * 30

    if scroll_y > 0:
        scroll_y = 0

    screen.fill(bg_color)

    text_canvas = pygame.Surface((WIDTH, HEIGHT - 60))
    text_canvas.fill(bg_color)

    chars_per_line = 75
    line_height = 25

    for row in range(0, len(pi_state.current_pi_str), chars_per_line):
        line_index = row // chars_per_line
        y_pos = 10 + (line_index * line_height) + scroll_y
        
        if y_pos < -30: continue
        if y_pos > text_canvas.get_height(): break
            
        line_text = pi_state.current_pi_str[row:row+chars_per_line]
        text_surface = font.render(line_text, True, text_color)
        text_canvas.blit(text_surface, (20, y_pos))


    #pygame.draw.rect(screen, header_bg_color, (0, 0, WIDTH, 60))
    #pygame.draw.line(screen, text_color, (0, 60), (WIDTH, 60), 2)

    status_text = "CALCULATING..." if pi_state.is_playing else "PAUSED"
    status_color = text_color if pi_state.is_playing else pause_color
    status_surface = status_font.render(f"Status: {status_text} | Iteration: {pi_state.i}", True, status_color)
    screen.blit(status_surface, (20, 20))
    
    chars_per_line = 75
    y_offset = 60
    
    for row in range(0, len(pi_state.current_pi_str), chars_per_line):
        line_text = pi_state.current_pi_str[row:row+chars_per_line]
        text_surface = font.render(line_text, True, text_color)
        screen.blit(text_surface, (20, y_offset))
        y_offset += 25
        
        if y_offset > HEIGHT - 20: 
            break

    screen.blit(text_canvas, (0, 60))
    
    pygame.display.flip()
    
    clock.tick(screen_speed)

pygame.quit()
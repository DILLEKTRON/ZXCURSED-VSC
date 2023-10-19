# import pygame
# import random

# # Инициализация Pygame
# pygame.init()

# # Устанавливаем размеры экрана
# WINDOW_WIDTH = 300
# WINDOW_HEIGHT = 600
# WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# a = 1
# # Определение цветов
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# CYAN = (0, 255, 255)
# MAGENTA = (255, 0, 255)
# YELLOW = (255, 255, 0)
# ORANGE = (255, 165, 0)

# # Создаем матрицу для поля тетриса
# GRID_WIDTH = 10
# GRID_HEIGHT = 20
# GRID = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# # Определение фигур тетриса
# SHAPES = [
#     [[1, 1, 1],
#      [0, 1, 0]],

#     [[1, 1, 0],
#      [0, 1, 1]],

#     [[1, 1],
#      [1, 1]],

#     [[1, 1, 1, 1]],

#     [[1, 1, 1],
#      [1, 0, 0]],
# ]

# SHAPES_COLORS = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE]

# # Определение класса для фигур
# class Shape:
#     def __init__(self, shape_type):
#         self.shape_type = shape_type
#         self.color = random.choice(SHAPES_COLORS)
#         self.rotation = 0
#         self.x = GRID_WIDTH // 2 - len(SHAPES[shape_type][0]) // 2
#         self.y = 0

#     def rotate(self):
#         self.rotation = (self.rotation + 1) % len(SHAPES[self.shape_type])
#         return SHAPES[self.shape_type][self.rotation]

#     def draw(self):
#         shape_matrix = SHAPES[self.shape_type][self.rotation]
#         for i in range(len(shape_matrix)):
#             for j in range(len(shape_matrix[i])):
#                 if shape_matrix[i][j]:
#                     pygame.draw.rect(WINDOW, self.color, (self.x * 30 + j * 30, self.y * 30 + i * 30, 30, 30))

#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy

#     def check_collision(self):
#         shape_matrix = SHAPES[self.shape_type][self.rotation]
#         for i in range(len(shape_matrix)):
#             for j in range(len(a)(shape_matrix[i])):
#                 if shape_matrix[i][j]:
#                     if self.x + j < 0 or self.x + j >= GRID_WIDTH or self.y + i >= GRID_HEIGHT or GRID[self.y + i][self.x + j]:
#                         return True
#         return False

#     def lock(self):
#         shape_matrix = SHAPES[self.shape_type][self.rotation]
#         for i in range(len(shape_matrix)):
#             for j in range(len(shape_matrix[i])):
#                 if shape_matrix[i][j]:
#                     GRID[self.y + i][self.x + j] = 1

# # Создаем фигуру
# current_shape = Shape(random.randint(0, len(SHAPES) - 1))

# # Основной игровой цикл
# clock = pygame.time.Clock()
# run = True
# game_over = False

# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#         if event.type == pygame.KEYDOWN and not game_over:
#             if event.key == pygame.K_LEFT and not current_shape.move(-1, 0) and not current_shape.check_collision():
#                 current_shape.move(-1, 0)
#             elif event.key == pygame.K_RIGHT and not current_shape.move(1, 0) and not current_shape.check_collision():
#                 current_shape.move(1, 0)
#             elif event.key == pygame.K_DOWN:
#                 current_shape.move(0, 1)
#                 if current_shape.check_collision():
#                     current_shape.move(0, -1)
#                     current_shape.lock()
#                     current_shape = Shape(random.randint(0, len(SHAPES) - 1))
#                     if current_shape.check_collision():
#                         game_over = True
#             elif event.key == pygame.K_UP:
#                 rotated_shape = current_shape.rotate()
#                 if not rotated_shape.check_collision():
#                     current_shape.rotation = (current_shape.rotation + 1) % len(SHAPES[current_shape.shape_type])
#                 elif not current_shape.move(-1, 0) and not current_shape.check_collision():
#                     current_shape.move(-1, 0)
#                     current_shape.rotation = (current_shape.rotation + 1) % len(SHAPES[current_shape.shape_type])
#                 elif not current_shape.move(1, 0) and not current_shape.check_collision():
#                     current_shape.move(1, 0)
#                     current_shape.rotation = (current_shape.rotation + 1) % len(SHAPES[current_shape.shape_type])

#     if not game_over:
#         if not current_shape.move(0, 1) and not current_shape.check_collision():
#             current_shape.move(0, 1)
#         else:
#             current_shape.lock()
#             current_shape = Shape(random.randint(0, len(SHAPES) - 1))
#             if current_shape.check_collision():
#                 game_over = True

#     # Отрисовка
#     WINDOW.fill(BLACK)
#     for i in range(GRID_HEIGHT):
#         for j in range(GRID_WIDTH):
#             if GRID[i][j]:
#                 pygame.draw.rect(WINDOW, WHITE, (j * 30, i * 30, 30, 30))
#     current_shape.draw()
#     if game_over:
#         font = pygame.font.Font(None, 36)
#         text_surface = font.render("GAME OVER", True, WHITE)
#         text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
#         WINDOW.blit(text_surface, text_rect)

#     pygame.display.flip()
#     clock.tick(10)

# # Завершение Pygame
# pygame.quit()
















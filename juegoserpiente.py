import pygame
import random
 
pygame.init()
 
# dimensiones de la ventana
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
 
# colores RGB
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
 
# Snake setup
snake_size = 10
snake_speed = 15
snake = [(100, 50), (90, 50), (80, 50)]  # lista de tuples
dx, dy = 10, 0  # variables determinan la posisicon
 
# Manzanas setup
apples_x = random.randint(0, (width - snake_size) // snake_size) * snake_size
apples_y = random.randint(0, (height - snake_size) // snake_size) * snake_size
 
# Ejecucion del juego
running = True  # variable bandera
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Controles usando eventos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -snake_size, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = snake_size, 0
            elif event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -snake_size
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, snake_size
 
    # Movimiento snake
    cabeza = (snake[0][0] + dx, snake[0][1] + dy)
    snake = [cabeza] + snake[:-1]
 
    # Checar colisiones con manzanas
    if cabeza == (apples_x, apples_y):
        snake.append(snake[-1])  # crece la serpiente
        apples_x = random.randint(0, (width - snake_size) // snake_size) * snake_size
        apples_y = random.randint(0, (height - snake_size) // snake_size) * snake_size
 
    # Checar colisiones con nosotros mismos      
    if (
        cabeza[0] < 0 or cabeza[0] >= width
        or cabeza[1] < 0 or cabeza[1] >= height
        or cabeza in snake[1:]
    ):
        running = False  # game over
 
    # Configurar el espacio graficamente
    screen.fill(black)
    for bloque in snake:
        pygame.draw.rect(screen, green, (bloque[0], bloque[1], snake_size, snake_size))
 
    # Dibujar la manzana
    pygame.draw.rect(screen, red, (apples_x, apples_y, snake_size, snake_size))
 
    pygame.display.update()
    clock.tick(snake_speed)
 
pygame.quit()




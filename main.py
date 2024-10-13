import pygame

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la pantalla
screen = pygame.display.set_mode((800, 600))

# Definir colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
FONT_COLOR = (0, 0, 0)

# Cargar el sonido de frenado
brake_sound = pygame.mixer.Sound("brake_sound.wav")

# Definir posiciones iniciales del vehículo y obstáculo
car_x, car_y = 0, 300
obstacle_x, obstacle_y = 600, 300

# Definir velocidad inicial del vehículo
speed = 5

# Definir la velocidad y dirección del obstáculo
obstacle_speed = 2

# Variable para la distancia
distance = 0

# Ejecutar la simulación
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()  # Obtener las teclas presionadas
    if keys[pygame.K_UP]:  # Acelerar
        speed += 0.1
    if keys[pygame.K_DOWN]:  # Frenar
        speed -= 0.1
        brake_sound.play()
        if speed < 0:
            speed = 0

    if keys[pygame.K_r]:  # Reiniciar la simulación
        # Reiniciar las variables
        car_x, car_y = 0, 300
        speed = 5
        obstacle_x = 600  # Reiniciar posición del obstáculo

    # Mover el obstáculo
    obstacle_x -= obstacle_speed
    if obstacle_x < -50:  # Si el obstáculo sale de la pantalla, reiniciarlo
        obstacle_x = 800  # Reiniciar a la derecha

    # Calcular distancia entre el vehículo y el obstáculo
    distance = obstacle_x - car_x

    # Sistema de frenado automático
    if distance < 100:
        speed -= 0.3  # Reducir la velocidad gradualmente
        if speed < 0:
            speed = 0  # Asegurarse de que no sea negativa

    # Mover el vehículo
    car_x += speed

    # Reiniciar la simulación si el vehículo se detiene
    if speed == 0 and distance <= 0:
        car_x = 0  # Reiniciar la posición del vehículo
        speed = 5  # Reiniciar la velocidad

    # Dibujar el fondo, el vehículo y el obstáculo
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (car_x, car_y, 50, 30))  # El vehículo
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, 50, 30))  # El obstáculo

    # Mostrar la velocidad en pantalla
    font = pygame.font.Font(None, 36)
    speed_text = font.render(f'Speed: {speed:.2f}', True, FONT_COLOR)
    screen.blit(speed_text, (10, 10))

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar los FPS
    pygame.time.Clock().tick(30)

# Cerrar Pygame
pygame.quit()
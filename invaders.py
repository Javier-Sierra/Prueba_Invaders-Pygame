import pygame
import random
import math

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Invasores Espaciales")
icon = pygame.image.load("Imagenes/Mando.png")
pygame.display.set_icon(icon)

# Colores
WHITE = (255, 255, 255)

# Estados del juego
MENU = "menu"
PLAYING = "playing"
RUNNING = True
game_state = MENU

# Fuente para el score
font = pygame.font.Font(None, 36)

# Variables del jugador
player_img = pygame.image.load("Imagenes/Nave.png")
player_x, player_y = 400, 500
player_speed = 0.2
player_x_change = 0

# Variables del disparo
gun_img = pygame.image.load("Imagenes/bala.png")
gun_x, gun_y = 0, player_y
gun_y_change = 0.9
gun_state = "ready"

# Fondo
fondo = pygame.image.load("Imagenes/fondo.jpg")

# Variables de enemigos
def generate_enemies(num, speed):
    enemies = []
    for _ in range(num):
        enemies.append({
            "img": pygame.image.load("Imagenes/Alienigena.png"),
            "x": random.randint(0, 835),
            "y": random.randint(50, 150),
            "x_change": speed,
            "y_change": 40
        })
    return enemies

difficulty_levels = {
    "facil": (8, 0.1),
    "medio": (10, 0.2),
    "dificil": (12, 0.3)
}

enemies = []
score = 0
previous_score = 0  # Para controlar cuándo aumentar la velocidad
selected_difficulty = "facil"

# Funciones
def draw_player(x, y):
    screen.blit(player_img, (x, y))

def draw_enemy(enemy):
    screen.blit(enemy["img"], (enemy["x"], enemy["y"]))

def fire_bullet(x, y):
    global gun_state
    gun_state = "fire"
    screen.blit(gun_img, (x + 16, y + 10))

def check_collision(enemy, bullet_x, bullet_y):
    distance = math.sqrt((enemy["x"] - bullet_x) ** 2 + (enemy["y"] - bullet_y) ** 2)
    return distance < 27

def show_menu():
    screen.fill(WHITE)
    screen.blit(fondo, (0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Selecciona una dificultad:", True, (0, 0, 0))
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 3))
    easy_text = font.render("1. Fácil", True, (0, 0, 0))
    medium_text = font.render("2. Medio", True, (0, 0, 0))
    hard_text = font.render("3. Difícil", True, (0, 0, 0))
    screen.blit(easy_text, (WIDTH // 2 - 50, HEIGHT // 2))
    screen.blit(medium_text, (WIDTH // 2 - 50, HEIGHT // 2 + 40))
    screen.blit(hard_text, (WIDTH // 2 - 50, HEIGHT // 2 + 80))
    pygame.display.update()

def reset_game():
    global player_x, player_y, gun_y, gun_state, score, enemies, previous_score
    player_x, player_y = 400, 500
    gun_y = player_y
    gun_state = "ready"
    score = 0
    previous_score = 0
    num_enemies, speed = difficulty_levels[selected_difficulty]
    enemies = generate_enemies(num_enemies, speed)

def show_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Bucle principal
while RUNNING:
    screen.fill((0, 0, 0))
    screen.blit(fondo, (0, 0))
    
    if game_state == MENU:
        show_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_difficulty = "facil"
                elif event.key == pygame.K_2:
                    selected_difficulty = "medio"
                elif event.key == pygame.K_3:
                    selected_difficulty = "dificil"
                reset_game()
                game_state = PLAYING
    
    elif game_state == PLAYING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -player_speed
                elif event.key == pygame.K_RIGHT:
                    player_x_change = player_speed
                elif event.key == pygame.K_SPACE and gun_state == "ready":
                    gun_x = player_x
                    fire_bullet(gun_x, gun_y)
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    player_x_change = 0
        
        player_x += player_x_change
        player_x = max(0, min(player_x, WIDTH - 64))
        
        if gun_state == "fire":
            fire_bullet(gun_x, gun_y)
            gun_y -= gun_y_change
            if gun_y <= 0:
                gun_y = player_y
                gun_state = "ready"
        
        for enemy in enemies:
            enemy["x"] += enemy["x_change"]
            if enemy["x"] <= 0 or enemy["x"] >= WIDTH - 64:
                enemy["x_change"] *= -1
                enemy["y"] += enemy["y_change"]
            if enemy["y"] >= player_y:
                RUNNING = False  # Cierra el juego si un enemigo toca la nave
            if check_collision(enemy, gun_x, gun_y):
                gun_y = player_y
                gun_state = "ready"
                score += 1
                enemy["x"] = random.randint(0, WIDTH - 64)
                enemy["y"] = random.randint(50, 150)
            draw_enemy(enemy)
        
        # Aumentar la velocidad de los enemigos cada 5 puntos 
        if score >= previous_score + 5:
            for enemy in enemies:
                enemy["x_change"] *= 1.1
            previous_score = score  # Actualizar el puntaje de referencia

        draw_player(player_x, player_y)
        show_score()  # Mostrar el puntaje
    
    pygame.display.update()

pygame.quit()

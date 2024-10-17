import pygame
import random

# Inicializar PyGame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroides")

# Configuración de reloj
clock = pygame.time.Clock()

# Clase Jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/cohete.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -5
        if keys[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x

        # Limitar movimiento a la pantalla
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# Clase Enemigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/asteroide_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed_y = random.randint(3, 6)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed_y = random.randint(3, 6)

# Función para mostrar menú

title = "¡Lluvia de asteroides!"
press_key = "Presiona cualquier tecla para comenzar."

def show_menu():
    font = pygame.font.Font(None, 74)
    title_ = font.render(title, True, WHITE)
    title_rect = title_.get_rect(center=(WIDTH // 2, 250))
    font_small = pygame.font.Font(None, 36)
    press_k = font_small.render(press_key, True, WHITE)
    press_k_rect = press_k.get_rect(center=(WIDTH // 2, 320))
    screen.fill(BLACK)
    screen.blit(title_, title_rect)
    screen.blit(press_k, press_k_rect)
    pygame.display.flip()
    wait_for_key()

# Función para esperar una tecla
def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

# Configurar el juego
def game():
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    for i in range(8):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar sprites
        all_sprites.update()

        # Verificar colisiones
        if pygame.sprite.spritecollide(player, enemies, False):
            running = False

        # Dibujar todo
        screen.fill(BLACK)
        all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()

# Llamar al menú y al juego
show_menu()
game()

import pygame
import random
import numpy as np

# --- Parâmetros da Simulação ---
GRID_SIZE = 100  # Tamanho da grade (GRID_SIZE x GRID_SIZE)
CELL_SIZE = 8    # Tamanho de cada célula em pixels

# Cores
COLOR_BACKGROUND = (25, 25, 25)
COLOR_SUSCEPTIVEL = (50, 150, 250)  # Azul
COLOR_EXPOSTO = (255, 165, 0)       # Laranja
COLOR_INFECTADO = (255, 0, 0)       # Vermelho
COLOR_RECUPERADO = (0, 200, 0)      # Verde

# Estados
SUSCETIVEL = 0
EXPOSTO = 1
INFECTADO = 2
RECUPERADO = 3

# Parâmetros Epidemiológicos
# As probabilidades devem ser ajustadas para o passo de tempo da simulação (1 frame = 1 passo de tempo)
# Esses valores são as chance por passo de tempo.
BETA = 0.15   # Probabilidade de transmissão (contato Suscetível-Infectado)
SIGMA = 0.05  # Probabilidade de um Exposto se tornar Infectado (1/período_latente)
GAMMA = 0.02  # Probabilidade de um Infectado se Recuperar (1/período_infeccioso)

INITIAL_INFECTED_COUNT = 1 # Número inicial de indivíduos infectados

# --- Setup Pygame ---
WIDTH, HEIGHT = GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulação de Epidemia - Autômato Celular SEIR")
clock = pygame.time.Clock()

# --- Funções do Autômato Celular ---
def create_grid():
    grid = np.full((GRID_SIZE, GRID_SIZE), SUSCETIVEL, dtype=int)
    
    # Adicionar alguns infectados iniciais aleatoriamente
    for _ in range(INITIAL_INFECTED_COUNT):
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        grid[x, y] = INFECTADO
    
    return grid

def get_neighbors(grid, x, y):
    neighbors = []
    # Vizinhança de Moore (8 vizinhos)
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                neighbors.append(grid[nx, ny])
    return neighbors

def update_grid(current_grid):
    new_grid = current_grid.copy()
    
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            current_state = current_grid[x, y]
            
            if current_state == SUSCETIVEL:
                neighbors = get_neighbors(current_grid, x, y)
                if INFECTADO in neighbors:
                    # Checar se a transmissão ocorre
                    if random.random() < BETA:
                        new_grid[x, y] = EXPOSTO
            
            elif current_state == EXPOSTO:
                # Checar se o exposto se torna infeccioso
                if random.random() < SIGMA:
                    new_grid[x, y] = INFECTADO
            
            elif current_state == INFECTADO:
                # Checar se o infectado se recupera
                if random.random() < GAMMA:
                    new_grid[x, y] = RECUPERADO
            
            # Recuperados permanecem recuperados neste modelo SIR simples
            # if current_state == RECUPERADO:
            #    pass 
                    
    return new_grid

def draw_grid(screen, grid):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            state = grid[x, y]
            color = COLOR_BACKGROUND
            if state == SUSCETIVEL:
                color = COLOR_SUSCEPTIVEL
            elif state == EXPOSTO:
                color = COLOR_EXPOSTO
            elif state == INFECTADO:
                color = COLOR_INFECTADO
            elif state == RECUPERADO:
                color = COLOR_RECUPERADO
            
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# --- Loop Principal do Jogo ---
grid = create_grid()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: # Pressione 'R' para reiniciar a simulação
                grid = create_grid()

    # Atualizar o grid
    grid = update_grid(grid)
    
    # Desenhar o grid
    screen.fill(COLOR_BACKGROUND)
    draw_grid(screen, grid)
    pygame.display.flip()
    
    # Controlar a velocidade da simulação
    clock.tick(10) # 10 frames por segundo

pygame.quit()
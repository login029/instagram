import pygame
import sys

# Inizializza Pygame
pygame.init()

# Impostazioni del terminale
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 16
PADDING = 10
BG_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
PROMPT = "$ "

# Crea la finestra del terminale
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ubuntu-like Terminal")

# Carica il font
font = pygame.font.SysFont("Ubuntu Mono", FONT_SIZE)

# Variabili per l'input e l'output
input_text = ""
output_lines = []

# Funzione per stampare il testo di output
def print_output(text):
    global output_lines
    output_lines.append(text)
    # Limita il numero di righe di output visualizzate
    if len(output_lines) * FONT_SIZE > HEIGHT - PADDING * 2:
        del output_lines[0]

# Loop principale
running = True
while running:
    # Gestione degli eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print_output(PROMPT + input_text)
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_ESCAPE:
                running = False
            else:
                input_text += event.unicode

    # Pulisci lo schermo
    screen.fill(BG_COLOR)

    # Disegna il testo di output
    y = PADDING
    for line in output_lines:
        text_surf = font.render(line, True, TEXT_COLOR)
        screen.blit(text_surf, (PADDING, y))
        y += FONT_SIZE

    # Disegna il prompt e l'input dell'utente
    prompt_surf = font.render(PROMPT, True, TEXT_COLOR)
    input_surf = font.render(input_text, True, TEXT_COLOR)
    screen.blit(prompt_surf, (PADDING, HEIGHT - FONT_SIZE - PADDING))
    screen.blit(input_surf, (PADDING + prompt_surf.get_width(), HEIGHT - FONT_SIZE - PADDING))

    # Aggiorna la finestra
    pygame.display.flip()

# Chiudi Pygame
pygame.quit()
sys.exit()

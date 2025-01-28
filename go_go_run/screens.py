import pygame
from db_utils import load_top_scores

def show_menu(screen):
    font = pygame.font.Font(None, 74)
    title = font.render("Go, Go, Run!", True, (0, 0, 0))
    start_button = pygame.Rect(200, 300, 300, 50)
    scores_button = pygame.Rect(200, 400, 300, 50)

    screen.fill((255, 255, 255))
    screen.blit(title, (200, 200))

    pygame.draw.rect(screen, (0, 0, 0), start_button)
    start_text = font.render("Start", True, (255, 255, 255))
    screen.blit(start_text, (300, 300))

    pygame.draw.rect(screen, (0, 0, 0), scores_button)
    scores_text = font.render("Scores", True, (255, 255, 255))
    screen.blit(scores_text, (280, 400))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return "start"
                elif scores_button.collidepoint(event.pos):
                    return "scores"

def show_scores(screen):
    font = pygame.font.Font(None, 36)
    scores = load_top_scores()
    
    screen.fill((255, 255, 255))
    title = font.render("Top Scores", True, (0, 0, 0))
    screen.blit(title, (300, 50))

    for i, score in enumerate(scores):
        score_text = font.render(f"{i + 1}. {score}", True, (0, 0, 0))
        screen.blit(score_text, (300, 100 + i * 40))

    pygame.display.flip()
    pygame.time.wait(3000)

def show_game_over(screen, score, best_score):
    font = pygame.font.Font(None, 74)
    screen.fill((255, 255, 255))

    game_over_text = font.render("Game Over", True, (255, 0, 0))
    screen.blit(game_over_text, (250, 200))

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (270, 300))

    best_text = font.render(f"Best: {best_score}", True, (0, 0, 0))
    screen.blit(best_text, (270, 400))

    restart_button = pygame.Rect(250, 500, 300, 50)
    pygame.draw.rect(screen, (0, 0, 0), restart_button)
    restart_text = font.render("Restart", True, (255, 255, 255))
    screen.blit(restart_text, (300, 500))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    return "restart"

import pygame
from screens import *
from game_logic import *
from db_utils import load_best_score, save_score

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Go, Go, Run!")
clock = pygame.time.Clock()

player_img = pygame.image.load("assets/player.png")
player_img = pygame.transform.scale(player_img, (50, 50))

def main():
    running = True
    score = 0
    lives = 3
    player = pygame.Rect(WIDTH // 2, HEIGHT - 50, 50, 50)
    objects = []
    spawn_timer = 0

    while running:
        screen.fill(WHITE)

        choice = show_menu(screen)
        if choice == "start":
            in_game = True
        elif choice == "scores":
            show_scores(screen)
            continue
        else:
            pygame.quit()
            break

        while in_game:
            pygame.time.Clock().tick(FPS)
            screen.fill(WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    in_game = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    in_game = False

            keys = pygame.key.get_pressed()
            handle_player_movement(keys, player, WIDTH)

            spawn_timer += 1
            if spawn_timer > 30:
                spawn_object(objects, WIDTH)
                spawn_timer = 0

            move_objects(objects, HEIGHT)
            score, lives = check_collisions(objects, player, score, lives)

            if lives <= 0:
                save_score(score)
                best_score = load_best_score()
                show_game_over(screen, score, best_score)
                in_game = False
                lives = 3
                score = 0
                objects.clear()
                break

            screen.blit(player_img, (player.x, player.y))
            for obj in objects:
                pygame.draw.rect(screen, obj["color"], obj["rect"])

            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {score}", True, BLACK)
            lives_text = font.render(f"Lives: {lives}", True, BLACK)
            screen.blit(score_text, (10, 10))
            screen.blit(lives_text, (10, 50))

            pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

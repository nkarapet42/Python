import pygame
import random

def handle_player_movement(keys, player, width):
    speed = 5
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.left > 0:
        player.x -= speed
    if (keys[pygame.K_RIGHT]or keys[pygame.K_d]) and player.right < width:
        player.x += speed

def spawn_object(objects, width):
    x = random.randint(0, width - 30)
    y = -30
    is_good = random.choice([True, False])
    color = (0, 255, 0) if is_good else (255, 0, 0)
    obj = {"rect": pygame.Rect(x, y, 30, 30), "color": color, "is_good": is_good}
    objects.append(obj)

def move_objects(objects, height):
    for obj in objects:
        obj["rect"].y += 5
    objects[:] = [obj for obj in objects if obj["rect"].y < height]

def check_collisions(objects, player, score, lives):
    for obj in objects[:]:
        if player.colliderect(obj["rect"]):
            if obj["is_good"]:
                score += 1
            else:
                lives -= 1
            objects.remove(obj)
    return score, lives
import pygame
import random
import time
import math
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
small = 15
medium = 25
big = 40
dt = 0
dt = clock.tick(60) / 1000
a = 2
class entity:
    def __init__(character, size, hp, damage, speed): 
        character.size = size
        character.hp = hp
        character.damage = damage
        character.speed = speed

player = entity(medium, 100, 10, 300 * dt)
melee_enemy = entity(medium, 30, 10, 150 * dt)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#7B3F00")
    pygame.draw.circle(screen, "green", player_pos, player.size)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= player.speed
    if keys[pygame.K_DOWN]:
        player_pos.y += player.speed
    if keys[pygame.K_LEFT]:
        player_pos.x -= player.speed
    if keys[pygame.K_RIGHT]:
        player_pos.x += player.speed
    
    while a == 2:
        enemy1 = pygame.Vector2(random.randint(0, 1280), random.randint(0, 720))
        a = a - 1
        if math.dist((enemy1), (player_pos)) < (100):
            enemy1 = pygame.Vector2(random.randint(0, 1280), random.randint(0, 720))
    pygame.draw.circle(screen, "red", enemy1, melee_enemy.size)
    
    while a == 1:
        enemy2 = pygame.Vector2(random.randint(0, 1280), random.randint(0, 720))
        a = a - 1
        if math.dist((enemy2), (player_pos)) < (100):
            enemy2 = pygame.Vector2(random.randint(0, 1280), random.randint(0, 720))
    pygame.draw.circle(screen, "red", enemy2, melee_enemy.size)

    
    def enemy_movement(enemy_pos):
        if enemy_pos.x < player_pos.x:
            enemy_pos.x += melee_enemy.speed
        if enemy_pos.y < player_pos.y:
            enemy_pos.y += melee_enemy.speed
        if enemy_pos.x > player_pos.x:
            enemy_pos.x -= melee_enemy.speed
        if enemy_pos.y > player_pos.y:
            enemy_pos.y -= melee_enemy.speed

        enemy_movement(enemy1)
        enemy_movement(enemy2)

    # if enemy1.x < player_pos.x:
    #     enemy1.x += melee_enemy.speed
    # if enemy1.y < player_pos.y:
    #     enemy1.y += melee_enemy.speed
    # if enemy1.x > player_pos.x:
    #     enemy1.x -= melee_enemy.speed
    # if enemy1.y > player_pos.y:
    #     enemy1.y -= melee_enemy.speed

    def border(player_pos):  
        if player_pos.x < 0: player_pos.x = 0
        if player_pos.y < 0: player_pos.y = 0
        if player_pos.x > 1280: player_pos.x = 1280
        if player_pos.y > 720: player_pos.y = 720

    border(player_pos)
    border(enemy1)
    border(enemy2)


    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()


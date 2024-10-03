import pygame
import random
import time
import math
import threading
pygame.init()

height = 1280
width = 720
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('gimma')
acht = pygame.image.load(r"achtergrond.png").convert()

clock = pygame.time.Clock()
running = True
small = 15
medium = 25
big = 40
dt = 0
dt = clock.tick(60) / 1000
a = 2
class entity:
    def __init__(character, name, size, hp, damage, speed): 
        character.name = name
        character.size = size
        character.hp = hp
        character.damage = damage
        character.speed = speed    

class enemy(entity):
    def __init__(character, name, size, hp, damage, speed):
        super().__init__(name, size, hp, damage, speed)

class player(entity):
    def __init__(character, name, size, hp, damage, speed):
        super().__init__(name, size, hp, damage, speed)
       
def timer():
    global tijd
    tijd = 10
    while tijd >= 0:
        for x in range(10):
            tijd -=1
            time.sleep(1)


    print('tijd voor nieuwe enemy')

timer_thread = threading.Thread(target = timer)
timer_thread.start()

player = player("player", medium, 50, 10, 300 * dt)
melee_enemy = enemy("melee_enemy", medium, 30, 10, 150 * dt)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(acht, (0,0))
    green_dot = pygame.draw.circle(screen, "green", player_pos, player.size)
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

    
    def melee_enemy_movement(enemy_pos):  
        if math.dist((enemy_pos), (player_pos)) >= 50:  
            if enemy_pos.x < player_pos.x:
                enemy_pos.x += melee_enemy.speed
            if enemy_pos.y < player_pos.y:
                enemy_pos.y += melee_enemy.speed
            if enemy_pos.x > player_pos.x:
                enemy_pos.x -= melee_enemy.speed
            if enemy_pos.y > player_pos.y:
                enemy_pos.y -= melee_enemy.speed
        

    melee_enemy_movement(enemy1)
    melee_enemy_movement(enemy2)


        

    def border(player_pos):  
        if player_pos.x < 0: player_pos.x = 0
        if player_pos.y < 0: player_pos.y = 0
        if player_pos.x > 1280: player_pos.x = 1280
        if player_pos.y > 720: player_pos.y = 720

    border(player_pos)
    border(enemy1)
    border(enemy2)

    if tijd <= 0:
        print('wow')
        tijd = 10

    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()

# hitbox
# spawn timer
# add new enemies after timer
# hits
import pygame
import random
import threading
import math
import time
pygame.init()
height = 1280
width = 720
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('achtergrond')
acht = pygame.image.load(r"achtergrond.png").convert()

clock = pygame.time.Clock()
running = True
dt = clock.tick(300) / 1000
a = 2

class object:
    def __init__(self, size, damage):
        self.size = size
        self.damage = damage

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


class character(entity):
    def __init__(character, name, size, hp, damage, speed):
        super().__init__(name, size, hp, damage, speed)

player = character("player", 25, 60, 10, 300 * dt)
melee_enemy1 = enemy("melee_enemy", 25, 50, 10, 150 * dt)
melee_enemy2 = enemy("melee_enemy", 25, 50, 10, 150 * dt)
ranged_enemy = enemy("ranged_enemy", 15, 20, 15, 150 * dt)
sword = object(15, 10)

def hp_down_enemy(enemy_hp, sword_damage, sword_pos, enemy_pos, sword_size, enemy_size):
    score = 0
    if math.dist((sword_pos), (enemy_pos)) < sword_size + enemy_size:
        enemy_hp = enemy_hp - sword_damage
        
        if enemy_hp <= 0:
            score = score + 10
            enemy_pos = pygame.Vector2(random.randint(0, 1280), random.randint(0, 720))
        
        if enemy_pos.x > player_pos.x:
            enemy_pos.x += 900 * dt
        if enemy_pos.y > player_pos.y:
            enemy_pos.y += 900 * dt
        if enemy_pos.x < player_pos.x:
            enemy_pos.x -= 900 * dt
        if enemy_pos.y < player_pos.y:
            enemy_pos.y -= 900 * dt
        
        return enemy_hp
    return score

def easier_hit(enemy_pos, melee_enemy):
        hp_down_enemy(melee_enemy.hp, 10, sword_pos, enemy_pos, 15, 25)
            

def draw(enemy_pos, melee_enemy):
    pygame.draw.circle(screen, "red", enemy_pos, melee_enemy.size)


def spawn_timer():
    global spawn_tijd
    spawn_tijd = 10
    while spawn_tijd >= 0:
        for x in range(spawn_tijd):
            spawn_tijd -= 1
            time.sleep(1)

def melee_enemy_hitbox(enemy_pos1, enemy_pos2, melee_enemy):
    if math.dist((enemy_pos1), (enemy_pos2)) < melee_enemy.size + melee_enemy.size:
        if enemy_pos1.x < enemy_pos2.x:
            enemy_pos1.x -= 0.5 * melee_enemy.speed
        if enemy_pos1.y < enemy_pos2.y:
            enemy_pos1.y -= 0.5 * melee_enemy.speed
        if enemy_pos1.x > enemy_pos2.x:
            enemy_pos1.x += 0.5 * melee_enemy.speed
        if enemy_pos1.y > enemy_pos2.y:
            enemy_pos1.y += 0.5 * melee_enemy.speed
        if enemy_pos2.x < enemy_pos1.x:
            enemy_pos2.x -= 0.5 * melee_enemy.speed
        if enemy_pos2.y < enemy_pos1.y:
            enemy_pos2.y -= 0.5 * melee_enemy.speed
        if enemy_pos2.x > enemy_pos1.x:
            enemy_pos2.x += 0.5 * melee_enemy.speed
        if enemy_pos2.y > enemy_pos1.y:
            enemy_pos2.y += 0.5 * melee_enemy.speed


        if enemy_pos1.x < player_pos.x:
            enemy_pos1.x -= 0.5 * melee_enemy.speed
        if enemy_pos1.y < player_pos.y:
            enemy_pos1.y -= 0.5 * melee_enemy.speed
        if enemy_pos1.x > player_pos.x:
            enemy_pos1.x += 0.5 * melee_enemy.speed
        if enemy_pos1.y > player_pos.y:
            enemy_pos1.y += 0.5 * melee_enemy.speed
        if enemy_pos2.x < player_pos.x:
            enemy_pos2.x -= 0.5 * melee_enemy.speed
        if enemy_pos2.y < player_pos.y:
            enemy_pos2.y -= 0.5 * melee_enemy.speed
        if enemy_pos2.x > player_pos.x:
            enemy_pos2.x += 0.5 * melee_enemy.speed
        if enemy_pos2.y > player_pos.y:
            enemy_pos2.y += 0.5 * melee_enemy.speed


spawn_timer_thread = threading.Thread(target=spawn_timer, daemon=True)
spawn_timer_thread.start()


def melee_enemy_movement(enemy_pos, melee_enemy):
    if math.dist((enemy_pos), (player_pos)) >= player.size + melee_enemy.size:
        if enemy_pos.x < player_pos.x:
            enemy_pos.x += melee_enemy.speed
        if enemy_pos.y < player_pos.y:
            enemy_pos.y += melee_enemy.speed
        if enemy_pos.x > player_pos.x:
            enemy_pos.x -= melee_enemy.speed
        if enemy_pos.y > player_pos.y:
            enemy_pos.y -= melee_enemy.speed
    elif math.dist((enemy_pos), (player_pos)) < player.size + melee_enemy.size:
        if enemy_pos.x > player_pos.x:
            enemy_pos.x += melee_enemy.speed
        if enemy_pos.y > player_pos.y:
            enemy_pos.y += melee_enemy.speed
        if enemy_pos.x < player_pos.x:
            enemy_pos.x -= melee_enemy.speed
        if enemy_pos.y < player_pos.y:
            enemy_pos.y -= melee_enemy.speed

def border(player_pos):
    if player_pos.x < 0:
        player_pos.x = 0
    if player_pos.y < 0:
        player_pos.y = 0
    if player_pos.x > 1280:
        player_pos.x = 1280
    if player_pos.y > 720:
        player_pos.y = 720

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
sword_pos = pygame.Vector2(screen.get_width() / 2 + 30, screen.get_height() / 2 + 30)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(acht, (0, 0))
    green_dot = pygame.draw.circle(screen, "green", player_pos, player.size)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_pos.y -= player.speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_pos.y += player.speed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos.x -= player.speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_pos.x += player.speed

    if a == 2:
        enemy_pos1 = pygame.Vector2(random.randint(0, 1280), random.randint(0, 720))
        a = a - 1
    if a == 1:
        enemy_pos2 = pygame.Vector2(random.randint(0, 1280), random.randint(0, 720))
        a = a - 1

    sword = pygame.draw.circle(screen, "purple", sword_pos, 15)
    
    while math.dist((sword_pos), (player_pos)) > 50:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            sword_pos.y -= player.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            sword_pos.y += player.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            sword_pos.x -= player.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            sword_pos.x += player.speed



    melee_enemy_hitbox(enemy_pos1, enemy_pos2, melee_enemy1)
    melee_enemy_hitbox(enemy_pos1, enemy_pos2, melee_enemy2)
    draw(enemy_pos1, melee_enemy1)
    draw(enemy_pos2, melee_enemy1)
    melee_enemy_movement(enemy_pos1, melee_enemy1)
    melee_enemy_movement(enemy_pos2, melee_enemy2)
    easier_hit(enemy_pos1, melee_enemy1)
    easier_hit(enemy_pos2, melee_enemy2)

    border(sword_pos)
    border(player_pos)
    border(enemy_pos1)
    border(enemy_pos2)

    if spawn_tijd <= 0:
        print('wow')
        spawn_tijd = 10

    pygame.display.flip()
    dt = clock.tick(300) / 1000
pygame.quit()

# hitbox
# spawn timer
# add new enemies after timer
# hits
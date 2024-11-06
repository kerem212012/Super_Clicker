import pgzrun
import pygame

WIDTH = 600
HEIGHT = 400


pygame.event.get()
TITLE = 'Super Clicker'
FPS = 30
fon = Actor('fon')
enemy = Actor('enemy', (400, 230))
bonus_1 = Actor("bonus", (100, 100))
bonus_2 = Actor("bonus", (100, 200))
win = Actor("win")
button_menu = Actor("bonus", (300, 300))
button_back = Actor("bonus", (300, 350))
count = 10000000
price1 = 15
price2 = 200
bonus_damage = 0
mode = 'menu'
button_play = Actor("bonus", (300, 200))
button_gallery = Actor("bonus", (300, 300))
button_quit = Actor("bonus", (300, 350))
enemy_gallery1 = Actor("enemy", (150, 80))
enemy_gallery2 = Actor("enemy_2", (280, 80))
enemy_gallery3 = Actor("enemy_3", (450, 80))
enemy_gallery4 = Actor("enemy_4", (220, 230))
enemy_gallery5 = Actor("enemy_5", (400, 230))
bonus_give = 0
damage = 1
hp = 100


def draw():
    global hp
    global mode
    if mode == 'menu':
        win.draw()
        button_play.draw()
        screen.draw.text("PLAY", color="black", fontsize=36, center=(300, 200))
        button_gallery.draw()
        screen.draw.text("GALLERY", color="black", fontsize=36, center=(300, 300))


    elif mode == 'gallery':
        win.draw()
        enemy_gallery1.draw()
        enemy_gallery2.draw()
        enemy_gallery3.draw()
        enemy_gallery4.draw()
        enemy_gallery5.draw()
        button_back.draw()

        screen.draw.text("Back", color="black", fontsize=36, center=(300, 350))
    elif mode == 'game':
        fon.draw()
        screen.draw.text(f'coin:{count}', center=(570, 30), color="black", fontsize=30)
        bonus_1.draw()
        bonus_2.draw()
        screen.draw.text('1 dam every 2 sec', center=(100, 80), color='black', fontsize=30)
        screen.draw.text('20 coin every 2 sec', center=(100, 180), color='black', fontsize=30)
        screen.draw.text(f'{price1} coin', center=(100, 110), color='black', fontsize=30)
        screen.draw.text(f'{price2} coin', center=(100, 210), color='black', fontsize=30)

        if hp > 0:
            enemy.draw()
            screen.draw.text(f'{hp}', center=(400, 130), color="#DC143C", fontsize=30, background="#FFE4B5")
        elif hp <= 0:
            screen.draw.text('You Kill Enemy', center=(400, 130), color='black', fontsize=30, background="#FFE4B5")

        if hp <= 0 and enemy.image == 'enemy':
            hp = 200
            enemy.image = 'enemy_2'
        elif hp <= 0 and enemy.image == 'enemy_2':
            hp = 300
            enemy.image = 'enemy_3'
        elif hp <= 0 and enemy.image == 'enemy_3':
            hp = 400
            enemy.image = 'enemy_4'
        elif hp <= 0 and enemy.image == 'enemy_4':
            hp = 500
            enemy.image = 'enemy_5'
        elif hp <= 0 and enemy.image == 'enemy_5':
            win.draw()
            screen.draw.text("You Kill All Enemy", color="black", fontsize=36, center=(300, 100))
            button_menu.draw()
            screen.draw.text("Return to Menu", color="black", fontsize=36, center=(300, 300))
        button_quit.draw()
        screen.draw.text('QUIT', center=(300, 350), color='black', fontsize=36)

def on_mouse_down(button, pos):
    global count
    global damage
    global hp
    global price1
    global price2
    global bonus_give
    global bonus_damage
    global mode
    global HEIGHT
    global WIDTH
    if button == mouse.LEFT:
        if button_play.collidepoint(pos):
            mode = 'game'
            hp = 100
            count = 10000000
            bonus_give = 0
            bonus_damage = 0
            price1 = 15
            price2 = 200
            enemy.image = 'enemy'
        elif button_quit.collidepoint(pos):
            mode = 'menu'
        elif button_gallery.collidepoint(pos):
            mode = 'gallery'
        elif button_back.collidepoint(pos):
            mode = "menu"
        elif button_menu.collidepoint(pos):
            mode = 'menu'

        elif enemy.collidepoint(pos) and hp != 0:
            count += 1
            hp -= damage
            enemy.y = 200
            animate(enemy, tween='bounce_end', duration=0.5, y=230)
        elif bonus_1.collidepoint(pos) and count >= price1:
            clock.schedule_interval(bonus1, 2)
            count -= price1
            price1 *= 2
            bonus_damage += 1
        elif bonus_2.collidepoint(pos) and count >= price2:
            clock.schedule_interval(bonus1, 2)
            count -= price2
            price2 *= 2
            bonus_give += 20


def bonus1():
    global hp
    global count
    if hp > 0:
        hp -= bonus_damage
        count += 1


def bonus2():
    global count
    count += bonus_give


pgzrun.go()

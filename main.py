import pgzrun

WIDTH = 600
HEIGHT = 400

TITLE = 'Super Clicker'
FPS = 30
fon = Actor('fon')
enemy = Actor('enemy', (400, 230))
bonus_1 = Actor("bonus", (100, 100))
bonus_2 = Actor("bonus", (100, 200))
count = 0
price1 = 15
price2 = 200
bonusdamage1 = 0
bonusgive1 = 0
damage = 1
hp = 50


def draw():
    fon.draw()

    screen.draw.text(f'coin:{count}', center=(570, 30), color="black", fontsize=30)
    bonus_1.draw()
    bonus_2.draw()
    screen.draw.text('1 dam every 2 sec', center=(100, 80), color='black', fontsize=30)
    screen.draw.text('1 dam every 2 sec', center=(100, 180), color='black', fontsize=30)
    screen.draw.text(f'{price1} coin', center=(100, 110), color='black', fontsize=30)
    screen.draw.text(f'{price2} coin', center=(100, 210), color='black', fontsize=30)
    if hp > 0:
        enemy.draw()
        screen.draw.text(f'{hp}', center=(400, 130), color="#DC143C", fontsize=30, background="#FFE4B5")
    elif hp <= 0:
        screen.draw.text('You Kill Enemy', center=(400, 130), color='black', fontsize=30, background="#FFE4B5")


def on_mouse_down(button, pos):
    global count
    global damage
    global hp
    global price1
    global price2
    global bonusgive1
    global bonusdamage1
    if button == mouse.LEFT and enemy.collidepoint(pos) and hp != 0:
        count += 1
        hp -= damage
        enemy.y = 200
        animate(enemy, tween='bounce_end', duration=0.5, y=230)
    elif button == mouse.LEFT and bonus_1.collidepoint(pos) and count >= price1:
        clock.schedule_interval(bonus1, 2)
        count -= price1
        price1 *= 2
        bonusdamage1 += 1
    elif button == mouse.LEFT and bonus_2.collidepoint(pos) and count >= price2:
        clock.schedule_interval(bonus1, 2)
        count -= price2
        price1 *= 2
        bonusgive1 += 20
def bonus1():
    global hp
    global count
    if hp > 0:
        hp -= bonusdamage1
        count += 1
def bonus2():
    global count
    count += bonusgive1

pgzrun.go()

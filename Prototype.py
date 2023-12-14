import pygame
import random
from pygame.rect import *

pygame.init()
pygame.display.set_caption("Clarinet")

def resultProcess(direction):
    global isColl, score, DrawResult, result_ticks, chance

    if isColl and CollDirection.direction == direction:
        score += 10
        CollDirection.y = -1
        DrawResult = 1
    else:
        if CollDirection != 0:
            # CollDirection.y = -1
            chance -= 1
            DrawResult = 2
    result_ticks = pygame.time.get_ticks()

def eventProcess():
    global isActive, score, chance, first_ticks
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isActive = False
            if chance > 0:
                if event.key == pygame.K_d:
                    resultProcess(0)
                if event.key == pygame.K_f:
                    resultProcess(1)
                if event.key == pygame.K_j:
                    resultProcess(2)
                if event.key == pygame.K_k:
                    resultProcess(3)
            else:
                if event.key == pygame.K_SPACE:
                    score = 0
                    chance = chance_MAX
                    for direc in Directions:
                        direc.y = -1
                    first_ticks = pygame.time.get_ticks()

class Direction(object):
    def __init__(self):
        self.pos = None
        self.direction = 0
        self.image = pygame.image.load(f"data/direction.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.y = -1
        self.x = int(SCREEN_WIDTH*0.75)-(self.image.get_width()/2)

    def lane(self, direction=0):
        self.direction = direction
        if (direction == 0):
            self.x = 20
        elif (direction == 1):
            self.x = 120
        elif (direction == 2):
            self.x = 220
        else:
            self.x = 320

    def draw(self, v):
        if self.y >= SCREEN_HEIGHT:
            self.y = -1
            return True
        elif self.y == -1:
            return False
        else:
            self.y += v
            self.pos = screen.blit(self.image, (self.x, self.y))
            return False

def drawIcon():
    global start_ticks, chance, first_ticks

    if chance <= 0:
        return

    elapsed_time = (pygame.time.get_ticks() - start_ticks)
    cur_time = (pygame.time.get_ticks() - first_ticks)
    
    if (cur_time < 30000):
        if elapsed_time > 1800:
            start_ticks = pygame.time.get_ticks()
            for direc in Directions:
                if direc.y == -1:
                    direc.y = 0
                    direc.lane(direction=random.randint(0, 3))
                    break
        velocity = 0.5
        for direc in Directions:
            if direc.draw(velocity):
                chance -= 1
    elif (cur_time < 60000 and cur_time >= 30000):
        if elapsed_time > 900:
            start_ticks = pygame.time.get_ticks()
            for direc in Directions:
                if direc.y == -1:
                    direc.y = 0
                    direc.lane(direction=random.randint(0, 3))
                    break
        velocity = 1
        for direc in Directions:
            if direc.draw(velocity):
                chance -= 1
    elif (cur_time < 90000 and cur_time >= 60000):
        if elapsed_time > 600:
            start_ticks = pygame.time.get_ticks()
            for direc in Directions:
                if direc.y == -1:
                    direc.y = 0
                    direc.lane(direction=random.randint(0, 3))
                    break
        velocity = 1.5
        for direc in Directions:
            if direc.draw(velocity):
                chance -= 1
    elif (cur_time < 120000 and cur_time >= 90000):
        if elapsed_time > 450:
            start_ticks = pygame.time.get_ticks()
            for direc in Directions:
                if direc.y == -1:
                    direc.y = 0
                    direc.lane(direction=random.randint(0, 3))
                    break
        velocity = 2
        for direc in Directions:
            if direc.draw(velocity):
                chance -= 1
    elif (cur_time < 150000 and cur_time >= 120000):
        if elapsed_time > 360:
            start_ticks = pygame.time.get_ticks()
            for direc in Directions:
                if direc.y == -1:
                    direc.y = 0
                    direc.lane(direction=random.randint(0, 3))
                    break
        velocity = 2.5
        for direc in Directions:
            if direc.draw(velocity):
                chance -= 1
    elif (cur_time < 180000 and cur_time >= 150000):
        if elapsed_time > 300:
            start_ticks = pygame.time.get_ticks()
            for direc in Directions:
                if direc.y == -1:
                    direc.y = 0
                    direc.lane(direction=random.randint(0, 3))
                    break
        velocity = 3
        for direc in Directions:
            if direc.draw(velocity):
                chance -= 1
    elif (cur_time < 210000 and cur_time >= 180000):
        if elapsed_time > 257:
            start_ticks = pygame.time.get_ticks()
            for direc in Directions:
                if direc.y == -1:
                    direc.y = 0
                    direc.lane(direction=random.randint(0, 3))
                    break
        velocity = 3.5
        for direc in Directions:
            if direc.draw(velocity):
                chance -= 1
    elif (cur_time < 240000 and cur_time >= 210000):
        if elapsed_time > 225:
            start_ticks = pygame.time.get_ticks()
            for direc in Directions:
                if direc.y == -1:
                    direc.y = 0
                    direc.lane(direction=random.randint(0, 3))
                    break
        velocity = 4
        for direc in Directions:
            if direc.draw(velocity):
                chance -= 1
    elif (cur_time < 270000 and cur_time >= 240000):
        if elapsed_time > 200:
            start_ticks = pygame.time.get_ticks()
            for direc in Directions:
                if direc.y == -1:
                    direc.y = 0
                    direc.lane(direction=random.randint(0, 3))
                    break
        velocity = 4.5
        for direc in Directions:
            if direc.draw(velocity):
                chance -= 1
    elif  (cur_time < 300000 and cur_time >= 270000):
        if elapsed_time > 180:
            start_ticks = pygame.time.get_ticks()
            for direc in Directions:
                if direc.y == -1:
                    direc.y = 0
                    direc.lane(direction=random.randint(0, 3))
                    break
        velocity = 5
        for direc in Directions:
            if direc.draw(velocity):
                chance -= 1
    elif  (cur_time < 330000 and cur_time >= 300000):
        if elapsed_time > 164:
            start_ticks = pygame.time.get_ticks()
            for direc in Directions:
                if direc.y == -1:
                    direc.y = 0
                    direc.lane(direction=random.randint(0, 3))
                    break
        velocity = 5.5
        for direc in Directions:
            if direc.draw(velocity):
                chance -= 1
    elif  (cur_time < 360000 and cur_time >= 330000):
        if elapsed_time > 150:
            start_ticks = pygame.time.get_ticks()
            for direc in Directions:
                if direc.y == -1:
                    direc.y = 0
                    direc.lane(direction=random.randint(0, 3))
                    break
        velocity = 6
        for direc in Directions:
            if direc.draw(velocity):
                chance -= 1
    elif  (cur_time < 390000 and cur_time >= 360000):
        if elapsed_time > 138:
            start_ticks = pygame.time.get_ticks()
            for direc in Directions:
                if direc.y == -1:
                    direc.y = 0
                    direc.lane(direction=random.randint(0, 3))
                    break
        velocity = 6.5
        for direc in Directions:
            if direc.draw(velocity):
                chance -= 1
    else:
        if elapsed_time > 129:
            start_ticks = pygame.time.get_ticks()
            for direc in Directions:
                if direc.y == -1:
                    direc.y = 0
                    direc.lane(direction=random.randint(0, 3))
                    break
        velocity = 7
        for direc in Directions:
            if direc.draw(velocity):
                chance -= 1

def draw_targetArea():
    global isColl, CollDirection
    isColl = False
    for direc in Directions:
        if direc.y == -1:
            continue
        if direc.pos.colliderect(targetArea):
            isColl = True
            CollDirection = direc
            pygame.draw.rect(screen, (255, 0, 0), targetArea)
            break
    pygame.draw.rect(screen, (0, 255, 0), targetArea, 5)

def setText():
    global score, chance
    mFont = pygame.font.SysFont("굴림", 40)

    mtext = mFont.render(f'score : {score}', True, 'yellow')
    screen.blit(mtext, (10, 10, 0, 0))

    mtext = mFont.render(f'chance : {chance}', True, 'yellow')
    screen.blit(mtext, (10, 42, 0, 0))

    if chance <= 0:
        mFont = pygame.font.SysFont("굴림", 90)
        mtext = mFont.render(f'Game over!!', True, 'red')
        tRec = mtext.get_rect()
        tRec.centerx = SCREEN_WIDTH/2
        tRec.centery = SCREEN_HEIGHT/2 - 40
        screen.blit(mtext, tRec)

def drawResult():
    global DrawResult, result_ticks
    if result_ticks > 0:
        elapsed_time = (pygame.time.get_ticks() - result_ticks)
        if elapsed_time > 400:
            result_ticks = 0
            DrawResult = 0
    screen.blit(resultImg[DrawResult], resultImgRec)

isActive = True
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
chance_MAX = 30
score = 0
chance = chance_MAX
isColl = False
CollDirection = 0
DrawResult, result_ticks = 0,0
start_ticks= pygame.time.get_ticks()
first_ticks= pygame.time.get_ticks()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

Directions = [Direction() for i in range(0, 15)]

targetArea = Rect(0, 450, SCREEN_WIDTH, 150)

resultFileNames = ["data/normal.png", "data/good.png", "data/bad.png"]
resultImg = []
for i, name in enumerate(resultFileNames):
    resultImg.append(pygame.image.load(name))
    resultImg[i] = pygame.transform.scale(resultImg[i], (150, 75))

resultImgRec = resultImg[0].get_rect()
resultImgRec.centerx = SCREEN_WIDTH/2 - resultImgRec.width/2 - 40
resultImgRec.centery = targetArea.centery

while(isActive):
    screen.fill((0, 0, 0))
    eventProcess()
    draw_targetArea()
    drawIcon()
    setText()
    drawResult()
    pygame.display.update()
    clock.tick(400)
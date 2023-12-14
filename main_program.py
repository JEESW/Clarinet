import pygame
import random
import pandas as pd
from pygame.rect import *



pygame.init()
pygame.display.set_caption("Clarinet")


# 전체 기본 셋팅
bisActive = True
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
iHP_MAX = 10
iScore = 0
iCurHP = iHP_MAX
bisColl = False

CollDirection = 0
iDrawResult, iresult_ticks = 0,0
istart_ticks = pygame.time.get_ticks()

pClock = pygame.time.Clock()
pScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


targetArea = Rect(0, 400, SCREEN_WIDTH, 80)

#키 셋팅
bPressed_D = False
bPressed_F = False
bPressed_J = False
bPressed_K = False

# 이미지 로드
resultFileNames = ["data/normal.png", "data/good.png", "data/bad.png"]
resultImg = []
for i, name in enumerate(resultFileNames):
    resultImg.append(pygame.image.load(name))
    resultImg[i] = pygame.transform.scale(resultImg[i], (150, 75))

resultImgRec = resultImg[0].get_rect() # 콜라이더 설정
resultImgRec.centerx = SCREEN_WIDTH/2 - resultImgRec.width/2 - 40
resultImgRec.centery = targetArea.centery

# 노드 이미지 로딩
nodeFileNames = ["data/direction.png", "data/direction.png", "data/direction.png", "data/direction.png"]
nodeTex = []
for i, name in enumerate(nodeFileNames):
    nodeTex.append(pygame.image.load(name))
    nodeTex[i] = pygame.transform.scale(nodeTex[i], (60,15))
    
# 텍스트 출력
def setText():
    global iScore, iCurHP, first_tick
    mFont = pygame.font.SysFont("굴림", 40)

    mtext = mFont.render(f'score : {iScore}', True, 'yellow')
    pScreen.blit(mtext, (10, 10, 0, 0))

    mtext = mFont.render(f'chance : {iCurHP}', True, 'yellow')
    pScreen.blit(mtext, (10, 42, 0, 0))
    
    cur_time = pygame.time.get_ticks() - first_tick
    
    if cur_time >= 72500:
        mFont = pygame.font.SysFont("굴림", 90)
        mtext = mFont.render(f'Clear!!', True, 'green')
        tRec = mtext.get_rect()
        tRec.centerx = SCREEN_WIDTH/2
        tRec.centery = SCREEN_HEIGHT/2 - 40
        pScreen.blit(mtext, tRec)

    if iCurHP <= 0:
        mFont = pygame.font.SysFont("굴림", 90)
        mtext = mFont.render(f'Game over!!', True, 'red')
        tRec = mtext.get_rect()
        tRec.centerx = SCREEN_WIDTH/2
        tRec.centery = SCREEN_HEIGHT/2 - 40
        
        cFont = pygame.font.SysFont("굴림", 25)
        ctext = cFont.render(f'Restart -> Space bar', True, 'red')
        cRec = ctext.get_rect()
        cRec.centerx = SCREEN_WIDTH/2
        cRec.centery = SCREEN_HEIGHT/2 + 80
        
        pScreen.blit(mtext, tRec)
        pScreen.blit(ctext, cRec)

# 노드 x좌표 구해주는 함수
def CalculPos(etype):
    if etype == 0:
        return 20
    elif etype == 1:
       return 105
    elif etype == 2:
        return 235
    elif etype == 3:
        return 320
    
def CalculPos2(etype):
    if etype == 0:
        return 10
    elif etype == 1:
       return 95
    elif etype == 2:
        return 225
    elif etype == 3:
        return 310
    
# ============= 라인 클래스 =============
class Line(object):
    def __init__(self):
        self.Rect = None
        self.eType = 0
        self.image = None
        self.y = 0
        self.x = 0
        self.bChangeImage = False
        self.bClick = False
    
    def Setting(self, type, image_Key):
        self.eType = type
        
        self.y = 500
        self.x = CalculPos2(self.eType)
        
        self.image = pygame.image.load(image_Key)
        self.image = pygame.transform.scale(self.image, (80, 30))
        
    def tick(self):
        global bPressed_D, bPressed_F, bPressed_J, bPressed_K, iScore, iCurHP
        
        self.bClick = False
        bcollision_pf = False
        bcollision_gd = False
        pTargetNode = None
        iIndex = 0
        coli_rect = Rect(0, 480, SCREEN_WIDTH, 550)
                
        if self.eType == 0 and bPressed_D:
            self.bChangeImage = True
            self.bClick = True
        elif self.eType == 1 and bPressed_F:
            self.bChangeImage = True
            self.bClick = True
        elif self.eType == 2 and bPressed_J:
            self.bChangeImage = True
            self.bClick = True
        elif self.eType == 3 and bPressed_K:
            self.bChangeImage = True
            self.bClick = True
        else:
            self.bChangeImage =False
        if pNodeMgr != None:
            for _Node in pNodeMgr.GetNodes():
                if _Node.GetType() == self.eType and self.Rect != None and _Node.Rect != None and self.Rect.colliderect(_Node.Rect):
                    bcollision_pf = True
                    break
                elif _Node.GetType() == self.eType and self.Rect != None and _Node.Rect != None and coli_rect.colliderect(_Node.Rect):
                    bcollision_gd = True
                    break
                iIndex += 1
                    
        
        if self.bClick:
            if bcollision_pf:
                iScore += 20
                pNodeMgr.DelNode(iIndex)
            elif bcollision_gd:
                iScore += 10
                pNodeMgr.DelNode(iIndex)
            else:
                iCurHP -= 1
                    
        
    def render(self):
        self.Rect = pScreen.blit(self.image, (self.x, self.y))
        
class LineMgr(object):
    def __init__(self):
        self.vec_Lines = []
        
        Line_D = Line()
        Line_D.Setting(0,"data/direction.png")
        Line_F = Line()
        Line_F.Setting(1,"data/direction.png")
        Line_J = Line()
        Line_J.Setting(2,"data/direction.png")
        Line_K = Line()
        Line_K.Setting(3,"data/direction.png")
        
        self.vec_Lines.append(Line_D)
        self.vec_Lines.append(Line_F)
        self.vec_Lines.append(Line_J)
        self.vec_Lines.append(Line_K)
        
    def tick(self):
        for _Line in self.vec_Lines:
            _Line.tick()
        
    def render(self):
        for _Line in self.vec_Lines:
            _Line.render()
# ======================================

    
# ============= 노드 클래스 =============
class Node(object):
    def __init__(self):
        self.Rect = None
        self.eType = random.randint(0, 2)
        self.image = (nodeTex[self.eType])
        self.y = -1
        self.x = CalculPos(self.eType)
        self.m_bRender = False
        self.m_bDead = False
        
    def GetType(self):
        return self.eType
    
    def SeteType(self, num):
        self.eType = num
        self.x = CalculPos(self.eType)
        
    def SetNodeMgr(self, _NodeMgr):
        self.m_pNodeMgr = _NodeMgr
        
    def tick(self):
        global iCurHP
        if self.y >= SCREEN_HEIGHT and self.m_bDead != True:
            iCurHP -= 1
            self.m_bDead = True
            
        else:
            self.m_bRender = True
            self.y += 1
        
    def render(self):
        if self.m_bRender == True:
            self.Rect = pScreen.blit(self.image, (self.x, self.y))
        else:
            return
# ======================================

# ========== 노드 매니져 클래스 ==========
class NodeMgr(object):
    def __init__(self):
        self.Nodes = []
        
    def tick(self):
        iIndex = 0
        for _Node in self.Nodes:
            if _Node.m_bDead == True:
                del self.Nodes[iIndex]
            else:
                iIndex += 1
                _Node.tick()
    
    def render(self):
        for _Node in self.Nodes:
            _Node.render()
        
    def AddNode(self, n):
        tmp = Node()
        tmp.SeteType(n)
        self.Nodes.append(tmp)
        
    def GetNodes(self):
        return self.Nodes
    
    def DelNode(self, idx):
        del self.Nodes[idx]
# ======================================


        
# ============= KEY Func =============
def KeyClear():
    global bPressed_D, bPressed_F, bPressed_J, bPressed_K
    bPressed_D = False
    bPressed_F = False
    bPressed_J = False
    bPressed_K = False

def KeyMgrTick():
    global bisActive, iScore, iCurHP, bPressed_D, bPressed_F, bPressed_J, bPressed_K, first_tick, music, eType_list, timing_list
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                bisActive = False
            if iCurHP > 0:
                if event.key == pygame.K_d:
                    bPressed_D = True
                if event.key == pygame.K_f:
                    bPressed_F = True
                if event.key == pygame.K_j:
                    bPressed_J = True
                if event.key == pygame.K_k:
                    bPressed_K = True
            else:
                if event.key == pygame.K_SPACE:
                    iScore = 0
                    iCurHP = iHP_MAX
                    load_data("data/The_Spectre.csv")
                    first_tick = pygame.time.get_ticks()
                    music.play()
# ====================================



# ============= Load Data Func ========
def load_data(target):
    global eType_list, timing_list
    df = pd.read_csv(target, encoding='utf-8')
    eType_list = list(df["Nodes"])
    timing_list = list(df["Timing"])
# =====================================



# ========== Create Note Func =========
def create_note(fall_spd):
    global eType_list, timing_list, first_tick, iCurHP
    
    if iCurHP <= 0:
        eType_list = []
        timing_list = []
    
    cur_time = pygame.time.get_ticks() - first_tick
    
    if timing_list:
        n = eType_list[0]
        if timing_list[0] - fall_spd <= cur_time:
            pNodeMgr.AddNode(n)
            del eType_list[0]
            del timing_list[0]
# =====================================


# ========== Stop Music Func ==========
def music_stop():
    global first_tick, music, iCurHP
    
    cur_time = pygame.time.get_ticks() - first_tick
    
    if iCurHP <= 0:
        music.stop()
    
    if cur_time >= 72500:
        music.stop()
# =====================================


pNodeMgr = NodeMgr()
pLineMgr = LineMgr()
first_tick = pygame.time.get_ticks()
eType_list = []
timing_list = []
load_data("data/The_Spectre.csv")
music = pygame.mixer.Sound("data/The_Spectre.wav")
music.play()

# 게임 틱
while(bisActive):
    pScreen.fill((0, 0, 0)) # 스크린 초기화
    KeyClear() # 키 체크 초기화
    KeyMgrTick() # 키 입력체크
    pNodeMgr.tick()
    pLineMgr.tick()
    pLineMgr.render()
    pNodeMgr.render()
    setText()
    create_note(1000)
    music_stop()
    pygame.display.update()
    pClock.tick(400)
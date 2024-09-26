import pygame.display
import pygame.locals
import pygame.window
import wordlist
import random
import pygame
import math

# RANDOM WORD && ANAGRAM GENERATION

words = wordlist.words

pygame.init()

screen = pygame.display.set_mode((300,300))

"""
logo = pygame.image.load("logo.png").convert()
screen.blit(logo,(0,0))
pygame.transform.scale(screen,(300,300),screen)
"""

sprites = pygame.sprite.Group()

"""class bar(pygame.sprite.Sprite):
    def __init__(self,val,x,y):
        super().__init__()
        
        self.val = val
        self.x = x
        self.y = y
        
        self.image = pygame.Surface([30,10])
        self.rect = pygame.Rect(0,0,(100*val)/30,10)
        self.image.fill((255,0,0))
        self.rect.center = (self.x // 2, self.y // 2)
        
    
    def update(self):
        self.rect = pygame.Rect(0,0,(100*self.val)/30,10)"""

i = 0

class letter(pygame.sprite.Sprite):
    def __init__(self,x,y,char):
        super().__init__()
        
        self.highlighted = False
        
        self.i = 0
        self.x = x
        self.y = y + .001 * math.sin(i)
        self.letter = char
        self.speed = 50
        
        font = pygame.font.Font('freesansbold.ttf', 32)
        
        self.image = font.render(self.letter, True, (255,255,255))
        
        textRect = self.image.get_rect()
        textRect.center = (self.x // 2, self.y // 2)
        
        self.rect = textRect   
        
    
    def update(self):
        self.y += (random.random()-.5)/30
        self.x += (random.random()-.5)/30
        
        self.rect.center = (self.x // 2, self.y // 2)
            
    def highlight(self,on):
        font = pygame.font.Font('freesansbold.ttf', 32)
        if (on):
            self.highlighted = True
            self.image = font.render(self.letter, True, (255,255,0))
        else:
            self.highlighted = False
            self.image = font.render(self.letter, True, (255,255,255))

sprlist = []

for myletter in random.choice(words):
    ## Use distance formula to not overlap letters
    while True:
        flag = True
        x = random.choice(range(50,550))
        y = random.choice(range(200,400))
        for l in sprlist:
            if (math.sqrt(((l.x-x)**2)+((l.y-y)**2)) < 50):
                flag = False
        if flag:
            break
    
    # Generate letter
        
    new_letter = letter(x,y,myletter)
    sprites.add(new_letter)
    sprlist.append(new_letter)
    
i = 0        

typed = ""

score = 0
score_func = lambda l : math.floor(1.5**l)

font = pygame.font.Font('freesansbold.ttf', 48)

time_left = 300

clock = pygame.time.Clock()
words_formed = 0

while True:
    screen.fill([0, 0, 0])
    
    bar = pygame.Rect(0,0,300-time_left,10)
    
    pygame.draw.rect(screen,(255,255,0),bar)
    
    scorekeeper = font.render(str(score),True,(255,255,255))
    screen.blit(scorekeeper,[0,15])
    
    sprites.update()
    sprites.draw(screen)    
    
    for event in pygame.event.get():
        
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_RETURN):
                
                to_remove = []
                
                if typed in words and len(typed) >= 3:
                    score += score_func(len(typed))
                    words_formed += 1
                    
                    #Delete letters when valid word
                    for spr in sprlist:
                        if (spr.highlighted):
                            sprites.remove(spr)
                            to_remove.append(spr)
                    
                    for spr in to_remove:
                        sprlist.remove(spr)
                        
                #Remove highlighting when invalid word
                for spr in sprlist:
                    spr.highlight(False)
                    
                typed = ""
                
            for spr in sprlist:
                if pygame.key.key_code(spr.letter) == event.key:
                    if (not spr.highlighted):
                        typed += spr.letter
                        spr.highlight(True)
                        break
    
    
    clock.tick(60)
    
    if len(sprlist) == 0:
        score += 50
        time_left = 1
    
    time_left -= 1
    
    if time_left == 0:
        if words_formed == 0:
            break
        
        words_formed = 0
        
        sprlist.clear()
        sprites.empty()
        time_left = 300
        
        for myletter in random.choice(words):
            while True:
                flag = True
                x = random.choice(range(50,550))
                y = random.choice(range(200,400))
                for l in sprlist:
                    if (math.sqrt(((l.x-x)**2)+((l.y-y)**2)) < 50):
                        flag = False
                if flag:
                    break   
            new_letter = letter(x,y,myletter)
            sprites.add(new_letter)
            sprlist.append(new_letter)
        
    pygame.display.update()
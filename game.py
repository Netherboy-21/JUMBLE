import pygame.display
import pygame.locals
import wordlist
import random
import pygame
from string import ascii_lowercase as alphabet
import math

# RANDOM WORD && ANAGRAM GENERATION

words = wordlist.words

orig = random.choice(words)

anagrams = []

orig_l = list(orig)

for word in words:
    orig_l = list(orig)
    if set(word) == set(orig) and len(word) == len(orig):
        for i in word:
            if i not in orig_l:
                break
            orig_l.remove(i)
        anagrams.append(word)
                
    
print(orig,anagrams)

word = list(orig)

jumbled = ""

for i in range(len(word)):
    jumbled += word.pop(random.choice(range(len(word))))

print(jumbled)

# PYGAME GUI

pygame.init()

screen = pygame.display.set_mode((300,300))

"""
logo = pygame.image.load("logo.png").convert()
screen.blit(logo,(0,0))
pygame.transform.scale(screen,(300,300),screen)
"""

sprites = pygame.sprite.Group()

class letter(pygame.sprite.Sprite):
    def __init__(self,x,y,char):
        super().__init__()
        self.x = x
        self.y = y
        self.letter = char
        self.image = pygame.Surface([32,32])
        
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(self.letter, True, (255,255,255))
        textRect = text.get_rect()
        textRect.center = (self.x // 2, self.y // 2)
        
        pygame.draw.rect(self.image,
                         (0,0,0),
                         textRect)
        
        self.rect = self.image.get_rect()        
h = letter(50,75,"h")
sprites.add(h)
i = 0        
        
while True:
    
    i += .001
    
    h.y = h.y + math.sin(i)
    
    sprites.update()
    sprites.draw(screen)
    
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
    
    pygame.display.update()
    
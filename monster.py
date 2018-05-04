import pygame

class Monster(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([20, 20])#specify height, width
        #self.image.fill((255, 0, 0))#this sets background color for square
        self.image = pygame.image.load('./images/monster.png').convert_alpha()
        self.rect = self.image.get_rect()#leave this, inherited, collision depends on this

        self.rect.center = pos
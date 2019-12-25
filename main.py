# using pygame virtual env

import pygame

pygame.init()

win = pygame.display.set_mode((900,900))

pygame.display.set_caption("Bacterialize")

class Position:
  def __init__(self):
    self.x = 0
    self.y = 0

class GameObject:
  def __init__(self):
    self.position = Position()
    self.sprite = []
    self.frameCount = 0

  def setPositionXY(self, x, y):
    self.position.x = x
    self.position.y = y  

  def addSprite(self, image_path):
    self.sprite.append(pygame.image.load(image_path))

  def draw(self):
    if self.frameCount == 0 and self.sprite.__len__() == 1:
      win.blit(self.sprite[0], (self.position.x, self.position.y))


class Bacteria(GameObject):
  def __init__(self):
    super().__init__()

  def setPositionXY(self, x, y):
    super().setPositionXY(x, y)

  def addSprite(self, image_path):
    super().addSprite(image_path)

  def draw(self):
    super().draw()

class Egg(GameObject):
  def __init__(self):
    super().__init__()
    self.isHatched = False
  
  def setPositionXY(self, x, y):
    super().setPositionXY(x, y)

  def addSprite(self, image_path):
    super().addSprite(image_path)

  def draw(self):
    super().draw()

player = Bacteria()
player.addSprite('player.png')

egg = Egg()
egg.addSprite('eggs.png')

run = True
# main loop
while run:
  pygame.time.delay(60)

  # Refresh display
  win.fill((0,0,0))
  egg.draw()
  player.draw()
  pygame.display.update()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

pygame.quit()
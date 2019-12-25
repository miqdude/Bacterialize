# using pygame virtual env

import pygame

pygame.init()

win = pygame.display.set_mode((900,900))

pygame.display.set_caption("Bacterialize")

class Position:
  def __init__(self):
    self.x = 0
    self.y = 0

class Sprite:
  def __init__(self):
    self.images = []
    self.length = len(self.images)
    self.resize = (0,0)
  
  # @param image_path : array or string
  # set image to an object
  def setImages(self, image_path):
    if len(image_path) == 1:
      self.images.append(pygame.image.load(image_path[0]))
    else:
      print("Not supported")

  # draw sprite to screen
  def draw(self, x, y):
    if self.resize == (0,0):
      win.blit(self.images[0], (x, y))
    else:
      # resize the image first
      win.blit(pygame.transform.scale(self.images[0], self.resize), (x,y))

class GameObject:
  def __init__(self):
    self.position = Position()
    self.sprite = Sprite()
    self.speed = 0

  def setPositionXY(self, x, y):
    self.position.x = x
    self.position.y = y  

  def addSprite(self, image_path):
    self.sprite.setImages(image_path)

  def draw(self):
    self.sprite.draw(self.position.x, self.position.y)

  def move(self, direction):
    if (direction == 'UP'):
      self.position.y -= self.speed
    elif (direction == 'DOWN'):
      self.position.y += self.speed
    elif (direction == 'LEFT'):
      self.position.x -= self.speed
    elif (direction == 'RIGHT'):
      self.position.x += self.speed


class Bacteria(GameObject):
  def __init__(self):
    super().__init__()
    self.speed = 5

class Egg(GameObject):
  def __init__(self):
    super().__init__()
    self.isHatched = False

player = Bacteria()
player.addSprite(['player.png'])
player.sprite.resize = (100,100)

egg = Egg()
egg.addSprite(['eggs.png'])
egg.sprite.resize = (50,50)

run = True
# main loop
while run:
  pygame.time.delay(60)

  player.move('DOWN')

  # Refresh display
  win.fill((0,0,0))
  egg.draw()
  player.draw()
  pygame.display.update()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

pygame.quit()
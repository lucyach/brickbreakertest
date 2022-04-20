from processing import *
import random

widthD = 400
heightD = 500


#/*******RGB Class**************/
class RGB:
  def __init__(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b


#/*******Ball Class**************/
class Ball:
  def __init__(self):
    self.ballX = random.randint(0, widthD)
    self.ballY = heightD/2
    self.ballWidth = 16
    self.speedY = 4
    self.speedX = 4
    self.ballColor = RGB(255, 0, 0)

  def move(self):
    self.ballX += self.speedX
    self.ballY +=self.speedY
    
    #bounce off top and side walls
    if self.ballX > widthD - self.ballWidth/2:
      self.speedX  = -abs(self.speedX)
    if self.ballX < self.ballWidth/2:
       self.speedX = abs(self.speedX)
    if self.ballY < self.ballWidth/2:
      self.speedY= abs(self.speedY)
  
  def reset(self):
    self.ballX = random.randint(0, widthD)
    self.ballY = heightD/2
    self.speedY = 4
    self.speedX = 4
  
  def shouldLoseLife(self):
    if self.ballY > heightD - self.ballWidth/2:
        self.speedY = -abs(self.speedY)
        return True
    return False
    
  def collidesWith(self, brick):
    hasHitSomething = False
    
    #check the top of the ball
    if(pointInRect(self.ballX, self.ballY - self.ballWidth/2, brick.blockX, brick.blockY, brick.blockWidth, brick.blockHeight)):
        self.speedY = -self.speedY
        hasHitSomething = True
    
    #check the bottom of the ball
    elif(pointInRect(self.ballX, self.ballY + self.ballWidth/2, brick.blockX, brick.blockY, brick.blockWidth, brick.blockHeight)):
        self.speedY = -self.speedY
        hasHitSomething = True
      
    #check the right of the ball
    elif(pointInRect(self.ballX + self.ballWidth/2, self.ballY, brick.blockX, brick.blockY, brick.blockWidth, brick.blockHeight)):
        self.speedX = -self.speedX
        hasHitSomething = True
        
    #check the left of the ball
    elif(pointInRect(self.ballX - self.ballWidth/2, self.ballY, brick.blockX, brick.blockY, brick.blockWidth, brick.blockHeight)):
        self.speedX = -self.speedX
        hasHitSomething = True
        
    return hasHitSomething


#/*******Block Class**************/
class Block:
  def __init__(self, x, y, width, height, color):
    self.blockX = x
    self.blockY = y
    self.blockWidth = width
    self.blockHeight = height
    self.maxHits = 1
    self.hits = self.maxHits
    self.brickColor = color
    
   #this draws the block on the screen
  def draw(self):
    noStroke()
    fill(self.brickColor.r, self.brickColor.g, self.brickColor.b)
    rect(self.blockX, self.blockY, self.blockWidth, self.blockHeight)
  
  #this moves the block 
  #to be centered on X, Y coordinates
  def move(self, X, Y):
    self.blockX = X - self.blockWidth/2
    self.blockY = Y - self.blockHeight/2
    
    #prevents it from going off screen on the X direction
    if self.blockX + self.blockWidth > widthD:
      self.blockX = widthD - self.blockWidth
    elif self.blockX < 0:
      self.blockX = 0

    #prevents it from going off screen on the the Y direction
    if self.blockY + self.blockHeight > heightD:
      self.blockY=height-blockWidth
    elif self.blockY < 0:
      self.blockY = 0
  
  #allows you to change the number of times an individual block can be hit
  def setMaxHits(self, numberOfHits):
    self.maxHits=numberOfHits
    self.hits = self.maxHits
  
  #tells you if the brick can be hit more
  #returns 0 if the brick needs to be removed
  #useful if you want the brick hit multiple times
  def getHits(self):
   return self.hits


#generic collision detection function
def pointInRect(pt_x, pt_y, rect_x, rect_y, rect_w, rect_h):
  if (pt_x > rect_x) and (pt_x < rect_x + rect_w) and (pt_y > rect_y) and (pt_y < rect_y + rect_h):
    return True
  else:
    return False
    
    
    
    
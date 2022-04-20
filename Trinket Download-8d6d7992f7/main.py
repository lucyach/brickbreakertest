from processing import *
from classes import RGB
from classes import Ball
from classes import Block

#non-changing variables
width = 400
height = 500
spaceBetweenBricks = 5
numberOfBricks = 10
numberOfBrickRows = 10
spaceFromCeiling = 20 #space between the first row of bricks and the ceiling
brickWidth = (width-(numberOfBricks-1)*spaceBetweenBricks)/numberOfBricks
brickHeight = 10
brickColors = [RGB(255, 0,0), RGB(255, 183, 0), RGB(255,255,0), RGB(0,255,0), RGB(0,0,255), RGB(156,0,255), RGB(255, 0,0), RGB(255,183, 0), RGB(255,255,0), RGB(0,255,0)]


#changing variables
basketOfBricks= []
class gameState:
  score = 0
  lives = 3
  hasLost = False
  hasWon = False
gs = gameState()


#Paddle is an object of type Block, similar to the bricks
paddle = Block(width/2, height-50, 70, 20, RGB(255, 0, 255))
balls = [Ball(), Ball(), Ball()]



#initialize all the bricks
def setupBricks():
  for rowNumber in range(numberOfBrickRows):
      for brickNumber in range(numberOfBricks):
        brickColor = brickColors[rowNumber]
        brickY = spaceFromCeiling + (brickHeight+spaceBetweenBricks)*rowNumber
        brickX = (brickWidth+spaceBetweenBricks)*brickNumber
        basketOfBricks.append(Block(brickX, brickY, brickWidth, brickHeight, brickColor))

  for brickNumber in range(90, 99):
    basketOfBricks[brickNumber].setMaxHits(3)

def drawBricks(): 
  for brickNumber in range(len(basketOfBricks)):
    brick = basketOfBricks[brickNumber]
    brick.draw()


def checkBrickCollisions(): 
  for ball in balls:
    for brickNumber in range(len(basketOfBricks)):
      brick = basketOfBricks[brickNumber]
      if(ball.collidesWith(brick)):
        brick.hits -= 1
        if(brick.hits ==0):
          basketOfBricks.remove(brick)
          if basketOfBricks[brickNumber] <90:
            gs.score = gs.score + 10
          else:
            gs.score += 30
        return #don't let it hit more than one brick at a time


def drawBall():
  for ball in balls:
    noStroke()
    fill(ball.ballColor.r, ball.ballColor.g, ball.ballColor.b)
    ellipse(ball.ballX, ball.ballY, ball.ballWidth, ball.ballWidth)

  

def moveBall():
  for ball in balls:
    ball.move()
    if(ball.shouldLoseLife()):
      gs.lives = gs.lives - 1
      for ball in balls:
        ball.reset()


def displayText(message, x, y, isCentered):
  fill(0)
  textSize(25)
  textX = x
  if (isCentered):
    widthText = textWidth(message)
    textX = (width-widthText)/2
  text(message, textX, y)


def checkWinOrLose():
  if(gs.score == numberOfBricks*numberOfBrickRows*10):
    gs.hasWon = True
    
  if(gs.lives==0):
    gs.hasLost = True


def displayLabels():
  displayText("Score: "+ str(gs.score), 5, height-2, False)
  
  livesLabel = "Lives: " + str(gs.lives)
  displayText(livesLabel, width-textWidth(livesLabel)-5, height-2, False)
  
  if(gs.hasWon):
    displayText("You win!", 0, height/2, True)
  
  if(gs.hasLost):
    displayText("You lose!", 0, height/2, True)


def wipeScreen():
  background(240, 240, 240)


def setup():
  size(width, height)
  wipeScreen()
  setupBricks()
  frameRate(30)


def draw():
  for ball in balls:
    if not gs.hasLost and not gs.hasWon:
      wipeScreen()
      
      #move everything
      moveBall()
      paddle.move(mouseX, height-50)
  
      #check conditions
      checkBrickCollisions()
      if(ball.collidesWith(paddle)):
        #always set the ball movement back up
        ball.speedY = -abs(ball.speedY)
      if(ball.collidesWith(paddle)):
        ball.speedY = -abs(ball.speedY)
      checkWinOrLose()
      
      #draw everything
      drawBricks()
      drawBall()
      paddle.draw()
      displayLabels()

      
run()
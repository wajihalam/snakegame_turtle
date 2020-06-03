# This is a simple ping pong game using turtle

########################################################################################################################
##### Author: Mohammad Wajih Alam ######################################################################################
##### Version: 1.0 #####################################################################################################
########################################################################################################################


# importing  turtle module. This module is great for starting with games.
import winsound
import turtle

wn = turtle.Screen() # create a window
wn.title("Ping Pong by Wajih") # Giving the screen a title
wn.bgcolor("green") # changing background color to green. As the background of a ping pong table is green
wn.setup(width=800, height= 600) # Controlling the size of the window
wn.tracer(0) # tracer basically stops the window from updating automatically

########################################### Initial Score ##############################################################

player_score_a = 0
player_score_b = 0

############################################ Bat one ###################################################################

bat_one = turtle.Turtle() # Turtle is the class name.
bat_one.speed(0) # Animation speed. 0 makes the maximum speed.
bat_one.shape("square") # Animation shape
bat_one.color("red") # bat color
bat_one.shapesize(stretch_wid=5, stretch_len=1) # we want to make it rectangular, instead of square
bat_one.penup() # we don't want turtle to draw line automatically, so we write the below code
bat_one.goto(-350, 0) # position of the bat one

###################################### Moving bat one up and down ######################################################

def bat_one_up():
    y = bat_one.ycor()
    y += 20
    bat_one.sety(y)

def bat_one_down():
    y = bat_one.ycor()
    y -= 20
    bat_one.sety(y)

# keyboard binding
wn.listen()
wn.onkey(bat_one_down, "s")
wn.onkey(bat_one_up, "w")



##################################################### Bat two ##########################################################

bat_two = turtle.Turtle() # Turtle is the class name.
bat_two.speed(0) # Animation speed. 0 makes the maximum speed.
bat_two.shape("square") # Animation shape
bat_two.color("red") # bat color
bat_two.shapesize(stretch_wid=5, stretch_len=1) # we want to make it rectangular, instead of square
bat_two.penup() # we don't want turtle to draw line automatically, so we write the below code
bat_two.goto(+350, 0) # position of the bat one

###################################### Moving bat two up and down ######################################################

def bat_two_up():
    y = bat_two.ycor()
    y += 20
    bat_two.sety(y)

def bat_two_down():
    y = bat_two.ycor()
    y -= 20
    bat_two.sety(y)

# keyboard binding
wn.listen()
wn.onkey(bat_two_down, "Down")
wn.onkey(bat_two_up, "Up")


################################################################ Ball ##################################################


ball = turtle.Turtle() # Turtle is the class name.
ball.speed(0) # Animation speed. 0 makes the maximum speed.
ball.shape("circle") # Animation shape
ball.color("black") # bat color
ball.penup() # we don't want turtle to draw line automatically, so we write the below code
ball.goto(0, 0) # position of the bat one
ball.dx = 0.1 ### here 0.1 means, that the ball will move by 0.1 pixel. You might need to adjust according to your monitor
ball.dy = -0.1


############################################## Displaying score on screen ##############################################

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


############ Main game loop. Every game needs one. This is where the main meat of the game goes in. ####################

while True:

    wn.update() # update=> updates the screen, every time when the loop runs.

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # restrict the ball within the border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(player_score_a, player_score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(player_score_a, player_score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # ball and bat collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bat_two.ycor() + 40 and ball.ycor() > bat_two.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bat_one.ycor() + 40 and ball.ycor() > bat_one.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)










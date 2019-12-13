import turtle as trtl
import random 

Daedalus = trtl.Turtle()
player = trtl.Turtle()
player.penup()

Daedalus.pensize(3)
Daedalus.speed(0)
Daedalus.ht()

x = 0
distance = 40
barrier_width = 20
gate_width= 20


def draw_Gate():
    Daedalus.penup()
    Daedalus.forward(gate_width)
    Daedalus.pendown()

def draw_Barrier():
    Daedalus.left(90)
    Daedalus.forward(barrier_width*2)
    Daedalus.backward(barrier_width*2)
    Daedalus.right(90)

while (x < 30):
    if x >4:  
        gate = random.randint(gate_width, distance - 2*gate_width)
        barrier = random.randint(2*barrier_width, distance - 2* gate_width)
        if gate < barrier:
            Daedalus.forward(gate)
            draw_Gate()
            Daedalus.forward(barrier - gate - gate_width)
            draw_Barrier()
            Daedalus.forward(distance - barrier )
        else:
            Daedalus.forward(barrier)
            draw_Barrier()
            Daedalus.forward(gate - barrier)
            draw_Gate()
            Daedalus.forward(distance - gate - gate_width)
    Daedalus.left(90)
    distance += barrier_width
    x = (x +1)

def Up():
    player.setheading(90)
    player.forward(10)

def Down():
    player.setheading(270)
    player.forward(10)
    
def Left():
    player.setheading(180)
    player.forward(10)


def Right():
    player.setheading(0)
    player.forward(10)






wn = trtl.Screen()
wn.onkeypress(Right, "Right")
wn.onkeypress(Left, "Left")
wn.onkeypress(Up,"Up")
wn.onkeypress(Down,"Down")
wn.listen()
wn.mainloop()

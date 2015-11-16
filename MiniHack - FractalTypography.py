import turtle #Turtleswag
from random import randrange

myTurtle = turtle.Turtle()

dictOfDensity = { 0 : -1, "A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "T": 15, "S": 16, "U": 17}

lettersList = [[[[0,0],[0,50]], [[0,50],[0,100]], [[0,50],[100,50]], [[0,100],[100,100]], [[100,100],[100,50]], [[100,50],[100,0]]],
               [[[0,0],[0,50]], [[0,50],[0,100]], [[0,0],[75,0]], [[0,50],[75,50]], [[0,100],[75,100]],[[75,100],[100,75]], [[100, 75],[75,50]], [[75,50],[100,25]], [[100,25],[75,0]]], 
               [[[0,0],[100,0]], [[0,0],[0,100]], [[0,100],[100,100]], [[100,0],[100,0]]],
               [[[0, 0],[0, 100]], [[0,0],[75,0]], [[0,100],[75,100]], [[75,100],[100,75]], [[100,75],[100,25]], [[100,25],[75,0]]],
               [[[0, 0],[0, 100]], [[0,100], [100, 100]], [[0, 0], [100, 0]], [[0, 50], [100, 50]]],
               [[[0, 0],[0, 100]], [[0,100], [100, 100]], [[0, 50], [100, 50]]],
               [[[75,75],[50,100]], [[50,100],[25,100]],[[25,100],[0,75]], [[0,75],[0,25]], [[0,25],[25,0]], [[25,0],[75,0]], [[75,0],[75,25]], [[75,25],[50,25]], [[50,25],[100,25]]],
               [[[0,0],[0,50]], [[0,50],[0,100]], [[0,50],[100,50]], [[100,100],[100,50]], [[100,50],[100,0]]],
               [[[0,0],[50,0]], [[50,0],[100,0]], [[50,0],[50,50]], [[50,50],[50,100]], [[0,100],[50,100]], [[50,100],[100,100]]],
               [[[0,25],[25,0]], [[25,0],[50,0]], [[50,0],[50,50]], [[50,50],[50,100]], [[0,100],[100,100]]],
               [[[0,0],[0,100]], [[0,50],[25,50]], [[25,50],[75,100]], [[25,50],[75,0]]],
               [[[0,100],[0,50]], [[0,50],[0,0]], [[0,0],[25,0]], [[25,0],[100,0]]],
               [[[0,0],[0,25]], [[0,25],[0,100]], [[0,100],[50,50]], [[50,50],[100,100]], [[100,100],[100,50]], [[100,50],[100,0]]],
               [[[0,0],[0,25]], [[0,25],[0,100]], [[0,100],[50,50]], [[50,50],[100,0]], [[100,0],[100,50]], [[100,50],[100,100]]],
               [[[0,25],[0,75]], [[0,75],[25,100]], [[25,100],[75,100]], [[75,100],[100,75]], [[100,75],[100,25]], [[100,25],[75,0]], [[75,0],[25,0]], [[25,0],[0,25]]],
               [[[50,0],[50,50]], [[50,50],[50,100]], [[0,100],[100,100]]],
               [[[0, 0],[100, 0]],[[100,0],[100,50]], [[100,50],[0,50]], [[0,50],[0,100]], [[0,100],[100,100]]],
               [[[0, 100],[0, 0]],[[0,0],[100,0]], [[100,0],[100,100]]]]

#O = [[[0,0],[0,100]], [[0,100],[100,100]], [[100,100],[100,0]], [[100,0],[0,0]]]
#N = [[[0,0],[0,100]], [[0,100],[100,0]], [[100,0],[100,100]]]


char = input("Enter letter between A and J: ")

def tree(branchLen,t):
    if branchLen > 5:
        #randTurn = randrange(1, 90)
        #randReverse = randTurn*2
        #To make a fractal that is random replace the code inside .forward() and .right() with randTurn and the code inside .left() with randReverse and uncomment lines 34 and 35       
        myTurtle.forward(branchLen)
        myTurtle.right(60)
        tree(branchLen-5,myTurtle)
        myTurtle.left(120)
        tree(branchLen-5,myTurtle)
        myTurtle.right(60)
        myTurtle.backward(branchLen)

def main():
    #randlength = randrange(20, 50)
    myTurtle.speed(0)
    myWin = turtle.Screen()
    myTurtle.color("red")
    myTurtle.left(180)
    myTurtle.down()
    #tree(randlength,myTurtle)
    tree(35,myTurtle)
    myTurtle.up()

    
myTurtle.up()

offset = (-75*len(char))+25
print(offset)
print(len(char))
                                                                                                  

for j in range (len (char)):
    for i in range(len (lettersList[dictOfDensity[char[j]]])):
        lettersList[dictOfDensity[char[j]]][i][0][0] += (offset+(150*j))
        lettersList[dictOfDensity[char[j]]][i][1][0] += (offset+(150*j))
    for i in range(len (lettersList[dictOfDensity[char[j]]])):
        myTurtle.speed(0)
        myTurtle.pensize(1)
        myTurtle.color("black")
        myTurtle.goto(lettersList[dictOfDensity[char[j]]][i][0])
        main()
        myTurtle.goto(lettersList[dictOfDensity[char[j]]][i][0])
        myTurtle.down()
        myTurtle.goto(lettersList[dictOfDensity[char[j]]][i][1])
        myTurtle.up()

    main()
    for i in range(len (lettersList[dictOfDensity[char[j]]])):
        myTurtle.pensize(8)
        myTurtle.speed(0)
        myTurtle.goto(lettersList[dictOfDensity[char[j]]][i][0])
        myTurtle.down()
        myTurtle.goto(lettersList[dictOfDensity[char[j]]][i][1])
        myTurtle.up()
    


import threading
from turtle import *
from random import *
from time import *

# setup(1000, 1000)
title("Parallel Processing Project")
bgcolor("black")
speed(0)
hideturtle()
up()

S = []
T = []
Height = []
N = 10

CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ("Arial", FONT_SIZE, "bold")


def generate(x, y):
    global Height
    global T
    button1.reset()

    for i in range(N):
        begin_poly()
        setheading(90)
        D = randint(100, 800)
        fd(D)
        Height.append(D)
        setheading(0)
        fd(25)
        setheading(270)
        fd(D)
        setheading(180)
        fd(25)
        end_poly()
        S.append(get_poly())

    for i in range(N):
        register_shape("rec{}".format(i), S[i])
        T.append(Turtle("rec{}".format(i)))
        T[i].speed(0)
        T[i].up()
        T[i].color("green")
        T[i].setheading(90)
        T[i].goto(-250 + i * 50, -450)
        T[i].speed(1)

    global button2
    button2 = Turtle()
    button2.hideturtle()
    button2.speed(0)
    button2.shape("circle")
    button2.color("orange")
    button2.penup()
    button2.goto(80, 400)
    button2.write("Bubble Sort", align="center", font=FONT)
    button2.sety(400 + CURSOR_SIZE + FONT_SIZE)
    button2.showturtle()
    button2.onclick(Bub)

    global button3
    button3 = Turtle()
    button3.hideturtle()
    button3.speed(0)
    button3.shape("circle")
    button3.color("orange")
    button3.penup()
    button3.goto(-80, 400)
    button3.write("Selection Sort", align="center", font=FONT)
    button3.sety(400 + CURSOR_SIZE + FONT_SIZE)
    button3.showturtle()
    button3.onclick(selectionSort)

    global button4
    button4 = Turtle()
    button4.hideturtle()
    button4.speed(0)
    button4.shape("circle")
    button4.color("orange")
    button4.penup()
    button4.goto(-80, 350)
    button4.write("Add Parallel", align="center", font=FONT)
    button4.sety(350 + CURSOR_SIZE + FONT_SIZE)
    button4.showturtle()
    button4.onclick(parallelSelectionSort)

    global button5
    button5 = Turtle()
    button5.hideturtle()
    button5.speed(0)
    button5.shape("circle")
    button5.color("orange")
    button5.penup()
    button5.goto(80, 350)
    button5.write("Add Parallel", align="center", font=FONT)
    button5.sety(350 + CURSOR_SIZE + FONT_SIZE)
    button5.showturtle()
    button5.onclick(ParallelBub)

    global txt1
    txt1 = Turtle()
    txt1.hideturtle()
    txt1.speed(0)
    txt1.color("white")
    txt1.up()
    txt1.goto(-400, 350)
    txt1.write("Time : 0 sec", font=("Arial", 18, "bold"))


button1 = Turtle()
button1.hideturtle()
button1.speed(0)
button1.shape("circle")
button1.color("red")
button1.penup()
button1.goto(0, 400)
button1.write("Generate", align="center", font=FONT)
button1.sety(400 + CURSOR_SIZE + FONT_SIZE)
button1.showturtle()
button1.onclick(generate)

list = Height
array = Height
size = N


def swap_positions(step, min_idx):
    jloc = T[step].position()
    j1loc = T[min_idx].position()

    T[step].speed(2)
    T[min_idx].speed(2)

    thread1 = threading.Thread(target=T[step].goto, args=(j1loc,))
    thread1.start()

    thread2 = threading.Thread(target=T[min_idx].goto, args=(jloc,))
    thread2.start()

    T[step].color("red")
    T[min_idx].color("blue")


def Bub(x, y):
    button2.reset()
    button3.reset()
    button4.reset()
    button5.reset()
    start = time()

    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                T[j].color("red")
                T[j + 1].color("blue")

                jloc = T[j].position()
                j1loc = T[j + 1].position()

                T[j].goto(j1loc)
                T[j + 1].goto(jloc)

                T[j], T[j + 1] = T[j + 1], T[j]

                list[j], list[j + 1] = list[j + 1], list[j]

                T[j].color("green")
                T[j + 1].color("green")

    end = time()
    Q = end - start
    txt1.clear()
    txt1.write("Time : {:.2f} sec".format(Q), font=("Arial", 18, "bold"))


def ParallelBub(x, y):
    button2.reset()
    button3.reset()
    button4.reset()
    button5.reset()
    start = time()

    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                T[j].color("red")
                T[j + 1].color("blue")

                swap_positions(j, j + 1)

                T[j], T[j + 1] = T[j + 1], T[j]

                list[j], list[j + 1] = list[j + 1], list[j]

                T[j].color("green")
                T[j + 1].color("green")

    end = time()
    Q = end - start
    txt1.clear()
    txt1.write("Time : {:.2f} sec".format(Q), font=("Arial", 18, "bold"))


def selectionSort(x, y):
    button2.reset()
    button3.reset()
    button4.reset()
    button5.reset()
    start = time()

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i

        T[step].color("red")
        T[min_idx].color("blue")

        jloc = T[step].position()
        j1loc = T[min_idx].position()

        T[step].speed(2)
        T[min_idx].speed(2)

        T[step].goto(j1loc)
        T[min_idx].goto(jloc)

        T[step], T[min_idx] = T[min_idx], T[step]

        array[step], array[min_idx] = array[min_idx], array[step]

        T[step].color("green")
        T[min_idx].color("green")

    end = time()
    Q = end - start
    txt1.clear()
    txt1.write("Time : {:.2f} sec".format(Q), font=("Arial", 18, "bold"))


def parallelSelectionSort(x, y):
    button2.reset()
    button3.reset()
    button4.reset()
    button5.reset()
    start = time()

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i

        T[step].color("red")
        T[min_idx].color("blue")

        swap_positions(step, min_idx)

        T[step], T[min_idx] = T[min_idx], T[step]

        array[step], array[min_idx] = array[min_idx], array[step]

        T[step].color("green")
        T[min_idx].color("green")

    end = time()
    Q = end - start
    txt1.clear()
    txt1.write("Time : {:.2f} sec".format(Q), font=("Arial", 18, "bold"))


done()

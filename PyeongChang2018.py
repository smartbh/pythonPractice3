#Pyeongchang2018.py
import random

colorlist = ['red', 'blue', 'orange', 'black', 'green']

x = input("텍스트를 입력하세요") #PyeongChang2018 입력

import turtle
t=turtle.Turtle()
t.goto(-100,0)
t.shape("turtle")
t.width(10)
t.color(colorlist[0])
t.forward(150)
t.up()#ㅍ 빨간색 부분


t.goto(-60,15)
t.down()
t.width(10)
t.color(colorlist[3])
t.left(90)
t.forward(80)
t.up() #ㅍ 검정색 부분

t.goto(10,15)
t.down()
t.width(10)
t.color(colorlist[4])
t.forward(80)
t.up() #ㅍ 초록색부분

t.goto(-100,110)
t.down()
t.width(10)
t.color(colorlist[1])
t.right(90)
t.forward(150)
t.up() #ㅍ 파란색 부분

# * 부분 시작

t.goto(150,150)
t.down()
t.width(10)
t.color(colorlist[4])
t.left(20)
t.forward(60)
t.up() # * 초록색부분

t.goto(150,150)
t.down()
t.width(10)
t.color(colorlist[3])
t.left(70)
t.forward(60)
t.up() # * 검정색부분

t.goto(150,150)
t.down()
t.width(10)
t.color(colorlist[2])
t.left(70)
t.forward(60)
t.up() # * 노란색부분

t.goto(150,150)
t.down()
t.width(10)
t.color(colorlist[0])
t.left(70)
t.forward(60)
t.up() # * 빨간색 부분

t.goto(150,150)
t.down()
t.width(10)
t.color(colorlist[1])
t.left(70)
t.forward(60)
t.up() # * 파란색 부분

#오륜기 시작

t.goto(-50,-200)
t.down()
t.width(4)
t.color(colorlist[1])
t.circle(26)
t.up() #오륜기 파란색

t.goto(10,-200)
t.down()
t.width(4)
t.color(colorlist[3])
t.circle(26)
t.up() #오륜기 검정색

t.goto(70,-200)
t.down()
t.width(4)
t.color(colorlist[0])
t.circle(26)
t.up() #오륜기 빨간색

t.goto(-20,-220)
t.down()
t.width(4)
t.color(colorlist[2])
t.circle(26)
t.up() #오륜기 노란색

t.goto(40,-220)
t.down()
t.width(4)
t.color(colorlist[4])
t.circle(26)
t.up() #오륜기 초록색

t.goto(0,-100)
t.color(colorlist[3])
t.write(x,False,"center",("",30))
#평창2018 출력

random.shuffle(colorlist)
#리스트 색상 뒤섞음

t.goto(250,-250)
t.color(colorlist[0])
t.write("1791258 이병헌", False, "center", ("",15))
#학번, 이름 출력

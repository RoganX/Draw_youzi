"""
creat by 啊牛
"""
import turtle as t
from xiaowo import xiaowo
# t.setworldcoordinates(-400, -500, 500, 250)

pink1 = (255,250,255)
# # 设置速度
t.speed(100)  # 速度
t.colormode(255)
t.delay(10)  # 延迟
# t.tracer(False)


#hair 
t.penup()
t.goto(85, -171)
t.pendown()
t.fillcolor(255, 220, 250)
t.begin_fill()
t.setheading(-70)
t.circle(300, 25)
t.setheading(190)
t.circle(-600,16)
t.penup()
t.goto(-100, -160)
t.end_fill()
t.penup()
t.goto(-70,-174)
t.pendown()
t.begin_fill()
t.setheading(-80)
t.circle(200, 38)
t.setheading(-170)
t.circle(-400,17)
t.penup()
t.goto(-210,-30)
t.goto(-150, -30)
t.end_fill() 
 


# rightear
t.penup()
t.goto(60, 162)
t.setheading(70)
t.begin_fill()
t.fillcolor(pink1)
t.pendown()
t.circle(-230,10)
t.setheading(0)
t.circle(15, 300)
t.setheading(-120)
t.circle(220, 10)
t.end_fill()



#lefthair
t.penup()
t.goto(-200,-150)
t.setheading(90)
t.pendown()
t.begin_fill()
t.fillcolor(pink1)
t.circle(80, -145)
t.setheading(10)
t.circle(120, 57)
t.setheading(60)
t.circle(125,30)
t.setheading(85)
t.circle(-315, 46)
t.penup()
t.setheading(32)
t.circle(-180, 45)
t.end_fill()
# leftear
t.penup()
t.goto(-113, 128)
t.setheading(103)
t.pendown()
t.begin_fill()
t.fillcolor(pink1)
t.circle(200,28)
t.setheading(160)
t.circle(-15, 290)
t.setheading(-47)
t.circle(-200,26)
t.end_fill()

#righthair
t.penup()
t.goto(-106, 165)
t.setheading(27)
t.pendown()
t.circle(-180, 60)
t.begin_fill()
t.circle(-260, 50)
t.setheading(-78)
t.circle(-60, 150)
t.setheading(6)
t.circle(78, 33)
t.setheading(65)
t.circle(60, 23)
t.setheading(95)
t.circle(310, 49)
t.end_fill()

#face 
t.penup()
t.goto(108, 0)
t.setheading(-90)
t.pendown()
t.circle(1300, 2)
t.setheading(-80)
t.circle(80, 20)

#jaw
t.penup()
t.goto(125, -103)
t.setheading(-66)
t.begin_fill()
t.fillcolor(255,255,255)
t.pendown()
t.circle(-38, 60)
t.circle(-90, 10)
t.setheading(-140)
t.circle(-150, 70)
t.penup()
t.setheading(90)
t.circle(30, 90)
t.end_fill()

#mouth
t.penup()
t.goto(10,-80)
t.setheading(-32)
t.pendown()
t.circle(-67, 74)

t.penup()
t.goto(32, -106)
t.setheading(90)
t.pendown()
t.circle(-13, 240)
t.setheading(20)
t.circle(-10, 240)
t.goto(40, -130)


#lefteye

t.penup()
t.goto(-65,0)
t.setheading(0)
t.pendown()
t.begin_fill()
t.color(0,0,0)
t.circle(-180,15)
t.setheading(-88)
t.circle(-60,18)
t.setheading(170)
t.circle(180, 16)
t.goto(-65,0)
t.end_fill()


#righteye
t.penup()
t.goto(50, -20)
t.pendown()
t.begin_fill()
t.goto(85, 5)
t.goto(85, -17)
t.goto(67, -25)
t.goto(50, -20)
t.end_fill()

#below lefteye

t.penup()
t.goto(-65, -48)
t.setheading(75)            # 朝上（正北方向）
t.pendown()
t.color(255,120,147)
t.begin_fill()
len = 0.05
for k in range(2):
    for j in range(60):        # 重复执行120次
        if j < 30:              # 当j<30，也就是画前一半的弧线
            len += 0.06        # 让速度越走越快
        else:                   # 画后一半弧线
            len -= 0.06          # 让速度越走越慢
        t.forward(len)
        t.right(3)
t.end_fill()

#below righteye
t.penup()
t.goto(50, -50)
t.setheading(30)            # 朝上（正北方向）
t.pendown()
t.begin_fill()
t.circle(-45, 55)
t.circle(-5,180)
t.setheading(-162)  
t.circle(-50, 45)
t.end_fill()

#hair middle
t.color(0,0,0)
t.penup()
t.goto(127, -7)
t.pendown()
t.begin_fill()
t.fillcolor(pink1)
t.setheading(155)
t.circle(-200, 30)
t.setheading(-80)
t.circle(-130, 40)
t.setheading(170)
t.circle(-60, 20)
t.setheading(148)
t.circle(-140, 45)
t.setheading(-110)
t.circle(-250, 25)
tmp1 = t.position()
t.setheading(90)
t.circle(-240, 59)
t.setheading(-36.5)
t.circle(-310, 43)
t.end_fill()


#hair left

t.penup()
t.goto(tmp1)
t.pendown()
t.begin_fill()
t.setheading(-85)
t.circle(50, 90)
t.setheading(-90)
t.circle(-38, 135)
t.setheading(145)
t.circle(-90, 70)
tmp2 = t.position()
t.setheading(-160)
t.circle(-100, 20)
t.setheading(10)
t.circle(35, 60)
t.setheading(80)
t.circle(-230, 40)
t.penup()
t.circle(-63,54)
t.setheading(-151)
t.circle(225, 40)
t.end_fill()

# hair 
t.penup()
t.goto(-85,-106)
t.setheading(-75)
t.pendown()
t.begin_fill()
t.circle(300, 3)
t.setheading(-80)
t.circle(23, 110)
t.setheading(-90)
t.circle(-38, 140)
t.setheading(133)
t.circle(-105, 52)
t.setheading(-58)
t.circle(80,46)
t.end_fill()

#hair decorate
t.penup()
t.goto(tmp2)
t.pendown()
t.begin_fill()
t.color(0,0,0)
t.setheading(-160)
t.circle(-100, 15)
t.setheading(-90)
t.circle(-50,65)
t.setheading(-170)
t.circle(-60,18)
t.circle(-1700,1)
t.setheading(-25)
t.goto(-180, -80)
tmp3 = t.position()
t.circle(5, 50)
t.goto(tmp2)
t.end_fill()    


# hair 2
t.penup()
t.goto(-150, -61)
t.pendown()
t.begin_fill()
t.fillcolor(255,228, 245)
t.setheading(-97)
t.circle(500, 28)
t.setheading(185)
t.circle(-60, 55)
t.circle(-130, 45)
t.setheading(93)
t.circle(-1000, 6.5)
t.goto(tmp3)
t.circle(5, 50)
t.goto(tmp2)
t.circle(5, 50)
t.goto(tmp2)
t.setheading(-106)
t.circle(90, 42)
t.end_fill()

# hair right
t.penup()
t.goto(130, -102)
t.setheading(-80)
t.pendown()
t.begin_fill()
t.fillcolor(pink1)
t.circle(-40, 70)
t.setheading(196)
t.circle(-60, 40)
t.setheading(-40)
t.circle(100, 26)
t.setheading(-27)
t.circle(32, 120)
t.setheading(83)
t.circle(200, 10)
t.setheading(-155)
t.circle(-60,28)
t.end_fill()

#decorate up
t.penup()
t.goto(-50, 130)
t.setheading(29)
t.pendown()
t.begin_fill()
t.fillcolor(0,0,0)
t.circle(-130, 47)
t.setheading(-50)
t.circle(-300, 3)
t.setheading(159)
t.circle(140, 53)
t.goto(-50, 130)
t.end_fill()

#decorate down
t.penup()
t.goto(-73, 100)
t.setheading(30)
t.pendown()
t.begin_fill()
t.circle(-180, 48)
t.setheading(-67)
t.circle(50, 10)
t.setheading(200)
t.circle(-20, 60)
for i in range(3):
    t.setheading(-145 + i * 5)
    t.circle(-35, 70 - i * 2)
t.setheading(-120)
t.circle(-28, 58)
t.goto(-73, 100)
t.end_fill()


t.penup()
t.goto(250,-250)

def eggs():
    cnt = 0
    flag = True
    def f(x,y):
        nonlocal cnt 
        if cnt > 19: 
            cnt += 1
            return
        cnt += 1
        t.goto(x,y)
        t.write("Tui~", True, align="center", font= ('Cooper Black', 40, 'normal'))
        if cnt == 20:
            t.clear()
            xiaowo(flag)
    def nofinger():
        nonlocal flag
        flag = False
        return
    t.onkeyrelease(nofinger, 'f')       
    t.onscreenclick(f)
    t.listen()
    
eggs()

t.goto(600,-600)
t.done()



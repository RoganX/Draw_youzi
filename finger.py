
"""
Created on Wed Mar 23 12:10:38 2022

@author: 阿牛
"""

import turtle as t
class finger():
    def __init__(self):
    # # 设置速度
        t.speed(100)  # 速度
        t.colormode(255)
        t.delay(10)  # 延迟
        # t.tracer(False)
        tmp11 = [100,-80]
        color0 = (255, 218, 185)
        color1 = (253, 245, 230)
        ##大拇指
        t.penup()
        t.goto([tmp11[0] - 52, tmp11[1] - 34])
        t.pendown()
        t.setheading(-105)
        t.begin_fill()
        t.fillcolor(color0)
        t.circle(500, 7)
        t.circle(5, 60)
        t.setheading(-70)
        t.circle(500,6)
        t.circle(15, 60)
        t.fd(55)
        t.setheading(10)
        t.circle(25, 173)
        t.fd(35)
        t.bk(15)
        t.setheading(120)
        t.circle(30, 30)
        t.penup()
        tmp15 = [tmp11[0] + 33, tmp11[1] - 125]
        t.goto([tmp15[0], tmp15[1] - 10])
        t.goto(tmp11)
        t.end_fill()
        
        ##食指
        t.penup()
        t.goto(tmp11)
        t.pendown()
        t.begin_fill()
        t.fillcolor(color0)
        t.setheading(-38)
        t.circle(-25, 90)
        t.circle(-35, 120)
        t.circle(-25, 75)
        t.setheading(88)
        t.circle(-40, 85)
        t.setheading(0)
        t.circle(-28, 45)
        for _ in range(3):
            t.setheading(-20)
            t.circle(20,40)
            t.setheading(12)
            t.circle(50,12)
            t.setheading(5)
            t.circle(-30,40)
        t.circle(-30,25)
        t.setheading(-76)
        t.circle(-225, 32)
        
        #其余三指
        t.circle(-22,168)
        t.setheading(95)
        t.circle(-225, 15)
        tmp12 = [tmp11[0] + 101.96,tmp11[1] - 98.48]
        t.penup()
        t.goto(tmp12)
        t.pendown()
        t.setheading(-100)
        t.circle(-26,155)
        t.setheading(95)
        t.circle(-225,16)
        t.penup()
        tmp13 = [tmp11[0] + 52, tmp11[1] - 100]
        t.goto(tmp13)
        t.pendown()
        t.setheading(-100)
        t.circle(-26,160)
        t.setheading(95)
        t.circle(-255,15)
        t.end_fill()
        
        t.penup()
        tmp14 = [tmp11[0] - 50, tmp11[1] - 8]
        t.goto(tmp14)
        t.pendown()
        t.begin_fill()
        t.fillcolor(color1)
        t.setheading(60)
        t.circle(-28, 120)
        t.goto(tmp14)
        t.end_fill()
        
        t.penup()
        t.goto(tmp15)
        t.setheading(160)
        t.pendown()
        t.begin_fill()
        t.circle(14, 220)
        t.goto(tmp15)
        t.end_fill()
        
        t.penup()
        t.goto(0,0)
        
        
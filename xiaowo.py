
"""
Created on Wed Mar 23 20:53:12 2022

@author: 阿牛
"""
from finger import finger
import turtle as t

class xiaowo(): 
    def __init__(self, flag = True):
        ke = (255, 175, 210)
        body = (255,250,255)
        pink = (255, 182, 193)
        shadow = (240, 138, 180)
        # # 设置速度
        t.speed(100)  # 速度
        t.colormode(255)
        t.delay(10)  # 延迟
        tmp21 = [0,0]
        tmp22 = [tmp21[0] - 165.27, tmp21[1] - 83.97]
        tmp23 = [tmp21[0] + 70, tmp21[1] + 110]
        tmp24 = [tmp23[0] + 75, tmp23[1] - 5]
        
        
        
        #ear
        #left
        t.penup()
        t.goto([tmp23[0], tmp23[1] + 86])
        t.pendown()
        t.begin_fill()
        t.fillcolor(body)
        t.setheading(85)
        t.circle(-200,25)
        t.setheading(130)
        t.circle(-10,300)
        t.setheading(-113)
        t.circle(200,25)
        t.end_fill()
        
        #right
        t.penup()
        t.goto([tmp24[0] + 30, tmp24[1] + 55])
        t.pendown()
        t.begin_fill()
        t.fillcolor(body)
        t.setheading(60)
        t.circle(-200,20)
        t.setheading(100)
        t.circle(-10,310)
        t.setheading(-135)
        t.circle(200,20)
        t.end_fill()
        
        #ke
        t.penup()
        t.goto(tmp22)
        t.pendown()
        t.begin_fill()
        t.fillcolor(ke)
        t.setheading(-30)
        t.circle(110, 360)
        t.end_fill()
        
        t.penup()
        t.goto(tmp21)
        t.setheading(130)
        t.pendown()
        t.begin_fill()
        t.fillcolor(body)
        t.circle(-120, 150)
        t.circle(-110,125)
        t.setheading(-80)
        t.circle(500,13)
        t.setheading(-30)
        t.circle(-10,120)
        t.setheading(191)
        t.circle(-900,27)
        t.setheading(33)
        t.circle(-200,20)
        t.setheading(-30)
        t.circle(110, 116)
        t.end_fill()
        #shadow
        t.penup()
        t.goto(tmp22)
        t.pendown()
        t.begin_fill()
        t.color(shadow)
        t.setheading(138)
        t.circle(-110,75)
        t.setheading(25)
        t.circle(-190,33)
        t.setheading(-60)
        t.circle(-80,90)
        t.setheading(150)
        t.circle(-80,32)
        t.setheading(100)
        t.circle(-17,205)
        t.setheading(-90)
        t.circle(5, 180)
        t.circle(30,120)
        t.setheading(-150)
        t.circle(20, 100)
        t.setheading(-70)
        t.circle(60,56)
        t.setheading(-10)
        t.fd(5)
        t.setheading(37)
        t.circle(100,85)
        t.setheading(165)
        t.circle(150,40)
        t.setheading(55)
        t.circle(-110,70)
        t.setheading(153)
        t.circle(110, 178)
        t.end_fill()
        t.color(0,0,0)
        
        
        #eye
        t.penup()
        #left
        t.goto(tmp23)
        t.pendown()
        t.begin_fill()
        t.fillcolor(0,0,0)
        t.setheading(175)
        len = 0.0
        for k in range(2):
            for j in range(60):        # 重复执行120次
                if j < 30:              # 当j<30，也就是画前一半的弧线
                    len += 0.03        # 让速度越走越快
                else:                   # 画后一半弧线
                    len -= 0.03          # 让速度越走越慢
                t.forward(len)
                t.right(3)
        t.end_fill()
        
        tmp25 = [tmp23[0], tmp23[1] + 19]
        t.penup()
        t.goto(tmp25)
        t.pendown()
        t.begin_fill()
        t.fillcolor(255,255,255)
        t.circle(3.5,360)
        t.end_fill()
        
        tmp27 = [tmp23[0], tmp23[1] - 13]
        t.penup()
        t.goto(tmp27)
        t.begin_fill()
        t.color(pink)
        t.pendown()
        t.setheading(-68)
        t.circle(-15, 360)
        t.end_fill()
        t.color(0,0,0)
        
        #right
        t.penup()
        t.goto(tmp24)
        t.pendown()
        t.begin_fill()
        t.fillcolor(0,0,0)
        t.setheading(170)
        len = 0.0
        for k in range(2):
            for j in range(60):        # 重复执行120次
                if j < 30:              # 当j<30，也就是画前一半的弧线
                    len += 0.03        # 让速度越走越快
                else:                   # 画后一半弧线
                    len -= 0.03          # 让速度越走越慢
                t.forward(len)
                t.right(3)
        t.end_fill()        
            
        tmp26 = [tmp24[0] + 2, tmp24[1] + 18]
        t.penup()
        t.goto(tmp26)
        t.pendown()
        t.begin_fill()
        t.fillcolor(255,255,255)
        t.circle(3.7,360)
        t.end_fill()
            
        tmp28 = [tmp24[0], tmp24[1] - 13]
        t.penup()
        t.goto(tmp28)
        t.begin_fill()
        t.color(pink)
        t.pendown()
        t.setheading(-90)
        t.circle(15, 360)
        t.end_fill()
        t.color(0,0,0) 
        
        
        
        #mouth
        t.penup()
        tmp30 = [tmp21[0] + 108, tmp21[1] + 82]
        t.goto(tmp30)
        t.pendown()
        t.setheading(45)
        t.circle(-60, 13)
        t.setheading(-35)
        t.circle(-60, 13)
        
        if flag:
            finger()
            t.penup()
            t.goto(-180,-250)
            t.color(255, 100, 255)
            t.write("被指到的人今年会发财 \n并给小蜗上个舰长!!!", True, align="center", font= ('华文彩云', 25, 'normal'))
        t.penup()
        t.goto(-900,900)

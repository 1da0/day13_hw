import turtle as t             # 거북이 입력
import random
t.shape("turtle")              # 거북이모양

t.up()                         # 선이 안나오게 한다
t.pos()                        
t.goto(-250, 250)              # 왼쪽 모서리로 보낸다
t.down()                       # 선을 그린다
t.goto(250, 250)               # 상자의 윗부분
t.goto(250, -250)              # 상자의 오른쪽 부분
t.goto(-250, -250)             # 상자의 아랫부분
t.goto(-250, 250)              # 상자의 왼쪽 부분  
t.up()        
t.goto(0, 0)                   # 상자의 중간으로 거북이를 보낸다
t.down()                       # 선이 나오게 한다

t.color("green")               # 공의 이동선의 색을 초록색으로 지정한다
t.shape("circle")              # 공모양으로 바꾼다
a = t.xcor()                   # 공의 x좌표를 a로 지정한다
b = t.ycor()                   # 공의 y좌표를 b로 지정한다

for x in range(100):           # 공튀기기를 100번 반복한다
    n = random.randint(1, 360) # 공이 튀길 각도를 랜덤 n으로 지정한다
    t.setheading(n)            # n 각도로 방향을 돌린다
    t.fd(1)
    t.pos()
    a = t.xcor()               # 이동 후 x좌표를 a로 지정한다
    b = t.ycor()               # 이동 후 y좌표를 b로 지정한다
    while -250 < a < 250:      # 상자 밖으로 나가지 않도록 x좌표의 범위를 조건으로 정한다
        if -250 < b < 250:     # 마찬가지로 이동 가능한 y좌표의 범위를 정한다
            t.forward(1)       # 범위 내에서 벽에 닿을 때까지 계속 앞으로 나아간다
            t.pos()
            a = t.xcor()
            b = t.ycor()

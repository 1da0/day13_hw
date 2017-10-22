import turtle as t        # 거북이 입력
t.shape("turtle")         # 거북이 모양
 
t.up()                    # 선이 안나오도록 꼬리를 뗀다
t.pos()              
t.goto(-250, 250)         # 상자의 왼쪽 모서리로 보낸다
t.down()                  # 선이 나타나도록 꼬리를 내린다
t.goto(250, 250)          # 상자의 윗부분을 그린다
t.goto(250, -250)         # 상자의 오른쪽부분을 그린다
t.goto(-250, -250)        # 상자의 아랫부분을 그린다
t.goto(-250, 250)         # 상자의 왼쪽부분을 그린다
t.up()                    
t.goto(0, 0)              # 공을 중앙으로 보낸다
t.down()                   

t.speed(5)                # 속도를 5로 정한다
t.color("green")          # 공의 색깔을 초록색으로 정한다  
t.shape("circle")         # 공모양으로 지정한다

t.setheading(65)          # 각도를 65도로 정한다
t.fd(1)                   # 앞으로 1만큼 간다
t.pos()                   # 이동 후  좌표를 구한다
a = t.xcor()              # 이동 후 x좌표를 a로 지정한다
b = t.ycor()              # 이동 후 y좌표를 b로 지정한다
while -250 < b < 250:     # 상자 밖으로 나가지 않도록 y좌표의 범위를 조건으로 정한다
    t.forward(3)          # 범위 내에서 벽에 닿을 때까지 계속 앞으로 나아간다
    t.pos()
    a = t.xcor()
    b = t.ycor()

t.color("blue")           # 공의 색깔을 파랑색으로 정한다

t.setheading(295)
t.fd(1)
t.pos()
a = t.xcor()              # 이동 후 x좌표를 a로 지정한다
b = t.ycor()              # 이동 후 y좌표를 b로 지정한다
while -250 < a < 250:     # 상자 밖으로 나가지 않도록 x좌표의 범위를 조건으로 정한다
    t.forward(3)          # 범위 내에서 벽에 닿을 때까지 계속 앞으로 나아간다
    t.pos()
    a = t.xcor()
    b = t.ycor()

t.speed(1)                # 공의 속도를 1로 변경한다

t.setheading(245)
t.fd(1)
t.pos()
a = t.xcor()              # 이동 후 x좌표를 a로 지정한다
b = t.ycor()              # 이동 후 y좌표를 b로 지정한다
while -250 < b < 250:     # 상자 밖으로 나가지 않도록 y좌표의 범위를 조건으로 정한다
    t.forward(3)          # 범위 내에서 벽에 닿을 때까지 계속 앞으로 나아간다
    t.pos()
    a = t.xcor()
    b = t.ycor()

t.color("red")            # 공의 색깔을 빨강색으로 변경한다
t.pensize(3)              # 굵기를 3으로 변경한다

t.setheading(169)
t.fd(1)
t.pos()
a = t.xcor()              # 이동 후 x좌표를 a로 지정한다
b = t.ycor()              # 이동 후 y좌표를 b로 지정한다
while -250 < a < 250:     # 상자 밖으로 나가지 않도록 x좌표의 범위를 조건으로 정한다
    t.forward(3)          # 범위 내에서 벽에 닿을 때까지 계속 앞으로 나아간다
    t.pos()
    a = t.xcor()
    b = t.ycor()

t.speed(0)                # 공의 속도를 0으로 변경한다
t.color("black")          # 공의 색깔을 검정색으로 변경한다

t.setheading(45)
t.fd(1)
t.pos()
a = t.xcor()              # 이동 후 x좌표를 a로 지정한다
b = t.ycor()              # 이동 후 y좌표를 b로 지정한다
while -250 < b < 250:     # 상자 밖으로 나가지 않도록 y좌표의 범위를 조건으로 정한다
    t.forward(3)          # 범위 내에서 벽에 닿을 때까지 계속 앞으로 나아간다
    t.pos()
    a = t.xcor()
    b = t.ycor()

t.pensize(1)              # 굵기를 1로 변경한다

t.setheading(315)
t.fd(1)
t.pos()
a = t.xcor()              # 이동 후 x좌표를 a로 지정한다
b = t.ycor()              # 이동 후 y좌표를 b로 지정한다
while -250 < a < 250:     # 상자 밖으로 나가지 않도록 x좌표의 범위를 조건으로 정한다
    t.forward(3)          # 범위 내에서 벽에 닿을 때까지 계속 앞으로 나아간다
    t.pos()
    a = t.xcor()
    b = t.ycor()

t.color("green")          # 공의 색깔을 초록색으로 변경한다
t.pensize(3)              # 굵기를 3으로 변경한다

t.setheading(190)
t.fd(1)
t.pos()
a = t.xcor()              # 이동 후 x좌표를 a로 지정한다
b = t.ycor()              # 이동 후 y좌표를 b로 지정한다
while -250 < a < 250:     # 상자 밖으로 나가지 않도록 x좌표의 범위를 조건으로 정한다
    t.forward(3)          # 범위 내에서 벽에 닿을 때까지 계속 앞으로 나아간다
    t.pos()
    a = t.xcor()
    b = t.ycor()

t.goto(0, 0)              # 상자의 중앙으로 공을 옮긴다

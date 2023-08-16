import turtle

def draw_heart():
    heart = turtle.Turtle()
    heart.shape("circle")
    heart.color("red")
    heart.fillcolor("white")  # Màu trong trái tim là trắng
    heart.speed(2)

    heart.begin_fill()
    heart.left(140)
    heart.forward(224)
    for _ in range(200):
        heart.right(1)
        heart.forward(2)
    heart.left(120)
    for _ in range(200):
        heart.right(1)
        heart.forward(2)
    heart.forward(224)
    heart.end_fill()

def draw_love_text():
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(0, 0)  # Đặt vị trí chữ "Ly" ở giữa trái tim
    text.color("red")  # Màu chữ "Ly" là đỏ
    text.write("Love", align="center", font=("Arial", 24, "normal"))

def main():
    window = turtle.Screen()
    window.bgcolor("white")

    draw_heart()
    draw_love_text()

    window.exitonclick()

if __name__ == "__main__":
    main()

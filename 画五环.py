import turtle


class OlympicTurtle(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self, shape="turtle")
        screen = turtle.Screen()
        screen.bgcolor("lightgrey")
        self.pensize(3)  # 设置画笔大小
        self.speed(3)  # 设置速度

    def draw_circle(self, x, y, color, radius=55):
        self.penup()  # 抬起画笔
        self.setposition(x, y)  # 找到位置
        self.pendown()  # 画笔落下
        self.color(color)  # 设置颜色
        self.circle(radius)  # 绘制一个 radius 指定半径的圆

    def draw_olympic_symbol(self):
        """
        (0, 0) 在画布的中央位置
        :return:
        """
        circle_lst = [(60, 0, "blue"), (-60, 0, "purple"), (120, 60, "red"),
                      (0, 60, "yellow"), (-120, 60, "green")]

        for x, y, color in circle_lst:
            self.draw_circle(x, y, color)

        self.drawText()

    def drawText(self):
        self.penup()
        self.setposition(0, 0)
        self.setheading(0)  # 设置小海龟的朝向
        self.pendown()
        self.color("black")
        self.write("bei京 666", font=("Arial", 30, "bold"))


if __name__ == "__main__":
    t = OlympicTurtle()
    t.draw_olympic_symbol()
    turtle.getscreen()._root.mainloop()

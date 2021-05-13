import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon


class MainWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        # 设置主窗体标签
        self.setWindowTitle("QMainWindow 例子")  # 设置主窗口文字
        self.resize(400, 200)  # 设置主窗口大小
        self.status = self.statusBar()  # 获取主窗口状态栏
        self.status.showMessage("这是状态栏提示", 5000)  # 设置主窗口状态栏文字
        self.center()  # 调用将窗口设置中间函数

        self.button1 = QPushButton('关闭主窗口')  # 实例化一个 按键
        self.button1.setStyleSheet("background-color: red")  # 设置按钮的风格和颜色
        self.button1.clicked.connect(self.onButtonClick)  # 绑定按键点击事件

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self):
        # sender 是发送信号的对象，此处发送信号的对象是button1按钮
        sender = self.sender()
        print(sender.text() + ' 被按下了')
        qApp = QApplication.instance()
        qApp.quit()

    def center(self):
        screen = QDesktopWidget().screenGeometry()  # 获取当前屏幕对象
        size = self.geometry()  # 获取窗口尺寸数据
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)  # 根据屏幕尺寸 和 窗口尺寸计算 相应位置


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/cartoon1.ico"))  # 设置主窗口的图标
    main = MainWidget()  # 获取主窗口对象
    main.show()
    sys.exit(app.exec_())

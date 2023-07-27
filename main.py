
import sys
import Win
import time
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow


if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    win = QMainWindow()
    ui = Win.Ui_MainWindow()
    ui.setupUi(win)
    win.show()
    # while True:
    #     win.repaint()
    #     time.sleep(1)

    # 进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)
    sys.exit(app.exec_())

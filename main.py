# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
"""Main()代码"""
import os
import sys
from test1 import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

if __name__ == "__main__":
    App = QApplication(sys.argv)    # 创建QApplication对象，作为GUI主程序入口
    aw = Ui_MainWindow()    # 创建主窗体对象，实例化Ui_MainWindow
    w = QMainWindow()      # 实例化QMainWindow类
    aw.setupUi(w)         # 主窗体对象调用setupUi方法，对QMainWindow对象进行设置
    w.show()               # 显示主窗体
    # App.exit()
    sys.exit(App.exec_())   # 循环中等待退出程序
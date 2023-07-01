# -- coding: utf-8 --
# 选择本地图片上传
import PyQt5
import sys
from test1 import Ui_MainWindow
import cv2
import cv2 as cv

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow


# 选择本地图片上传
def openImage(Ui_Mainwindow=None):
    global imgNamepath  # 这里为了方便别的地方引用图片路径，将其设置为全局变量
    # 弹出一个文件选择框，第一个返回值imgName记录选中的文件路径+文件名，第二个返回值imgType记录文件的类型
    # QFileDialog就是系统对话框的那个类第一个参数是上下文，第二个参数是弹框的名字，第三个参数是默认打开的路径，第四个参数是需要的格式
    imgNamepath, imgType = QFileDialog.getOpenFileName(Ui_Mainwindow.centralwidget, "选择图片",
                                                       "D:\\",
                                                       "*.jpg;;*.png;;All Files(*)")
    # 通过文件路径获取图片文件，并设置图片长宽为label控件的长、宽
    img = QtGui.QPixmap(imgNamepath).scaled(Ui_Mainwindow.showPic.width(), Ui_Mainwindow.showPic.height())
    # 在label控件上显示选择的图片
    Ui_Mainwindow.showPic.setPixmap(img)


# 保存图片到本地(第二种方式:首先提取相对应Qlabel中的图片，然后打开一个保存文件的弹出框，最后保存图片到选中的路径)
def saveImage(self):
    # 提取Qlabel中的图片
    img = self.result.pixmap().toImage()
    fpath, ftype = QFileDialog.getSaveFileName(self.centralwidget, "保存图片", "d:\\",
                                               "*.jpg;;*.png;;All Files(*)")
    img.save(fpath)

def cvimg_to_qtimg(self,cvimg):
    height, width, depth = cvimg.shape
    cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
    cvimg = QImage(cvimg.data, width, height, width * depth, QImage.Format_RGB888)

    return cvimg

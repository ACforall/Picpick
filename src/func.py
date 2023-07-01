# -- coding: utf-8 --
import PyQt5
import sys
import cv2
import cv2 as cv

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QMainWindow

def startAction(imgNamepath):
    img = cv2.imread(imgNamepath)
    img = cv2.resize(img, dsize=(768, 1080))
    # 图像转灰度图像
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 灰度图像到反转灰度图像
    inverted_gray_image = 255 - gray_image
    # 模糊倒置灰度图像
    blurred_inverted_gray_image = cv2.GaussianBlur(inverted_gray_image, (19, 19), 0)
    # 反转模糊图像
    inverted_blurred_image = 255 - blurred_inverted_gray_image
    # 准备照片素描
    sketck = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

    rows, columns = sketck.shape
    bytesPerLine = columns
    QImg = QImage(sketck.data, columns, rows, bytesPerLine, QImage.Format_Indexed8)
    # self.labelResult.setPixmap(QPixmap.fromImage(QImg).scaled(
    #     self.labelResult.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    return QImg

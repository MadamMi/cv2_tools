# -*- coding: utf-8 -*-
import cv2
import numpy as np
import copy


# 自适应二值化
def local_threshold(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGRA2GRAY)
    # binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,10)

    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 3)
    return binary


# 图像二值化并显示
def threshold_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray = 255 - gray
    # ret, binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    # ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
    ret, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    print("阈值：", ret)
    cv2.namedWindow('inv_gray', 0)
    # 显示框大小
    cv2.resizeWindow('inv_gray', (640, 480))
    cv2.imshow("inv_gray", gray)

    cv2.namedWindow('binary', 0)
    # 显示框大小
    cv2.resizeWindow('binary', (640, 480))
    cv2.imshow("binary", binary)
    cv2.waitKey()
    return binary


# 霍夫圆检测、画圆、显示
def circle(src_image):
    # bin_image = threshold_demo(src_image)
    image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
    # circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 20, param1=150, param2=30, minRadius=0, maxRadius=0)
    co_image = copy.deepcopy(image)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(co_image, (i[0], i[1]), i[2], (0, 255, 255), 2)
        cv2.circle(co_image, (i[0], i[1]), 2, (255, 255, 255), 2)
    cv2.imshow("src", src_image)
    cv2.imshow("circles", co_image)
    cv2.waitKey(0)


# rectangle画框
def drowCircles(image_path,txt_path):
    image = cv2.imread(image_path)
    print(image.shape)

    # 读取txt,strip()去掉行末'\n',split(',')表示按照','分离每一行内容
    with open(txt_path, 'r') as f:
        res = f.readlines()

    rect = res[0].strip().split(',')
    circles = res[1].strip().split(',')
    #circles_right = res[2].strip().split(',')

    cv2.rectangle(image, (int(rect[0]), int(rect[1])), (int(rect[2])+int(rect[0]), int(rect[3])+int(rect[1])), (0, 0, 255), 2)
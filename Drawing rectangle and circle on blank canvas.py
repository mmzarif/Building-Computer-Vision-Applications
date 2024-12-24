import cv2
import numpy as np

canvas = np.zeros((200, 200, 1), dtype = "uint8")

"""
start = (10, 10)
end = (100, 100)
color = (0, 255, 0)
thickness = -1

cv2.rectangle(canvas, start, end, color, thickness)
cv2.imwrite("rectangleOnCanvas.png", canvas)
cv2.imshow("Rectangle", canvas)
"""

center = (100, 100)
radius = 50

cv2.circle(canvas, center, radius, 155, -1)

cv2.imwrite("circleOnCanvas.png", canvas)
cv2.imshow("Circle", canvas)
cv2.waitKey(0)

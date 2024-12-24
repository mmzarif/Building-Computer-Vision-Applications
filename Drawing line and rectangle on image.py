import cv2

image_path = "E:\\UCSD\\SRIP\\PICTURES\\180 degrees.jpg"

image = cv2.imread(image_path)

start = (0, 0)
end = (image.shape[1], image.shape[0])

thickness = 4
color = (0, 255, 0) #pure green

cv2.line(image, start, end, color, thickness)

cv2.imshow("Modified Image", image)
cv2.waitKey(0)

start_rect = (50, 50)
end_rect = (200, 200)


cv2.rectangle(image, start_rect, end_rect, color, thickness)

cv2.imwrite("line+rect.jpg", image)

cv2.imshow("Modified Image", image)
cv2.waitKey(0)

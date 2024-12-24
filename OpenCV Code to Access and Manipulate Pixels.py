import cv2

image_path = "E:\\UCSD\\SRIP\\PICTURES\\180 degrees.jpg"

image = cv2.imread(image_path)

(b, g, r) = image[0, 0]
print("Blue, Green, Red values at (0, 0) are: ", format((b, g, r))) #prints values in parenthesis e.g. (46, 52, 157)

image[0:1000, 0:1000] = (255, 255, 0) #pure blue, pure green, no red
cv2.imshow("Modified Image", image)
cv2.waitKey(0)

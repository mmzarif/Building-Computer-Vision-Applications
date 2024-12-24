import cv2

image_path = "E:\\UCSD\\SRIP\\PICTURES\\180 degrees.jpg"

image = cv2.imread(image_path)

print("Dimensions of the image: ", image.ndim)
print("Image height: ", format(image.shape[0]))
print("Image width: ", format(image.shape[1]))
print("Image channels: ", format(image.shape[2]))
print("Size of image array: ", image.size)

cv2.imshow("Image", image)
cv2.waitKey(0)

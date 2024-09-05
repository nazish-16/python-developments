import cv2

image_file = input("Enter the image title: ")
image = cv2.imread(image_file, cv2.IMREAD_UNCHANGED)

scale_percent = int(input("Enter the value: "))
newWidth = int(image.shape[1] * scale_percent / 100)
newHeight = int(image.shape[1] * scale_percent / 100)

output = cv2.resize(image, (newWidth, newHeight))

cv2.imwrite('newImage.png', output)
cv2.imshow('newImage.png', output)
cv2.waitKey(0)
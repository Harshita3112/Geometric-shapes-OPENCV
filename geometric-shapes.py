import cv2
import numpy as np

# LINE
image = np.zeros((500, 500, 3), dtype=np.uint8)
start_point = (100, 100)
end_point = (400, 400)
color = (0, 0, 255) 
cv2.line(image, start_point, end_point, color, thickness=2)

# RECTANGLE
image1 = np.zeros((500, 500, 3), dtype=np.uint8)
top_left = (100, 100)
bottom_right = (400, 300)
color = (0, 255, 0)  
cv2.rectangle(image1, top_left, bottom_right, color, thickness=2)

# ELLIPSE
image2 = np.zeros((500, 500, 3), dtype=np.uint8)
center = (250, 250)
axes = (100, 50)  
angle = 45  
color = (255, 0, 0) 
cv2.ellipse(image2, center, axes, angle, 0, 360, color, thickness=2)

# CIRCLE
image3 = np.zeros((500, 500, 3), dtype=np.uint8)
radius = 100
color1 = (0, 255, 255)  
cv2.circle(image3, center, radius, color1, thickness=2)


cv2.imshow("Line", image)
cv2.waitKey(0)
cv2.imshow("Rectangle", image1)
cv2.waitKey(0)
cv2.imshow("Ellipse", image2)
cv2.waitKey(0)
cv2.imshow("Circle", image3)
cv2.waitKey(0)
cv2.destroyAllWindows()

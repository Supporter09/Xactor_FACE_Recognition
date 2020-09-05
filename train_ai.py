import time
import dlib
import cv2

# Đọc ảnh đầu vào
image = cv2.imread('D:/Xactor_FACE_Recognition/Crawl_WEB/news/news-0.png')
# print(image)
# Khai báo việc sử dụng các hàm của dlib
hog_face_detector = dlib.get_frontal_face_detector()
cnn_face_detector = dlib.cnn_face_detection_model_v1('D:/Xactor_FACE_Recognition/mmod_human_face_detector.dat')

# Thực hiện xác định bằng HOG và SVM
start = time.time()
faces_hog = hog_face_detector(image, 1)
end = time.time()
print("Hog + SVM Execution time: " + str(end-start))

# Vẽ một đường bao màu xanh lá xung quanh các khuôn mặt được xác định ra bởi HOG + SVM
for face in faces_hog:
  x = face.left()
  y = face.top()
  w = face.right() - x
  h = face.bottom() - y

  cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)

# Thực hiện xác định bằng CNN
# start = time.time()
# faces_cnn = cnn_face_detector(image, 1)
# end = time.time()
# print("CNN Execution time: " + str(end-start))

# Vẽ một đường bao đỏ xung quanh các khuôn mặt được xác định bởi CNN
# for face in faces_cnn:
#   x = face.rect.left()
#   y = face.rect.top()
#   w = face.rect.right() - x
#   h = face.rect.bottom() - y

#   cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 2)

cv2.imshow("image", image)
cv2.waitKey(0)
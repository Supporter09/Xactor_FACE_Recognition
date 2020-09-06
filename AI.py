import cv2
import os
from matplotlib import image
from matplotlib import pyplot
from PIL import Image
import glob
import face_recognition
def load_images_from_folder(folders):
    images = []
    for folder in os.listdir(folders):
        
        for filename in os.listdir(folders +'/'+ folder):
            if filename.endswith(".jpg"):
                img_link = os.path.join(folders + folder, filename)
                images.append(img_link)

    return images
folders="D:/Xactor_FACE_Recognition/lfw_funneled/"


images = load_images_from_folder(folders)
perfect_img_link_lists = []
for i in images:
    x= i.replace("\\","/")
    perfect_img_link_lists.append(x)

# print(images)
for img in perfect_img_link_lists:
    image = face_recognition.load_image_file(img)
    face_locations = face_recognition.face_locations(image)


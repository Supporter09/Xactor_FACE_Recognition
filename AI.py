import cv2
import os
from matplotlib import image
from matplotlib import pyplot
from PIL import Image
import glob
import face_recognition
def load_images_from_folder(folders):
    # images = []
    # for filename in os.listdir(folder):
    #     img = cv2.imread(os.path.join(folder,filename))
    #     if img is not None:
    #         images.append(img)
    # return images
    images = []
    for folder in os.listdir(folders):
        
        for filename in os.listdir(folders +'/'+ folder):
            # img = cv2.imread(os.path.join(folders +'/'+ folder,filename))
            # if img is not None:
            #     images.append(img)
            #     print(img)
            if filename.endswith(".jpg"):
                img_link = os.path.join(folders + folder, filename)
                images.append(img_link)
                # print(img_link)
    return images
folders="D:/Xactor_FACE_Recognition/lfw_funneled"
subfolders = [ f.name for f in os.scandir(folders) if f.is_dir() ]
# print(subfolders)
# print(os.listdir(folders))
images = load_images_from_folder(folders)
print(images)
# for img in images:
#     image = face_recognition.load_image_file(img)
#     face_locations = face_recognition.face_locations(image)


# for sub_name in subfolders:
#     image_list = []
#     for filename in glob.glob(folders+sub_name+'/*.jpg'): #assuming jpg
#         im=Image.open(filename)
#         image_list.append(im)
        



# print(image_list)
# pyplot.imshow(image_list)
# pyplot.show()

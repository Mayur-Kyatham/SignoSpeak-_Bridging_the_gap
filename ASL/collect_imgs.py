# The provided Python code captures images from a webcam and saves them to a directory for 
# the purpose of collecting a dataset.

import os # for working with the file system to create directories

import cv2 #  (OpenCV): for accessing the webcam and image processing

from pathlib import Path # for working with file paths

DATA_DIR = './data'           # This block sets up the directory where the captured data will be stored.
if not os.path.exists(DATA_DIR):   # If the directory ./data doesn't exist, it's created using os.makedirs.
    os.makedirs(DATA_DIR)

number_of_classes = 4  # define the number of classes (categories) you want to collect data for  <<<<<<<>>>>>>>>>>>
dataset_size = 100  # (3 classes in this case)and the size of the dataset for each class (100 images for each class)

cap = cv2.VideoCapture(0)
# This line initializes the webcam capture using OpenCV's VideoCapture. 
# The argument 0 indicates the default camera (usually the built-in webcam).


for j in range(number_of_classes):
# This loop iterates through the classes you want to collect data for. In this case, it will iterate three
#  times for three classes.
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))
# Within each class iteration, it checks if a directory for that class exists within the DATA_DIR. If not, 
# it creates one. For example, if j is 0, it creates a directory ./data/0.

    print('Collecting data for class {}'.format(j))
# This line prints a message indicating which class's data is being collected.


    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break
# This loop waits until the user presses the 'q' key to indicate that they are ready to start capturing data. 
# It displays a message on the webcam feed using OpenCV's putText and shows the video feed using imshow.
  
  
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)
        counter += 1
# This loop captures and saves images in real-time. It will capture dataset_size number of images (100 in this case) 
# for the current class. Images are saved in the appropriate class directory within the DATA_DIR with filenames like
#  '0/0.jpg', '0/1.jpg', '1/0.jpg', etc.

cap.release()
cv2.destroyAllWindows()
# these lines release the webcam (so it can be used elsewhere) and close the OpenCV windows.

# The code effectively captures images from the webcam for multiple classes and stores them in separate 
# directories for each class, creating a dataset
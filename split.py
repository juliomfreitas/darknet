# example: python split.py ../yolo-custom-object-detector/python/Dataset/images/ rubik/dataset/ 10

import glob
import os
import sys


dataset_path = sys.argv[1]

# Percentage of images to be used for the test set
percentage_test = int(sys.argv[3])

# Create and/or truncate train.txt and test.txt
file_train = open("{}/train.txt".format(sys.argv[2]), "w")
file_test = open("{}/test.txt".format(sys.argv[2]), "w")

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(dataset_path, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test + 1:
        counter = 1
        file_test.write(dataset_path + "/" + title + ".jpg" + "\n")
    else:
        file_train.write(dataset_path + "/" + title + ".jpg" + "\n")
        counter = counter + 1

import os

with os.scandir('C:/Users/User/Desktop/MSc Project/English Cued Speech/SelectedShapes/') as images:
    with open('Labels.txt', 'w') as text_file:
         for image in images:
             image_name = os.path.splitext(image.name)
             print (image_name[0], file = text_file)
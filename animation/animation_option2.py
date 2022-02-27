#Sophia Cofone 2.26.22
#https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
#https://imageio.readthedocs.io/en/stable/examples.html
#This is option 2 for how we could make a gif. 
#The function actually reads a folder for the images so the user would not have to change anything, but its important that the files are named correctly when they are saved/created

import imageio as iio
import os

def create_gif(filename_save):
    #makes a list of im NumPy arrays based on a list of .png images (read from folder)
    images = list()

    for filename in sorted(os.listdir('img')):
        if filename[0] != '.':
            f = os.path.join('img',filename)
            print(f)
            im = iio.imread(f)
            images.append(im)

    iio.mimsave(filename_save,images,duration = 1)

if __name__ == "__main__":
    create_gif('img/animation.gif')
# This file converts a clip into a .Gif File.
# Make sure to run "pip install imageio imageio-ffmpeg" and "pip install pygifsicle"

import os
import imageio 
from pygifsicle import optimize


# A variable for storing the absolute path to the vido that is to be converted to a GIF!
vid_path = os.path.abspath("spongebob-writeitdown.mp4")


def my_optimize(path):
    print("\nFile is being Optimized!\n")
  
    # GET THE FILE SIZE 
    file_size = os.stat(path).st_size
    print("File size before optimization was {} Bytes!".format(file_size))
    optimize(path)
    file_size2 = os.stat(path).st_size
    print("File size after optimization is {} Bytes!".format(file_size2))     
        
    print("\nFile has been Optimized!")

def gif_maker(INPUT_PATH,output_format): 

    #
    OUTPUT_PATH = os.path.splitext(INPUT_PATH)[0] + output_format

    # Logging to the terminal
    print("Converting\n{}\nto\n{} ".format(INPUT_PATH,OUTPUT_PATH))
 
    # IMAGEIO library reads the contents of MPf file
    reader = imageio.get_reader(INPUT_PATH)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(OUTPUT_PATH, fps=fps)

    for frames in reader:
        writer.append_data(frames)
   
    writer.close()

    my_optimize(OUTPUT_PATH)

    print("\nDone!!")

print("\n")
gif_maker(vid_path,".gif")
import cv2

import os



def make_frames(season, input_dir, output_dir, name):
    #
    if not os.path.exists(os.path.abspath(output_dir)):
        print(os.path.abspath(output_dir))
        os.makedirs(os.path.abspath(output_dir))
        
    
def main():
    
    #Get all files into a array
    for seasons in os.listdir('./assets/video'):
        episode = os.listdir('./assets/video/'+ seasons)[0]
        name = os.path.splitext(episode)[0]
        input_dir = os.path.abspath(episode)
        output_dir = "./assets/frames/" + seasons + "/" + name
        print(output_dir)
        make_frames(seasons, input_dir, output_dir, name)
main()
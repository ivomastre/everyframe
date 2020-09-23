import cv2

import os



def make_frames(season, input_dir, output_dir, name):
    #Create necessary folders
    if not os.path.exists(os.path.abspath(output_dir)):
        print(os.path.abspath(output_dir))
        os.makedirs(os.path.abspath(output_dir))

    vidcap = cv2.VideoCapture(input_dir)
    success, image = vidcap.read()
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    required_fps = 2
    #More fps = more frames
    multiplier = round(fps/required_fps)
    frame_number = 1
    """
    while success:
        frame_id = int(round(vidcap.get(1)))
        if frameId % multiplier == 0:
            frame_number+=1
            cv2.imwrite(os.path.join(), image)
    """
    vidcap.release()

        
        
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
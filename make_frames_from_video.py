import os
import cv2




def make_frames(input_dir, output_dir):
    #Create necessary folders
    if not os.path.exists(os.path.abspath(output_dir)):
        print(os.path.abspath(output_dir))
        os.makedirs(os.path.abspath(output_dir))
    vidcap = cv2.VideoCapture(input_dir)
    print(input_dir)
    success, image = vidcap.read()
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    required_fps = 3
    #More fps = more frames
    multiplier = round(fps/required_fps)
    frame_number = 1

    while success:
        frame_id = int(round(vidcap.get(1)))
        success, image = vidcap.read()

        if frame_id % multiplier == 0:
                  
            cv2.imwrite(os.path.join(output_dir, str(frame_number) + ".jpg"), image)
            frame_number+=1

    vidcap.release()     
def main():
    #Get all files into a array
    for seasons in os.listdir('./assets/video/'):
        episodes = os.listdir('./assets/video/'+ seasons)
        for episode in episodes:
            name = os.path.splitext(episode)[0]
            input_dir = os.path.abspath('./assets/video/'+ seasons+ '/'+ episode)
            output_dir = "./assets/frames/" + seasons + "/" + name
            make_frames(input_dir, output_dir)
main()

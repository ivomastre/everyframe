import os
import json
def save_to_json(status_data):
    a_file_read = open("status.json", "r")
    status_json = json.load(a_file_read)
    status_json.update(status_data)
    a_file_read.close()
    a_file_write = open("status.json", "w")
    
    json.dump(status_json, a_file_write)
    a_file_write.close()


def add_season_to_json():

    with open('./status.json') as f:
        status_data = json.load(f)
        status_data['Season']+=1
                    
        episode_dir = os.listdir('./assets/frames/' )

        for i,season in enumerate(episode_dir):
            episode_dir[i] = int(season)
        if(max(episode_dir)<status_data['Season']):
            save_to_json({'Season': 1})
        
        else:
            save_to_json({'Season': status_data['Season']})

def add_episode_to_json():

    with open('./status.json') as f:
        status_data = json.load(f)
        status_data['Episode']+=1
                   
        episode_dir = os.listdir('./assets/frames/' + str(status_data['Season']))
        for i,episode in enumerate(episode_dir):
            episode_dir[i] = int(episode)
        if(max(episode_dir)<status_data['Episode']):
            add_season_to_json()
            save_to_json({'Episode': 1})
            
        else:
            save_to_json({'Episode': status_data['Episode']})
        
def add_frame_to_json():
    
    with open('./status.json') as f:
        
        status_data = json.load(f)
        status_data['Frame']+=1
        #if(status_data['Frame']>)
        print(status_data)
        frame_dir = os.listdir('./assets/frames/' + str(status_data['Season']) + '/' + str(status_data['Episode']))
        #Get only the name of the file
        for i,frame in enumerate(frame_dir):
            frame_dir[i] = int(os.path.splitext(frame)[0])
        if(max(frame_dir) < status_data['Frame']):
            add_episode_to_json()
            save_to_json({'Frame': 0})
        else:
            save_to_json({'Frame': status_data['Frame']})

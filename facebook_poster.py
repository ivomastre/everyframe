import facebook
import os
import json
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("facebook_token")
def post():
    graph = facebook.GraphAPI(TOKEN)
    
    with open('./status.json') as f:
        status_data = json.load(f)
        frame_dir = os.listdir('./assets/frames/' + str(status_data['Season']) + '/' + str(status_data['Episode']))
        #Get only the name of the file
        for i,frame in enumerate(frame_dir):
                frame_dir[i] = int(os.path.splitext(frame)[0])
        relative_path = "./assets/frames/"+ str(status_data.get('Season')) + "/"+ str(status_data.get('Episode'))+ "/"+ str(status_data.get('Frame'))+".jpg"
        absolute_path = os.path.abspath(relative_path)
        msg = "Season "+ str(status_data.get('Season')) + "  Episode " + str(status_data.get('Episode')) + "  Frame " + str(status_data.get('Frame')) + "out of " 
        post = graph.put_photo(image=open(absolute_path, 'rb'), message = msg)
        print(post)
post()
#
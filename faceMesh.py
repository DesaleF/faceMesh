# for some importing problems 
import os
import sys    
p = os.path.abspath('.') 
sys.path.insert(1, p)  

import cv2
import mediapipe as mp
from utils.utils import create_dir, save_json, load_json, setup_logging



# create the FaceMesh object 
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

# read the video or camera
video_path = "data/news.mp4"    # 0:webcam, or video path
cap = cv2.VideoCapture(video_path)
if isinstance(video_path, int):
    save_dir = "data/detected_mesh/webcam"
else:
    save_dir =  "data/detected_mesh/{}".format(
        video_path.split(".")[0].split("/")[-1])

create_dir(save_dir)
if isinstance(video_path, int):
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    out = cv2.VideoWriter(
        'data/webcam.avi',
        cv2.VideoWriter_fourcc('M','J','P','G'), 
        30, (frame_width,frame_height)
    )

frame_counter = 0
while True:
    ret, frame = cap.read()
    if isinstance(video_path, int):
        out.write(frame)
        
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    if ret:
        image_mesh = {}
        mesh_results = face_mesh.process(rgb_frame)
        
        # if any detected face with mesh
        if mesh_results.multi_face_landmarks:
            x_y_coordinates = {}
            x_y_z_coordinates = {}
            
            # iterate through each detected faces
            for idx, landmarks in enumerate(mesh_results.multi_face_landmarks):
                x_y_coordinate = []
                x_y_z_coordinate = []
                
                # get all the points of the landmark
                for landmark in landmarks.landmark:
                    
                    # convert normalized the coordinates 
                    h, w, _ = rgb_frame.shape
                    x = int(landmark.x * w)
                    y = int(landmark.y * h)
                    
                    # append the points to save 
                    x_y_coordinate.append([x, y])
                    x_y_z_coordinate.append([landmark.x, landmark.y, landmark.z])
                    cv2.putText(frame, ".", (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1) 
                    
                x_y_coordinates["face_{}".format(idx)] = x_y_coordinate
                x_y_z_coordinates["face_{}".format(idx)] = x_y_z_coordinate
            
            key = save_dir.split("/")[-1]
            image_mesh[key] = {
                "2d_points": x_y_coordinates,
                "3d_points":x_y_z_coordinates
            }
            
            save_json("{}/frame_{}.json".format(save_dir, frame_counter), image_mesh)    
        cv2.imshow("raw frame", frame)
        frame_counter += 1
        key = cv2.waitKey(25)
        if key == 27:
            break
    
    else:
        continue
cap.release()
    
    
    
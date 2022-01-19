# for some importing problems 
import os
import sys    
p = os.path.abspath('.') 
sys.path.insert(1, p)  

import cv2
import mediapipe as mp
from utils.utils import setup_logging


logger = setup_logging()
class FaceMesh():
    def __init__(self, static_mode=False, maxFaces=1, min_detection_conf=0.5, min_track_conf=0.5):
        super(FaceMesh, self).__init__()
        """uses media pipe's api to detect face mesh points

            Args:
                static_mode (bool): whether track or just detect everytime
                maxFaces (int): number of faces to be detected
        """
        
        self.static_mode = static_mode
        self.maxFaces = maxFaces
        self.min_detection_conf = min_detection_conf
        self.min_track_conf = min_track_conf
        
        # create the FaceMesh object 
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=self.static_mode,
            max_num_faces=self.maxFaces,
            min_detection_confidence=self.min_detection_conf,
            min_tracking_confidence=self.min_track_conf)


    def get_mesh(self, cv_img, draw=True):
        """return the face messh of opencv image

        Args:
            cv_img (cv2Image): opencv Image to be processed
            draw (bool): whether to draw the mesh on the image or not
        
        Returns:
            coord (json): 2D & 2D coordinates of the mesh points
            img (cv2Image): the input image with the face mesh
        """
        
        rgb_frame = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        # if ret:
        image_mesh = {}
        mesh_results = self.face_mesh.process(rgb_frame)
        
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
                    if draw:
                        cv2.putText(cv_img, ".", (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1) 
                    
                x_y_coordinates["face_{}".format(idx)] = x_y_coordinate
                x_y_z_coordinates["face_{}".format(idx)] = x_y_z_coordinate
            image_mesh = {"2d_points": x_y_coordinates, "3d_points":x_y_z_coordinates}
        return image_mesh, cv_img




    
    
    
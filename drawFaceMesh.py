from operator import imod
import cv2
from faceMesh import FaceMesh
from cameraFeed import Camera
from utils.arguement import drawArgs
from utils.utils import setup_logging



logger = setup_logging()
def main():
    # read the video or camera
    args = drawArgs()
    faceMesh = FaceMesh(static_mode=True)
    if args.camera:
        
        # access the camera and get frames
        camera = Camera()
        image = camera.getImage()
        for img in image:
            
            # get the mesh and display
            _, img = faceMesh.get_mesh(img, draw=True)
            cv2.imshow('Mesh', img)
            cv2.namedWindow('Mesh',cv2.WINDOW_NORMAL)

            # exit if esc is pressed
            if cv2.waitKey(1) == 27: 
                break  # esc to quit
        
        # release all resource  
        camera.source.release()
        cv2.destroyAllWindows()
    
    # use video file instead of the camera
    elif args.video_path:
        cap = cv2.VideoCapture(args.video_path)

        # get face mesh for each frames
        while True:
            ret, frame = cap.read()
            _, frame = faceMesh.get_mesh(frame, draw=True)
            
            # display extracted face mesh
            cv2.imshow("raw frame", frame)
            key = cv2.waitKey(1)
            if key == 27:
                break
        
        # release all the resources 
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    
    

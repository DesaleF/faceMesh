import cv2
from faceMesh import FaceMesh
from cameraFeed import Camera
from utils.arguement import drawArgs
from utils.utils import setup_logging
from videoFeed import Video



logger = setup_logging()
def main():
    # read the video or camera
    args = drawArgs()
    faceMesh = FaceMesh(static_mode=False)

    # access the camera and get frames
    if args.camera:
        cap = Camera()   
    else:
        cap = Video(video_path=args.video_path)
   
    frames = cap.getImage()
    for img in frames:
        if img is None: # end of frames
            break
        
        # get the mesh and display
        _, img = faceMesh.get_mesh(img, draw=True)
        cv2.imshow('Mesh', img)
        cv2.namedWindow('Mesh',cv2.WINDOW_NORMAL)

        # exit if esc is pressed
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    
    # release all resource  
    cap.source.release()
    cv2.destroyAllWindows()
    

if __name__ == '__main__':
    main()
    
    

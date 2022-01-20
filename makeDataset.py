import cv2
import os.path as op
from faceMesh import FaceMesh
from utils.arguement import drawArgs

from cameraFeed import Camera
from videoFeed import Video
from utils.utils import create_dir, \
    save_json, setup_logging



logger = setup_logging()
def main(root_dir='data/detected_mesh'):
    """save the face mesh points into json files

    Args:
        root_dir (str, optional): root directory to save the dataset. 
                Defaults to 'data/detected_mesh'.
        video_path (str, optional): path to the video or camera id. 
                Defaults to None.
    """
    # read the video or camera
    cap = None
    args = drawArgs()
    faceMesh = FaceMesh(static_mode=False)

    # if we use camera feed, we need to save the video too  
    if args.camera:
        cap = Camera()
        
        save_dir = op.join(root_dir, "webcam")
        frame_width = int(cap.source.get(3))
        frame_height = int(cap.source.get(4))

        # video output object to save the video
        out = cv2.VideoWriter(
            'data/webcam.avi',
            cv2.VideoWriter_fourcc('M','J','P','G'), 
            30, (frame_width,frame_height)
        )

    else:
        cap = Video(args.video_path)
        video_name = op.basename(args.video_path)
        video_name = op.splitext(video_name)[0]
        save_dir =  op.join(root_dir, video_name)  

    create_dir(save_dir)
    frames = cap.getImage()
    frame_counter = 0
    
    for img in frames:
        if img is None: # end of frames
            break
        if args.camera:
            out.write(img)  
             
        # get the mesh 
        face_mesh, img = faceMesh.get_mesh(img, draw=True)
        json_file_name = "frame_{}.json".format(frame_counter)
        json_file_name = op.join(save_dir, json_file_name)
        
        # save the mesh and display the video
        save_json(json_file_name, face_mesh)    
        frame_counter += 1
        cv2.imshow('Face Mesh', img)
        cv2.namedWindow('Face Mesh',cv2.WINDOW_NORMAL)
        if cv2.waitKey(30) == 27: 
            break  # esc to quit
    
    cap.source.release()
    if args.camera:
        out.release()
    
 
    
if __name__ == '__main__':
    main()
    

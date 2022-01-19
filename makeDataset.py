



def main():
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
            
                
                key = save_dir.split("/")[-1]
                image_mesh[key] = 
                
                save_json("{}/frame_{}.json".format(save_dir, frame_counter), image_mesh)    
            cv2.imshow("raw frame", frame)
            frame_counter += 1
            key = cv2.waitKey(25)
            if key == 27:
                break
        
        else:
            continue
    cap.release()

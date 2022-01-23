"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""
import cv2
from utils.utils import setup_logging



logger = setup_logging()
class Video:
    def __init__(self, video_path, source=None, resize=False, width=224, height=224):
        self.source = source
        self.resize = resize
        self.video_path = video_path
        self.width = width
        self.height = height
        
    def getImage(self):
        if not self.source:
            self.source = cv2.VideoCapture(self.video_path)
            
        while True:
            ret_val, img = self.source.read()
            if self.resize:
                # resize the image
                img = cv2.resize(img, (self.width, self.height), 
                        interpolation=cv2.INTER_AREA)
            
            if not ret_val:
                logger.info("End of Video frame")
                yield None
            yield img
            

if __name__ == '__main__':
    video_path = "data/news.mp4" 
    video = Video(video_path=video_path)
    images = video.getImage()
    
    for img in images:
        if img is None: # last frame
            break

        cv2.imshow('yield', img)
        cv2.namedWindow('yield',cv2.WINDOW_NORMAL)

        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()
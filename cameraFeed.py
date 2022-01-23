"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""
import cv2


class Camera:
    def __init__(self, webcam=0, mirror=True, resize=False, width=224, height=224):
        self.mirror = mirror
        self.resize = resize
        self.width = width
        self.height = height
        self.source = cv2.VideoCapture(webcam)
        
    def getImage(self):
        if not self.source:
            self.source = cv2.VideoCapture(0)
        
        while True:
            ret, img = self.source.read()
            if ret and self.mirror: 
                img = cv2.flip(img, 1)
                
            if ret and self.resize:
                img = cv2.resize(img, (self.width, self.height), 
                        interpolation=cv2.INTER_AREA)
            
            yield img
            

if __name__ == '__main__':
    width, height=(224, 224)
    camera = Camera(resize=True)
    image = camera.getImage()
    
    for img in image:
        cv2.imshow('yield', img)
        cv2.namedWindow('yield',cv2.WINDOW_NORMAL)

        if cv2.waitKey(30) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()
import cv2

class VideoCamera(object):
    """Represents a VideoCamera object.
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(VideoCamera, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.check_if_camera_available()

    def __del__(self):
        self.video.release()        

    def check_if_camera_available(self):
        # check if the web camera is available
        if not self.video.isOpened():
            raise Exception("Could not open video device")
    
    def get_frame(self):
        _, frame = self.video.read()
        _, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
    
# Author: Shamika Tissera

import argparse
from flask import Flask, Response
import cv2


class VideoCamera(object):
    """Represents a VideoCamera object.
    """
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()        

    def get_frame(self):
        _, frame = self.video.read()
        _, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

app = Flask(__name__)

video_stream = VideoCamera()

def gen(camera: VideoCamera) -> bytes:
    """Video streaming generator function.

    Args:
        camera (VideoCamera): VideoCamera object.

    Yields:
        bytes: Frame bytes
        bytes: Image frame in bytes.
    """
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag.

    Returns:
        Response: Flask response object.
    """
    return Response(gen(video_stream),
                     mimetype='multipart/x-mixed-replace; boundary=frame')


def get_args():
    """Get command line arguments.

    Returns:
        Namespace: Namespace object containing command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, default='127.0.0.1', help='Host IP address.')
    parser.add_argument('--port', type=int, default=1111, help='Port number.')
    
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    app.run(host=args.host, debug=True, port=args.port)

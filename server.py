# Author: Shamika Tissera

import argparse
from flask import Flask, Response
import waitress
from classes.VideoCamera import VideoCamera

app = Flask(__name__)

def gen() -> bytes:
    """Video streaming generator function.

    Args:
        camera (VideoCamera): VideoCamera object.

    Yields:
        bytes: Frame bytes
        bytes: Image frame in bytes.
    """
    video_camera_singleton_obj = VideoCamera()
    
    while True:
        frame = video_camera_singleton_obj.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag.

    Returns:
        Response: Flask response object.
    """
    return Response(gen(),
                     mimetype='multipart/x-mixed-replace; boundary=frame')




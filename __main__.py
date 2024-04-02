from classes.VideoCamera import VideoCamera
from server import app
import waitress
import argparse

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
    print(f"Attempting to start the server at http://{args.host}:{args.port}")
    waitress.serve(app, host=args.host, port=args.port)

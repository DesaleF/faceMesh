import argparse


def drawArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--camera',
        action='store_true', 
       default=False,
        help='quad dataloader')
    
    parser.add_argument(
        '--video_path', 
        type=str, 
        default="data/news.mp4", 
        help='to use video file')
    
    parser.add_argument(
        '--image_path', 
        type=str, default=None, 
        help='to get face mesh for single image')
    
    parser.add_argument(
        '--save_path', 
        type=int, default=100, 
        help='path to save face mesh')
    
    return parser.parse_args()
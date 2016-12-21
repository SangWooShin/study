# get_frame_time_rate : measure frame time and frame rate

import random
import json
from pico2d import *

TARGET_FPS = 60.0
TARGET_FRAME_TIME = 1.0 / TARGET_FPS

def main():
    current_time = get_time()
    frame_time = get_time() - current_time
    frame_rate = 1.0 / frame_time
    print("Frame Rate: %f fps, Frame Time : %f sec, " %(frame_rate, frame_time))
    current_time += frame_time

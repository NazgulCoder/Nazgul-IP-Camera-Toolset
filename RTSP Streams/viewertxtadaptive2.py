import cv2
import math
import numpy as np
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Read RTSP stream URLs from a text file
with open("rtsp_urls.txt", "r") as file:
    rtsp_urls = [line.strip() for line in file]

# Calculate the number of rows and columns for the grid
num_streams = len(rtsp_urls)
if num_streams <= 2:
    num_cols = num_streams
    num_rows = 1
elif num_streams <= 4:
    num_cols = 2
    num_rows = 2
else:
    sqrt_num_streams = math.isqrt(num_streams)
    num_cols = sqrt_num_streams
    num_rows = math.ceil(num_streams / num_cols)

# Enable hardware acceleration if supported
cv2.setUseOptimized(True)
cv2.setUseOptimized(1)

# Create capture objects for each stream
caps = [cv2.VideoCapture(url) for url in rtsp_urls]

# Check if the capture objects were successfully opened
if not all(cap.isOpened() for cap in caps):
    logging.error("Error opening one or more streams")
    exit()

# Set the dimensions for each stream's window
window_width = 640
window_height = 480

# Create a window to display the streams
cv2.namedWindow("RTSP Streams", cv2.WINDOW_NORMAL)
cv2.resizeWindow("RTSP Streams", window_width * num_cols, window_height * num_rows)

# A list to keep track of last successful frame time for each stream
last_successful_frame_time = [time.time()] * num_streams

def handle_frame_read_error(cap_index):
    logging.warning(f"Error reading frame from stream {cap_index}")
    caps[cap_index].release()
    caps[cap_index].open(rtsp_urls[cap_index])
    last_successful_frame_time[cap_index] = time.time()

def main_loop():
    while True:
        frames = [cap.read()[1] for cap in caps]

        # Resize frames to the desired dimensions
        resized_frames = [cv2.resize(frame, (window_width, window_height)) if frame is not None else None for frame in frames]

        # Calculate the maximum width and height among the frames
        max_width = max(frame.shape[1] for frame in resized_frames if frame is not None)
        max_height = max(frame.shape[0] for frame in resized_frames if frame is not None)

        # Create a black canvas with the maximum dimensions
        canvas = np.zeros((max_height * num_rows, max_width * num_cols, 3), dtype=np.uint8)

        # Fill the canvas with the resized frames and black squares
        for i, frame in enumerate(resized_frames):
            if frame is not None:
                row = i // num_cols
                col = i % num_cols
                canvas[row * max_height:(row + 1) * max_height, col * max_width:(col + 1) * max_width] = frame
                last_successful_frame_time[i] = time.time()
            else:
                # Refresh the stream if it's been more than 5 seconds since the last successful frame
                if time.time() - last_successful_frame_time[i] > 5:
                    handle_frame_read_error(i)

        # Display the combined frame
        cv2.imshow("RTSP Streams", canvas)

        # Exit when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

try:
    main_loop()
except KeyboardInterrupt:
    pass
finally:
    # Release the capture objects and close the window
    for cap in caps:
        cap.release()
    cv2.destroyAllWindows()

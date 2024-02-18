import cv2

# Read RTSP stream URLs from a text file
with open("rtsp_urls.txt", "r") as file:
    rtsp_urls = [line.strip() for line in file]

# Create capture objects for each stream
caps = [cv2.VideoCapture(url) for url in rtsp_urls]

# Check if the capture objects were successfully opened
if not all(cap.isOpened() for cap in caps):
    print("Error opening one or more streams")
    exit()

# Set the dimensions for each stream's window
window_width = 640
window_height = 480

# Create a window to display the combined streams
cv2.namedWindow("RTSP Streams", cv2.WINDOW_NORMAL)
cv2.resizeWindow("RTSP Streams", window_width * 2, window_height * 2)

while True:
    frames = [cap.read()[1] for cap in caps]

    if not all(frame is not None for frame in frames):
        print("Error reading one or more frames")
        break

    # Resize frames to the desired dimensions
    resized_frames = [cv2.resize(frame, (window_width, window_height)) for frame in frames]

    # Arrange frames in a 2x2 grid
    top_row = cv2.hconcat(resized_frames[:2])
    bottom_row = cv2.hconcat(resized_frames[2:])
    combined_frame = cv2.vconcat([top_row, bottom_row])

    # Display the combined frame
    cv2.imshow("RTSP Streams", combined_frame)

    # Exit when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture objects and close the window
for cap in caps:
    cap.release()
cv2.destroyAllWindows()

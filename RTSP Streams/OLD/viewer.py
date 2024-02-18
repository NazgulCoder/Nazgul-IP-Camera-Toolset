import cv2

# Replace these URLs with your actual RTSP stream URLs
STREAM1_URL = "rtsp://URL"
STREAM2_URL = "rtsp://URL"
STREAM3_URL = "rtsp://URL"
STREAM4_URL = "rtsp://URL"

# Create capture objects for each stream
cap1 = cv2.VideoCapture(STREAM1_URL)
cap2 = cv2.VideoCapture(STREAM2_URL)
cap3 = cv2.VideoCapture(STREAM3_URL)
cap4 = cv2.VideoCapture(STREAM4_URL)

# Check if the capture objects were successfully opened
if not (cap1.isOpened() and cap2.isOpened() and cap3.isOpened() and cap4.isOpened()):
    print("Error opening one or more streams")
    exit()

# Set the dimensions for each stream's window
window_width = 640
window_height = 480

# Create a window to display the combined streams
cv2.namedWindow("RTSP Streams", cv2.WINDOW_NORMAL)
cv2.resizeWindow("RTSP Streams", window_width * 2, window_height * 2)

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()
    ret4, frame4 = cap4.read()

    if not (ret1 and ret2 and ret3 and ret4):
        print("Error reading one or more frames")
        break

    # Resize frames to the desired dimensions
    frame1 = cv2.resize(frame1, (window_width, window_height))
    frame2 = cv2.resize(frame2, (window_width, window_height))
    frame3 = cv2.resize(frame3, (window_width, window_height))
    frame4 = cv2.resize(frame4, (window_width, window_height))

    # Arrange frames in a 2x2 grid
    top_row = cv2.hconcat([frame1, frame2])
    bottom_row = cv2.hconcat([frame3, frame4])
    combined_frame = cv2.vconcat([top_row, bottom_row])

    # Display the combined frame
    cv2.imshow("RTSP Streams", combined_frame)

    # Exit when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture objects and close the window
cap1.release()
cap2.release()
cap3.release()
cap4.release()
cv2.destroyAllWindows()

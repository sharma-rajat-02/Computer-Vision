import cv2
import numpy as np
import pyautogui

# Initialize webcam
cap = cv2.VideoCapture(0)

# Define the HSV range for a bright Green object
# You can tweak these if your lighting is very dark
lower_green = np.array([40, 100, 100])
upper_green = np.array([80, 255, 255])

# Get screen size for mapping
screen_w, screen_h = pyautogui.size()

while True:
    success, frame = cap.read()
    if not success:
        break

    # 1. Flip frame horizontally for a mirror effect (more intuitive)
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # 2. Convert to HSV and create a mask
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # 3. Clean up noise (small dots)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # 4. Find the largest green object
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Get the largest contour by area
        largest_cnt = max(contours, key=cv2.contourArea)
        
        if cv2.contourArea(largest_cnt) > 500: # Minimum size threshold
            # Get the center point (Centroid)
            M = cv2.moments(largest_cnt)
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                # 5. Map camera coordinates to Screen coordinates
                # Scale cx/cy from camera resolution to screen resolution
                cursor_x = np.interp(cx, [0, w], [0, screen_w])
                cursor_y = np.interp(cy, [0, h], [0, screen_h])

                # Move the mouse
                pyautogui.moveTo(cursor_x, cursor_y, duration=0.1)

                # Visual feedback: Draw a circle on the tracked object
                cv2.circle(frame, (cx, cy), 10, (0, 255, 0), -1)

    # Display the windows
    cv2.imshow('Virtual Mouse - Feed', frame)
    cv2.imshow('Color Mask', mask)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
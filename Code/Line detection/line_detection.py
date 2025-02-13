import pygame
import pygame.camera
import numpy as np

pygame.init()
pygame.camera.init()

# Open the webcam
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0], (640, 480))
cam.start()

screen = pygame.display.set_mode((640, 480))

running = True
while running:
    # Capture frame
    frame = cam.get_image()
    
    # Convert to grayscale manually
    arr = pygame.surfarray.array3d(frame)
    gray = np.dot(arr[..., :3], [0.2989, 0.5870, 0.1140])  # Manual grayscale

    # Edge detection using Sobel filter
    dx = np.diff(gray, axis=1)
    dy = np.diff(gray, axis=0)
    edges = np.hypot(dx[:-1, :], dy[:, :-1])

    # Display
    pygame.surfarray.blit_array(screen, np.dstack([edges]*3))  # Convert to color format
    pygame.display.update()

    # Exit with 'q'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

cam.stop()
pygame.quit()

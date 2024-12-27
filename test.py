import kivy
import pygame
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer
from moviepy import VideoFileClip

# Initialize pygame
pygame.init()

# Load video using moviepy
clip = VideoFileClip(r"C:\Users\wanne\Desktop\Celestial-TCG-Blizzard\UI elements\Backgroundvideo3.mp4")

# Create a pygame window
screen = pygame.display.set_mode(clip.size)

# Play the video
for frame in clip.iter_frames(fps=30, with_times=False):
    # Convert frame to pygame surface
    frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

    # Display the frame
    screen.blit(frame_surface, (0, 0))
    pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

# Quit pygame
pygame.quit()

if __name__ == '__main__':
    VideoApp().run()
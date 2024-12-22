


import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer


class VideoApp(App):
    def build(self):
        player = VideoPlayer(source=r"C:\Users\wanne\Desktop\Celestial-TCG-Blizzard\UI elements\Backgroundvideo3.mp4")

        player.state = 'play'
        player.allow_stretch = True

        return player


if __name__ == '__main__':
    VideoApp().run()

    #
    #
    #
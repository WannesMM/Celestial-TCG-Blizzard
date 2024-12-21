from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
Config.set('kivy', 'log_level', 'debug')


class VideoApp(App):
    def build(self):
        layout = BoxLayout()
        video = VideoPlayer(source=r'C:\Users\wanne\Desktop\Celestial-TCG-Blizzard\UI elements\Backgroundvideo2.mp4', state='play')
        layout.add_widget(video)
        return layout

if __name__ == '__main__':
    VideoApp().run()

    #
    #
    #
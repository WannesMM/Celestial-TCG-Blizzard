import os
from kivy.app import App
from kivy.core.window import Window
from kivy.config import Config
from battlefield import build_battlefield
from kivy.core.audio import SoundLoader

# Set fullscreen mode before the window is created
Config.set('graphics', 'fullscreen', '0') #auto for fullscreen
Config.write()

class Main(App):

    def on_start(self):
        self.music = SoundLoader.load(r'C:\Users\wanne\Desktop\Celestial-TCG-Blizzard\UI elements\TitleScreen1.mp3')
        if self.music:
            self.music.loop = True
            self.music.play()

    def build(self):
        return build_battlefield()

if __name__ == "__main__":
    Main().run()

from kivy.app import App
from kivy.config import Config
from setup_game import setup_game

# Set fullscreen mode before the window is created
Config.set('graphics', 'fullscreen', '0') #auto for fullscreen
Config.write()

class Main(App):
    def build(self):
        return setup_game()
        
if __name__ == "__main__":
    Main().run()

import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config

# Set fullscreen mode before the window is created
Config.set('graphics', 'fullscreen', '0') #auto for fullscreen
Config.write()

Builder.load_file("style.kv")

def get_card_image_filepath(card_name):
    base_directory = os.path.join(os.path.dirname(__file__), 'images')
    image_filename = f"{card_name}.png"
    image_filepath = os.path.join(base_directory, image_filename)
    
    print(f"Checking for image at: {image_filepath}")  # Debug print
    
    if os.path.exists(image_filepath):
        print(f"Image found: {image_filepath}")  # Debug print
        return image_filepath
    else:
        print(f"IMAGE NIET GEVONDEN: {image_filepath}")
        return os.path.join(base_directory, 'image not found.png')

class Main(App):
    def build(self):
        # Set minimum window size for PC
        Window.minimum_width = 800
        Window.minimum_height = 600

        # Set default window size for PC to mimic landscape mode
        Window.fullscreen = False #'auto' for fullscreen

        # Set orientation to landscape for mobile devices
        Config.set('graphics', 'orientation', 'landscape')


        stylevars = Style()
        base_path = os.path.dirname(__file__)
        video_path = os.path.join(base_path, "UI elements", "Background video.mp4")
        
        print(f"Setting background video source to: {video_path}")  # Debug print
        
        # Print the contents of the UI elements directory
        ui_elements_path = os.path.join(base_path, "UI elements")
        print(f"Contents of {ui_elements_path}: {os.listdir(ui_elements_path)}")  # Debug print
        
        if os.path.exists(video_path):
            print(f"Background video file found: {video_path}")  # Debug print
        else:
            print(f"BACKGROUND VIDEO FILE NOT FOUND: {video_path}")  # Debug print
        
        stylevars.ids.background_video.source = video_path

        stylevars.ids.card_image_ally1.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_ally2.source = get_card_image_filepath("Noma Greon - skin1")
        stylevars.ids.card_image_ally3.source = get_card_image_filepath("Bartholomew Balderstone")

        stylevars.ids.card_image_ally_area1.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_ally_area2.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_ally_area3.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_ally_area4.source = get_card_image_filepath("torinn inn")

        stylevars.ids.card_image_ally_entity1.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_ally_entity2.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_ally_entity3.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_ally_entity4.source = get_card_image_filepath("torinn inn")

        stylevars.ids.card_image_enemy1.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_enemy2.source = get_card_image_filepath("Noma Greon - skin1")
        stylevars.ids.card_image_enemy3.source = get_card_image_filepath("Bartholomew Balderstone")

        stylevars.ids.card_image_enemy_area1.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_enemy_area2.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_enemy_area3.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_enemy_area4.source = get_card_image_filepath("torinn inn")

        stylevars.ids.card_image_enemy_entity1.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_enemy_entity2.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_enemy_entity3.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_enemy_entity4.source = get_card_image_filepath("torinn inn")

        return stylevars
    
class Style(Widget):
    pass

if __name__ == "__main__":
    Main().run()

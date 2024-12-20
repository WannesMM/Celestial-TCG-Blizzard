import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.video import Video

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
        stylevars = Style()


        #Code to get a background video (does not work)
        #base_path = os.path.dirname(__file__)

        # video_path = os.path.join(base_path, "UI elements", "Background.mp4")
        
        # print(f"Setting video source to: {video_path}")  # Debug print
        
        # if os.path.exists(video_path):
        #     print(f"Video file found: {video_path}")  # Debug print
        # else:
        #     print(f"VIDEO FILE NOT FOUND: {video_path}")  # Debug print
        
        # stylevars.ids.background_video.source = video_path

        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "UI elements", "Background image.jpeg")
        
        print(f"Setting background image source to: {image_path}")  # Debug print
        
        if os.path.exists(image_path):
            print(f"Background image file found: {image_path}")  # Debug print
        else:
            print(f"BACKGROUND IMAGE FILE NOT FOUND: {image_path}")  # Debug print
        
        stylevars.ids.background_image.source = image_path

        stylevars.ids.card_image_ally1.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_ally2.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_ally3.source = get_card_image_filepath("torinn inn")

        stylevars.ids.card_image_enemy1.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_enemy2.source = get_card_image_filepath("torinn inn")
        stylevars.ids.card_image_enemy3.source = get_card_image_filepath("torinn inn")

        return stylevars

class Style(Widget):
    pass

if __name__ == "__main__":
    Main().run()

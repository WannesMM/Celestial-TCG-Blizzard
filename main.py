import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from catalog import get_card_image_filepath
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.video import Video

Builder.load_file("style.kv")

class Main(App):
    def build(self):
        stylevars = Style()
        stylevars.ids.background_video.source = r"C:\Users\wanne\OneDrive\Bureaublad\Celestial Mobile\UI elements\Background.mp4"

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

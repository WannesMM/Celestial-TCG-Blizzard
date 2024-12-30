import os
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from card_info_right import CardInfoPopup
Builder.load_file("user_interface/BattlefieldRelative.kv")

class BattlefieldRelative(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.card_button = Button(text="Select Card")
        self.card_button.bind(on_press=self.show_card_info)
        self.add_widget(self.card_button)
        # Add buttons for character cards
        self.character_buttons = []
        for i in range(3):
            btn = Button(text=f"Character {i+1}")
            btn.bind(on_press=self.show_card_info)
            self.character_buttons.append(btn)
            self.add_widget(btn)

    def show_card_info(self, instance):
        card_info = "Card Name: Example Card\nAttack: 10\nDefense: 5"
        popup = CardInfoPopup(card_info)
        popup.open()

def build_battlefield():
    # Set minimum window size for PC
    Window.minimum_width = 800
    Window.minimum_height = 600

    # Set default window size for PC to mimic landscape mode
    Window.fullscreen = False #'auto' for fullscreen

    # Set orientation to landscape for mobile devices
    Config.set('graphics', 'orientation', 'landscape')

    stylevars = BattlefieldRelative()
    base_path = os.path.dirname(__file__)
    image_path = os.path.join(base_path, '..', 'UI elements', 'Background image.jpeg')
    
    print(f"Setting background image source to: {image_path}")  # Debug print
    
    # Print the contents of the UI elements directory
    ui_elements_path = os.path.join(base_path, '..', 'UI elements')
    print(f"Contents of {ui_elements_path}: {os.listdir(ui_elements_path)}")  # Debug print
    
    if os.path.exists(image_path):
        print(f"Background image file found: {image_path}")  # Debug print
        stylevars.ids.background_image.source = image_path
    else:
        print(f"BACKGROUND IMAGE FILE NOT FOUND: {image_path}")  # Debug print
        # Set a default image if the background image is not found
        stylevars.ids.background_image.source = os.path.join(base_path, '..', 'images', 'image not found.png')

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

def get_card_image_filepath(card_name):
    base_directory = os.path.join(os.path.dirname(__file__), '..', 'images')
    image_filename = f"{card_name}.png"
    image_filepath = os.path.join(base_directory, image_filename)
    
    print(f"Checking for image at: {image_filepath}")  # Debug print
    
    if os.path.exists(image_filepath):
        print(f"Image found: {image_filepath}")  # Debug print
        return image_filepath
    else:
        print(f"IMAGE NIET GEVONDEN: {image_filepath}")
        return os.path.join(base_directory, 'image not found.png')
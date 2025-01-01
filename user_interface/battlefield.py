import os
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.app import App
from .card_info_right import CardInfoPopup  # Ensure correct import
from kivy.uix.anchorlayout import AnchorLayout

def build_battlefield():
    # Set minimum window size for PC
    Window.minimum_width = 800
    Window.minimum_height = 600

    # Set default window size for PC to mimic landscape mode
    Window.fullscreen = False  # 'auto' for fullscreen

    # Set orientation to landscape for mobile devices
    Config.set('graphics', 'orientation', 'landscape')

    # Initialize and return BattlefieldRelative
    battlefield = BattlefieldRelative()

    return battlefield

class BattlefieldRelative(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.create_battlefield_background()
        #self.create_battlefield_layout()
        #self.create_buttons()

    def create_battlefield_background(self):
        # Background image
        self.background_image = Image(size_hint=(1, 1), allow_stretch=True, keep_ratio=True)
        self.add_widget(self.background_image)

        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, '..', 'UI elements', 'Background image.jpeg')
        if os.path.exists(image_path):
            self.background_image.source = image_path
        else:
            self.background_image.source = os.path.join(base_path, '..', 'images', 'image not found.png')

    def create_buttons(self):
        # Create card selection button
        self.card_button = Button(text="Select Card", size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 0.95})
        self.card_button.bind(on_press=self.show_card_info)
        self.add_widget(self.card_button)

        # Add buttons for character cards
        self.character_buttons = []
        for i in range(3):
            btn = Button(text=f"Character {i+1}", size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'center_y': 0.85 - i * 0.1})
            btn.bind(on_press=self.show_card_info)
            self.character_buttons.append(btn)
            self.add_widget(btn)

    def show_card_info(self, instance):
        card_info = "Card Name: Example Card\nAttack: 10\nDefense: 5"
        popup = CardInfoPopup(card_info)
        popup.open()

    def create_battlefield_layout(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', size_hint=(0.9, 0.9), pos_hint={'center_x': 0.5, 'center_y': 0.5}, spacing=25, padding=50)
        self.add_widget(main_layout)

        # Enemy division
        enemy_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.5), spacing=10, padding=10)
        main_layout.add_widget(enemy_layout)

        # Enemy area cards
        enemy_area_layout = BoxLayout(orientation='horizontal', size_hint=(0.5, 1), spacing=10)
        enemy_layout.add_widget(enemy_area_layout)

        enemy_area_vertical1 = BoxLayout(orientation='vertical', spacing=10)
        enemy_area_layout.add_widget(enemy_area_vertical1)
        self.card_image_enemy_area1 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        self.card_image_enemy_area2 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        enemy_area_vertical1.add_widget(self.card_image_enemy_area1)
        enemy_area_vertical1.add_widget(self.card_image_enemy_area2)

        enemy_area_vertical2 = BoxLayout(orientation='vertical', spacing=10)
        enemy_area_layout.add_widget(enemy_area_vertical2)
        self.card_image_enemy_area3 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        self.card_image_enemy_area4 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        enemy_area_vertical2.add_widget(self.card_image_enemy_area3)
        enemy_area_vertical2.add_widget(self.card_image_enemy_area4)

        # Enemy character cards
        enemy_character_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint=(1.5, 1))
        enemy_layout.add_widget(enemy_character_layout)

        enemy_character1 = FloatLayout(size_hint=(1, 1))
        self.card_image_enemy1 = Image(source='', size_hint=(1, 1))
        self.hp_label_enemy1 = Label(text='HP', size_hint=(None, None), pos=(70, 90))
        self.hp_label_enemy1.size = self.hp_label_enemy1.texture_size  # Set size after initialization
        enemy_character1.add_widget(self.card_image_enemy1)
        enemy_character1.add_widget(self.hp_label_enemy1)
        enemy_character_layout.add_widget(enemy_character1)

        enemy_character2 = FloatLayout(size_hint=(1, 1))
        self.card_image_enemy2 = Image(source='', size_hint=(1, 1))
        self.hp_label_enemy2 = Label(text='HP', size_hint=(None, None), pos=(70, 90))
        self.hp_label_enemy2.size = self.hp_label_enemy2.texture_size  # Set size after initialization
        enemy_character2.add_widget(self.card_image_enemy2)
        enemy_character2.add_widget(self.hp_label_enemy2)
        enemy_character_layout.add_widget(enemy_character2)

        enemy_character3 = FloatLayout(size_hint=(1, 1))
        self.card_image_enemy3 = Image(source='', size_hint=(1, 1))
        self.hp_label_enemy3 = Label(text='HP', size_hint=(None, None), pos=(70, 90))
        self.hp_label_enemy3.size = self.hp_label_enemy3.texture_size  # Set size after initialization
        enemy_character3.add_widget(self.card_image_enemy3)
        enemy_character3.add_widget(self.hp_label_enemy3)
        enemy_character_layout.add_widget(enemy_character3)

        # Enemy entity cards
        enemy_entity_layout = BoxLayout(orientation='horizontal', size_hint=(0.5, 1), spacing=10)
        enemy_layout.add_widget(enemy_entity_layout)

        enemy_entity_vertical1 = BoxLayout(orientation='vertical', spacing=10)
        enemy_entity_layout.add_widget(enemy_entity_vertical1)
        self.card_image_enemy_entity1 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        self.card_image_enemy_entity2 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        enemy_entity_vertical1.add_widget(self.card_image_enemy_entity1)
        enemy_entity_vertical1.add_widget(self.card_image_enemy_entity2)

        enemy_entity_vertical2 = BoxLayout(orientation='vertical', spacing=10)
        enemy_entity_layout.add_widget(enemy_entity_vertical2)
        self.card_image_enemy_entity3 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        self.card_image_enemy_entity4 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        enemy_entity_vertical2.add_widget(self.card_image_enemy_entity3)
        enemy_entity_vertical2.add_widget(self.card_image_enemy_entity4)

        # Ally division
        ally_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.5), spacing=10, padding=10)
        main_layout.add_widget(ally_layout)

        # Ally area cards
        ally_area_layout = BoxLayout(orientation='horizontal', size_hint=(0.5, 1), spacing=10)
        ally_layout.add_widget(ally_area_layout)

        ally_area_vertical1 = BoxLayout(orientation='vertical', spacing=10)
        ally_area_layout.add_widget(ally_area_vertical1)
        self.card_image_ally_area1 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        self.card_image_ally_area2 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        ally_area_vertical1.add_widget(self.card_image_ally_area1)
        ally_area_vertical1.add_widget(self.card_image_ally_area2)

        ally_area_vertical2 = BoxLayout(orientation='vertical', spacing=10)
        ally_area_layout.add_widget(ally_area_vertical2)
        self.card_image_ally_area3 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        self.card_image_ally_area4 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        ally_area_vertical2.add_widget(self.card_image_ally_area3)
        ally_area_vertical2.add_widget(self.card_image_ally_area4)

        # Ally character cards
        ally_character_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint=(1.5, 1))
        ally_layout.add_widget(ally_character_layout)

        ally_character1 = RelativeLayout(size_hint=(1, 1))
        self.card_image_ally1 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 1))
        self.hp_label_ally1 = Label(text='HP', size_hint=(None, None), pos_hint={'right': 1, 'top': 1})
        self.hp_label_ally1.size = self.hp_label_ally1.texture_size  # Set size after initialization
        ally_character1.add_widget(self.card_image_ally1)
        ally_character1.add_widget(self.hp_label_ally1)
        ally_character_layout.add_widget(ally_character1)

        ally_character2 = RelativeLayout(size_hint=(1, 1))
        self.card_image_ally2 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 1))
        self.hp_label_ally2 = Label(text='HP', size_hint=(None, None), pos_hint={'right': 1, 'top': 1})
        self.hp_label_ally2.size = self.hp_label_ally2.texture_size  # Set size after initialization
        ally_character2.add_widget(self.card_image_ally2)
        ally_character2.add_widget(self.hp_label_ally2)
        ally_character_layout.add_widget(ally_character2)

        ally_character3 = RelativeLayout(size_hint=(1, 1))
        self.card_image_ally3 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 1))
        self.hp_label_ally3 = Label(text='HP', size_hint=(None, None), pos_hint={'right': 1, 'top': 1})
        self.hp_label_ally3.size = self.hp_label_ally3.texture_size  # Set size after initialization
        ally_character3.add_widget(self.card_image_ally3)
        ally_character3.add_widget(self.hp_label_ally3)
        ally_character_layout.add_widget(ally_character3)

        # Ally entity cards
        ally_entity_layout = BoxLayout(orientation='horizontal', size_hint=(0.5, 1), spacing=10)
        ally_layout.add_widget(ally_entity_layout)

        ally_entity_vertical1 = BoxLayout(orientation='vertical', spacing=10)
        ally_entity_layout.add_widget(ally_entity_vertical1)
        self.card_image_ally_entity1 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        self.card_image_ally_entity2 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        ally_entity_vertical1.add_widget(self.card_image_ally_entity1)
        ally_entity_vertical1.add_widget(self.card_image_ally_entity2)

        ally_entity_vertical2 = BoxLayout(orientation='vertical', spacing=10)
        ally_entity_layout.add_widget(ally_entity_vertical2)
        self.card_image_ally_entity3 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        self.card_image_ally_entity4 = Image(source='', allow_stretch=True, keep_ratio=True, size_hint=(1, 0.5))
        ally_entity_vertical2.add_widget(self.card_image_ally_entity3)
        ally_entity_vertical2.add_widget(self.card_image_ally_entity4)

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
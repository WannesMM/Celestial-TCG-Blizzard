from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button

class Card(App):
    def __init__(self, card_name,):
        self.card_name = card_name

    def build(self):
        layout = GridLayout(cols=4)
    
        card = Image(source=get_card_image_filepath(self.card_name))
        layout.add_widget(card)
        
        return layout

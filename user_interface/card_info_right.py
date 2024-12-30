from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class CardInfoPopup(Popup):
    def __init__(self, card_info, **kwargs):
        super(CardInfoPopup, self).__init__(**kwargs)
        self.title = 'Card Information'
        self.size_hint = (0.3, 1)  # Cover the right side of the screen
        self.pos_hint = {'right': 1}

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text=card_info))
        close_button = Button(text='Close', size_hint_y=None, height=50)
        close_button.bind(on_release=self.dismiss)
        layout.add_widget(close_button)

        self.add_widget(layout)

class TestApp(App):
    def build(self):
        main_layout = BoxLayout()
        card_button = Button(text='Show Card Info')
        card_button.bind(on_release=self.show_card_info)
        main_layout.add_widget(card_button)
        return main_layout

    def show_card_info(self, instance):
        card_info = "Card Name: Example\nCard Type: Spell\nCard Description: This is an example card."
        popup = CardInfoPopup(card_info)
        popup.open()

if __name__ == '__main__':
    TestApp().run()
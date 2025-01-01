from gamestate import Gamestate  
from character_cards.character_card import CharacterCard
from character_cards.torinn_inn import Torinn_Inn
from user_interface.battlefield import build_battlefield
from kivy.core.audio import SoundLoader

def setup_game():
    setup_music()
    #setup_game_state()
    return setup_battlefield()

def setup_music():
    music = SoundLoader.load(r'C:\Users\wanne\Desktop\Celestial-TCG-Blizzard\UI elements\TitleScreen1.mp3')
    if music:
        music.loop = True
        music.play()

def setup_battlefield():
    return build_battlefield()

def setup_game_state():
    
    torinn_inn_ally = Torinn_Inn(True)
    torinn_inn_enemy = Torinn_Inn(False)

    game_state = Gamestate([torinn_inn_ally],[torinn_inn_enemy])  # Corrected variable name
    torinn_inn_enemy.set_gamestate(game_state)
    torinn_inn_ally.set_gamestate(game_state)
    
    game_state.execute_round()

# Example usage
if __name__ == "__main__":
    game_state = setup_game_state()

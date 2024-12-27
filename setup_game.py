from gamestate import Gamestate  
from character_cards.character_card import CharacterCard
from character_cards.torinn_inn import Torinn_Inn

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

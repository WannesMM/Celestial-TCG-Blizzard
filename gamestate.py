import random

class Gamestate:
    def __init__(self, ally_characters, enemy_characters):
        self.turn_counter = 0
        self.round_counter = 0
        self.ally_characters = ally_characters
        self.enemy_characters = enemy_characters
        self.ally_active_character = None
        self.enemy_active_character = None
        self.scheduled_effects = []
        self.ally_gold = 0
        self.enemy_gold = 0
        self.ally_turn = True
        self.winner = None
        self.last_turn_ender = None
        self.ally_round_end = False
        self.enemy_round_end = False
        self.turn_end = False

    def get_turn_end(self):
        return self.turn_end

    def set_turn_end(self, turn_end):
        self.turn_end = turn_end

    def get_ally_round_end(self):
        return self.ally_round_end

    def set_ally_round_end(self, ally_round_end):
        self.ally_round_end = ally_round_end

    def get_enemy_round_end(self):
        return self.enemy_round_end

    def set_enemy_round_end(self, enemy_round_end):
        self.enemy_round_end = enemy_round_end

    # True means the ally ended turn last, False means the enemy ended turn last
    def get_last_turn_ender(self):
        return self.last_turn_ender

    def set_last_turn_ender(self, last_turn_ender):
        self.last_turn_ender = last_turn_ender

    def get_winner(self):
        return self.winner

    def set_winner(self, winner):
        self.winner = winner

    def get_ally_turn(self):
        return self.ally_turn
    
    def get_enemy_turn(self):
        return not self.ally_turn

    def set_ally_turn(self, ally_turn):
        self.ally_turn = ally_turn

    def get_ally_characters(self):
        return self.ally_characters

    def set_ally_characters(self, ally_characters):
        self.ally_characters = ally_characters

    def get_enemy_characters(self):
        return self.enemy_characters

    def set_enemy_characters(self, enemy_characters):
        self.enemy_characters = enemy_characters

    def get_ally_active_character(self):
        return self.ally_active_character

    def set_ally_active_character(self, ally_active_character):
        self.ally_active_character = ally_active_character

    def get_enemy_active_character(self):
        return self.enemy_active_character

    def set_enemy_active_character(self, enemy_active_character):
        self.enemy_active_character = enemy_active_character

    def get_scheduled_effects(self):
        return self.scheduled_effects

    def set_scheduled_effects(self, scheduled_effects):
        self.scheduled_effects = scheduled_effects

    def get_ally_gold(self):
        return self.ally_gold

    def set_ally_gold(self, ally_gold):
        self.ally_gold = ally_gold

    def set_gold(self, ally, amount):
        if ally:
            self.ally_gold = amount
        else:
            self.enemy_gold = amount

    def check_cost(self, ally, cost):
        """
        Checks if the specified ally has enough gold to cover the given cost.
        Args:
            allied (boolean)): Determines which player's gold to check against the cost.
            cost (int): The cost to be checked against the ally's gold.
        Returns:
            bool: True if the ally or enemy has enough gold, False otherwise.
        """

        if(cost <= self.get_gold(ally)):
            return True
        
        print("Not enough gold")
        return False

    def check_energy(self, character, cost):
        """
        Checks if the character has enough energy to cover the specified cost.
        Args:
            character (Character): The character whose energy is being checked.
            cost (int): The energy cost to be checked against the character's current energy.
        Returns:
            bool: True if the character has enough energy, False otherwise.
        """
        if(cost <= character.get_energy()):
            return True
        
        print("Not enough energy")
        return False

    def get_gold(self, ally):
        if ally:
            return self.ally_gold
        else:
            return self.enemy_gold

    def get_enemy_gold(self):
        return self.enemy_gold

    def set_enemy_gold(self, enemy_gold):
        self.enemy_gold = enemy_gold

    def next_turn(self):
        self.turn_counter += 1

    def next_round(self):
        """
        Reset the turn counter, increase the round counter and set the round end booleans to False
        """
    
        self.set_ally_round_end(False)
        self.set_enemy_round_end(False)
        self.round_counter += 1
        self.turn_counter = 0

    def draw_cards(self, ally, amount):
        pass

    def get_turn_counter(self):
        return self.turn_counter

    def get_round_counter(self):
        return self.round_counter
    
    def play_card(self):
        pass

    def gain_energy(self, character, amount):
        character.gain_energy(amount)

    def set_energy(self, character, amount):
        character.set_energy(amount)

    def gain_gold(self, ally, amount):
        if ally:
            self.ally_gold += amount
        else:
            self.enemy_gold += amount
        
    def reduce_gold(self, ally, amount):
        if ally:
            self.ally_gold -= amount
        else:
            self.enemy_gold -= amount

    def choose_active_character(self, ally):
        number = int(input("Choose a character number: ")) - 1
        if ally:
            self.ally_active_character = self.ally_characters[number]
            print(f"Active ally character: {self.ally_active_character.get_name()}")
        else:
            self.enemy_active_character = self.enemy_characters[number]
            print(f"Active enemy character: {self.enemy_active_character.get_name()}")

    def check_round_end(self):
        if self.ally_round_end and self.enemy_round_end:
            return True
        return False
    
    def end_round(self, ally):
        """
        Ends the current round for either the ally or enemy.
        Parameters:
        ally (bool): If True, ends the round for the ally. If False, ends the round for the enemy.
        Sets the following attributes based on the value of 'ally':
        - self.ally_round_end (bool): Set to True if 'ally' is True.
        - self.enemy_round_end (bool): Set to True if 'ally' is False.
        - self.set_last_turn_ender (bool): Calls this method with True if 'ally' is True, otherwise False.
        """
        if ally:
            self.ally_round_end = True
            self.set_last_turn_ender(True)
        else:
            self.enemy_round_end = True
            self.set_last_turn_ender(False)

    def execute_round(self):
        # Start of the game
        print(f"Game Start")
        print(f"Ally choose active character:")
        self.choose_active_character(True)
        print(f"Enemy choose active character:")
        self.choose_active_character(False)
        self.draw_cards(True, 3)
        self.draw_cards(False, 3)

        # Start of the round loop
        while(self.get_winner() == None):
   
            #Gold rolls
            self.set_ally_gold(self.dice_throw(8, 2, 'advantage'))
            print(f"Ally gold: {self.get_ally_gold()}")
            self.set_enemy_gold(self.dice_throw(8, 2, 'advantage'))
            print(f"Enemy gold: {self.get_enemy_gold()}")

            #Who moves first
            if(self.get_last_turn_ender()):
                self.set_ally_turn(False)
            elif(self.get_last_turn_ender() == False):
                self.set_ally_turn(True)
            elif(self.get_round_counter() == 0):
                if(self.get_ally_gold() <= self.get_enemy_gold()):
                    self.set_ally_turn(True)
                else:
                    self.set_ally_turn(False)
            
            #Initialise round
            self.next_round()

            #Draw cards
            self.draw_cards(True, 2)
            self.draw_cards(False, 2)

            print(f"Round {self.get_round_counter()}")

            #Start of the turn loop
            while(self.check_round_end() == False and self.get_winner() == None):

                #Initialise turn
                self.next_turn()
                print(f"Turn {self.get_turn_counter()}")

                #Turn
                self.turn()

        if self.get_winner():
            print(f"Ally wins")
        else:
            print(f"Enemy wins")



    def deal_damage(self, attacking_character, damage, target_character):
        """
        Deal damage to a target character
        """	

        print(f"{attacking_character.get_name()} deals {damage} damage to {target_character.get_name()}")
        target_character.take_damage(damage)
        

    def choose_target(self, attacker):
        number = input("Choose a character number: ") - 1
        if attacker.get_allied():
            print(f"Target selected: {self.enemy_characters[number].get_name()}")
            return self.enemy_characters[number]
        else:
            print(f"Target selected: {self.ally_characters[number].get_name()}")
            return self.enemy_characters[number]

    def get_active_opponent(self, attacker):
        if attacker.get_allied():
            return self.get_enemy_active_character()
        else:
            return self.ally_active_character

    # moment is an integer representing the moment in the round when the effect should be executed
    # 0 is the start of the round, 1 is after the first character has taken their turn, etc.
    def schedule_effect(self, effect, moment):
        pass

    def dice_throw(self, max_number, count, mode='normal'):
        numbers = [random.randint(1, max_number) for _ in range(count)]
        if mode == 'advantage':
            return max(numbers)
        elif mode == 'disadvantage':
            return min(numbers)
        else:
            return numbers
        
    def use_move(self, character, move):
        
        if move == 'na':
            character.normal_attack()
        elif move == 'sa':
            character.special_attack()
        elif move == 'ca':
            character.charged_attack()

    def input_action(self, character):
        action = input("Choose an action: move, use card, switch, end round --> ")
        self.use_action(character, action)

    def input_move(self, character):
        """
        Prompts the user to choose a move for the given character and executes the move if the cost and energy requirements are met.
        Parameters:
        character (Character): The character for which the move is being chosen.
        The function displays the descriptions of the character's normal, special, and charged attacks, then prompts the user to choose one of these moves by entering 'na', 'sa', or 'ca'. If the chosen move's cost and energy requirements are met, the move is executed and a message is printed indicating the move used by the character.
        """

        print(character.normal_attack_description())
        print("")
        print(character.special_attack_description())
        print("")
        print(character.charged_attack_description())
        print("")
        move = input("Choose a move: na, sa, ca --> ")
        print("")

        if(move == 'na'):
            if(self.check_cost(character.get_allied(), character.get_na_cost())):
                print(character.get_name() + " uses " + character.normal_attack_description()[0])
                self.use_move(character, move)
        elif(move == 'sa'):
            if(self.check_cost(character.get_allied(), character.get_sa_cost())):
                print(character.get_name() + " uses " + character.special_attack_description()[0])
                self.use_move(character, move)
        elif(move == 'ca'):
            if(self.check_cost(character.get_allied(), character.get_ca_cost())):
                if(self.check_energy(character, character.get_ca_energy_cost())):
                    print(character.get_name() + " uses " + character.charged_attack_description()[0])
                    self.use_move(character, move)
        

    def use_action(self, character, action):
        if action == 'move':
            self.input_move(character)
            self.set_turn_end(True)
        elif action == 'use card':
            self.play_card()
        elif action == 'switch':
            self.choose_active_character(character.get_allied())
            self.set_turn_end(True)
        elif action == 'end round':
            self.end_round(character.get_allied())
            self.set_turn_end(True)

        self.display_gamestate()

    def turn(self):
        """
        Execute a turn.
        checks whose turn it is and executes the turn accordingly.
        checks if the round has ended.
        calls the input_action method to get the player's action.
        """
        i = 0
        while i < 2:
            while(self.get_turn_end() == False):
                if self.get_ally_round_end() == True and self.get_ally_turn() == True:
                    self.set_ally_turn(not self.get_ally_turn())

                if self.get_enemy_round_end() == True and self.get_enemy_turn() == False:
                    self.set_ally_turn(not self.get_ally_turn())

                if self.get_ally_turn() and self.get_ally_round_end() == False:
                    character = self.get_ally_active_character()
                    print(f"Ally turn")
                    self.input_action(character)
                elif self.get_ally_turn() == False and self.get_enemy_round_end() == False:
                    print(f"Enemy turn")
                    character = self.get_enemy_active_character()
                    self.input_action(character)
            i += 1
            self.set_ally_turn(not self.get_ally_turn())
            self.set_turn_end(False)
        
    def check_winner(self):
        ally_ko = True
        enemy_ko = True

        for character in self.ally_characters:
            if not character.get_ko():
                ally_ko = False

        for character in self.enemy_characters_characters:
            if not character.get_ko():
                enemy_ko = False

        if ally_ko:
            self.set_winner(False)
        elif enemy_ko:
            self.set_winner(True)

    def play_card(self):
        pass

    def display_gamestate(self):
        print("")
        print("")
        print(f"Allies Gold: {self.get_gold(True)}")
        for character in self.ally_characters:
            print(character.get_name())
            print(f"HP: {character.get_hp()}")
            print(f"Energy: {character.get_energy()}")
            print("")

        print(f"Enemies Gold: {self.get_gold(False)}")
        for character in self.enemy_characters:
            print(character.get_name())
            print(f"HP: {character.get_hp()}")
            print(f"Energy: {character.get_energy()}")
            print("")
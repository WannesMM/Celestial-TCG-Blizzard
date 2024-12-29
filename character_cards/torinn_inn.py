from character_cards.character_card import CharacterCard
from typing import Tuple

class Torinn_Inn(CharacterCard):
    def __init__(self, allied):
        super().__init__(allied)
        self.name = "Torinn Inn"
        self.hp = 8
        self.max_hp = 10
        self.max_energy = 2
        self.energy = 0
        self.na_dmg = 1
        self.na_cost = 2
        self.ca_dmg = 0
        self.ca_cost = 4
        self.ca_energy_cost = 2
        self.sa_dmg = 2
        self.sa_cost = 3

        self.smite_active = False
        self.golden_breath_counter = 0
        self.lay_on_hands_active_previous_turn = 0


    def normal_attack_description(self):
        return "Battleaxe", "Torinn puts his axe in the face of the enemy"
    
    def special_attack_description(self):
        return "Golden Breath", "This attack deals 1 damage at the start at the next 2 rounds if the enemy has no less than 5 HP"
    
    def charged_attack_description(self):
        return "Divine Smite", "Torinn smites the enemy with a divine power, add an additional 5dmg to the next normal attack"
    
    def ability_description(self):
        return "Lay on Hands", "Once per round, when Torinn is attacked, he heals 1 HP"

    def normal_attack(self):

        damage = self.na_dmg
        if(self.smite_active):
            damage += 5
        self.smite_active = False

        self.gamestate.deal_damage(self, damage, self.gamestate.get_active_opponent(self))
        self.gamestate.gain_energy(self, 1)
        self.gamestate.reduce_gold(self.allied, self.na_cost)
    
    def special_attack(self):

        print(self.get_name() + " uses " + self.special_attack_description()[0] + " on " + self.gamestate.get_active_opponent(self).get_name())

        damage = self.sa_dmg
        self.gamestate.deal_damage(self, damage, self.gamestate.get_active_opponent(self))
        self.gamestate.schedule_effect(lambda: self.golden_breath_effect(self.gamestate.get_active_opponent(self)), self, "start of round")
        self.golden_breath_counter += 2

        self.gamestate.gain_energy(self, 1)
        self.gamestate.reduce_gold(self.allied, self.sa_cost)

    def golden_breath_effect(self, target):
        if(target.get_hp() >= 5):
            print("Golden Breath effect")
            self.gamestate.deal_damage(self, 1, self.gamestate.get_active_opponent(self))
        self.golden_breath_counter -= 1

        if(self.golden_breath_counter == 0):
            self.gamestate.remove_scheduled_effect(lambda: self.golden_breath_effect(self.gamestate.get_active_opponent(self)), self)

    def charged_attack(self):

        print(self.get_name() + " uses " + self.charged_attack_description()[0] + " on " + self.gamestate.get_active_opponent(self).get_name())

        self.smite_active = True

        self.gamestate.set_energy(self, 0)
        self.gamestate.reduce_gold(self.allied, self.ca_cost)

    def take_damage(self, damage):
        print(self.get_name() + " takes " + str(damage) + " damage!")
        self.set_hp(self.get_hp() - damage)
        print(self.get_name() + " has " + str(self.get_hp()) + " HP remaining!")
        if(self.get_hp() <= 0):
            print(self.get_name() + " is knocked out!")
            self.set_hp(0)
            self.set_ko(True)
        else:
            self.ability()

    def ability(self):
        if(self.gamestate.get_turn_counter() != self.lay_on_hands_active_previous_turn):
            self.heal_hp(1)
        
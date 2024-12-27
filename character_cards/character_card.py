from abc import ABC, abstractmethod
from typing import Tuple

class CharacterCard(ABC):
    def __init__(self, allied):
        self.max_hp = 10
        self.hp = 10
        self.max_energy = 3
        self.energy = 0
        self.name = "Character Card Name"
        self.na_dmg = 2
        self.na_cost = 2
        self.sa_dmg = 0
        self.sa_cost = 0
        self.ca_dmg = 0
        self.ca_cost = 0
        self.ca_energy = 0
        self.ca_energy_cost = 0
        self.allied = allied
        self.gamestate = None
        self.ko = False

    def get_ca_energy_cost(self):
        """
        Retrieve the charged attack energy cost of the character card.
        Returns:
            int: The charged attack energy cost.
        """
        return self.ca_energy_cost

    def set_ca_energy_cost(self, ca_energy_cost):
        """
        Set the charged attack energy cost of the character card.
        Args:
            ca_energy_cost (int): The new charged attack energy cost.
        """
        self.ca_energy_cost = ca_energy_cost

    def set_gamestate(self, gamestate):
        self.gamestate = gamestate

    def get_ko(self):
        return self.ko

    def set_ko(self, ko):
        self.ko = ko

    def get_allied(self):
        """
        Retrieve the allied status of the character card.
        Returns:
            bool: True if the character card is allied, False otherwise.
        """

        return self.allied

    def set_allied(self, allied):
        self.allied = allied

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp

    def get_energy(self):
        return self.energy

    def set_energy(self, energy):
        self.energy = energy

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_max_hp(self):
        return self.max_hp

    def set_max_hp(self, max_hp):
        self.max_hp = max_hp

    def get_na_dmg(self):
        return self.na_dmg

    def set_na_dmg(self, na_dmg):
        self.na_dmg = na_dmg

    def get_na_cost(self):
        return self.na_cost

    def set_na_cost(self, na_cost):
        self.na_cost = na_cost

    def get_sa_dmg(self):
        return self.sa_dmg

    def set_sa_dmg(self, sa_dmg):
        self.sa_dmg = sa_dmg

    def get_sa_cost(self):
        return self.sa_cost

    def set_sa_cost(self, sa_cost):
        self.sa_cost = sa_cost

    def get_ca_dmg(self):
        return self.ca_dmg

    def set_ca_dmg(self, ca_dmg):
        self.ca_dmg = ca_dmg

    def get_ca_cost(self):
        return self.ca_cost

    def set_ca_cost(self, ca_cost):
        self.ca_cost = ca_cost

    def get_ca_energy(self):
        return self.ca_energy

    def set_ca_energy(self, ca_energy):
        self.ca_energy = ca_energy

    def get_max_energy(self):
        return self.max_energy

    def set_max_energy(self, max_energy):
        self.max_energy = max_energy

    def gain_energy(self, amount):
        if(self.get_energy() + amount <= self.get_max_energy()):
            self.set_energy(self.get_energy() + amount)
        else:
            self.set_energy(self.get_max_energy())

    def take_damage(self, damage):
        print(self.get_name() + " takes " + str(damage) + " damage!")
        self.set_hp(self.get_hp() - damage)
        print(self.get_name() + " has " + str(self.get_hp()) + " HP remaining!")
        if(self.get_hp() < 0):
            self.set_hp(0)
            self.set_ko(True)

    def normal_attack(self):
        if(self.gamestate.check_cost(self.get_allied(), self.get_na_cost())):
            self.gamestate.deal_damage(self, self.get_na_dmg(), self.gamestate.get_active_opponent())
            self.gamestate.gain_energy(self, 1)
            self.gamestate.reduce_gold(self.allied, self.na_cost)

    @abstractmethod
    def normal_attack_description(self):
        pass

    @abstractmethod
    def special_attack(self):
        pass

    @abstractmethod
    def special_attack_description(self):
        pass

    @abstractmethod
    def charged_attack(self):
        pass

    @abstractmethod
    def charged_attack_description(self):
        pass

    @abstractmethod
    def ability(self):
        pass

    @abstractmethod
    def ability_description(self):
        pass
    
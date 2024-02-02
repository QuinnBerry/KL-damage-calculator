from enum import Enum

class AttackType(Enum):
    Range = 1
    Mage = 2
    Melee = 3

class Element(Enum):
    Fire = 1
    Water = 2
    Lightning = 3
    Earth = 4
    Light = 5
    Dark = 6
    Ice = 7
    Wind = 8

class DamageSource():
    def __init__(self, name: str, base_damage: int, element: Element):
        self.name = name
        self.base_damage = base_damage
        self.element = element

    def get_name(self) -> str:
        return self.name
    
    def get_base_damage(self) -> int:
        return self.base_damage
    
    def get_element(self) -> Element:
        return self.element

class Weapon(DamageSource):
    def __init__(self, name: str, base_damage: int, element: Element, attack_type: AttackType):
        super().__init__(name, base_damage, element)
        self.attack_type = attack_type
    
    def get_attack_type(self) -> AttackType:
        return self.attack_type
    
    @classmethod
    def from_dict(cls, dict: dict):
        if ('name' not in dict):
            raise Exception("Invalid Weapon, missing 'name'")
        if ('base_damage' not in dict):
            raise Exception("Invalid Weapon, missing 'base_damage'")
        if ('element' not in dict):
            raise Exception("Invalid Weapon, missing 'element'")
        if ('damage_type' not in dict):
            raise Exception("Invalid Weapon, missing 'damage_type")
        return Weapon(dict['name'],
                      dict['base_damage'],
                      getattr(Element, dict['element']),
                      getattr(AttackType, dict['damage_type']))
        
    
class Ability(DamageSource):
    # TODO
    pass

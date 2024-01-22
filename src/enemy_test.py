import unittest
from enemy import Enemy

dragon_dict = {
        "name": "Dragon",
        "max_health": 500,
        "base_damage": 25,
        "damage_type": "melee",
        "weaknesses": ["water", "melee"]
    }

class TestEnemy(unittest.TestCase):
    def test_default_creation(self):
        enemy = Enemy()
        self.assertIsNotNone(enemy)

    def test_load_creation(self):
        enemy = Enemy()
        enemy.load(dragon_dict)
        self.assertEquals(enemy.name, dragon_dict['name'])
        self.assertEquals(enemy.max_health, dragon_dict['max_health'])
        self.assertEquals(enemy.current_health, dragon_dict['max_health'])
        self.assertEquals(enemy.base_damage, dragon_dict['base_damage'])
        self.assertEquals(enemy.damage_type, dragon_dict['damage_type'])
        self.assertEquals(enemy.weaknesses, dragon_dict['weaknesses'])


if __name__ == '__main__':
    unittest.main()
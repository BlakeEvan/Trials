from dataclasses import dataclass
from name_generator import generator


@dataclass
class Attributes:
    strength: int = 0
    dexterity: int = 0
    constitution: int = 0
    intelligence: int = 0
    wisdom: int = 0
    charisma: int = 0


races = {'dragonborn': Attributes(strength=2, charisma=1),
         'dwarf': Attributes(constitution=2),
         'elf': Attributes(dexterity=2),
         'gnome': Attributes(intelligence=2),
         'half-elf': Attributes(charisma=1, )
         }


@dataclass
class Character:
    attributes: Attributes
    race: str = ''
    name: str = generator()
    char_class: str = ''



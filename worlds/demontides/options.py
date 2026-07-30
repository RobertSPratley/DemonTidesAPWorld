from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class StartingAbilities(Choice):
    """
    The abilities you will start with, by default you start with none.
    If you would like to remove CheckPoints and the Item Arrow from the pool select no_progression.
    """

    display_name = "Starting Abilities"

    option_none = 0
    option_no_progression = 1
    option_all = 2


    # Choice options must define an explicit default value.
    default = option_none


@dataclass
class DemonTidesOptions(PerGameCommonOptions):
    starting_abilities : StartingAbilities




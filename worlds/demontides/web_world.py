from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets


class DemonTidesWebWorld(WebWorld):
    game = "DemonTides"

    theme = "partyTime"

    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Demon Tides for MultiWorld.",
        "English",
        "setup.md",
        "setup/en",
        ["RobertSPratley", "Maya", "Trev"],
    )

    tutorials = [setup]

    option_groups = option_groups
    options_presets = option_presets
from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld



class DemonTidesWebWorld(WebWorld):
    game = "DemonTides"

    theme = "partyTime"

    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Demon Tides for MultiWorld.",
        "English",
        "setup.md",
        "setup",
        ["RobertSPratley", "Maya", "Trev"],
    )

    tutorials = [setup]
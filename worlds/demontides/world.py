from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, rules, web_world
from . import options as demontides_options

class DemonTidesWorld(World):
    """
    Demon Tides is a 3D platformer collectathon. Race across open oceans and uncover a kingdom’s dark secrets.
    Expressively platform your way across dozens of locales, upgrading your gear and modifying your move-set every step
    of the way!
    """

    game = "DemonTides"

    web = web_world.DemonTidesWebWorld()

    options_dataclass = demontides_options.DemonTidesOptions
    options: demontides_options.DemonTidesOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Lokitana"


    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.DemonTidesItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:

        return self.options.as_dict(
            "starting_abilities"
        )
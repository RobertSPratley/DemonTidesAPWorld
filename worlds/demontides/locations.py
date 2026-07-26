from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import DemonTidesWorld

LOKITANA_NAME_TO_ID = {
    "Radio Towers FM Radio" : 1,
    "Radio Towers FM Rings" : 2,
    "Smuggler's Den Roof Chest" : 3,
    "Smuggler's Den Rings" : 4,
    "Smuggler's Den Chest Crane" : 5,
    "Lofty Highways Race" : 6,
    "Lofty Highways Gearserker" : 7,
    "Stacked Outpost Chest" : 8,
    "Stacked Outpost Mr. Mint" : 9,
    "Stacked Outpost Rings" : 10,
    "Sunken Neighborhood Chest" : 11,
    "Sunken Neighborhood Mr. Mint" : 12,
    "Sunken Neighborhood Gear Bits" : 13,
    "Industrial nest Chest" : 14,
    "Industrial nest Kappernian Baby" : 15,
    "Split Islands Chest" : 16,
    "Split Islands Key Chest" : 17,
    "Split Islands Goop Crystal" : 18,
    "Trading Outpost Rings" : 19,
    "Trading Outpost Chest" : 20,
    "Gearserker Junction Chest" : 21,
    "Gearserker Junction Gearserker" : 22,
    "Merchant's Fleet Lever Chest" : 23,
    "Merchant's Fleet Chest" : 24,
    "Runa's Village Lever Chest" : 25,
    "Runa's Village Kappa Baby" : 26,
    "Vindra's Mills Fix Windmill" : 27,
    "Vindra's Mills Key Chest" : 28,
    "Vindra's Mills Mr. Mint" : 29,
    "Stiltsville Ruins Rescue Kid" : 30,
    "Jester's Minery Minery Chest" : 31,
    "Jester's Minery Mr. Mint" : 32,
    "Jester's Minery Rings" : 33,
    "Jester's Juicery Juicery Chest" : 34,
    "Jester's Juicery Gearserker" : 35,
    "Jester's Leviathan Leviathan Chest" : 36,
    "Jester's Leviathan Gear Bits" : 37,
    "Dissolving Tower Chest" : 38,
    "Gravity Well Chest" : 39,
    "Baby Storage Kappa Baby" : 40,
    "Shipwreck Twins Combat" : 41,
    "Blessed Optica Chest" : 42,
    "Blessed Optica Mr. Mint" : 43,
    "Blessed Optica Key Chest" : 44,
    "Altar of Hands Chest" : 45,
    "Jester" : 125,
}

SHIVERBEAKS_NAME_TO_ID = {
    "Slippery Slope Rings" : 46,
    "Tridentarius Gearserkium Mr. Mint" : 47,
    "Tridentarius Gearserkium Gearserker" : 48,
    "Frosty Bait Chest" : 49,
    "Frosty Bait Rings" : 50,
    "Frosty Bait Gear Bits" : 51,
    "Snowstorm Station Mr. Mint" : 52,
    "Snowstorm Station Gear Bits" : 53,
    "Red Forest Chest" : 54,
    "Red Forest Drone" : 55,
    "Red Forest Kappa Baby" : 56,
    "Kappernian Springs Chest" : 57,
    "Kappernian Springs Save All Babies" : 58,
    "Arctic Eden Chest" : 59,
    "Arctic Eden Rings" : 60,
    "Abandoned Barrack Chest" : 61,
    "Optica Festival Chest" : 62,
    "Optica Festival Mr. Mint" : 63,
    "Frostown Ruins Chest" : 64,
    "Frostown Ruins Mr. Mint" : 65,
    "Frostown Ruins Gearserker" : 66,
    "Dunkelwald Creature Chest" : 67,
    "Dunkelwald Orange Chest" : 68,
    "Dunkelwald Mr. Mint" : 69,
    "Dunkelwald Rings" : 70,
    "Lonely Glacier Radio" : 71,
    "Lonely Glacier Drone" : 72,
    "Frost Burg Chest" : 73,
    "Frost Burg Rings" : 74,
    "Frost Burg Kappa Baby" : 75,
    "The Crooked Crow Chest" : 76,
    "Blazing Bonanza Rings" : 77,
    "Blazing Bonanza Kappa Baby" : 78,
    "Giant's Fire Chest" : 79,
    "Giant's Fire Drone Rings" : 80,
    "Logtown High Chest" : 81,
    "Logtown Well Chest" : 82,
    "Rotund Ice Rings" : 83,
    "Laser Marathon Laser Challenge" : 84,
    "Night Sight Chest" : 85,
    "Frozen Gears Gearserker" : 86,
    "Tridentarius" : 126,
}

THUINTIR_NAME_TO_ID = {
    "Aurum Mine Chest" : 87,
    "Aurum Mine Mr. Mint" : 88,
    "Aurum Mine Rat" : 89,
    "Fungal Depths Surface Chest" : 90,
    "Fungal Depths Altar Chest" : 91,
    "Fungal Depths Ghost" : 92,
    "Skull Sceal Chest" : 93,
    "Skull Sceal Combat" : 94,
    "Skull Sceal Gear Bits" : 95,
    "Uisge Whirlpool Chest" : 96,
    "Uisge Whirlpool Gear Bits" : 97,
    "Sgudal Ruins Rings" : 98,
    "Sgudal Ruins Mr. Mint" : 99,
    "Sgudal Ruins Kappa Baby" : 100,
    "Bhaile Ruins Peak Chest" : 101,
    "Bhaile Ruins Building Chest" : 102,
    "Bhaile Ruins Gearserker" : 103,
    "Subway Ascension Race" : 104,
    "Subway Ascension Chest" : 105,
    "Heavenly Aqueducts Mr. Mint" : 106,
    "Heavenly Aqueducts Gear Bits" : 107,
    "Shroomfall Chest" : 108,
    "Shroomfall Mr. Mint" : 109,
    "Shroomfall Rat" : 110,
    "Chronia Cyclone Chest" : 111,
    "Avian Gaol Free Lokians" : 112,
    "Avian Gaol Mr. Mint" : 113,
    "Avian Gaol Gearserker" : 114,
    "Flooded Manachainn Bells" : 115,
    "Flooded Manachainn Kappa Baby" : 116,
    "Slocfall Ghost" : 117,
    "Drained Urbs Gear Bits" : 118,
    "Drained Urbs Rat" : 119,
    "Tartar Village Combat" : 120,
    "Tartar Village Kappa Baby" : 121,
    "Golden Inneal Gearserker" : 122,
    "DK's Curse Chest" : 123,
    "Twisting Barrels Chest" : 124,
    "Roc" : 127,
}

RAGNAR_NAME_TO_ID = {
    "Ragnar" : 128
}

LOCATION_NAME_TO_ID = {
    **LOKITANA_NAME_TO_ID,
    **SHIVERBEAKS_NAME_TO_ID,
    **THUINTIR_NAME_TO_ID,
    **RAGNAR_NAME_TO_ID,
}



class DemonTidesLocation(Location):
    game = "Demon Tides"



def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: DemonTidesWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: DemonTidesWorld) -> None:
    Lokitana = world.get_region("Lokitana")
    Shiverbeaks = world.get_region("Shiverbeaks")
    Thuintir = world.get_region("Thuintir")
    Ragnars_Castle = world.get_region("Ragnar's Castle")

    Lokitana.add_locations(LOKITANA_NAME_TO_ID)
    Shiverbeaks.add_locations(SHIVERBEAKS_NAME_TO_ID)
    Thuintir.add_locations(THUINTIR_NAME_TO_ID)



def create_events(world: DemonTidesWorld) -> None:
    Lokitana = world.get_region("Lokitana")
    Shiverbeaks = world.get_region("Shiverbeaks")
    Thuintir = world.get_region("Thuintir")
    Ragnars_Castle = world.get_region("Ragnar's Castle")

    Ragnars_Castle.add_event(
        "Ragnar", "Victory", location_type=DemonTidesLocation, item_type=items.DemonTidesItem
    )
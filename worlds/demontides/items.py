from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import DemonTidesWorld

PROGRESSION_NAME_TO_ID = {
    "Bat Form": 1,
    "Boost": 2,
    "Snake Form": 5,
    "Spin Form": 6,
    "Golden Gear": 7
}

MISC_NAME_TO_ID = {
    "Talisman Slot": 8,
    "10 Eyetems": 9,
    "Item Arrow": 4,
    "Checkpoint": 3,
}

TALISMAN_NAME_TO_ID = {
    "Talisman Pendant" : 130,
    "Talisman Health Minus" : 131,
    "Talisman Health Plus" : 132,
    "Talisman Health Regen" : 133,
    "Talisman Guardian Fairy" : 134,
    "Talisman Paraglider" : 135,
    "Talisman White Bubble" : 136,
    "Talisman Blue Bubble" : 137,
    "Talisman Infernal Engine" : 138,
    "Talisman Icy Steps" : 139,
    "Talisman Flutter Steps" : 140,
    "Talisman Sticky Feet" : 141,
    "Talisman Sticky Fingers" : 142,
    "Talisman Item Arrow Tracker" : 143,
    "Talisman Eyetem Collector" : 144,
    "Talisman Time Out" : 145,
    "Talisman Flying Drone" : 146,
    "Talisman Airpoint" : 147,
    "Talisman Flash Photography" : 148,
    "Talisman Rollerskates" : 149,
    "Talisman \"Friendly\" Face": 207,
    "Talisman Big Head Mode" : 150,
    "Talisman Original Depth" : 151,
    "Talisman Pixel Art" : 152,
    "Talisman No Jump" : 153,
    "Talisman Timed Triple" : 154,
    "Talisman Triple Twist" : 155,
    "Talisman Relaxed Triple Jump" : 156,
    "Talisman Growing Triple Jump" : 157,
    "Talisman Crouch Jump" : 158,
    "Talisman Twirl Jump" : 159,
    "Talisman Lightweight Bouncer" : 160,
    "Talisman Light Feather" : 161,
    "Talisman Mega Dribble" : 162,
    "Talisman Ninja Skid" : 163,
    "Talisman Speedy Demon" : 164,
    "Talisman Ground Booster" : 165,
    "Talisman Wall Runner" : 166,
    "Talisman Boost Reflect" : 167,
    "Talisman Boost Punch" : 168,
    "Talisman Shoulder Tackle" : 169,
    "Talisman Boost Attack Lift" : 170,
    "Talisman Ricochet Beast" : 171,
    "Talisman Bat Flutter" : 172,
    "Talisman Bat Glide" : 173,
    "Talisman Bat Booster" : 174,
    "Talisman Bat Dasher" : 175,
    "Talisman Bat Dive Arrow" : 176,
    "Talisman Cannonbat" : 177,
    "Talisman Cannonball Leap" : 178,
    "Talisman Cannonball Momentum" : 179,
    "Talisman Super Bat Jump" : 180,
    "Talisman B-Ball" : 181,
    "Talisman Bat Optica" : 182,
    "Talisman Spin Updraft" : 183,
    "Talisman Longer Spin" : 184,
    "Talisman Spin Drill Leap" : 185,
    "Talisman Spin Drill Helicopter" : 186,
    "Talisman Spin Whirlwind" : 187,
    "Talisman Spincopter" : 188,
    "Talisman Spinning Spin" : 189,
    "Talisman Spin Optica" : 190,
    "Talisman Snake Boating" : 191,
    "Talisman Snake Drifting" : 192,
    "Talisman Snake Lob" : 193,
    "Talisman Snake Double Jump" : 194,
    "Talisman Snake Hop" : 195,
    "Talisman Snake Climber" : 196,
    "Talisman Snake Optica" : 197,
}

OUTFIT_NAME_TO_ID = {
    "Outfit Neon Splash Dress" : 198,
    "Outfit Tower Dress" : 199,
    "Outfit Swimsuit" : 200,
    "Outfit Bob Cut" : 201,
    "Outfit Buzz Cut" : 202,
    "Outfit Clown" : 203,
    "Outfit Chum Cosplay Body" : 204,
    "Outfit Angry Chum Body" : 205,
    "Outfit Chum Cosplay Head" : 206,
    "Outfit Angry Chum Head" : 10,
    "Outfit Neon Drip Body" : 11,
    "Outfit Sleeveless Drip" : 12,
    "Outfit Neon Drip Head" : 13,
    "Outfit Neon Dripless" : 14,
    "Outfit Privateer Body" : 15,
    "Outfit Bloody Privateer Body" : 16,
    "Outfit Privateer Head" : 17,
    "Outfit Bloody Privateer Head" : 18,
    "Outfit Witch's Garb" : 19,
    "Outfit Jester's Garb" : 20,
    "Outfit Witch's Hat" : 21,
    "Outfit Giant Witch's Hat" : 22,
    "Outfit Witch's Hair" : 23,
    "Outfit Beach Top" : 24,
    "Outfit Light Beach Wear" : 25,
    "Outfit Beach Cap" : 26,
    "Outfit Beach Cap Alpha" : 27,
    "Outfit Delinquent's Suit" : 28,
    "Outfit Jacketless Suit" : 29,
    "Outfit Delinquent's Do" : 30,
    "Outfit Maskless Cut" : 31,
    "Outfit Cereal Box Mask" : 32,
    "Outfit Paper Bag Mask" : 33,
    "Outfit Broken Mask" : 34,
    "Outfit Spooky Mask" : 35,
    "Outfit Punk Mask" : 36,
    "Outfit Wooden Mask" : 37,
    "Outfit Trashmask" : 38,
    "Outfit Angry Trashmask" : 39,
    "Outfit Creepy Trashmask" : 40,
    "Outfit Happy Trashmask" : 41,
    "Outfit Fish Demon Mask" : 42,
    "Outfit Demon Mask" : 43,
    "Outfit Negative Visor" : 44,
    "Outfit Rave Visor" : 45,
    "Outfit Visor" : 46,
    "Outfit Snail Helmet" : 47,
    "Outfit Space Helmet" : 48,
    "Outfit Golden Chum Skull" : 49,
    "Outfit Painted Chum Skull" : 50,
    "Outfit Chum Skull" : 51,
    "Outfit Toy Helmet" : 52,
    "Outfit Lamp Helmet" : 53,
    "Outfit Serker Body-Gear" : 54,
    "Outfit Noir Body-Gear" : 55,
    "Outfit Serker Head-Gear" : 56,
    "Outfit Noir Head-Gear" : 57,
    "Outfit Undemon Body" : 58,
    "Outfit Fallen Angel Body" : 59,
    "Outfit Undemon Head" : 60,
    "Outfit Fallen Angel Head" : 61,
    "Outfit Long Spiky Hair" : 62,
    "Outfit Scientista Body" : 63,
    "Outfit Suit and Tie" : 64,
    "Outfit Scientista Head" : 65,
    "Outfit Ponytail" : 66,
    "Outfit Kowai Kawaii Body" : 67,
    "Outfit Kowai Kei Body" : 68,
    "Outfit Kowai Kawaii Head" : 69,
    "Outfit Kowai Kei Head" : 70,
    "Outfit Frosty Explorer Body" : 71,
    "Outfit Frosty Sweater" : 72,
    "Outfit Frosty Explorer Head" : 73,
    "Outfit Bear Ears" : 74,
    "Outfit Rainy Getup Body" : 75,
    "Outfit Red Getup" : 76,
    "Outfit Rainy Getup Head" : 77,
    "Outfit Runa's Jacket" : 78,
    "Outfit Wet Hair" : 79,
    "Outfit Escaped Barbarian Body" : 80,
    "Outfit Bald Barbarian" : 81,
    "Outfit Escaped Barbarian Head" : 82,
    "Outfit Weightless Barbarian" : 83,
    "Outfit Gamer Shirt" : 84,
    "Outfit Aggro Crab Shirt" : 85,
    "Outfit Demon Turf Shirt" : 86,
    "Outfit Billie Bust Up Shirt" : 87,
    "Outfit Crosscode Shirt" : 88,
    "Outfit GearGrit Shirt" : 89,
    "Outfit Grapple Dog Shirt" : 90,
    "Outfit Skellboy Shirt" : 91,
    "Outfit Slime-san Shirt" : 92,
    "Outfit Tako Shirt" : 93,
    "Outfit Unbeatable Shirt" : 94,
    "Outfit Gamer Headband" : 95,
    "Outfit Aggro Crab Headband" : 96,
    "Outfit Demon Turf Headband" : 97,
    "Outfit Billie Bust Up Headband" : 98,
    "Outfit Crosscode Headband" : 99,
    "Outfit GearGrit Headband" : 100,
    "Outfit Grapple Dog Headband" : 101,
    "Outfit Skellboy Headband" : 102,
    "Outfit Slime-san Headband" : 103,
    "Outfit Tako Headband" : 104,
    "Outfit Unbeatable Headband" : 105,
    "Outfit Baby Kappernian Suit Body" : 106,
    "Outfit Shiverbeaks Kappernian" : 107,
    "Outfit Thuintir Kappernian Body" : 108,
    "Outfit Baby Kappernian Suit Head" : 109,
    "Outfit Baby Kappernian Suit Head Variant 1" : 110,
    "Outfit Thuintir Kappernian Head" : 111,
    "Outfit Beakless" : 112,
    "Outfit Raven Wrestler" : 113,
    "Outfit Neon Wrestler" : 114,
    "Outfit Raven Tips" : 115,
    "Outfit Neon Tips" : 116,
    "Outfit Vindra's Gale Body" : 117,
    "Outfit Flame Goddess" : 118,
    "Outfit Vindra's Gale Head" : 119,
    "Outfit Fiery Haircut" : 120,
    "Outfit Royal Guard Body" : 121,
    "Outfit Capeless Armor" : 122,
    "Outfit Royal Guard Head" : 123,
    "Outfit Helmetless Cut" : 124,
    "Outfit Luci's Glasses" : 125,
    "Outfit Luci's Glasses Down" : 126,
    "Outfit Midgi's Barrel" : 127,
    "Outfit DK's Magic Face" : 128,
    "Outfit DK's Magic Body" : 129,
}

ITEM_NAME_TO_ID = {
    **PROGRESSION_NAME_TO_ID,
    **MISC_NAME_TO_ID,
    **TALISMAN_NAME_TO_ID,
    **OUTFIT_NAME_TO_ID
}

# Items should have a defined default classification.
# In our case, we will make a dictionary from item name to classification.
DEFAULT_ITEM_CLASSIFICATIONS = {
    **{name: ItemClassification.progression for name in PROGRESSION_NAME_TO_ID},
    **{name: ItemClassification.useful for name in TALISMAN_NAME_TO_ID},
    **{name: ItemClassification.filler for name in OUTFIT_NAME_TO_ID},
    "Talisman Slot": ItemClassification.useful,
    "10 Eyetems": ItemClassification.filler,
    "Item Arrow": ItemClassification.useful,
    "Checkpoint": ItemClassification.useful,
}


class DemonTidesItem(Item):
    game = "Demon Tides"



def get_random_filler_item_name(world: DemonTidesWorld) -> str:
    return "10 Eyetems"


def create_item_with_correct_classification(world: DemonTidesWorld, name: str) -> DemonTidesItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    return DemonTidesItem(name, classification, ITEM_NAME_TO_ID[name], world.player)



def create_all_items(world: DemonTidesWorld) -> None:


    itempool = []

    match world.options.starting_abilities.value:
        case world.options.starting_abilities.option_all:
            for name in PROGRESSION_NAME_TO_ID:
                starting_item = world.create_item(name)
                world.push_precollected(starting_item)
            starting_item = world.create_item("Item Arrow")
            world.push_precollected(starting_item)
            starting_item = world.create_item("Checkpoint")
            world.push_precollected(starting_item)

        case world.options.starting_abilities.option_no_progression:
            itempool += [world.create_item(name) for name in PROGRESSION_NAME_TO_ID]

            starting_item = world.create_item("Item Arrow")
            world.push_precollected(starting_item)
            starting_item = world.create_item("Checkpoint")
            world.push_precollected(starting_item)

        case world.options.starting_abilities.option_none:
            itempool += [world.create_item(name) for name in PROGRESSION_NAME_TO_ID]
            itempool += [world.create_item("Item Arrow"), world.create_item("Checkpoint")]


    itempool += [world.create_item(name) for name in TALISMAN_NAME_TO_ID]
    itempool += [world.create_item("Talisman Slot") for _ in range(3)]
    itempool += [world.create_item("Golden Gear") for _ in range(45)]

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

    for name in OUTFIT_NAME_TO_ID:
        starting_outfit_item = world.create_item(name)
        world.push_precollected(starting_outfit_item)


from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import DemonTidesWorld

def create_and_connect_regions(world: DemonTidesWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: DemonTidesWorld) -> None:
    Lokitana = Region("Lokitana", world.player, world.multiworld)
    Shiverbeaks = Region("Shiverbeaks", world.player, world.multiworld)
    Thuintir = Region("Thuintir", world.player, world.multiworld)
    Ragnars_Castle = Region("Ragnar's Castle", world.player, world.multiworld)

    regions = [Lokitana, Shiverbeaks, Thuintir, Ragnars_Castle]

    world.multiworld.regions += regions


def connect_regions(world: DemonTidesWorld) -> None:
    Lokitana = world.get_region("Lokitana")
    Shiverbeaks = world.get_region("Shiverbeaks")
    Thuintir = world.get_region("Thuintir")
    Ragnars_Castle = world.get_region("Ragnar's Castle")

    Lokitana.connect(Shiverbeaks, "Shiverbeaks Cannon")
    Lokitana.connect(Thuintir, "Thunitir Cannon")
    Lokitana.connect(Ragnars_Castle, "Ragnar's Castle Cannon")


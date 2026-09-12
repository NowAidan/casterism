from data.world.item import Item

def create_items() -> dict[str, Item]:
    return {
        "spacesuit": Item(
            take_message_id="take_spacesuit",
            command_aliases=["put", "wear", "equip"],
            aliases=["space suit", "suit"]
        ),
        "screwdriver": Item(
            take_message_id="take_screwdriver"
        ),
        "web": Item( # space rover equiv to a black box
            take_message_id="take_web",
            command_aliases=["recover", "unscrew"]
        ),
        "transmission_data": Item(
            take_message_id="take_transmission_data",
            command_aliases=["recover", "restore"]
        )
    }
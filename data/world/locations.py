from data.world.location import Location
from data.world.interactable import Interactable
from data.world.item import Item
from data.world.items import create_items

items: dict[str, Item] = create_items()

def create_locations() -> tuple[Location, dict[str, Location]]:
    # the parameter being assigned to is referenced for readability purposes
    shelter: Location = Location(
        location_id="shelter",
        message_id="location_shelter",
        interactables={
            "whiteboard": Interactable(
                message_id="look_whiteboard",
            ),
            "spacesuit": Interactable(
                message_id="look_spacesuit",
                items={"spacesuit": items["spacesuit"]},
                items_taken_message_id="look_spacesuit_taken",
                aliases=["AX-5", "space suit", "AX-5 spacesuit", "AX-5 space suit", "AX5 spacesuit", "AX5 space suit", "AX 5 spacesuit", "AX 5 space suit", "suit"]
            ),
            "door": Interactable(
                message_id="look_shelter_door",
                is_locked=True,
                required_item=items.get("spacesuit"),
                locked_message_id="locked_shelter_door",
                unlocked_message_id="unlocked_shelter_door",
                aliases=["exit", "outside", "handle"],
                location_id="landing"
            )
        },
    )
    
    landing: Location = Location(
        location_id="landing",
        message_id="location_landing",
        interactables={
            "shelter": Interactable(
                message_id="look_shelter",
            ),
            "research station": Interactable(
                message_id="look_research_station",
                location_id="research_station",
                is_locked=True,
                required_item=items.get("web"),
                locked_message_id="locked_research_station",
                unlocked_initial_message_id="initial_unlocked_research_station",
                aliases=["station", "research"]
            ),
            "lander": Interactable(
                message_id="look_lander",
                items={"screwdriver": items["screwdriver"]},
                items_taken_message_id="look_lander_items_taken",
            ),
        }
    )
    
    research_station: Location = Location(
        location_id="research_station",
        message_id="location_research_station",
        interactables={
            "computer": Interactable(
                message_id="look_computer",
                is_locked=True,
                required_item=items.get("web"),
                locked_message_id="locked_computer",
                unlocked_initial_message_id="ending_reveal",
                unlocked_message_id="unlocked_compuer",
                items={"transmission data": items["transmission_data"]},
                aliases=["web", "warm electronics box"],
            ),
            "door": Interactable(
                message_id="look_research_station_door",
                is_locked=True,
                required_item=items.get("transmission_data"),
                locked_message_id="locked_research_station_door",
                unlocked_message_id="unlocked_research_station_door",
                aliases=["exit", "outside", "handle"],
                location_id="landing"
            )
        }
    )

    vertebral_nexus: Location = Location(
        location_id="arch",
        message_id="location_arch",
        interactables={
            "satellite dish": Interactable(
                message_id="look_satellite_dish",
            ),
            "true data": Interactable(
                message_id="look_satellite_dish",
                locked_message_id="locked_satellite_data",
                is_locked=True,
                required_item=items.get("transmission_data"),
                location_id="ending_good",
                aliases=["transmission data", "data", "transmission"]
            ),
            "falsified data": Interactable(
                message_id="look_satellite_dish",
                locked_message_id="locked_satellite_data",
                is_locked=True,
                required_item=items.get("transmission_data"),
                location_id="ending_bad",
            )
        }
    )
    
    rib_orchid: Location = Location(
        location_id="rib_orchid",
        message_id="location_rib_orchid",
        interactables={
            "rover": Interactable(
                message_id="look_rover",
                is_locked=True,
                is_items_locked=True,
                locked_message_id="locked_rover",
                unlocked_message_id="unlocked_rover",
                unlocked_initial_message_id="initial_unlocked_research_station",
                items_taken_message_id="look_rover_items_taken",
                required_item=items["screwdriver"],
                items={"web": items["web"]},
                aliases=["panel", "rover panel", "panel rover", "web", "warm electronics box"]
            )
        }
    )
    
    ending_good: Location = Location(
        location_id="ending_good",
        message_id="ending_good"
    )
    
    ending_bad: Location = Location(
        location_id="ending_bad",
        message_id="ending_bad"
    )
    
    shelter.add_connection("Door", landing)

    landing.add_connection("North", vertebral_nexus)
    vertebral_nexus.add_connection("South", landing)

    vertebral_nexus.add_connection("West", rib_orchid)
    rib_orchid.add_connection("East", vertebral_nexus)

    INITIAL_LOCATION: Location = shelter
    REGISTERED_LOCATIONS: list[Location] = [shelter, research_station, landing, vertebral_nexus, rib_orchid, ending_good, ending_bad]

    locations: dict[str, Location] = {}
    
    # runs through all registered locations and assigns them to a dict by their id
    for location in REGISTERED_LOCATIONS:
        locations[location.location_id] = location
    
    return INITIAL_LOCATION, locations

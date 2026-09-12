from data.world.location import Location
from data.world.locations import create_locations
from data.world.item import Item

class Player():
    def __init__(self) -> None:
        self.current_location, self.locations = create_locations()
        self.inventory: list[Item] = []
    
    # returns True if the player successfully moves, otherwise returns False
    def move(self, direction: str) -> bool:
        direction = direction.capitalize()
        
        if direction in self.current_location.connections:
            self.current_location = self.current_location.connections[direction]
            
            return True
        
        return False

    # returns True if the player successfully teleports, otherwise returns False
    def teleport(self, location_id: str) -> bool:
        destination: Location | None = self.locations.get(location_id)
        
        if destination:
            self.current_location = destination
            
            return True
    
        return False
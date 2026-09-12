import pygame

from data.world.interactable import Interactable
from data.world.item import Item

class Location():
    def __init__(self, location_id: str, message_id: str, interactables: dict[str, Interactable] | None = None) -> None:
        self.location_id: str = location_id
        self.message_id: str = message_id
        self.interactables: dict[str, Interactable] | None = interactables
        self.connections: dict[str, Location] = {}
    
    # cannot type-define connections as it references this class
    def add_connection(self, direction: str, connection) -> None:
        self.connections[direction] = connection
    
    def find_item(self, name: str) -> Item | None:
        if not self.interactables:
            return
        
        for interactable in self.interactables.values():
            item: Item | None = interactable.items.get(name)
            
            if item:
                return item
            
            for item in interactable.items.values():
                if name in item.aliases:
                    print(item.take_message_id)
                    return item
        
        return None
    
    def take_item(self, name: str) -> Item | None:
        if not self.interactables:
            return
        
        # values() returns a list of all the dictionary values (all the items) in the interactables
        for interactable in self.interactables.values():
            if interactable.is_locked:
                continue
            
            item: Item | None = interactable.take_item(name)
            
            if item:
                return item
        
        print("not found")
        return None
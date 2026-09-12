from data.world.item import Item

class Interactable():
    def __init__(self, message_id: str, is_locked: bool = False, is_items_locked: bool = False, required_item: Item | None = None, locked_message_id: str | None = None, unlocked_message_id: str | None = None, unlocked_initial_message_id: str | None = None, location_id: str | None = None, items: dict[str, Item] | None = None, items_taken_message_id: str | None = None, aliases: list[str] | None = None) -> None:
        self.message_id: str = message_id # message shown on look
        
        self.is_locked: bool = is_locked
        self.is_items_locked: bool = is_items_locked
        
        self.required_item: Item | None = required_item
        
        self.locked_message_id: str | None = locked_message_id
        self.unlocked_message_id: str | None = unlocked_message_id
        self.unlocked_initial_message_id: str | None = unlocked_initial_message_id
        self.items_taken_message_id: str | None = items_taken_message_id # shown once all items are taken
        
        self.location_id: str | None = location_id # if the Interactable acts as a teleporter this is the location_id of the location to teleport to
        
        self.items: dict[str, Item] = items or {} # creates empty dict if no items are provided, avoids some possible errors
        
        self.aliases: list[str] = aliases or []
    
    def unlock(self, inventory: list[Item]) -> str:
        if not self.is_locked:
            # or will return the first value if it exists and if not will fallback on the second value
            return self.unlocked_message_id or self.message_id

        # check if the player has the required item to unlock in their inventory
        if self.required_item and self.required_item in inventory:
            self.is_locked = False
            
            # only shown once when the Interactable is initally unlocked
            if self.unlocked_initial_message_id:
                return self.unlocked_initial_message_id
            
            # fallback on message_id if there isn't an unlocked_message_id
            return self.unlocked_message_id or self.message_id

        # the player does not have the required item to unlock, so show the locked message
        return self.locked_message_id or self.message_id

    def take_item(self, name: str) -> Item | None:
        item: Item | None = self.items.get(name)

        if not item:
            for item_id, stored_item in self.items.items(): # items() returns a key value pair
                if name in stored_item.aliases:
                    item = self.items.pop(item_id)
                    
                    break
        
        # if item exists, no items are left in interactable "inventory", and there's a message id for when items are taken, swap the message id to it
        if item and not self.items and self.items_taken_message_id:
            self.message_id = self.items_taken_message_id
        
        return item
class Item():
    def __init__(self, take_message_id: str = "take_generic", command_aliases: list[str] | None = None, aliases: list[str] | None = None) -> None:
        self.take_message_id: str = take_message_id
        self.command_aliases: list[str] = command_aliases or [] # aliases that can be used as a command to pick up the object
        self.aliases: list[str] = aliases or [] # aliases for the name of the input
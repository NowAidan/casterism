from data.core.engine import Engine

# run from here to ensure all system paths are correct

# name is only set to "__main__" if the script is run directly
if __name__ == "__main__":
    engine: Engine = Engine()
    engine.engine_update()
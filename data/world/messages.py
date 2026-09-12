import pygame

from data.world.message import TextSegment
from data.core.settings import DEFAULT_LINE_SPEED

ACCENT_FONT_COLOUR: pygame.Color = pygame.Color(247, 163, 52)
SECONDARY_ACCENT_FONT_COLOUR: pygame.Color = pygame.Color(59, 131, 247)

DRAMATIC_SPEED: int = 3

def create_messages() -> dict[str, list]:
    return {
        "command_list":
            [
                TextSegment("Commands", colour=ACCENT_FONT_COLOUR),
                TextSegment("look ", colour=ACCENT_FONT_COLOUR, new_line=True),
                TextSegment("at [thing you're looking at]"),
                TextSegment("go ", colour=ACCENT_FONT_COLOUR, new_line=True),
                TextSegment("to [thing you want to go to]"),
                TextSegment("take ", colour=ACCENT_FONT_COLOUR, new_line=True),
                TextSegment("the [thing you want to take]"),
                TextSegment("unlock ", colour=ACCENT_FONT_COLOUR, new_line=True),
                TextSegment("[thing you want to unlock]")
            ],
    
        "location_shelter":
            [
                # TextSegment("The year is 5950. You have been alone for 3962 years.", speed=5),
                TextSegment("For 3962 years you have been one with the void."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Everything aches as your eyes groan open.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Spaghetti streams across the ceiling.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Sharp agony strikes your judgement.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("You cannot muster a thought yet the questions linger.", new_line=True),
                TextSegment("         ", new_line=True, speed=DEFAULT_LINE_SPEED),
                TextSegment("You respite in a shallow dome.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("It is only furnished by a", new_line=True),
                TextSegment(" whiteboard", colour=ACCENT_FONT_COLOUR),
                TextSegment(", "),
                TextSegment("a large metallic"),
                TextSegment(" door", colour=ACCENT_FONT_COLOUR),
                TextSegment(", and what looks to "),
                TextSegment("be a modified AX-5", new_line=True),
                TextSegment(" spacesuit", colour=ACCENT_FONT_COLOUR),
                TextSegment(". Your sarcophagus is the center of the room."),
                TextSegment("         ", new_line=True, speed=DEFAULT_LINE_SPEED),
                TextSegment("You garner the strength to rise and your eyes begin to dart around the room.", new_line=True)
            ],
        "location_landing":
            [
                TextSegment("You step into the landing.", colour=SECONDARY_ACCENT_FONT_COLOUR),
                TextSegment("         ", new_line=True, speed=DEFAULT_LINE_SPEED),
                TextSegment("Deep craters consume the tissue of the star.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The domes of the", new_line=True),
                TextSegment(" shelter ", colour=ACCENT_FONT_COLOUR),
                TextSegment("and"),
                TextSegment(" research station ", colour=ACCENT_FONT_COLOUR),
                TextSegment("evoke a feeling of uncanniness."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                # TextSegment("Yet you feel comfort. You are cocooned with the shroud of silence.", new_line=True),
                # TextSegment("         ", speed=4),
                TextSegment("A", new_line=True),
                TextSegment(" lander ", colour=ACCENT_FONT_COLOUR),
                TextSegment("can be seen not too far off into the haze."),
                TextSegment("         ", new_line=True, speed=DEFAULT_LINE_SPEED),
                TextSegment("Shallow rover tracks can be seen drifting towards the", new_line=True),
                TextSegment(" north", colour=ACCENT_FONT_COLOUR),
                TextSegment(".")
                # TextSegment("This is your", new_line=True),
                # TextSegment(" only ", speed=7, colour=pygame.Color("red")),
                # TextSegment("tether to the earth."),
            ],
        "location_research_station":
            [
                TextSegment("Machinery conceals the insulated walls, a chill runs through your body.", colour=SECONDARY_ACCENT_FONT_COLOUR),
                TextSegment("         ", new_line=True, speed=DEFAULT_LINE_SPEED),
                TextSegment("The room is no larger than your shelter.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Even packed with mechanisms, the room still feels empty.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Half the machines look ripped straight from two decades ago.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("A large rudimentary", new_line=True),
                TextSegment(" computer ", colour=ACCENT_FONT_COLOUR),
                TextSegment("stands out, it is the only thing not vieled by"),
                TextSegment("the dust.", new_line=True)
            ],
        "location_arch":
            [
                TextSegment("You take a few steps forward then freeze.", colour=SECONDARY_ACCENT_FONT_COLOUR),
                TextSegment("         ", new_line=True, speed=DEFAULT_LINE_SPEED),
                TextSegment("A colossal arch towers over the landscape, blocking out the faint light", new_line=True),
                TextSegment("from the void above. You can only make out a fraction of the fossil before", new_line=True),
                TextSegment("it is enveloped by the atmosphere.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Balancing on top of the arch is a", new_line=True),
                TextSegment(" satellite dish", colour=ACCENT_FONT_COLOUR),
                TextSegment("."),
                TextSegment("         ", new_line=True, speed=DEFAULT_LINE_SPEED),
                TextSegment("Rover tracks have been etched into the surface, continuing", new_line=True),
                TextSegment(" west ", colour=ACCENT_FONT_COLOUR),
                TextSegment("from the"),
                TextSegment(" south", colour=ACCENT_FONT_COLOUR),
                TextSegment(".")
            ],
        "location_rib_orchid":
            [
                TextSegment("You trek forward a few steps, entering into a valley of remains.", colour=SECONDARY_ACCENT_FONT_COLOUR),
                TextSegment("         ", new_line=True, speed=DEFAULT_LINE_SPEED),
                TextSegment("Serrated bones carved to ribs blossom like daises in a field, their stature", new_line=True),
                TextSegment("grasps at the lights above.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("You can only look on in admiration.", new_line=True),
                TextSegment("         ", new_line=True, speed=DEFAULT_LINE_SPEED),
                TextSegment("The tracks continue, streaming from the", new_line=True),
                TextSegment(" east", colour=ACCENT_FONT_COLOUR),
                TextSegment(", becoming sparser and eventually"),
                TextSegment("trailing to the mutilated carcass of a", new_line=True),
                TextSegment(" rover", colour=ACCENT_FONT_COLOUR),
                TextSegment(".")
            ],
        
        "look_whiteboard":
            [
                TextSegment("Trapped against the curving wall, the whiteboard reads:"),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Mission ID:", new_line=True),
                TextSegment(" CA1988/O-27"),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Mission Objective: ", new_line=True),
                TextSegment("Observe and record the presence of cosmic anomolies"),
                TextSegment("located on star Eta Tauri and analyse the ossification of the surface.", new_line=True),
            ],
        "look_spacesuit":
            [
                TextSegment("Featuring a rigid aluminum shell and a casing of enamel, the AX-5 hard-shell"),
                TextSegment("spacesuit characterised itself by its flexible and curved nature.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("It was the most advanced spacesuit at the time of your departure.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("You will need to", new_line=True),
                TextSegment(" wear ", colour=ACCENT_FONT_COLOUR),
                TextSegment("this before exiting the dome.")
            ],
        "look_shelter_door":
            [
                TextSegment("The door dominantes the room."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("A large steel valve handle extrudes from the center.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("It is cold upon touch.", new_line=True),
            ],
        "look_research_station":
            [
                TextSegment("The research station is oddly rectangular, departing from the usual curved"),
                TextSegment("architecture.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("It is tethered to two towering silos housing your oxygen.", new_line=True),
            ],
        "look_research_station_door":
            [
                TextSegment("The door is oddly door shaped."),
            ],
        "look_lander":
            [
                TextSegment("The lander lonely dozes in the field of bone."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Shattered glass is spread across the aluminium floor.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The walls are", new_line=True),
                TextSegment(" smeared ", speed=7, colour=pygame.Color("lightcoral")),
                TextSegment("with the esscense of life."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("A", new_line=True),
                TextSegment(" screwdriver ", colour=ACCENT_FONT_COLOUR),
                TextSegment("is buried underneath some of the rubble.")
            ],
        "look_shelter":
            [
                TextSegment("A small dome bulges from the star."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Veins of copper flow throughout the strucutre.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Barrenness hollows the within.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("It is a lonely tomb.", new_line=True)
            ],
        "look_rover":
            [
                TextSegment("The rover has been completely mangled."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Impaled by a fragment of splintered bone.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Unscrewing", colour=ACCENT_FONT_COLOUR, new_line=True),
                TextSegment(" the Warm Electronics Box ("),
                TextSegment("WEB", colour=ACCENT_FONT_COLOUR),
                TextSegment(") would be beneficial for study."),
            ],
        "look_computer":
            [
                TextSegment("The computer is a large logical box with a CRT stacked on top."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The only method of input is a stiff keyboard.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("To analyse the data from the web you need to", new_line=True),
                TextSegment(" mount ", colour=ACCENT_FONT_COLOUR),
                TextSegment("the"),
                TextSegment(" WEB", colour=ACCENT_FONT_COLOUR),
                TextSegment(".")
            ],
        "look_satellite_dish":
            [
                TextSegment("The satellite dish is a marvel of a sight."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Through this satellite dish you have the power to", new_line=True),
                TextSegment(" transmit true data", colour=ACCENT_FONT_COLOUR),
                TextSegment("."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Or alternatively you could", new_line=True),
                TextSegment(" transmit falsified data", colour=ACCENT_FONT_COLOUR),
                TextSegment("."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The power lies in your hands.", new_line=True)
            ],
            
        "look_lander_items_taken":
            [
                TextSegment("The lander lonely dozes in the field of bone."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Shattered glass is spread across the aluminium floor.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The walls are", new_line=True),
                TextSegment(" smeared ", colour=pygame.Color("lightcoral")),
                TextSegment("with the pure esscense of life."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("You have no recollection of the events that took place here.", new_line=True)
            ],
        "look_spacesuit_taken":
            [
                TextSegment("You think to yourself, what am I more than a corpse in distant space?"),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("This suit my coffin, and this star my grave.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Before your mind can stray any further, the discomfort of the feeding", new_line=True),
                TextSegment("tube rubbing against your cheek pulls you out from your thoughts.", new_line=True)
            ],
        "look_rover_items_taken":
            [
                TextSegment("After your extraction job the rover is unidentifiable."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The shaft of your screwdriver penetrates the upper body.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Your screwdriver did not survive the ordeal.", new_line=True)
            ],
        
        "locked_shelter_door":
            [
                TextSegment("You reach to unbolt the door before an urge flows through your body."),
                TextSegment("         ", new_line=True, speed=DEFAULT_LINE_SPEED),
                TextSegment("The atmosphere would eviscerate you in miliseconds, to even step out", new_line=True),
                TextSegment("you would need a", new_line=True),
                TextSegment(" spacesuit", colour=ACCENT_FONT_COLOUR),
                TextSegment(".")
            ],
        "locked_research_station":
            [
                TextSegment("Only a limited amount of oxygen circulates within the research station."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("It would be best not to enter unless you had something to study.", new_line=True)
            ],
        "locked_research_station_door":
            [
                TextSegment("You should"),
                TextSegment(" get ", colour=ACCENT_FONT_COLOUR),
                TextSegment("the"),
                TextSegment(" transmission data ", colour=ACCENT_FONT_COLOUR),
                TextSegment("from the computer first.")
            ],
        "locked_rover":
            [
                TextSegment("The panel containing the WEB is screwed shut."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("You remember seeing a glisten of a tool back at the landing.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("It was located near the lander.", new_line=True),
            ],
        "locked_transmission_data":
            [
                TextSegment("You do not have any transmission data...")
            ],
        "locked_computer":
            [
                TextSegment("To analyse the data from recoverd from the rover you need to"),
                TextSegment(" mount ", colour=ACCENT_FONT_COLOUR),
                TextSegment("the"),
                TextSegment(" WEB", colour=ACCENT_FONT_COLOUR),
                TextSegment(".")
            ],
        "locked_satellite_data": 
            [
                TextSegment("To transmit anything using the satellite you need data to transmit..."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Currently, you do not have any transmission data.", new_line=True)
            ],
        
        "unlocked_shelter_door":
            [
                TextSegment("The door unlocks."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The swift breeze of the star blows under.", new_line=True),
            ],
        "unlocked_research_station_door":
            [
                TextSegment("The door is now unlocked."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("A smell of curiosity reeks from within.", new_line=True),
            ],
        "unlocked_rover":
            [
                TextSegment("The rover has been completely mangled."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Impaled by a fragment of splintered bone.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The", new_line=True),
                TextSegment(" WEB ", colour=ACCENT_FONT_COLOUR),
                TextSegment("is left loosely exposed."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The metal panel bent backwards beyond its limits.", new_line=True)
            ],
        "unlocked_computer":
            [
                TextSegment("You can take the transmission.")
            ],
        
        "initial_unlocked_research_station":
            [
                TextSegment("You open the airlock chamber to the research station."),
                TextSegment("         ", new_line=True, speed=DEFAULT_LINE_SPEED),
                TextSegment("You can now", new_line=True),
                TextSegment(" step ", colour=ACCENT_FONT_COLOUR),
                TextSegment("into the research station.")
            ],
        "initial_unlocked_research_station":
            [
                TextSegment("You plunge the screwdriver under the panel and pull up.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The burnt panel bends backwards as you wedge the screwdriver in further.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The hinges of the panel finally give way, exposing the", new_line=True),
                TextSegment(" WEB", colour=ACCENT_FONT_COLOUR),
                TextSegment("."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("You should", new_line=True),
                TextSegment(" take ", colour=ACCENT_FONT_COLOUR),
                TextSegment("the"),
                TextSegment(" WEB ", colour=ACCENT_FONT_COLOUR),
                TextSegment("back to the research station to study it.")
            ],
        
        "take_generic":
            [
                TextSegment("You take the item.")
            ],
        "take_spacesuit":
            [
                TextSegment("You step into the hefty metallic body."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Each muscle begging for mercy as you hoist the upper suit upon yourself.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Finally you fully encase yourself with the helmet, significantly dampening", new_line=True),
                TextSegment("your vision and once again allowing the nothingness to steal a part of you.", new_line=True)
            ],
        "take_screwdriver":
            [
                TextSegment("You retrieve the screwdriver from within the earth."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Deep red ", colour=pygame.Color("firebrick"), new_line=True),
                TextSegment("ichor streams down the handle of the screwdriver."),
                TextSegment("         ", speed=4),
                TextSegment("You flinch at the sight.", new_line=True)
            ],
        "take_web":
            [
                TextSegment("You lift the Warm Electronics Box out of the rover."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("It isn't too heavy but you struggle to hold it comfortably.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The bulkiness of your spacesuit only complicates the effort.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("You should return to the landing to analyse the recoverable data.", new_line=True)
            ],
        "take_transmission_data":
            [
                TextSegment("You take the transmission data.")
            ],
        
        "ending_reveal":
            [
                TextSegment("Recovered Crew Transmission Transcript - 4/9/5946", speed=DRAMATIC_SPEED),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED, new_line=True),
                TextSegment("Do not come for us, I repeat, do not come for us.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The surface is some sort of an intelligent species.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("It can manipulate time to its will. Cause and effect are meaningless.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("We were lured here by a message we had not yet sent.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("It's already got my crew and I'm slowly losing oxygen.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("If anything I hope it takes me whilst I'm still me.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED, new_line=True),
                TextSegment("No further transmissions could be recovered...", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The computer spits out the", new_line=True),
                TextSegment(" transmission data", colour=ACCENT_FONT_COLOUR),
                TextSegment(". You can"),
                TextSegment(" take ", colour=ACCENT_FONT_COLOUR),
                TextSegment("this to the"),
                TextSegment("satellite dish", colour=ACCENT_FONT_COLOUR, new_line=True),
                TextSegment(". You should"),
                TextSegment(" go outside ", colour=ACCENT_FONT_COLOUR),
                TextSegment("before the oxygen depletes.")
            ],
        "ending_good":
            [
                TextSegment("You send the recovered data off across the cosmos."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("You have no idea if the warning ever reached anyone.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Years pass, the star slowly draining your capacity to live.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("By your eighth year your oxygen supply has significantly dwindled.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The star has consumed all of the other structures except for the shelter.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("You are aware that you don't have much time left.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("One day it will come for you but until then you feel at peace.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED, new_line=True),
                TextSegment("Thank you for playing. You can exit the game with the 'ESC' key.", new_line=True, colour=SECONDARY_ACCENT_FONT_COLOUR),
            ],
        "ending_bad":
            [
                TextSegment("You falsify the transmission. Your words of fraudulence barrel towards Earth."),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("You watch the signal alongside your sense of self dissapear into the void.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Your lie slowly floats through space.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("The entity seems to sense your guilt.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("It punishes you, disconnecting one of your oxygen tanks.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("You are subjected to constant visions of future expenditions.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("Spaceships from a mush of time periods.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("One night your paranoia swallows you whole.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED),
                TextSegment("All whilst the star burns on.", new_line=True),
                TextSegment("         ", speed=DEFAULT_LINE_SPEED, new_line=True),
                TextSegment("Thank you for playing. You can exit the game with the 'ESC' key.", new_line=True, colour=SECONDARY_ACCENT_FONT_COLOUR),
            ],
    }

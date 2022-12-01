import numpy as np

# relevant list of job data
job = [
    "Torchbearer",
    "Labourer",
    "Tunnel Digger",
    "Armourer / Blacksmith",
    "Local Guide",
    "Mouse-at-arms",
    "Scholar",
    "Knight",
    "Interpreter",
]

# which die determines amount of mice found in that profession
Number = [6, 6, 4, 2, 4, 6, 2, 3, 2]

# daily wage of that profession
Wage = [1, 2, 5, 8, 10, 10, 20, 25, 30]

# lists of appearances, dispositions, etc.
Birthsign = [
    "Star: Brave / reckless",
    "Wheel: Industrious / Unimaginative",
    "Acorn: Inquisitive / Stubborn",
    "Storm: Generous / Wrathful",
    "Moon: Wise / Mysterious",
    "Mother: Nurturing / Worrying",
]
coat_color = ["Chocolate", "Black", "White", "Tan", "Grey", "Blue"]

coat_pattern = ["Solid", "Brindle", "Patchy", "Branded", "Marbled", "Flecked"]

physical_detail = [
    "Scarred Body",
    "Corpulent Body",
    "Skeletal Body",
    "Willowy Body",
    "Tiny Body",
    "Massive Body",
    "War painted Body",
    "Foreign clothes",
    "Elegant clothes",
    "Patched clothes",
    "Fashionable clothes",
    "Unwashed clothes",
    "Missing ear",
    "Lumpy face",
    "Beautiful face",
    "Round face",
    "Delicate face",
    "Elongated face",
    "Groomed fur",
    "Dreadlocks",
    "Dyed fur",
    "Shaved fur",
    "Frizzy fur",
    "Silky fur",
    "Night black eyes",
    "Eye patch",
    "Blood red eyes",
    "Wise eyes",
    "Sharp eyes",
    "Luminous eyes",
    "Cropped tail",
    "Whip-like tail",
    "Tufted tail",
    "Stubby tail",
    "Prehensile tail",
    "Curly tail",
]

first_name = [
    "Ada",
    "Agate",
    "Agnes",
    "Aloe",
    "April",
    "Azalea",
    "Bay",
    "Belladonna",
    "Blossom",
    "Brie",
    "Brynn",
    "Cherry",
    "Claire",
    "Crocus",
    "Dahlia",
    "Daisy",
    "Else",
    "Emerald",
    "Erin",
    "Grace",
    "Gwendoline",
    "Hazel",
    "Heather",
    "Hette",
    "Holly",
    "Hyacinth",
    "Iris",
    "Juniper",
    "Lavender",
    "Lily",
    "Magnolia",
    "Marigold",
    "Marjoram",
    "Myrtle",
    "Odette",
    "Olive",
    "Opal",
    "Pearl",
    "Pepper",
    "Poppy",
    "Rosemary",
    "Rue",
    "Saffron",
    "Sandy",
    "Sassafras",
    "Shale",
    "Susan",
    "Thistle",
    "Violet",
    "Willow",
    "Alder",
    "Ambrose",
    "Anise",
    "Anotto",
    "August",
    "Avens",
    "Basil",
    "Beryl",
    "Birch",
    "Boldo",
    "Bill",
    "Burdock",
    "Butter",
    "Cassia",
    "Chicory",
    "Clive",
    "Colby",
    "Dill",
    "Dock",
    "Eared",
    "Edmund",
    "Elmer",
    "Ernest",
    "Fennel",
    "Festus",
    "Francis",
    "Gil",
    "Hawthorn",
    "Heath",
    "Horatio",
    "Jack",
    "Jasper",
    "Konrad",
    "Larkspur",
    "Laurel",
    "Lorenz",
    "Mace",
    "Oliver",
    "Orin",
    "Reepicheep",
    "Rowan",
    "Simon",
    "Sorrel",
    "Stilton",
    "Tarragon",
    "Warren",
    "Wattle",
    "Whitacre",
    "Wormwood",
    "Yarrow",
]

last_name = [
    "Baiter",
    "Black",
    "Buckthorne",
    "Burley",
    "Butterball",
    "Catreizen",
    "Danger",
    "Deerider",
    "Grant",
    "Halva",
    "Maker",
    "Pipp",
    "Seedfall",
    "Snow",
    "Summerholme",
    "Thorne",
    "Tunneler",
    "White",
    "Winterholme",
    "Witter",
]

# Background for PCs
Backgrounds = np.genfromtxt(
    "/Users/simon/Documents/Projects/Learning_Python/mausritter/Backgrounds.csv",
    delimiter=",",
    skip_header=1,
    dtype=str,
)


print(Backgrounds)
GALOS_DB = {
    "Rooster Normal": {
        "tipo": "Basic",
        "hp_base": 150, 
        "caminho_imagem": "assets/galos/00_2.png",
        "skills": {
            1: {"nome": "Peck", "min": 14, "max": 23},
            2: {"nome": "Spur strike", "min": 10, "max": 26},
            3: {"nome": "Kick", "min": 20, "max": 29},
            4: {"nome": "Sweep", "min": 25, "max": 29},
            5: {"nome": "Charge", "min": 23, "max": 32},
            7: {"nome": "Heavy charge", "min": 26, "max": 35},
            8: {"nome": "Flying kick", "min": 30, "max": 38},
            9: {"nome": "Glide", "min": 35, "max": 41},
            11: {"nome": "Iron peck", "min": 35, "max": 44, "efeito": "Bleeding"},
            12: {"nome": "Stomp", "min": 38, "max": 47},
            14: {"nome": "Dominant kick", "min": 41, "max": 50},
            15: {"nome": "Supreme peck", "min": 35, "max": 40, "efeito": "Origami"},
            18: {"nome": "Lightning kicks", "min": 44, "max": 52},
            20: {"nome": "Lightning sweep", "min": 47, "max": 55},
            22: {"nome": "Double peck", "min": 30, "max": 35, "efeito": "Hemorrhage"},
            24: {"nome": "Divine kick", "min": 35, "max": 50, "efeito": "Shield"},
            30: {"nome": "Peck of the gods", "min": 50, "max": 70},
            31: {"nome": "Labere Volans", "min": 55, "max": 90} # Evolução
        }
    },
    "Rooster Paper": {
        "tipo": "Craft", 
        "hp_base": 150, 
        "caminho_imagem": "assets/galos/014_2.png", # Altere para o nome correto do arquivo se precisar
        "skills": {
            1: {"nome": "Paper rain", "min": 10, "max": 27},
            2: {"nome": "Paper clone", "min": 1, "max": 5, "efeito": "Origami"},
            3: {"nome": "Paper strike", "min": 15, "max": 20},
            4: {"nome": "Paper sword", "min": 15, "max": 18, "efeito": "Bleeding"},
            5: {"nome": "Paper meteor", "min": 25, "max": 30},
            6: {"nome": "Explosive paper", "min": 27, "max": 30},
            7: {"nome": "Paper storm", "min": 28, "max": 31},
            8: {"nome": "Fury of papers", "min": 30, "max": 32},
            10: {"nome": "Black paper", "min": 33, "max": 40},
            12: {"nome": "Black paper rain", "min": 40, "max": 50},
            13: {"nome": "Magic paper", "min": 35, "max": 40, "efeito": "Healing"},
            15: {"nome": "Paper star", "min": 50, "max": 60},
            17: {"nome": "Magic paper rain", "min": 42, "max": 47, "efeito": "Healing"},
            18: {"nome": "Scarlet paper", "min": 50, "max": 57},
            22: {"nome": "Catastrophe", "min": 5, "max": 100},
            24: {"nome": "Paper big bang", "min": 55, "max": 63},
            30: {"nome": "Paper universe", "min": 65, "max": 90},
            31: {"nome": "Aeterna Munus", "min": 65, "max": 95, "efeito": "Origami"} # Evolução
        },
    },
    "Rooster Rock": {
        "tipo": "Basic",
        "hp_base": 150,
        "caminho_imagem": "assets/galos/01_2.png", # Ajuste o número se necessário
        "skills": {
            1: {"nome": "Stone rain", "min": 17, "max": 22},
            2: {"nome": "Stone throw", "min": 20, "max": 25},
            3: {"nome": "Stone shot", "min": 10, "max": 30},
            4: {"nome": "Stone prison", "min": 15, "max": 20, "efeito": "Stun", "chance": 30, "turnos": 1},
            6: {"nome": "Stone punch", "min": 27, "max": 35},
            7: {"nome": "Earthquake", "min": 10, "max": 60},
            8: {"nome": "Stone kick", "min": 35, "max": 38},
            10: {"nome": "Tectonic crush", "min": 35, "max": 40},
            12: {"nome": "Shield bash", "min": 15, "max": 25, "efeito": "Shield", "chance": 100, "turnos": 4},
            14: {"nome": "Volcano", "min": 43, "max": 48},
            15: {"nome": "Tectonic rupture", "min": 20, "max": 30, "efeito": "Stun", "chance": 33, "turnos": 1},
            16: {"nome": "Supreme stone", "min": 50, "max": 58},
            19: {"nome": "Crush", "min": 55, "max": 60},
            21: {"nome": "Supreme shield", "min": 20, "max": 30, "efeito": "Shield", "chance": 100, "turnos": 4},
            23: {"nome": "Obsidian rain", "min": 56, "max": 63},
            25: {"nome": "Brick throw", "min": 35, "max": 45, "efeito": "Stun", "chance": 50, "turnos": 1},
            30: {"nome": "Meteors", "min": 50, "max": 75},
            31: {"nome": "Saxum Griseus", "min": 50, "max": 55, "efeito": "Stun", "chance": 80, "turnos": 1} # Evolução
        }
    },
    "Rooster Cutting": {
        "tipo": "Basic",
        "hp_base": 150, 
        "caminho_imagem": "assets/galos/02_2.png", # Ajuste o número da imagem conforme o seu repositório
        "skills": {
            1: {"nome": "Scissor cut", "min": 17, "max": 22},
            2: {"nome": "Intermittent scissor cut", "min": 20, "max": 25, "efeito": "Bleeding", "chance": 30, "turnos": 2},
            3: {"nome": "Razor slash", "min": 10, "max": 30, "efeito": "Bleeding", "chance": 20, "turnos": 2},
            4: {"nome": "Double razor slash", "min": 5, "max": 15, "efeito": "Bleeding", "chance": 40, "turnos": 2},
            6: {"nome": "Offensive acupuncture", "min": 24, "max": 32},
            7: {"nome": "Scissor explosion", "min": 20, "max": 60},
            8: {"nome": "Iron box", "min": 31, "max": 35, "efeito": "Iron Box", "chance": 100, "turnos": 2},
            10: {"nome": "Axe strike", "min": 41, "max": 43},
            12: {"nome": "Iron maiden", "min": 35, "max": 40, "efeito": "Iron Box", "chance": 100, "turnos": 2},
            14: {"nome": "Katana-style scissor cut", "min": 47, "max": 50},
            15: {"nome": "Intermittent katana strike", "min": 35, "max": 38, "efeito": "Bleeding", "chance": 30, "turnos": 2},
            16: {"nome": "Prince cutter", "min": 42, "max": 50, "efeito": "Bleeding", "chance": 100, "turnos": 2},
            19: {"nome": "Scissor hands", "min": 50, "max": 60},
            21: {"nome": "Interstellar axe strike", "min": 40, "max": 45, "efeito": "Iron Maiden", "chance": 100, "turnos": 2},
            23: {"nome": "One hundred thousand scissor cuts", "min": 40, "max": 50, "efeito": "Iron Maiden", "chance": 100, "turnos": 2},
            25: {"nome": "Guillotine", "min": 25, "max": 35, "efeito": "Iron Maiden", "chance": 100, "turnos": 2},
            30: {"nome": "Excalibur", "min": 55, "max": 80, "efeito": "Bleeding", "chance": 100, "turnos": 2},
            31: {"nome": "Ferrum Forfex", "min": 50, "max": 65, "efeito": "Strong Bleeding", "chance": 100, "turnos": 2}
        }
    },
    "Rooster Fire": {
        "tipo": "Ruin",
        "hp_base": 150,
        "caminho_imagem": "assets/galos/03_2.png", # Ajuste o número da imagem conforme o seu repositório
        "skills": {
            1: {"nome": "Flame fist", "min": 13, "max": 24},
            2: {"nome": "Flame", "min": 1, "max": 5, "efeito": "Flames", "chance": 100, "turnos": 2},
            3: {"nome": "Dancing flames", "min": 10, "max": 25},
            4: {"nome": "Flaming sword", "min": 13, "max": 20, "efeito": "Flames", "chance": 100, "turnos": 2},
            5: {"nome": "Blaze", "min": 15, "max": 20, "efeito": "Flames", "chance": 100, "turnos": 2},
            6: {"nome": "Extensive fire", "min": 20, "max": 25},
            7: {"nome": "Fire tornado", "min": 25, "max": 30},
            8: {"nome": "Powerful flames", "min": 5, "max": 10, "efeito": "Powerful Flames", "chance": 100, "turnos": 2},
            9: {"nome": "Fireball", "min": 27, "max": 32},
            11: {"nome": "Fireball rain", "min": 32, "max": 40},
            13: {"nome": "Furious flame", "min": 25, "max": 27, "efeito": "Powerful Flames", "chance": 100, "turnos": 2},
            14: {"nome": "Stellar fire", "min": 1, "max": 5, "efeito": "Cremation", "chance": 100, "turnos": 1},
            17: {"nome": "Fire pillar", "min": 43, "max": 48, "efeito": "Flames", "chance": 100, "turnos": 2},
            18: {"nome": "Blue fire", "min": 10, "max": 15, "efeito": "Cremation", "chance": 100, "turnos": 1},
            22: {"nome": "Stellar cremation", "min": 18, "max": 23, "efeito": "Cremation", "chance": 100, "turnos": 1},
            24: {"nome": "Sun", "min": 58, "max": 65},
            30: {"nome": "Star", "min": 20, "max": 30, "efeito": "Powerful Flames", "chance": 100, "turnos": 2},
            31: {"nome": "Stella Alba", "min": 35, "max": 65, "efeito": "Flames", "chance": 100, "turnos": 2}
        }
    },
    "Rooster Ice": {
        "tipo": "Aquatic",
        "hp_base": 150,
        "caminho_imagem": "assets/galos/04_2.png", # Ajusta o nome do ficheiro conforme o teu repositório
        "skills": {
            1: {"nome": "Ice rain", "min": 17, "max": 22},
            2: {"nome": "Freezing", "min": 1, "max": 3, "efeito": "Stun", "chance": 100, "turnos": 1},
            3: {"nome": "Ice bow", "min": 19, "max": 21},
            4: {"nome": "Frozen thorn", "min": 15, "max": 18, "efeito": "Bleeding", "chance": 40, "turnos": 2},
            5: {"nome": "Ice crystals", "min": 27, "max": 28},
            7: {"nome": "Ice wave", "min": 30, "max": 35},
            9: {"nome": "Frozen barrier", "min": 24, "max": 25, "efeito": "Shield", "chance": 50, "turnos": 4},
            10: {"nome": "Blue ice", "min": 37, "max": 38},
            12: {"nome": "Complete freezing", "min": 19, "max": 21, "efeito": "Stun", "chance": 70, "turnos": 1},
            13: {"nome": "Cold", "min": 45, "max": 46},
            15: {"nome": "Hypothermia", "min": 20, "max": 22, "efeito": "Hypothermia", "chance": 100, "turnos": 3},
            17: {"nome": "Ice wounds", "min": 30, "max": 32, "efeito": "Bleeding", "chance": 100, "turnos": 2},
            19: {"nome": "Supreme cold", "min": 30, "max": 35, "efeito": "Hypothermia", "chance": 100, "turnos": 3},
            21: {"nome": "Icy armor", "min": 14, "max": 16, "efeito": "Shield", "chance": 100, "turnos": 4},
            22: {"nome": "Infinite ice", "min": 56, "max": 58},
            25: {"nome": "Absolute zero", "min": 40, "max": 45, "efeito": "Absolute Zero", "chance": 100, "turnos": 2},
            30: {"nome": "Icy meteor", "min": 16, "max": 36, "efeito": "Stun", "chance": 65, "turnos": 1},
            31: {"nome": "Gehenna Glacies", "min": 35, "max": 65, "efeito": "Hypothermia", "chance": 100, "turnos": 3}
        }
    },
    "Rooster Metal": {
        "tipo": "Basic",
        "hp_base": 150,
        "caminho_imagem": "assets/galos/05_2.png", # Ajusta o número da imagem conforme o teu repositório
        "skills": {
            1: {"nome": "Metal hand", "min": 10, "max": 29},
            2: {"nome": "Metal leg", "min": 15, "max": 28},
            3: {"nome": "Metal body", "min": 20, "max": 25},
            4: {"nome": "Metal blades", "min": 1, "max": 5, "efeito": "Bleeding", "chance": 100, "turnos": 2},
            5: {"nome": "Metal wall", "min": 1, "max": 2, "efeito": "Shield", "chance": 100, "turnos": 4},
            7: {"nome": "Metal ball", "min": 25, "max": 30},
            8: {"nome": "Steel", "min": 28, "max": 35},
            9: {"nome": "Steel fist", "min": 30, "max": 38},
            11: {"nome": "Steel thorns", "min": 15, "max": 20, "efeito": "Bleeding", "chance": 100, "turnos": 2},
            13: {"nome": "Steel daggers", "min": 25, "max": 30, "efeito": "Hemorrhage", "chance": 100, "turnos": 3},
            15: {"nome": "Molten metal", "min": 25, "max": 35, "efeito": "Flames", "chance": 100, "turnos": 2},
            16: {"nome": "Steel wall", "min": 25, "max": 35, "efeito": "Shield", "chance": 100, "turnos": 4},
            19: {"nome": "Metal avalanche", "min": 35, "max": 50},
            21: {"nome": "Molten metal pit", "min": 25, "max": 30, "efeito": "Powerful Flames", "chance": 100, "turnos": 2},
            23: {"nome": "Condensed metal", "min": 40, "max": 55},
            25: {"nome": "Metallization", "min": 30, "max": 40, "efeito": "Hemorrhage", "chance": 100, "turnos": 3},
            30: {"nome": "Divine shield", "min": 20, "max": 30, "efeito": "Divine Shield", "chance": 100, "turnos": 2},
            31: {"nome": "Ferrum Mors", "min": 65, "max": 70}
        }
    },
    "Rooster Acid": {
        "tipo": "Ruin",
        "hp_base": 150,
        "caminho_imagem": "assets/galos/06_2.png", # Ajusta o número da imagem conforme o teu repositório
        "skills": {
            1: {"nome": "Acid", "min": 12, "max": 20, "efeito": "Acid", "chance": 30, "turnos": 2},
            2: {"nome": "Poisoned knife", "min": 5, "max": 10, "efeito": "Poison", "chance": 30, "turnos": 2},
            3: {"nome": "Acid fists", "min": 14, "max": 22},
            4: {"nome": "Sulfuric acid", "min": 8, "max": 15, "efeito": "Acid", "chance": 100, "turnos": 2},
            5: {"nome": "Acid jet", "min": 11, "max": 17, "efeito": "Acid", "chance": 100, "turnos": 2},
            6: {"nome": "Poison syringe", "min": 1, "max": 5, "efeito": "Poison", "chance": 100, "turnos": 2},
            7: {"nome": "Poison pit", "min": 10, "max": 20, "efeito": "Poison", "chance": 50, "turnos": 2},
            8: {"nome": "Strong acid", "min": 5, "max": 7, "efeito": "Strong Acid", "chance": 100, "turnos": 2},
            9: {"nome": "Acid rain", "min": 20, "max": 25, "efeito": "Acid", "chance": 100, "turnos": 2},
            11: {"nome": "Acid pillar", "min": 30, "max": 35, "efeito": "Acid", "chance": 100, "turnos": 2},
            12: {"nome": "Fluoroantimonic acid", "min": 22, "max": 25, "efeito": "Strong Acid", "chance": 100, "turnos": 2},
            14: {"nome": "Acidity", "min": 23, "max": 28, "efeito": "Strong Acid", "chance": 100, "turnos": 2},
            16: {"nome": "Poisoned weapon", "min": 10, "max": 20, "efeito": "Poison", "chance": 100, "turnos": 2},
            18: {"nome": "Acid river", "min": 20, "max": 35, "efeito": "Acid", "chance": 100, "turnos": 2},
            22: {"nome": "Acid ocean", "min": 30, "max": 35, "efeito": "Strong Acid", "chance": 100, "turnos": 2},
            24: {"nome": "Divine acid", "min": 1, "max": 5, "efeito": "Divine Acid", "chance": 100, "turnos": 3},
            30: {"nome": "Poison rain", "min": 10, "max": 30, "efeito": "Poison", "chance": 100, "turnos": 2},
            31: {"nome": "Summi Corrosionis", "min": 20, "max": 40, "efeito": "Divine Acid", "chance": 100, "turnos": 3}
        }
    },
    "Rooster Wood": {
        "tipo": "Wild",
        "hp_base": 150,
        "caminho_imagem": "assets/galos/07_2.png", # Ajusta o número da imagem conforme o teu repositório
        "skills": {
            1: {"nome": "Wood strike", "min": 17, "max": 22},
            2: {"nome": "Wooden knife", "min": 1, "max": 10, "efeito": "Bleeding", "chance": 100, "turnos": 2},
            3: {"nome": "Thicket", "min": 13, "max": 25},
            4: {"nome": "Sharp roots", "min": 25, "max": 30},
            5: {"nome": "Healing tree", "min": 2, "max": 6, "efeito": "Healing", "chance": 100, "turnos": 3},
            7: {"nome": "Giant tree", "min": 30, "max": 31},
            8: {"nome": "Hardened root", "min": 37, "max": 40},
            10: {"nome": "Wood prison", "min": 20, "max": 25, "efeito": "Stun", "chance": 70, "turnos": 1},
            12: {"nome": "Black wood", "min": 40, "max": 45},
            14: {"nome": "Devastating tree", "min": 45, "max": 50},
            15: {"nome": "Forest of giant trees", "min": 45, "max": 50},
            16: {"nome": "Roots of death", "min": 50, "max": 58},
            19: {"nome": "Healing roots", "min": 35, "max": 45, "efeito": "Healing", "chance": 100, "turnos": 3},
            21: {"nome": "Fist of nature", "min": 53, "max": 60},
            23: {"nome": "Animal attack", "min": 55, "max": 64},
            25: {"nome": "Forest of devastating trees", "min": 58, "max": 67},
            30: {"nome": "World tree", "min": 30, "max": 55, "efeito": "Powerful Healing", "chance": 100, "turnos": 3},
            31: {"nome": "Yggdrasil", "min": 55, "max": 70, "efeito": "Powerful Healing", "chance": 100, "turnos": 3} # Evolução
        }
    },
    "Rooster Rubber": {
        "tipo": "Craft",
        "hp_base": 150,
        "caminho_imagem": "assets/galos/08_2.png", # Ajusta o número da imagem conforme o teu repositório
        "skills": {
            1: {"nome": "Rubber punch", "min": 18, "max": 22},
            2: {"nome": "Rubber kick", "min": 20, "max": 25},
            3: {"nome": "Rubber bullet", "min": 22, "max": 27},
            4: {"nome": "Stretched punch", "min": 25, "max": 32},
            6: {"nome": "Hardened rubber", "min": 27, "max": 35},
            7: {"nome": "Stretched kick", "min": 30, "max": 38},
            8: {"nome": "Double punch", "min": 33, "max": 42},
            10: {"nome": "Melted rubber", "min": 35, "max": 43},
            12: {"nome": "Rubber impact", "min": 38, "max": 44},
            14: {"nome": "Melted rubber punch", "min": 43, "max": 48},
            15: {"nome": "Black rubber", "min": 46, "max": 52},
            16: {"nome": "Rubber body", "min": 50, "max": 58},
            19: {"nome": "Elastic kick", "min": 55, "max": 59},
            21: {"nome": "Rubber smash", "min": 52, "max": 65},
            23: {"nome": "Rubber fury", "min": 54, "max": 67},
            25: {"nome": "Elastic fist", "min": 56, "max": 65},
            30: {"nome": "Rubber world", "min": 53, "max": 85},
            31: {"nome": "Gear five", "min": 65, "max": 95} # Evolução
        }
    },
    "Rooster Emo": {
        "tipo": "Illusion",
        "hp_base": 150,
        "caminho_imagem": "assets/galos/09_2.png", # Ajusta o número da imagem conforme o teu repositório
        "skills": {
            1: {"nome": "Depressing peck", "min": 15, "max": 22},
            2: {"nome": "Depressing spur strike", "min": 11, "max": 25},
            3: {"nome": "Depressing kick", "min": 21, "max": 28},
            4: {"nome": "Depressing sweep", "min": 26, "max": 32},
            5: {"nome": "Depressing charge", "min": 25, "max": 33},
            7: {"nome": "Depression", "min": 52, "max": 70, "efeito": "Depression", "chance": 100, "turnos": 2},
            8: {"nome": "Overwhelming depression", "min": 33, "max": 37},
            9: {"nome": "Disturbing sadness", "min": 36, "max": 40},
            11: {"nome": "Reverse happiness", "min": 36, "max": 43},
            12: {"nome": "Depressing blade", "min": 28, "max": 40, "efeito": "Bleeding", "chance": 100, "turnos": 2},
            14: {"nome": "Immeasurable anguish", "min": 43, "max": 50},
            15: {"nome": "Double depression", "min": 65, "max": 75, "efeito": "Depression", "chance": 100, "turnos": 2},
            18: {"nome": "Pillar of depression", "min": 45, "max": 51},
            20: {"nome": "Depressing lightning sweep", "min": 50, "max": 55},
            22: {"nome": "Depressing double peck", "min": 40, "max": 45, "efeito": "Hemorrhage", "chance": 100, "turnos": 3},
            25: {"nome": "The end of happiness", "min": 50, "max": 70},
            30: {"nome": "Chiyoku", "min": 105, "max": 145, "efeito": "Strong Depression", "chance": 100, "turnos": 2},
            31: {"nome": "Sofia", "min": 130, "max": 165, "efeito": "Strong Depression", "chance": 100, "turnos": 2} # Evolução
        }
    },
    "Rooster Dinosaur": {
        "tipo": "Wild",
        "hp_base": 150,
        "caminho_imagem": "assets/galos/10_2.png", # Ajusta o número da imagem conforme o teu diretório
        "skills": {
            1: {"nome": "Bite", "min": 15, "max": 21},
            2: {"nome": "Claws", "min": 8, "max": 13, "efeito": "Bleeding", "chance": 50, "turnos": 2},
            3: {"nome": "Charge", "min": 20, "max": 27},
            4: {"nome": "Roar", "min": 23, "max": 33},
            6: {"nome": "Stomp", "min": 25, "max": 32},
            7: {"nome": "Tail swipe", "min": 30, "max": 40},
            8: {"nome": "Stunning roar", "min": 1, "max": 5, "efeito": "Stun", "chance": 100, "turnos": 1},
            10: {"nome": "Deep bite", "min": 21, "max": 23, "efeito": "Flames", "chance": 100, "turnos": 2},
            12: {"nome": "Headbutt", "min": 40, "max": 45},
            14: {"nome": "Sharp tooth", "min": 25, "max": 35, "efeito": "Bleeding", "chance": 100, "turnos": 2},
            15: {"nome": "Big run", "min": 44, "max": 50},
            16: {"nome": "Lethal bite", "min": 12, "max": 20, "efeito": "Internal Hemorrhage", "chance": 100, "turnos": 2},
            19: {"nome": "Protection roar", "min": 25, "max": 40, "efeito": "Shield", "chance": 100, "turnos": 4},
            21: {"nome": "Predatory instinct", "min": 45, "max": 55},
            23: {"nome": "Enhanced claws", "min": 42, "max": 50, "efeito": "Bleeding", "chance": 100, "turnos": 2},
            25: {"nome": "Strong tail", "min": 53, "max": 60},
            30: {"nome": "Extinction", "min": 65, "max": 90},
            31: {"nome": "Chicxulub", "min": 22, "max": 50, "efeito": "Internal Hemorrhage", "chance": 100, "turnos": 2} # Evolução
        }
    },
}

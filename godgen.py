import random

domains = []
while True:
    domains.append(random.randint(1,4))
    if random.randint(1,2) == 1 and len(domains) >= 2:
        break

dom_table = {
        1: ["Play", "Fertility/Harvest/Babies", "Health/Disease", "Hunt", "Hearth", "Doors/Household Safety", "Baking", "Wine/Beer", "Sewing/Weaving", "Wealth", "Household Item", "Food (particular)", "Important Commodity", "Male Virility", "Bridges/Gates/Crossing/Crossroads", "Fidelity/Adultery", "Animal Husbandry", "Gossip/Reputation", "Books/Scrolls", "Important Domestic Animal/Insect"],
        2: ["Invention", "War", "Indulgence", "Theft/Kidnapping", "Travel/Hospitality to Strangers", "Sailing", "Building", "Exploration/Adventure", "Cannibalism", "Honor/Justice/Vengeance", "Trade/Commerce/Unexpected Windfalls", "Slavery/Freedom", "Learning/Ignorance", "Hiding", "Art/Poetry", "Healing", "Protector of Our People", "Mining", "Sport", "Gambling"],
        3: ["Animal", "Mountains", "Night", "Oceans", "Season (1d4: Spring/Summer/Autumn/Winter)", "Plants/Woods", "Predominant Local Climate/Weather Type", "Fresh Waters", "Natural Disasters", "Thunder / Storms /Monsoon Season", "Death/Destruction", "Sun", "Moon", "Planet/Stars", "Air", "Fire", "Earth", "Water (all)", "Natural Beauty", "Decay (and rebirth)"],
        4: ["Wisdom", "Compassion", "Tricks", "Protection from Spirits", "Miracles", "Afterlife", "Pre-life", "Karma", "Undead", "Laughter", "Song", "Love/Sex", "Destiny/Fate", "Dreams", "Fear/Bravery", "Greed/Generosity", "Jealousy/Equanimity", "Hate/Love (non-romantic)", "Abstinance/Indulgence", "Bardo (Trial grounds between lifetimes)"]
        }

purviews = [dom_table[d][random.randint(0,19)] for d in domains]
print purviews, random.choice(['male']*10+['female']*10+['androgynous'])

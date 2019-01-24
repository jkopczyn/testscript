import random

domains = []
while True:
    domains.append(random.randint(0,3))
    if random.randint(1,2) == 1:
        break

if len(domains) < 2:
    domains.append(random.randint(0,3))

dom_table = [["Play/Tricksters/Sports", "Farming/Harvest", "Virility/Fertility/Babies", "Health/Disease", "Hunt", "Hearth", "Family", "Baking", "Wine/Beer", "Sewing/Weaving", "Wealth", "Household Item", "Food (particular)", "Important Commodity", "Marriage/Fidelity", "Doors/Bridges/Gates/Crossing/Crossroads", "Herding/Animal Husbandry/Domestic Animals", "Gossip/Reputation", "Books/Scrolls/Knowledge", "Important Domestic Animal or Insect"],

["Invention", "War/Peace", "Indulgence", "Theft/Kidnapping", "Travel/Hospitality to Strangers", "Sailing", "Building", "Exploration/Adventure", "Cannibalism", "Honor/Justice/Vengeance", "Trade/Commerce", "Slavery/Freedom", "Learning/Ignorance", "Luck/Skill", "Art/Poetry/Music", "Healing", "Protector of Our People", "Mining", "Sport", "Gambling"],

["Animal", "Mountains/Hills/Stone", "Night/Darkness", "Oceans", "Spring/Fall", "Summer/Winter", "Plants/Forests", "Local Climate/Weather", "Rivers/Lakes/Springs", "Natural Disasters/Storms", "Death", "Destruction", "Sun", "Moon", "Planet/Stars", "Air/Earth", "Fire/Water", "Volcanoes", "Natural Beauty", "Decay/Rebirth"],

["Wisdom/Ethics", "Compassion", "Bigotry/Madness", "Time/Distance", "Murder/Deceit", "Dedication", "Afterlife/Pre-life", "Karma", "Undead", "Laughter/Humor", "Song", "Love(eros)/Sex", "Destiny/Fate", "Dreams", "Fear/Bravery", "Greed/Generosity", "Jealousy/Equanimity", "Hate/Love(philia)", "Abstinance/Indulgence", "Magic"]]


pur_nums = [random.randint(0,19) for d in domains]
purviews = [dom_table[domains[idx]][pur_nums[idx]] for idx in xrange(len(domains))]
print purviews, random.choice(['male']*10+['female']*10+['androgynous'])

import random
import numpy as np
import matplotlib.pyplot as plt

#Do note that this simulator assumes you are only pulling from the latest set of booster packs. (Last Updated: Secluded Springs)
#If you are pulling from older packs, the rates will be different. This does account for pack points tho.
#This only calculates Chances of getting:
# - Crown
# - Shiny x2
# - Shiny
# - 3 Star Cards
# - 2 Star Cards
# - 4 Silver Cards (EX cards)

REGULAR_PACK_CHANCE=0.9162         #Has 2 chances to get a required card, since theres roundings we will just not use this value, and only pull a regular pack if the below 2 packs are not pulled.
REGULAR_PACKPLUSONE_CHANCE=0.0833   #Has 2 chances to get a required card, is the same as regular pack but may have a unique 1 star card (not counted here)
RARE_PACK_CHANCE=0.0005            #Has 5 chances to get a required card

# --------------------
# Card Rates in Regular Pack (Fourth Card) (Regular pack plus one uses the same rates)
REG_PACK_FOURTH_CARD_CROWN = 0.0004
REG_PACK_FOURTH_CARD_2SHINY = 0.00333
REG_PACK_FOURTH_CARD_SHINY = 0.00714
REG_PACK_FOURTH_CARD_3STAR = 0.00222
REG_PACK_FOURTH_CARD_2STAR = 0.0005
REG_PACK_FOURTH_CARD_4SILVER = 0.01666

# --------------------
# Card Rates in Regular Pack (Fifth Card) (Regular pack plus one uses the same rates)
REG_PACK_FIFTH_CARD_CROWN = 0.0016
REG_PACK_FIFTH_CARD_2SHINY = 0.01333
REG_PACK_FIFTH_CARD_SHINY = 0.02857
REG_PACK_FIFTH_CARD_3STAR = 0.00888
REG_PACK_FIFTH_CARD_2STAR = 0.02
REG_PACK_FIFTH_CARD_4SILVER = 0.06664

# --------------------
# Card Rates in Rare Pack (1-5th Cards)
RARE_PACK_CARD_CROWN = 0.0303
RARE_PACK_CARD_2SHINY = 0.12121
RARE_PACK_CARD_SHINY = 0.30303
RARE_PACK_CARD_3STAR = 0.0303
RARE_PACK_CARD_2STAR = 0.025
RARE_PACK_CARD_4SILVER = 0.36363

# --------------------
# Simulation parameters (We are looking for exactly 1 of each type of card)
# This means that if your pack has 2 different Crown Cards, Change TARGET_CROWN_CARDS to 2, and so on.
# --------------------
TARGET_CROWN_CARDS = 1
TARGET_SHINY2_CARDS = 4
TARGET_SHINY_CARDS = 10
TARGET_3STAR_CARDS = 1
TARGET_2STAR_CARDS = 12
TARGET_4SILVER_CARDS = 5
PACK_POINT_FOR_EACH_RARITY = [2500, 1350, 1000, 1500, 1250, 500]
TOTAL_TARGET_CARDS = (TARGET_CROWN_CARDS + TARGET_SHINY2_CARDS + TARGET_SHINY_CARDS + TARGET_3STAR_CARDS + TARGET_2STAR_CARDS + TARGET_4SILVER_CARDS)
TARGET_CARD_LIST = [TARGET_CROWN_CARDS, TARGET_SHINY2_CARDS, TARGET_SHINY_CARDS, TARGET_3STAR_CARDS, TARGET_2STAR_CARDS, TARGET_4SILVER_CARDS]
EXPERIMENTS = 5000
Total_target_cards_Unique = 0

#Helper functions
Shiny2_Card_pool = list(range(TARGET_SHINY2_CARDS))
Shiny1_Card_pool = list(range(TARGET_SHINY_CARDS))
TwoStar_Card_pool = list(range(TARGET_2STAR_CARDS))
FourSilver_Card_pool = list(range(TARGET_4SILVER_CARDS))
Crown_Card_pool = list(range(TARGET_CROWN_CARDS))
ThreeStar_Card_pool = list(range(TARGET_3STAR_CARDS))

def card_check(Card_pool, Card_set):
    global Total_target_cards_Unique
    card = random.choice(Card_pool)
    if card not in Card_set:
        Card_set.add(card)
        Total_target_cards_Unique += 1

def pack_points_needed(CARD_LIST, card_set_list, PACK_POINT_LIST):
    pack_point_needed = 0
    for index, value in enumerate(CARD_LIST):
        missing_cards = value - len(card_set_list[index])
        pack_point_needed += missing_cards*PACK_POINT_LIST[index]
    return pack_point_needed

def roll_regular_pack_plus_one():
    Fourth_card_roll = random.random()
    Fifth_card_roll = random.random()
    global Total_target_cards_Unique
    #4th card roll
    if Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN:
        card_check(Crown_Card_pool, Crownset)
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY:
        card_check(Shiny2_Card_pool, Shiny2set)
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY:
        card_check(Shiny1_Card_pool, Shiny1set)
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY + REG_PACK_FOURTH_CARD_3STAR:
        card_check(ThreeStar_Card_pool, ThreeStarset)
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY + REG_PACK_FOURTH_CARD_3STAR + REG_PACK_FOURTH_CARD_2STAR:
        card_check(TwoStar_Card_pool, TwoStarset)
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY + REG_PACK_FOURTH_CARD_3STAR + REG_PACK_FOURTH_CARD_2STAR + REG_PACK_FOURTH_CARD_4SILVER:
        card_check(FourSilver_Card_pool, FourSilverset)
    #5th card roll
    if Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN:
        card_check(Crown_Card_pool, Crownset)
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY:
        card_check(Shiny2_Card_pool, Shiny2set)
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY:
        card_check(Shiny1_Card_pool, Shiny1set)
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY + REG_PACK_FIFTH_CARD_3STAR:
        card_check(ThreeStar_Card_pool, ThreeStarset)
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY + REG_PACK_FIFTH_CARD_3STAR + REG_PACK_FIFTH_CARD_2STAR:
        card_check(TwoStar_Card_pool, TwoStarset)
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY + REG_PACK_FIFTH_CARD_3STAR + REG_PACK_FIFTH_CARD_2STAR + REG_PACK_FIFTH_CARD_4SILVER:
        card_check(FourSilver_Card_pool, FourSilverset)
        #Nothing of interest happens afterwards, as there are rarities that we dont count (thus probabilities do not add up to 1.)
        #This is the same for packs below.

def roll_one_rare_pack_card():
    rare_pack_roll = random.random()
    global Total_target_cards_Unique
    if rare_pack_roll < RARE_PACK_CARD_CROWN:
        card_check(Crown_Card_pool, Crownset)
    elif rare_pack_roll < RARE_PACK_CARD_CROWN + RARE_PACK_CARD_2SHINY:
        card_check(Shiny2_Card_pool, Shiny2set)
    elif rare_pack_roll < RARE_PACK_CARD_CROWN + RARE_PACK_CARD_2SHINY + RARE_PACK_CARD_SHINY:
        card_check(Shiny1_Card_pool, Shiny1set)
    elif rare_pack_roll < RARE_PACK_CARD_CROWN + RARE_PACK_CARD_2SHINY + RARE_PACK_CARD_SHINY + RARE_PACK_CARD_3STAR:
        card_check(ThreeStar_Card_pool, ThreeStarset)
    elif rare_pack_roll < RARE_PACK_CARD_CROWN + RARE_PACK_CARD_2SHINY + RARE_PACK_CARD_SHINY + RARE_PACK_CARD_3STAR + RARE_PACK_CARD_2STAR:
        card_check(TwoStar_Card_pool, TwoStarset)
    elif rare_pack_roll < RARE_PACK_CARD_CROWN + RARE_PACK_CARD_2SHINY + RARE_PACK_CARD_SHINY + RARE_PACK_CARD_3STAR + RARE_PACK_CARD_2STAR + RARE_PACK_CARD_4SILVER:
        card_check(FourSilver_Card_pool, FourSilverset)

def roll_regular_pack():
    Fourth_card_roll = random.random()
    Fifth_card_roll = random.random()
    global Total_target_cards_Unique
    #4th card roll
    if Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN:
        card_check(Crown_Card_pool, Crownset)
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY:
        card_check(Shiny2_Card_pool, Shiny2set)
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY:
        card_check(Shiny1_Card_pool, Shiny1set)
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY + REG_PACK_FOURTH_CARD_3STAR:
        card_check(ThreeStar_Card_pool, ThreeStarset)
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY + REG_PACK_FOURTH_CARD_3STAR + REG_PACK_FOURTH_CARD_2STAR:
        card_check(TwoStar_Card_pool, TwoStarset)
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY + REG_PACK_FOURTH_CARD_3STAR + REG_PACK_FOURTH_CARD_2STAR + REG_PACK_FOURTH_CARD_4SILVER:
        card_check(FourSilver_Card_pool, FourSilverset)
    #5th card roll
    if Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN:
        card_check(Crown_Card_pool, Crownset)
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY:
        card_check(Shiny2_Card_pool, Shiny2set)
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY:
        card_check(Shiny1_Card_pool, Shiny1set)
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY + REG_PACK_FIFTH_CARD_3STAR:
        card_check(ThreeStar_Card_pool, ThreeStarset)
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY + REG_PACK_FIFTH_CARD_3STAR + REG_PACK_FIFTH_CARD_2STAR:
        card_check(TwoStar_Card_pool, TwoStarset)
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY + REG_PACK_FIFTH_CARD_3STAR + REG_PACK_FIFTH_CARD_2STAR + REG_PACK_FIFTH_CARD_4SILVER:
        card_check(FourSilver_Card_pool, FourSilverset)

# --------------------
# Run a single experiment
# --------------------

def run_experiment():
    global Total_target_cards_Unique, Shiny2set, Shiny1set, TwoStarset, FourSilverset, Crownset, ThreeStarset
    Total_target_cards_Unique = 0
    pulls_done = 0
    pack_points = 0
    Crownset = set()
    Shiny2set = set()
    Shiny1set = set()
    ThreeStarset = set()
    TwoStarset = set()
    FourSilverset = set()
    set_list = [Crownset, Shiny2set, Shiny1set, ThreeStarset, TwoStarset, FourSilverset]

    while Total_target_cards_Unique < int(TOTAL_TARGET_CARDS):
        if pulls_done == 10000:  #To prevent infinite loops when pack points were not added, now to just ensure code can run if code breaks
            break
        pulls_done += 1
        pack_points += 5
        roll = random.random()
        if roll < RARE_PACK_CHANCE:
            for _ in range(5):
                roll_one_rare_pack_card()  #5 cards in a rare pack, so we roll for a card 5 times
        elif roll < RARE_PACK_CHANCE + REGULAR_PACKPLUSONE_CHANCE:
            roll_regular_pack_plus_one()
        else:
            roll_regular_pack()
        if pack_points >= pack_points_needed(TARGET_CARD_LIST, set_list, PACK_POINT_FOR_EACH_RARITY):
            break

    # Debugging Check (uncomment to use, make sure to set experiments to a lower value)
    # print("collected:", {
    #     "crown": f"{len(Crownset)}/{TARGET_CROWN_CARDS}",
    #     "shiny2": f"{len(Shiny2set)}/{TARGET_SHINY2_CARDS}",
    #     "shiny1": f"{len(Shiny1set)}/{TARGET_SHINY_CARDS}",
    #     "3star": f"{len(ThreeStarset)}/{TARGET_3STAR_CARDS}",
    #     "2star": f"{len(TwoStarset)}/{TARGET_2STAR_CARDS}",
    #     "4silver": f"{len(FourSilverset)}/{TARGET_4SILVER_CARDS}",
    # }, "pulls:", pulls_done, "pack_points:", pack_points)
    #You have to manually calculate if the missing cards can be bought by pack points, im too lazy to do that

    return pulls_done


# --------------------
# Main simulation
# --------------------
def main():
    total_pulls_list =[]

    for _ in range(EXPERIMENTS):
        pulls_needed = run_experiment()
        total_pulls_list.append(pulls_needed)
    # --------------------
    # Stats
    # --------------------
    print("========== RESULTS ==========")
    print(f"Experiments run: {EXPERIMENTS}")
    print(f"Minimum pulls to get every card in the set: {min(total_pulls_list)}")
    print(f"Maximum pulls to get every card in the set(limted to 10 000 in case code breaks): {max(total_pulls_list)}")
    print(f"Average pulls to get every card in the set: {np.mean(total_pulls_list):.2f}")
    print(f"5th percentile pulls: {np.percentile(total_pulls_list,5):.0f}")
    print(f"95th percentile pulls: {np.percentile(total_pulls_list,95):.0f}\n")


    # --------------------
    # Histogram generation
    # --------------------
    plt.figure(figsize=(10,6))
    plt.hist(total_pulls_list, bins=50)
    plt.xlabel("Total Pulls")
    plt.ylabel("Frequency")
    plt.title(
    "Pulls needed to get every card in the set "
    "(excluding Gold 1 Star Cards, 3-1 Silver Cards, and Pack Point Calculation)"
    )
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()

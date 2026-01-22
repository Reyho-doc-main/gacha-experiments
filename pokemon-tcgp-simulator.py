import random
import numpy as np
import statistics
import matplotlib.pyplot as plt

#Do note that this simulator assumes you are only pulling from the latest set of booster packs. (Last Updated: Secluded Springs)
#If you are pulling from older packs, the rates will be different.
#This does not include any Pack Points or Pack Point Exchange mechanics. (It is 5 pack points per pack)
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
TOTAL_TARGET_CARDS = (TARGET_CROWN_CARDS + TARGET_SHINY2_CARDS + TARGET_SHINY_CARDS + TARGET_3STAR_CARDS + TARGET_2STAR_CARDS + TARGET_4SILVER_CARDS)
EXPERIMENTS = 7000
Total_target_cards_Unique = 0

#Helper functions
Shiny2_Card_pool = list(range(TARGET_SHINY2_CARDS))
Shiny1_Card_pool = list(range(TARGET_SHINY_CARDS))
TwoStar_Card_pool = list(range(TARGET_2STAR_CARDS))
FourSilver_Card_pool = list(range(TARGET_4SILVER_CARDS))
Crown_Card_pool = list(range(TARGET_CROWN_CARDS))
ThreeStar_Card_pool = list(range(TARGET_3STAR_CARDS))

def roll_regular_pack_plus_one():
    Fourth_card_roll = random.random()
    Fifth_card_roll = random.random()
    global Total_target_cards_Unique
    #4 star roll
    if Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN:
        card = random.choice(Crown_Card_pool)
        if card not in Crownset:
            Crownset.add(card)
            Total_target_cards_Unique += 1
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY:
        card = random.choice(Shiny2_Card_pool)
        if card not in Shiny2set:
            Shiny2set.add(card)
            Total_target_cards_Unique += 1
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY:
        card = random.choice(Shiny1_Card_pool)
        if card not in Shiny1set:
            Shiny1set.add(card)
            Total_target_cards_Unique += 1
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY + REG_PACK_FOURTH_CARD_3STAR:
        card = random.choice(ThreeStar_Card_pool)
        if card not in ThreeStarset:
            ThreeStarset.add(card)
            Total_target_cards_Unique += 1
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY + REG_PACK_FOURTH_CARD_3STAR + REG_PACK_FOURTH_CARD_2STAR:
        card = random.choice(TwoStar_Card_pool)
        if card not in TwoStarset:
            TwoStarset.add(card)
            Total_target_cards_Unique += 1
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY + REG_PACK_FOURTH_CARD_3STAR + REG_PACK_FOURTH_CARD_2STAR + REG_PACK_FOURTH_CARD_4SILVER:
        card = random.choice(FourSilver_Card_pool)
        if card not in FourSilverset:
            FourSilverset.add(card)
            Total_target_cards_Unique += 1
    #5 star roll
    if Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN:
        card = random.choice(Crown_Card_pool)
        if card not in Crownset:
            Crownset.add(card)
            Total_target_cards_Unique += 1
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY:
        card = random.choice(Shiny2_Card_pool)
        if card not in Shiny2set:
            Shiny2set.add(card)
            Total_target_cards_Unique += 1
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY:
        card = random.choice(Shiny1_Card_pool)
        if card not in Shiny1set:
            Shiny1set.add(card)
            Total_target_cards_Unique += 1
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY + REG_PACK_FIFTH_CARD_3STAR:
        card = random.choice(ThreeStar_Card_pool)
        if card not in ThreeStarset:
            ThreeStarset.add(card)
            Total_target_cards_Unique += 1
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY + REG_PACK_FIFTH_CARD_3STAR + REG_PACK_FIFTH_CARD_2STAR:
        card = random.choice(TwoStar_Card_pool)
        if card not in TwoStarset:
            TwoStarset.add(card)
            Total_target_cards_Unique += 1
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY + REG_PACK_FIFTH_CARD_3STAR + REG_PACK_FIFTH_CARD_2STAR + REG_PACK_FIFTH_CARD_4SILVER:
        card = random.choice(FourSilver_Card_pool)
        if card not in FourSilverset:
            FourSilverset.add(card)
            Total_target_cards_Unique += 1

def roll_one_rare_pack_card():
    rare_pack_roll = random.random()
    global Total_target_cards_Unique
    if rare_pack_roll < RARE_PACK_CARD_CROWN:
        card = random.choice(Crown_Card_pool)
        if card not in Crownset:
            Crownset.add(card)
            Total_target_cards_Unique += 1
    elif rare_pack_roll < RARE_PACK_CARD_CROWN + RARE_PACK_CARD_2SHINY:
        card = random.choice(Shiny2_Card_pool)
        if card not in Shiny2set:
            Shiny2set.add(card)
            Total_target_cards_Unique += 1
    elif rare_pack_roll < RARE_PACK_CARD_CROWN + RARE_PACK_CARD_2SHINY + RARE_PACK_CARD_SHINY:
        card = random.choice(Shiny1_Card_pool)
        if card not in Shiny1set:
            Shiny1set.add(card)
            Total_target_cards_Unique += 1
    elif rare_pack_roll < RARE_PACK_CARD_CROWN + RARE_PACK_CARD_2SHINY + RARE_PACK_CARD_SHINY + RARE_PACK_CARD_3STAR:
        card = random.choice(ThreeStar_Card_pool)
        if card not in ThreeStarset:
            ThreeStarset.add(card)
            Total_target_cards_Unique += 1
    elif rare_pack_roll < RARE_PACK_CARD_CROWN + RARE_PACK_CARD_2SHINY + RARE_PACK_CARD_SHINY + RARE_PACK_CARD_3STAR + RARE_PACK_CARD_2STAR:
        card = random.choice(TwoStar_Card_pool)
        if card not in TwoStarset:
            TwoStarset.add(card)
            Total_target_cards_Unique += 1
    elif rare_pack_roll < RARE_PACK_CARD_CROWN + RARE_PACK_CARD_2SHINY + RARE_PACK_CARD_SHINY + RARE_PACK_CARD_3STAR + RARE_PACK_CARD_2STAR + RARE_PACK_CARD_4SILVER:
        card = random.choice(FourSilver_Card_pool)
        if card not in FourSilverset:
            FourSilverset.add(card)
            Total_target_cards_Unique += 1

def roll_regular_pack():
    Fourth_card_roll = random.random()
    Fifth_card_roll = random.random()
    global Total_target_cards_Unique, Shiny2set, Shiny1set, TwoStarset, FourSilverset, Crownset, ThreeStarset
    #4 star roll
    if Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN:
        card = random.choice(Crown_Card_pool)
        if card not in Crownset:
            Crownset.add(card)
            Total_target_cards_Unique += 1
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY:
        card = random.choice(Shiny2_Card_pool)
        if card not in Shiny2set:
            Shiny2set.add(card)
            Total_target_cards_Unique += 1
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY:
        card = random.choice(Shiny1_Card_pool)
        if card not in Shiny1set:
            Shiny1set.add(card)
            Total_target_cards_Unique += 1
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY + REG_PACK_FOURTH_CARD_3STAR:
        card = random.choice(ThreeStar_Card_pool)
        if card not in ThreeStarset:
            ThreeStarset.add(card)
            Total_target_cards_Unique += 1
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY + REG_PACK_FOURTH_CARD_3STAR + REG_PACK_FOURTH_CARD_2STAR:
        card = random.choice(TwoStar_Card_pool)
        if card not in TwoStarset:
            TwoStarset.add(card)
            Total_target_cards_Unique += 1
    elif Fourth_card_roll < REG_PACK_FOURTH_CARD_CROWN + REG_PACK_FOURTH_CARD_2SHINY + REG_PACK_FOURTH_CARD_SHINY + REG_PACK_FOURTH_CARD_3STAR + REG_PACK_FOURTH_CARD_2STAR + REG_PACK_FOURTH_CARD_4SILVER:
        card = random.choice(FourSilver_Card_pool)
        if card not in FourSilverset:
            FourSilverset.add(card)
            Total_target_cards_Unique += 1
    #5 star roll
    if Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN:
        card = random.choice(Crown_Card_pool)
        if card not in Crownset:
            Crownset.add(card)
            Total_target_cards_Unique += 1
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY:
        card = random.choice(Shiny2_Card_pool)
        if card not in Shiny2set:
            Shiny2set.add(card)
            Total_target_cards_Unique += 1
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY:
        card = random.choice(Shiny1_Card_pool)
        if card not in Shiny1set:
            Shiny1set.add(card)
            Total_target_cards_Unique += 1
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY + REG_PACK_FIFTH_CARD_3STAR:
        card = random.choice(ThreeStar_Card_pool)
        if card not in ThreeStarset:
            ThreeStarset.add(card)
            Total_target_cards_Unique += 1
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY + REG_PACK_FIFTH_CARD_3STAR + REG_PACK_FIFTH_CARD_2STAR:
        card = random.choice(TwoStar_Card_pool)
        if card not in TwoStarset:
            TwoStarset.add(card)
            Total_target_cards_Unique += 1
    elif Fifth_card_roll < REG_PACK_FIFTH_CARD_CROWN + REG_PACK_FIFTH_CARD_2SHINY + REG_PACK_FIFTH_CARD_SHINY + REG_PACK_FIFTH_CARD_3STAR + REG_PACK_FIFTH_CARD_2STAR + REG_PACK_FIFTH_CARD_4SILVER:
        card = random.choice(FourSilver_Card_pool)
        if card not in FourSilverset:
            FourSilverset.add(card)
            Total_target_cards_Unique += 1

# --------------------
# Run a single experiment
# --------------------

def run_experiment():
    global Total_target_cards_Unique, Shiny2set, Shiny1set, TwoStarset, FourSilverset, Crownset, ThreeStarset
    Total_target_cards_Unique = 0
    pulls_done = 0
    Shiny2set = set()
    Shiny1set = set()
    TwoStarset = set()
    FourSilverset = set()
    Crownset = set()
    ThreeStarset = set()

    while Total_target_cards_Unique < int(TOTAL_TARGET_CARDS):
        if pulls_done == 10000:  #To prevent infinite loops in extreme cases
            break
        pulls_done += 1
        roll = random.random()
        if roll < RARE_PACK_CHANCE:
            for _ in range(5):
                roll_one_rare_pack_card()
        elif roll < RARE_PACK_CHANCE + REGULAR_PACKPLUSONE_CHANCE:
            roll_regular_pack_plus_one()
        else:
            roll_regular_pack()
    # Debugging Check (uncomment to use, make sure to set experiments to a lower value)
    # print("collected:", {
    #     "crown": Crownset,
    #     "shiny2": Shiny2set,
    #     "shiny1": Shiny1set,
    #     "2star": TwoStarset,
    #     "4silver": FourSilverset,
    #     "3star": ThreeStarset
    # }, "pulls:", pulls_done)
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
    print(f"Maximum pulls to get every card in the set(can be infinite, limted to 10 000): {max(total_pulls_list)}")
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

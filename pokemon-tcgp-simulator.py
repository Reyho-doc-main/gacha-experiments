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

REGULAR_PACK_CHANCE=0.9162         #Has 2 chances to get a required card
REGULAR_PACKPLUSONE_CHANCE=0.833   #Has 2 chances to get a required card, is the same as regular pack but may have a unique 1 star card (not counted here)
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
# Simulation parameters (Get one of each card(The following is also the amount of unique cards in the pack for the rarity listed))
# --------------------
TARGET_CROWN_CARDS = 1
TARGET_SHINY2_CARDS_UNIQUE = 4
TARGET_SHINY_CARDS_UNIQUE = 10
TARGET_3STAR_CARDS = 1
TARGET_2STAR_CARDS_UNIQUE = 12
TARGET_4SILVER_CARDS = 5
TOTAL_TARGET_CARDS = (TARGET_CROWN_CARDS + TARGET_SHINY2_CARDS_UNIQUE + TARGET_SHINY_CARDS_UNIQUE + TARGET_3STAR_CARDS + TARGET_2STAR_CARDS_UNIQUE + TARGET_4SILVER_CARDS)
EXPERIMENTS = 10000


# --------------------
# Run a single experiment
# --------------------
def run_experiment():
    pulls = 0
    Total_target_cards = 0

    while Total_target_cards < TOTAL_TARGET_CARDS:
        pulls += 1
                # Roll for Rare Pack/Regular Pack +1
        roll = random.random()
        if roll < RARE_PACK_CHANCE:
            #Rare Pack drops
            pass
        elif roll < RARE_PACK_CHANCE + REGULAR_PACKPLUSONE_CHANCE:
            #Regular Pack +1 drops
            pass
        else:
            #Regular Pack drops
            pass



# --------------------
# Main simulation
# --------------------
def main():
    total_pulls_list =[]
    first_rate_up_pulls = []

    for _ in range(EXPERIMENTS):
        pulls_needed, first_pull = run_experiment()
        total_pulls_list.append(pulls_needed)
        first_rate_up_pulls.append(first_pull)
    # --------------------
    # Stats
        # --------------------
    print("========== RESULTS ==========")
    print(f"Experiments run: {EXPERIMENTS}")
    print(f"Minimum pulls to get every card in the set: {min(total_pulls_list)}")
    print(f"Maximum pulls to get every card in the set(can be infinite): {max(total_pulls_list)}")
    print(f"Average pulls to get every card in the set: {np.mean(total_pulls_list):.2f}")
    print(f"5th percentile pulls: {np.percentile(total_pulls_list,5):.0f}")
    print(f"95th percentile pulls: {np.percentile(total_pulls_list,95):.0f}\n")


    # --------------------
    # Smooth integer-based line: total pulls
    # --------------------
    counts_total = np.bincount(total_pulls_list)
    x_total = np.arange(len(counts_total))
    plt.figure(figsize=(10,6))
    plt.plot(x_total, counts_total, linewidth=2)
    plt.xlabel("Total Pulls")
    plt.ylabel("Frequency")
    plt.title("Pulls needed to get every card in the set (excluding Gold 1 Star Cards, 3-1 Silver Cards, and Pack Point Calculation)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

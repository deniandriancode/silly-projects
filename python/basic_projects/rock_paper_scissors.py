import random


def get_random_rps():
    rps_list = ["R", "P", "S"]
    return rps_list[random.randint(0, len(rps_list) - 1)]


def compare_rps(npc, player):
    rps_dict = {
            "R": "ROCK",
            "P": "PAPER",
            "S": "SCISSORS"}
    if player not in rps_dict.keys():
        print("Please choose between R, P, and S")
        return
    print(f"Computer chooses {rps_dict[npc]}, You choose {rps_dict[player]}")
    if npc == player:
        print("DRAW!")
    elif npc == "R" and player == "S" or npc == "P" and player == "R" or npc == "S" and player == "P":
        print("You LOSE!")
    else:
        print("You WIN!")


def main():
    while True:
        opp = get_random_rps()
        inp = input("> ")[0].upper()
        if inp == "Q":
            break
        compare_rps(opp, inp)

    print("Thank you for playing!")




if __name__ == "__main__":
    main()

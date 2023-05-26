import random


def roll_dice():
    return random.randint(0, 6)


def main():
    """Main driver function"""
    dice = roll_dice()
    print(f"You got {dice}")



if __name__ == "__main__":
    main()

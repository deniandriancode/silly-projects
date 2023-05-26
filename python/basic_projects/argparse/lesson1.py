import argparse


def main():
    parse = argparse.ArgumentParser(
            prog="lesson_one",
            description="Hello worlding the argument parser",
            epilog="Just some bottom text"
            )
    parse.add_argument("-k", "--key", action="store", help="user's unique key",
                       required=False)
    parse.add_argument("file_input", action="store")
    parse.add_argument("file_output", action="store")
    parse.add_argument("-e", "--encrypt", action="store_true", help="encrypt message")
    parse.add_argument("-d", "--decrypt", action="store_false", help="decrypt message")
    args = parse.parse_args()
    print(args)
    print(args.key)


if __name__ == "__main__":
    main()

import base64
import sys


def main():
    if len(sys.argv) != 3:
        print("usage: decode input output", file=sys.stderr)
        exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, "rb") as fpi:
        with open(output_file, "w") as fpo:
            fpo.write(base64.b64decode(fpi.read()).decode("utf-8"))



if __name__ == "__main__":
    main()


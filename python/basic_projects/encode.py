import base64
import sys


def main():
    if len(sys.argv) != 3:
        print("usage: encode input output", file=sys.stderr)
        exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, "r") as fpi:
        with open(output_file, "wb") as fpo:
            fpo.write(base64.b64encode(fpi.read().encode("utf-8")))



if __name__ == "__main__":
    main()

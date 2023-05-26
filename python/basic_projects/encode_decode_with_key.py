import argparse


def encrypt(key, message):
    result_list = []
    l_key = len(key)
    for i in range(len(message)):
        k = ord(key[i % l_key])
        enc = chr(ord(message[i]) + k)
        result_list.append(enc)

    result = "".join(result_list)
    return result


def decrypt(key, message):
    result_list = []
    l_key = len(key)
    for i in range(len(message)):
        k = ord(key[i % l_key])
        enc = chr(ord(message[i]) - k)
        result_list.append(enc)

    result = "".join(result_list)
    return result


def get_parser():
    parser = argparse.ArgumentParser(
            prog="encdec",
            description="Encode and Decode message with special key",
            epilog=""
            )
    parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt the message")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the message")
    parser.add_argument("-k", "--key", action="store", required=True, help="String of unique key")
    parser.add_argument("IN", help="Input file")
    parser.add_argument("OUT", help="Output file")
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    fp_in = args.IN
    fp_out = args.OUT
    key = args.key
    with open(fp_in, "r") as fpi:
        content = fpi.read()
        if args.decrypt:
            out_content = decrypt(key, content)
        else:
            out_content = encrypt(key, content)
        with open(fp_out, "w") as fpo:
            fpo.write(out_content)


if __name__ == "__main__":
    main()

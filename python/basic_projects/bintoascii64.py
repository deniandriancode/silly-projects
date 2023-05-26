import argparse
import base64
import codecs

# Convert binary-ascii ascii-binary with special key


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


def encode_base64(key, fp_in, fp_out, read_mode, write_mode):
    with open(fp_in, read_mode) as fpi:
        content = fpi.read()
        with open(fp_out, write_mode) as fpo:
            content_string = base64.b64encode(content).decode("ascii")
            out_content = encrypt(key, content_string)
            fpo.write(out_content)


def decode_base64(key, fp_in, fp_out, read_mode, write_mode):
    with open(fp_in, read_mode) as fpi:
        content = fpi.read()
        out_content = decrypt(key, content)
        with open(fp_out, write_mode) as fpo:
            content_bin = base64.b64decode(out_content)
            fpo.write(content_bin)


def main():
    parser = get_parser()
    args = parser.parse_args()
    fp_in = args.IN
    fp_out = args.OUT
    key = args.key
    if args.encrypt:
        encode_base64(key, fp_in, fp_out, "rb", "w")
    else:
        decode_base64(key, fp_in, fp_out, "r", "wb")


if __name__ == "__main__":
    main()

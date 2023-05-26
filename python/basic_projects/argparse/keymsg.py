msg = "hello there"
key = "yh739"

enc_msg = []

for c in msg:
    enc = chr(ord(c) + 8)
    enc_msg.append(enc)

print("".join(enc_msg))
print()

def ency_more():
    res = []
    l_key = len(key)
    for i in range(len(msg)):
        k = ord(key[i % l_key])
        enc = chr(ord(msg[i]) + k)
        res.append(enc)

    secret = "".join(res)
    print(secret)


def decy_more():
    res = []
    l_key = len(key)
    for i in range(len(secret)):
        k = ord(key[i % l_key])
        enc = chr(ord(secret[i]) - k)
        res.append(enc)

    print("".join(res))


msg = "hello there"
key = "yh736"

def ency(k, m):
    s = 0
    for i in k:
        s += ord(i)
    s %= 263
    
    res = []
    for c in m:
        res.append(chr(ord(c) + s))

    return "".join(res)


def decy(k, m):
    s = 0
    for i in k:
        s += ord(i)
    s %= 263
    
    res = []
    for c in m:
        res.append(chr(ord(c) - s))

    return "".join(res)


result = ency(key, msg)
print(result)

result = decy(key, result)
print(result)

import random

from Crypto.Cipher import AES

BLOCK_SIZE = 16  # bytes
INIT_VEC = 'This is an IV456'  # hardcoding this is a terrible idea

EXAMPLE_TEXT = "This is some very secret ciphertxt"


def blockify(text, block_size=BLOCK_SIZE):
    return [text[i:i + block_size] for i in range(0, len(text), block_size)]


def key_gen():
    return "".join([chr(random.getrandbits(8)) for _ in xrange(BLOCK_SIZE)])


def validate_padding(padded_text):
    return all([n == padded_text[-1] for n in padded_text[-ord(padded_text[-1]):]])


def pkcs7_pad(text):
    length = BLOCK_SIZE - (len(text) % BLOCK_SIZE)
    text += chr(length) * length
    return text


def pkcs7_depad(text):
    if not validate_padding(text):
        raise InvalidPadding()
    return text[:-ord(text[-1])]


def encrypt(plaintext, key, init_vec):
    cipher = AES.new(key, AES.MODE_CBC, init_vec)
    padded_text = pkcs7_pad(plaintext)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext


def decrypt(ciphertext, key, init_vec):
    cipher = AES.new(key, AES.MODE_CBC, init_vec)
    padded_text = cipher.decrypt(ciphertext)
    plaintext = pkcs7_depad(padded_text)
    return plaintext


def numberify(characters):
    return map(lambda x: ord(x), characters)


def stringify(numbers):
    return "".join(map(lambda x: chr(x), numbers))


def test_padding_oracle():
    my_key = key_gen()
    IV = numberify(INIT_VEC)
    ciphertext = numberify(encrypt(EXAMPLE_TEXT, my_key, INIT_VEC))
    blocks = blockify(ciphertext)

    cleartext = []
    for block_num, (c1, c2) in enumerate(zip([IV] + blocks, blocks)):
        print "cracking block {} out of {}".format(block_num + 1, len(blocks))
        i2 = [0] * 16
        p2 = [0] * 16
        for i in xrange(15, -1, -1):
            for b in xrange(0, 256):
                prefix = c1[:i]
                pad_byte = (BLOCK_SIZE - i)
                suffix = [pad_byte ^ val for val in i2[i + 1:]]
                evil_c1 = prefix + [b] + suffix
                try:
                    result = decrypt(stringify(c2), my_key, stringify(evil_c1))
                except InvalidPadding:
                    pass
                else:
                    i2[i] = evil_c1[i] ^ pad_byte
                    p2[i] = c1[i] ^ i2[i]
                    break
        cleartext += p2
    print "========================="
    print stringify(cleartext)
    print "========================="
    return stringify(cleartext)


class InvalidPadding(Exception):
    pass

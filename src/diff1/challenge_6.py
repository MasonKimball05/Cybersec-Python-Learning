# Break repeating-key XOR
# There's a file here (challenge-data/6.txt). It's been base64'd after being
# encrypted with repeating-key XOR.
# Decrypt it.
# Here's how:
#
# 1. Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
# 2. Write a function to compute the edit distance/Hamming distance between two
#    strings. The Hamming distance is just the number of differing bits. The
#    distance between:
#
#    this is a test
#
#    and
#
#    wokka wokka!!!
#
#    is 37. Make sure your code agrees before you proceed.
# 3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second
#    KEYSIZE worth of bytes, and find the edit distance between them.
#    Normalize this result by dividing by KEYSIZE.
# 4. The KEYSIZE with the smallest normalized edit distance is probably the
#    key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or
#    take 4 KEYSIZE blocks instead of 2 and average the distances.
# 5. Now that you probably know the KEYSIZE: break the ciphertext into blocks
#    of KEYSIZE length.
# 6. Now transpose the blocks: make a block that is the first byte of every
#    block, and a block that is the second byte of every block, and so on.
# 7. Solve each block as if it was single-character XOR. You already have
#    code to do this.
# 8. For each block, the single-byte XOR key that produces the best looking
#    histogram is the repeating-key XOR key byte for that block. Put them
#    together and you have the key.
#
# This code is going to turn out to be surprisingly useful later on. Breaking
# repeating-key XOR ("Vigenere") statistically is obviously an academic
# exercise, a "Crypto 101" thing. But more people "know how" to break it than
# can actually break it, and a similar technique breaks something much more
# important.

import base64

def hamming_dist(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    total_dist = 0
    if len(str1) != len(str2):
        raise Exception("str1 and str2 must be the same length")

    for i in range(len(str1)):
        str1_bits = ord(str1[i])
        str2_bits = ord(str2[i])
        total_dist += bin(str1_bits ^ str2_bits).count("1")

    return total_dist

def hamming_dist_bytes(str1, str2):
    total_dist = 0
    if len(str1) != len(str2):
        raise Exception("str1 and str2 must be the same length")

    for i in range(len(str1)):
        total_dist += bin(str1[i] ^ str2[i]).count("1")

    return total_dist

keysize = -float("inf")

txt_file = open('ch6.txt', 'r')
file_contents = txt_file.read()
ciphertext = base64.b64decode(file_contents)
print(len(ciphertext)) # 2876




if __name__ == "__main__":
    print(hamming_dist("this is a test", "wokka wokka!!!"))
    print(hamming_dist_bytes(b"this is a test", b"wokka wokka!!!"))


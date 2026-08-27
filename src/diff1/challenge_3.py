# Single-byte XOR cipher
# The hex encoded string:
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.
# You can do this by hand. But don't: write code to do it for you.
# How? Devise some method for "scoring" a piece of English plaintext.
# Character frequency is a good metric. Evaluate each output and choose the one with the best score.

encoded_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

raw_bytes = bytes.fromhex(encoded_string)

# Frequency key chart of all the english letters
freq = {
    'e': 12.7, 't': 9.1, 'a': 8.2, 'o': 7.5, 'i': 7.0, 'n': 6.7,
    's': 6.3, 'h': 6.1, 'r': 6.0, 'd': 4.3, 'l': 4.0, 'c': 2.8,
    'u': 2.8, 'm': 2.4, 'w': 2.4, 'f': 2.2, 'g': 2.0, 'y': 2.0,
    'p': 1.9, 'b': 1.5, 'v': 1.0, 'k': 0.8, 'j': 0.2, 'x': 0.2,
    'q': 0.1, 'z': 0.1
}

def score(text_bytes):
    score = 0
    for i in text_bytes:
        c = chr(i).lower()
        if c in freq:
            score += freq[c]
        elif c == ' ':
            score += 2 # Give points for spaces too
        elif i < 32 or i > 126:
            score -= 10 # penalize non-printable chars
    return score

best_score = -float('inf') # Not 0 incase for some reason every candidate is negative for some reason
best_key = None
best_text = None


for key in range(256):
    candidate = bytes([i ^ key for i in raw_bytes])
    s = score(candidate)
    if s > best_score:
        best_score = s
        best_key = key
        best_text = candidate


if __name__ == "__main__":
    print(f"Key: {best_key}\nText: {best_text.decode('utf-8')}")
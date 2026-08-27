# detect single character xor
# One of the 60-character strings in this file has been encrypted by single-character XOR.
# Find it.
# (Your code from #3 should help.)
import challenge_3

txt_file = open('ch4.txt','r')

best_score = -float('inf') # Not 0 incase for some reason every candidate is negative for some reason
best_key = None
best_text = None

def break_single_xor(ciphertext):
    global best_score
    global best_key
    global best_text
    for key in range(256):
        candidate = bytes([i ^ key for i in ciphertext])
        s = challenge_3.score(candidate)
        if s > best_score:
            best_score = s
            best_key = key
            best_text = candidate

    return s

def collect_all_text():
    for line in txt_file:
        ciphertext = bytes.fromhex(line.strip())
        break_single_xor(ciphertext)

    return best_score, best_key, best_text.strip().decode('utf-8')

if __name__ == '__main__':
    best_score, best_key, best_text = collect_all_text()
    print(f"Best Score: {best_score}\nBest Key: {best_key}\nBest Text: {best_text}")
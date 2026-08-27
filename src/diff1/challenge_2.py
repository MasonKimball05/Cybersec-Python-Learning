# Decode starting input then xor the decoded bytes
# The instructions are as follows
# If your function works properly, then when you feed it the string:
# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:
# 686974207468652062756c6c277320657965
# ... should produce:
# 746865206b696420646f6e277420706c6179
import base64


starting_input = "1c0111001f010100061a024b53535009181c"
xor_against = "686974207468652062756c6c277320657965"
expected_output = "746865206b696420646f6e277420706c6179"

raw_bytes = bytearray.fromhex(starting_input)
xor_bytes = bytearray.fromhex(xor_against)

xor_output = bytes(xor_bytes ^ raw_bytes for xor_bytes, raw_bytes in zip(xor_bytes, raw_bytes))

output = xor_output.hex()

print(output)

assert expected_output == output, "error in input"
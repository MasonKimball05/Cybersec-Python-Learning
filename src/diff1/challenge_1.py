# Convert hex to base64
# This one is simple, convert
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# to SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
# With this rule "Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing."
import base64

hexinput = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
expected_output = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


raw_bytes = bytearray.fromhex(hexinput)
base64_bytes = base64.b64encode(raw_bytes)

base64_output = base64_bytes.decode("utf-8")

print(base64_output)

assert expected_output == base64_output, "error in output"

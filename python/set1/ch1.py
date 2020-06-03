# Set 1 Challenge 1
# Convert hex to base64
# hex string: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d 
# base64: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t 
from binascii import unhexlify
from base64 import b64encode, b64decode

def main():
    hexstr = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    b64str = b64encode(unhexlify(hexstr))
    # b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    b64dec = b64decode(b64str)
    # b"I'm killing your brain like a poisonous mushroom"
    print(b64str)
    print(b64dec)

if __name__ == "__main__":
    main()

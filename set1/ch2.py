# Set 1 Challenge 2
# Fixed XOR
# XORed strings should produce 746865206b696420646f6e277420706c6179 
import binascii

def main():
    b1 = binascii.a2b_hex("1c0111001f010100061a024b53535009181c")
    b2 = binascii.a2b_hex("686974207468652062756c6c277320657965")
    # XOR b1 and b2
    print(b1)

if __name__ == "__main__":
    main()

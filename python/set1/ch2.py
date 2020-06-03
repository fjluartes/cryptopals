# Set 1 Challenge 2
# Fixed XOR
# XORed strings should produce 746865206b696420646f6e277420706c6179 
from binascii import hexlify, unhexlify

def main():
    b1 = unhexlify("1c0111001f010100061a024b53535009181c")
    b2 = unhexlify("686974207468652062756c6c277320657965")
    # XOR each byte in both byte arrays b1 and b2
    ans = bytes([x^y for (x,y) in zip(b1, b2)])
    # b"the kid don't play"
    ansstr = hexlify(ans)
    # b'746865206b696420646f6e277420706c6179'
    print(ansstr)
    
if __name__ == "__main__":
    main()

# Set 1 Challenge 3
# Single-byte XOR Cipher
# hex string 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# XORed against a single character
from binascii import hexlify, unhexlify, b2a_uu

def main():
    str1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    byt = unhexlify(str1)
    all_freq = {}
    for i in byt:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    # sort by character frequency
    sorted_af = sorted(all_freq.items(), key=lambda item: item[1])
    a = sorted_af[len(sorted_af) - 1]
    # XOR most frequent character in byt
    ans = bytes([a[0]^x for x in byt])
    # b'cOOKING\x00mc\x07S\x00LIKE\x00A\x00POUND\x00OF\x00BACON'
    print(ans)


if __name__ == "__main__":
    main()


def main():
    arg_str = input("")
    for i in range(1, 26):
        decode_str = caesar(arg_str, i)
        print(decode_str)

def caesar(str, key):
    plaintext = ""
    for ch in list(str):
        if 'A' <= ch <= 'Z':
            plaintext += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            plaintext += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            plaintext += ch

    return plaintext

if __name__ == "__main__":
    main()

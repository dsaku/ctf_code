
input_str = "EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT."

path = 'ans.txt'

def main():
    # arg_str = input("")
    arg_str = input_str
    f = open(path, mode="w")
    for i in range(1, 26):
        decode_str = caesar(arg_str, i)
        print(decode_str)
        f.write(decode_str)
    f.close()

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

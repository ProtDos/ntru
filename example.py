import NTRU2

if __name__ == "__main__":
    m = input("Enter message: ")
    f = input("Enter filename to save keys: ")
    mod = input("Enter mode [moderate, high, highest]: ")

    NTRU2.generate_keys(f, mode=mod)  # moderate, high, highest
    enc = NTRU2.encrypt(f, m)
    print("Encrypted message:", enc)
    dec = NTRU2.decrypt(f, enc)
    print("Decrypted message:", dec)

    assert m == dec, "Decryption failed"

    print("\nDecryption was successfully done")

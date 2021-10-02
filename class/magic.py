class   Key:
    def __init__(self):
        self.passphrase = "zax2rulez"
    def __len__(self):
        return 1337
    def __getitem__(self,key):
        return 3
    def __gt__(self,other):
        return True
    def __str__(self):
        return "GeneralTsoKeycard"



if __name__ == "__main__":
    print("\033[38;5;154mmain_test\033[0m")

    key = Key()

    print("len(key) =", len(key))
    print("key[404] =", key[404])
    print("key > 9000 =", key > 9000)
    print("key.passphrase =", key.passphrase)
    print("str(key) =", str(key))

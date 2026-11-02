def functhree():
    print("Three")

def functwo():
    functhree()
    print("Two")

def funcone():
    # calls another function
    functwo()
    print("One")

funcone()
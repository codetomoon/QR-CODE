# A Python script to convey a heartfelt poem "to my far love".

def create_poem():
    poem = (
        "Across the distance, my heart takes flight,\n"
        "Through endless days and starry night.\n"
        "Each whispering breeze carries your name,\n"
        "A constant spark, an eternal flame.\n\n"
        "The sun may rise, the moon may fall,\n"
        "But my love for you surpasses all.\n"
        "Though oceans wide keep us apart,\n"
        "You're always here, within my heart.\n\n"
        "So hold this truth, let it be known,\n"
        "Our bond is strong, our love has grown.\n"
        "No miles nor time can break our chain,\n"
        "Till we meet again, through joy or pain."
    )
    return poem

def display_poem():
    poem = create_poem()
    border = "*" * (len(max(poem.splitlines(), key=len)) + 4)
    print(border)
    for line in poem.splitlines():
        print(f"* {line.ljust(len(border) - 4)} *")
    print(border)

if __name__ == "__main__":
    display_poem()

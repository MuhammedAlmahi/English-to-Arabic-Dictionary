from Data import dictionary


dictionary = dictionary.eng_to_ara
while True:
    word = input("Word: ").strip()
    if word in dictionary:
        print(f"\nFound:\n meaning: {dictionary[word]}\n")
    else:
        print(f"Can not find result for '{word}' \n")

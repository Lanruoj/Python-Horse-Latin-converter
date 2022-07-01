def horse_latin_translator():
    VOWELS = ("a", "e", "i", "o", "u")

    raw_text = str(input("Enter text:  "))
    raw_words = raw_text.split()
    horse_word_list = []

    for word in raw_words:
        if word.endswith(VOWELS):
            horse_word = f"{word}nay"
            horse_word_list.append(horse_word)
        else:
            horse_word = f"{word}hay"
            horse_word_list.append(horse_word)

    horse_word_tuple = tuple(horse_word_list)
    horse_result = " ".join(horse_word_tuple)
    return horse_result

print(horse_latin_translator())
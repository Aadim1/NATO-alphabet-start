import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
its_on = True
while its_on:
    try:
        word = input("Enter a word: ").upper()
        every_letter_in_a_word_list = [letter for letter in word]
        NATO_result_string = [nato_dictionary[letter] for letter in word]
        print(NATO_result_string)
        its_on = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        continue

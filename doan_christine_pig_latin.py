# Programmer: Christine Doan
# Prompt: Make a pig latin translator
# vowel = add -way
# consonant = move consonants to beginning of word to the end and add -ay

# defining function to translate pig Latin
def pigLatin(word):
    index = 0
    while (word[index] not in "AEIOUaeiou"): # words starting with consonants
        return word[index:] + word[0:index] + "ay"
    else:
        return word + "way"

# defining main function
def main():
    finished = False
    while not finished:
        sentence = input ("Enter string here or press ENTER to quit: ")
        if sentence != '':
            pigLatinText = ""
            splitS = sentence.split()

            for word in splitS:
                pigLatinText += pigLatin(word) + " "
            print(pigLatinText[:-1])

        else:
            finished = True
main()
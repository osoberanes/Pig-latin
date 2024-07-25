#I need a list of articles and prepositions that i won't translate
articles_and_preps = (
    # Articles
    "a", "an", "the",

    # Prepositions
    "about", "above", "across", "after", "against", "along", "among", "around", "at",
    "before", "behind", "below", "beneath", "beside", "between", "beyond", "by",
    "despite", "down", "during", "except", "for", "from", "in", "inside", "into",
    "like", "near", "of", "off", "on", "out", "outside", "over", "past", "since",
    "through", "throughout", "to", "under", "until", "up", "upon", "with",
    "within", "without",

    # Conjunctions
    "and", "but", "or", "nor", "for", "yet", "so", "although", "because",
    "before", "even if", "if", "since", "though", "unless", "until",
    "when", "where", "while"
)
# Input a word. Used a random message.
word = input("Welcome to Pig Latin, where we can translate all of your wildest words. \n Please input your word: \n")
# Transform it to lowercase
word = word.lower()
# Is it an article or a preposition?
# Compare it one by one to the list of preposition
for x in articles_and_preps:
    if word == x:
        # If there is one match, print the word as it is. You're done.
        print(f"Your word is {word}")
        quit()
# Create a list of vowels
vowels = "aeiou"
# Is the first letter a vowel?
if word[0] in vowels:
    # If so, add nay to the end of the word. 
    pig_latin = word + "nay"
    # Print it, you're done
    print(f"Your word is {pig_latin}")
# If none of the previous has worked, then it is a word that begins with a consonant
else:
    # Take the word from the second letter, then add the first letter, then add "ay" to the end.
    pig_latin = word[1:]+word[0]+"ay"
    # Print it, you're done
    print(f"Your word is {pig_latin}")

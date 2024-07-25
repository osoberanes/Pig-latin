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
word = input("Welcome to Pig Latin, where we can translate all of your wildest words. \n Please input your word: \n")
word = word.lower()
for x in articles_and_preps:
    if word == x:
        print(f"Your word is {word}")
        quit()
vowels = "aeiou"
if word[0] in vowels:
    pig_latin = word + "nay"
    print(f"Your word is {pig_latin}")
else:
    pig_latin = word[1:]+word[0]+"ay"
    print(f"Your word is {pig_latin}")

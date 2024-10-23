import string

# Get the sentence from the user
sentence = input("Enter a sentence: ")

# Remove commas and periods from the sentence
sentence = sentence.replace(",", "").replace(".", "")

# Convert the sentence to lowercase
sentence = sentence.lower()

# Split the sentence into words
words = sentence.split()

# Initialize a dictionary to count the occurrences of each word
word_count = {}

# Count the frequency of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the count of each word
for word, count in word_count.items():
    print(f"{word} : {count}")
word_to_search = input("Enter the word to search in file: ").lower()
count = 0

with open("sample.txt", "r") as file:
    for word in file.read().lower().split():
        if word == word_to_search:
            count += 1

print(f"The word '{word_to_search}' occurred {count} times.")
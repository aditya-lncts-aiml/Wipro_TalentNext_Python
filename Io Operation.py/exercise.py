# 1 Read the entire content from a .txt file and display it

with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

# 2 Read first n lines from a .txt file (take n from user input)

n = int(input("Enter the number of lines to read: "))

with open("sample.txt", "r") as file:
    for i in range(n):
        line = file.readline()
        if line:
            print(line.strip())
        else:
            break

# 3 Accept input from user and append it to a .txt file

text = input("Enter text to append to the file: ")

with open("sample.txt", "a") as file:
    file.write(text + "\n")

print("Text appended successfully.")

# 4  Read contents line by line and store each into a list

lines_list = []

with open("sample.txt", "r") as file:
    for line in file:
        lines_list.append(line.strip())

print("Lines stored in list:")
print(lines_list)

# 5  Find the longest word in the file (assume only one longest word

with open("sample.txt", "r") as file:
    words = file.read().split()
    longest_word = max(words, key=len)

print("Longest word:", longest_word)

# 6 Count frequency of a user-entered word in the file

word_to_search = input("Enter the word to search in file: ").lower()
count = 0

with open("sample.txt", "r") as file:
    for word in file.read().lower().split():
        if word == word_to_search:
            count += 1

print(f"The word '{word_to_search}' occurred {count} times.")

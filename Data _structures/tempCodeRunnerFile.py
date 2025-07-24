def count_alex_occurrences(input_string):
    words = input_string.split()
    count = 0
    for word in words:
        if 'Alex' in word:
            count += 1
    return count
input_string = "Hi Alex WelcomeAlex Bye Alex."
occurrences = count_alex_occurrences(input_string)
print(f"Number of times 'Alex' appears: {occurrences}")
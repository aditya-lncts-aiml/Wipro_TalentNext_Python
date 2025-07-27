# Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells you the place and time where you have to go and meet him.
# He challenges you to find it out without seeing the content of the file. He has given hints to find it. Let’s surprise him by breaking the challenge with our Python code.


from collections import Counter

def find_meeting_details(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Get number of lines (meeting time)
    num_lines = len(lines)
    if num_lines <= 12:
        meeting_time = f"{num_lines} AM"
    else:
        meeting_time = f"{num_lines % 12} PM"

    # Count words
    words = []
    for line in lines:
        for word in line.strip().split():
            # Remove punctuation and make lowercase
            clean_word = ''.join(char for char in word if char.isalpha())
            if clean_word:
                words.append(clean_word.lower())
    
    word_counts = Counter(words)
    most_common_word, _ = word_counts.most_common(1)[0]
    
    # Capitalize first letter and append 'Street'
    meeting_place = most_common_word.capitalize() + " Street"

    # Output
    print("Meeting time:", meeting_time)
    print("Meeting place:", meeting_place)

# Example usage:
find_meeting_details("sample.txt")
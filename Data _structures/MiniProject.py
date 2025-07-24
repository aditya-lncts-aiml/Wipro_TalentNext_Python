'''Mini-Project1'''

'''
Create a dictionary that contains a list of people and one interesting fact about each of them.
Display each person and his or her interesting fact to the screen. Next, change a fact about one of
the people. Also add an additional person and corresponding fact. Display the new list of people
and facts. Run the program multiple times and notice if the order changes.

Sample output:
Jeff: Is afraid of Dogs.
David: Plays the piano.
Jason: Can fly an airplane.

Jeff: Is afraid of heights.
David: Plays the piano.
Jason: Can fly an airplane.
Jill: Can hula dance.
'''

people_facts = {
    'Jeff': 'Is afraid of Dogs.',
    'David': 'Plays the piano.',
    'Jason': 'Can fly an airplane.'
}

def display_facts(facts):
    for person, fact in facts.items():
        print(f"{person}: {fact}")
display_facts(people_facts)

people_facts['Jeff'] = 'Is afraid of heights.'
people_facts['Jill'] = 'Can hula dance.'
print("\nUpdated Facts:")
display_facts(people_facts)


'''Mini-Project2'''

'''
Given the participant's score sheet for your University Sports Day, you are
required to find the runner-up score. You have scores. Store them in a list and
find the score of the runner-up.

Sample input: [2, 3, 6, 6, 5]

Sample output: 5

Explanation: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second
maximum is 5. Hence, we print 5 as the runner-up score.
'''
given_list = [2, 3, 6, 6, 5]
print("Given list:", )
def find_runner_up_score(scores):
    max_score = max(scores)
    scores.sort()
    for i in range(len(scores) - 1, -1, -1):
        if scores[i] != max_score:
            return scores[i]
    return max_score
print("Runner-up score:", find_runner_up_score(given_list))


'''Mini-Project3'''

'''
You have a record of n students. Each record contains the student's name, and
their percent marks in Math, Physics and Chemistry. The marks can be floating
values. You are required to save the record in a dictionary data type.

Student's name is the key. Marks stored in a list is the value. The user enters a
student's name. Output the average percentage marks obtained by that
student.

Formula: (sum of marks) / (no of subjects)

Sample input: { "Krishna" : [67, 68, 69],

"Arjun" : [70, 98, 63],

"Malika" : [52, 56, 60] }

Sample output:

Enter a name: Malika

Average percentage mark: 56

Explanation:

Marks for Malika are [52, 56, 60] whose average is (52 + 56 + 60) / 3 => 56
'''

sample_input = { 
    "Krishna" : [67, 68, 69],
    "Arjun" : [70, 98, 63],
    "Malika" : [52, 56, 60] 
}

def calculate_average_percentage(student_name, records):
    if student_name in records:
        marks = records[student_name]
        average = sum(marks) / len(marks)
        return average
    else:
        return None
name_input = input("Enter a name: ")
average_percentage = calculate_average_percentage(name_input, sample_input)
if average_percentage is not None:
    print(f"Average percentage mark: {average_percentage:.2f}")
else:
    print("Student not found.")


'''Mini-Project4'''

'''
Given a string of n words, help Alex to find out how many times his name
appears in the string.

Constraint: 1 <= n <= 200

Sample input: Hi Alex WelcomeAlex Bye Alex.

Sample output: 3

Explanation: Alex name appears 3 times in the string. Hi Alex WelcomeAlex
Bye Alex.
'''
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
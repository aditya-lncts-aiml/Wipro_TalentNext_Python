'''
Q1) WAP to find check if a string has only octal digits. Given string ['789','123','004']
'''

import re
def is_octal(s):
    return bool(re.match(r'^[0-7]+$', s))

test_strings = ['789', '123', '004']
for s in test_strings:
    if is_octal(s):
        print(f"{s} is an octal number.")
    else:
        print(f"{s} is not an octal number.")

'''
Q2) Extract the user id, domain name and suffix from the following email addresses.
emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""
'''
import re
emails = "zuck@facebook.com"

mail = re.search(r'(\w+)@(\w+).(\w+)', emails)
print("User ID:", mail.group(1))
print("Domain Name:", mail.group(2))
print("Suffix:", mail.group(3))

'''
Q3) Split the following irregular sentence into proper words
sentence = """""A, very very; irregular_sentence""" ## expected outout : A very very irregular sentence
'''
import re
sentence = "A, very very; irregular_sentence"
words = re.split(r'[ ,;_]+', sentence)
print(" ".join(words))

'''
Q4) Clean up the following tweet so that it contains only the user's message.
 That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.
tweet = 'Good advice! RT @TheNextWeb: What I would do differently if I was 
learning to code today http://t.co/lbwej0px0d cc: @garybernhardt #rstats'
##desired_output = 'Good advice What I would do differently if I was learning to code today'
'''
import re
tweet = 'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0px0d cc: @garybernhardt #rstats'
cleaned_tweet = re.sub(r"[!:]|https?://\S+|@\w+|#\w+|RT|CC|cc", "", tweet)
print("Cleaned Tweet:", cleaned_tweet.strip())

'''
Q5) Extract all the text portions between the tags from the following HTML page:
https://raw.githubusercontent.com/selva86/datasets/master/sample.html

Code to retrieve the HTML page is given below:

import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
r.text # html text is contained here

desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph!', 'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']
'''

import re
import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html_text = r.text
print(html_text)
pattern = r'[<HTML>]+(.*?)</HTML>|<TITLE>(.*?)</TITLE>|<a href=".*?">(.*?)</a>|<H1>(.*?)</H1>|<H2>(.*?)</H2>|<P>(.*?)</P>|<B><I>(.*?)</I></B>'
matches = re.findall(pattern, html_text)
desired_output = []
for match in matches:
    for group in match:
        if group:  # Check if the group is not empty
            desired_output.append(group.strip())
print("Extracted Text Portions:", desired_output)


'''
Q6) Given below list of words, identify the words that begin and end with the same character.
civic
trust
widows
maximum
museums
aa
as
'''

import re
words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
same_char_words = [word for word in words if re.match(r'^(.)\w*\1$', word)]
print("Words that begin and end with the same character:", same_char_words)
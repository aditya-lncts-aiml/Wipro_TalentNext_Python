import re
words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
same_char_words = [word for word in words if re.match(r'^(.)\w*\1$', word)]
print("Words that begin and end with the same character:", same_char_words)
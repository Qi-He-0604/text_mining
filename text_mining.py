import re

f = open('TheRaven.txt', 'r+')
text = f.read()
f.close()

text = text.lower()
new_text = re.sub('[^ a-zA-Z0-9]', '', text)

text_count = list(map(len, new_text.split()))
print('Number of 4 letter words: ' + str(text_count.count(4)))
print('Number of 5 letter words: ' + str(text_count.count(5)))
print('Number of 6 letter words: ' + str(text_count.count(6)))

input_word = input('Please enter a word? ').lower()
print('input_word: ' + input_word)
count = new_text.count(input_word)
print('The count is: '+ str(count))


word_input = str(raw_input("Please enter a word: "))
counter = {}
for letter in word_input:
  if letter in counter:
    counter[letter] += 1
  else:
    counter[letter] = 1

print counter
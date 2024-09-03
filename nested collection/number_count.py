lst=[10,20,10,20,11,12,11,12,13,14]

number_count={num:lst.count(num) for num in lst }

print(number_count)



text=["hello","hai","hello","hai","hello"]

word_count={w:text.count(w) for w in text}

print(word_count)
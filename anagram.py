anagram ={}

words = [word.rstrip('\n') for word in open('filename.txt', 'r').readlines()]

for word in words:
    if "".join(sorted(word)) in anagram:
        if word != anagram["".join(sorted(word))][0]:
            anagram["".join(sorted(word))].append(word)
    else:
        anagram["".join(sorted(word))]=[word]
        
"To find maximum number unique anagram pairs"
i=0
for a in anagram:
    if len(anagram[a])>1:
        i = i+1
print 'the number of unique anagrams are ',i

"Assuming the longest anagram is the word with the longest length"
z=[]
for a in anagram:
    
    if len(a)>1:
        x = len(a)
        z.append(x)
print 'Assuming the longest anagram is the word with maximum characters- the length of longest anagram is ', max(z)

"Assuming the longest anagram is the total number of words which have identical characters"
y=[]
for a in anagram:
    if len(anagram[a])>1:
        x=len(anagram[a])
        y.append(x)

print 'Assuming the longest anagram is the total number of words which have identical characters, the answer is: ', max(y)

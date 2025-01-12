frequency={'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
k=2
count=0

for i in frequency:
    if frequency[i]==k:
        count=count+1
print("The frequency in this dictioary is:",count)


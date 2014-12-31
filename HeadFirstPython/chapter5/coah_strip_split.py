with open('james.txt') as jaf:
    data = jaf.readline()
james = []
for i in data.split(',').strip():
    james.append(i.strip())
print(james)

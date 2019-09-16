
import random

def read_process_data(fileName):
    with open(fileName) as f:
        # the following line
        # - joins each line in the file into one big string
        # - removes all newlines and carriage returns
        # - converts everything to lowercase
        content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower()
        return content.split(' ')

dictionary = {}

#enter any text file
content = read_process_data("constitution.txt")

length = int(raw_input("Enter a seed length: "))
start = 0

for i in range (0,(len(content)-1)):
    seed = tuple(content[start:length])
    if seed not in dictionary and length < (len(content)-1):
        dictionary[seed] = [content[length]]
    elif length < (len(content)-1):
        dictionary[seed].append(content[length])
    length += 1
    start += 1

key = random.choice(list(dictionary))
print (str(key)),

for i in range (0, len(dictionary)):
    valueIndex = random.randint(0,(len(dictionary[key])-1))
    nextWord = dictionary[key][valueIndex]
    print(" " + nextWord),
    key = list(key)
    key.pop(0)
    key.append(nextWord)
    key = tuple(key)

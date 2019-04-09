

#Imports
import math
import random
import matplotlib.pyplot as plt #
#python learner
x = 5
y = 10
numList = [1,2,2,4,6,7,9]
d = "done\n\n"

#####Lists
alphabet = []
#alphabet = alphabet + ['a']
bc = ['b','c']
#a = ['a'] This makes a string, not a list of length 1
alphabet.append('a')
alphabet.extend(bc)
alphabet.extend(['e','d'])
print(alphabet)
alphabet.sort()
print(alphabet)
dee = alphabet.pop(3)
print(dee)
print(alphabet)
alphabet[1:4] = [1,2,3]
print(alphabet)
del alphabet[1:4] #delete b,c
print(alphabet) #should print a
sentence = "This is a sentence with words and spacing"
sentence_ = "This_is_a_sentence_with_words_and_underscores"
wordList = sentence.split()
wordList2 = sentence_.split('_')
joinDelim = '-'
sentenceDash = joinDelim.join(wordList2)
print(sentenceDash)
print(sentence,wordList, wordList2)
word = "word"
listWord = list(word)
print(word)
print(listWord)
print(d)

#### Dictionaries
eng2sp = dict() #empty dict {}
eng2sp['one'] = 'uno'
print(eng2sp)
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp['three'])


### math
print(max(numList)) #9
print(min(numList)) #1
print(len(numList)) #7
print(sum(numList)) #31
num9 = numList[len(numList)-1]
print(num9)
ratio = x/y
decibel = 10*math.log10(ratio)
print(decibel)

#sinusoids
radians = 0.6
height = math.sin(radians)
print(height)

#Exponents
tenToThe5 = math.pow(10,5)
print(tenToThe5)
print(math.pi) #pi
print(d)

### random
for i in range(10):
    rando = random.random() #random float from 0 to 0.99999999999999999999999
    print(rando)
print('\n')
rando = random.randint(5,10) #random integer from 5 to 10
print(rando)
print(d)

#print
print('spam '*4) #spam spam spam spam

#IF
if x<10:
    print('smaller')
elif x>=10:
    print('bigger')
elif (y or x > 9) and x < 5:
    print('not gonna print')
elif y or x > 9 and x < 6:
    print('y is big then nine. X is smol 6 too')
print(d)

#type all these lines at once in atom: Ctrl + click lines
#Click Click Click I PICK UP STICK
#Click Click Click I PICK UP STICK
#Click Click Click I PICK UP STICK
#Click Click Click I PICK UP STICK

#WHILE
while x>0:
    print('x')
    x = x-1
print(d)

#list of Strings
fruits = ["apple","pear","banana","pineapple","eggplant"]
for fruit in fruits:
    print(fruit,"purdy good")

a = fruits[0][0]
ear = fruits[1][1:4] #1 to 4 including first (1) excluding last (4)
orear = fruits[1][1:] #[:3] is first two indexes
print(a)
print(ear)
print(d)

#File manipulation
file = open('OwnedGnome.txt')
count = 0
Mcount = 0
for line in file:
    if line.startswith('M'):
        Mcount = Mcount+1
    print(line.rstrip()) #gets rid of extra \n
    count = count+1
print("line count:",count,"First letter N:",Mcount)
print(d)

#Dictionary
thisDictionary = dict()
thisDictionary['entry 1'] = 1
thisDictionary['entry 2'] = 2
print("my dict:",thisDictionary)
print(d)

counts = dict()
keys = ['key1','key2','key3']
for key in keys:
    counts[key] = counts.get(key,0)+1
print(counts)
print(d)

#function
def variance(List):
    length = len(List)
    average = math.fsum(List)/length
    tempVar = 0
    for item in numList:
        tempVar = tempVar + math.pow(item-average,2)
    tempVar = tempVar/length
    return tempVar

var = variance(numList)
print(var)

print(d)

#typeCast
int('32')
int(3.999) #equals 3
str(3.14)
float(32) #32.0
print(d)

#Data Cleaning
# remove parentheses from string
moma = "(hello),(nice),to,(meet),you \n (I) am (not human)"
for row in moma:
    row = row.replace("(","")
    row = row.replace(")","")

# Remove bad characters
test_data = ["1912", "1870-79", "1929",
             "1913\\-1923", "(1951)", "1994",
             "1934", "c. 1915", "2009", "1978",
             "1947", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "1964\\-65", "c. 1955.",
             "c. 1970's", "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","\\","s","'"]

def strip_characters(strings):
    for char in bad_chars:
        strings = strings.replace(char,"")
    strings = strings.strip()
    return strings

stripped_test_data = []

for word in test_data:
    stripped_test_data.append(strip_characters(word))

processed_test_data = []

def process_date(string):
    if "-" in string:
        years = string.split("-")
        if len(years[1]) == 2:
            years[1] = years[0][:2] + years[1]
            string = round( (int( years[0] ) + int( years[1] ))/2 )
        else:
            string = int(date)
        return string

for date in stripped_test_data:
    processed_test_data.append(process_date(date)

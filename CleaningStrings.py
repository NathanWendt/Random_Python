#REPLACE A SUBSTRING WITHIN A STRING
green_ball = "red ball".replace("red", "green")

#Remove a substring:
friend_removed = "hello there friend!".replace(" friend", "")

#Remove a series of characters from a string:
bad_chars = ["'", ",", ".", "!"]
string = "We'll remove apostrophes, commas, periods, and exclamation marks!"
for char in bad_chars:
    string = string.replace(char, "")

#Convert a string to title cases
Hello = "hello".title()
print(Hello)

#Check a string for the existence of a substring:
if "car" in "carpet":
    print("The substring was found.")
else:
    print("The substring was not found.")

#Split a string into a list of strings:
split_on_dash = "1980-12-08".split("-")

#Last 5 char:
last_five_chars = "This is a long string."[-5:]
print(last_five_chars)

#concatenate
superman = "Clark" + " " + "Kent"

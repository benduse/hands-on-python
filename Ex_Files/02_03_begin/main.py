NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

JOHN = NAMES[0]
PAUL = NAMES[1]

JOHN_PAUL = NAMES[:2] #slicing name to the left of two
GEORGE_RINGO = NAMES[2:4] #slicing name from index 2 to 4
REVERSE = NAMES[::-1] #reversing the list
EVERY_OTHER = NAMES[::2] #taking every other element

print("this is the sum: " + str(sum(AGES)))
print("this is the minimum: " + str(min(AGES)))
print("this is the maximum: " + str(max(AGES)))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print("this is the reverse: " + str(REVERSE))
print("this is every other: " + str(EVERY_OTHER))

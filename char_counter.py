# Write a program that asks the user to input a string and then
# prints out the counts of each character used in the string.
#
# For example, if the input string is 'hello, world!' the output
# should be something like
#
# 'h': 1
# 'e': 1
# 'l': 3
# 'o': 2
# ',': 1
# ' ': 1
# 'w': 1
# 'r': 1
# 'd': 1
# '!': 1
#
# You don't have to match this format exactly, but it's important
# for the autograder that the message you print contains
# each of the character/count pairs in the following format.
# 
# '<character>': <count>
#
# You should get input from the user using the input function. Your
# code should work for arbitrary strings, including the empty string.

def char_counter():
    input_string= input("Enter a string:")
    char_count= {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        print(f"'{char}': {count} ")
        
if __name__ == "__main__":
    char_counter()
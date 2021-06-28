"""
Given a string that has set of words and spaces, write a program to move all spaces to front of string, by traversing the string only once.

Examples:

Input  : str = "geeks for geeks"
Output : ste = "  geeksforgeeks"

Input  : str = "move these spaces to beginning"
Output : str = "    movethesespacestobeginning"
There were four space characters in input,
all of them should be shifted in front.
"""

def move_space_front(text):
    text_lngth = len(text)
    new_text = ''
    for ch in text:
        if ch != ' ':
            new_text += ch
    spaces = ' '*(len(text) - len(new_text))
    print(len(spaces))
    modified_text = spaces + new_text
    return modified_text


if __name__ == '__main__':
    text ='move these spaces to beginning'
    modified_text = move_space_front(text)
    print(modified_text)

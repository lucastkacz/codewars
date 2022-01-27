"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
Any whitespace at the end of the line should also be stripped out. 

Example:

Given an input string of:
    >>> apples, pears # and bananas
    >>> grapes
    >>> bananas !apples

The output expected would be:
    >>> apples, pears
    >>> grapes
    >>> bananas
"""

def solution(string,markers):
    content = string.split("\n")
    clean_content = []

    for full_line in content:

        clean_line = ""
        for char in full_line:
            if not char in markers:
                clean_line += char
            else:
                break
        
        clean_line = clean_line.strip()
        clean_content.append(clean_line)
        
    return "\n".join(clean_content)

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print(solution("a #b\nc\nd $e f g", ["#", "$"]))

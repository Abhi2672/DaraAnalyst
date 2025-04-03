# Defining strings
str1 = "Hello"
str2 = "World"

# 1. Concatenation
str3 = str1 + " " + str2
print("Concatenation:", str3)

# 2. Append (using +=)
str1 += " Everyone"
print("Append:", str1)

# 3. Length of string
print("Length of str1:", len(str1))

# 4. Access character
print("First character of str1:", str1[0])

# 5. Modify character (strings are immutable, so we need to create a new one)
str1 = "h" + str1[1:]
print("Modified str1:", str1)

# 6. Substring (Slicing)
sub = str1[:5]
print("Substring:", sub)

# 7. Find a substring
pos = str1.find("Everyone")
if pos != -1:
    print("'Everyone' found at position:", pos)

# 8. Replace
str1 = str1.replace("Everyone", "Python Learners")
print("After Replace:", str1)

# 9. Uppercase and Lowercase
print("Uppercase:", str1.upper())
print("Lowercase:", str1.lower())

# 10. Split string
words = str1.split()
print("Split into words:", words)

# 11. Join string
joined = "-".join(words)
print("Joined with '-':", joined)

# 12. Check if string starts/ends with a substring
print("Starts with 'h':", str1.startswith("h"))
print("Ends with 'Learners':", str1.endswith("Learners"))

# 13. Count occurrences of a substring
count = str1.count("o")
print("Count of 'o':", count)

# 14. Strip (removes leading and trailing spaces)
str4 = "  Hello World  "
print("Stripped:", str4.strip())

# 15. Reverse a string
reversed_str = str1[::-1]
print("Reversed:", reversed_str)

# 16. Find the string
print(str1.find("ll"))

# 17. Index of string
print(str3.index("Hello"))


# 18. Is lower 
print(str2.islower())

# 19. Is upper
print(str3.isupper())

#20. Replace string with specific value
print(str3.replace("Hello","Hi"))


#21. Split the string using specific
print(str3.split(" "))

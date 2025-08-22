# break the loop as soon it sees 'e'
# or 's'
i = 0
str = "geeksforgeeks"

while i < len(str):
    if str[i] == "s" or str[i] == "f":
        i += 1
        break
        
    print(str[i])
    i += 1
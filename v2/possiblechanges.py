# def possibleChanges(usernames):
#     # Write your code here
        
#     result = []
    
#     for i in usernames:
#         min = 0
        
#         for y in i:
#             for z in i:
#                 if (ord(y) == ord(z)):
#                     continue
#                 elif ord(y) > ord(z) and i.index(y) < i.index(z):
#                     min = ord(z)
            
#         if (min > 0):
#             result.append("YES")
#         else:
#             result.append("NO")
        
#         min = 0
            
#     return result



# Optimized code
def possibleChanges(usernames):
    # List to store results for each username
    result = []
    
    for username in usernames:
        can_change = False
        min_char = username[-1]  # Start with the last character
        
        # Iterate from the second last character to the first character
        for i in range(len(username) - 2, -1, -1):
            if username[i] > min_char:
                # Found a character that is larger than a character after it
                can_change = True
                break
            # Update the minimum character encountered so far
            min_char = min(min_char, username[i])
        
        # Append result based on whether a change is possible
        if can_change:
            result.append("YES")
        else:
            result.append("NO")
    
    return result

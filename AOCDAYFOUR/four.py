
# --- Day 4: The Ideal Stocking Stuffer ---

# Example Input : abcdef  Answer : 609043
# Example Input 2: pqrstuv Answer : 1048970

# Puzzle Input : iwrupvqb

import hashlib


# Part 1: First 5 Zeroes
def generate_hash():
    stringhash = "iwrupvqb"
    found = False 
    i = 0
    while found == False:
        i+=1
        print(stringhash + str(i))
        teststring = stringhash + str(i)
        
        result = hashlib.md5(teststring.encode())
        testhash = result.hexdigest() 
        print(testhash)
        
        
        # We need to Check for leading zeroes (Atleast 5)
        # Changed [:5] -> [:6], looking for 6 zeroes in P2
        first_five = testhash[:6]
        # print(type(first_five))
        print(first_five)
        leading_zeroes = "000000"
        if first_five == leading_zeroes:
            found = True
            break
        else:
            found = False
        
    new_string = stringhash + str(i)
    print(new_string)
    return i
 
print(generate_hash())









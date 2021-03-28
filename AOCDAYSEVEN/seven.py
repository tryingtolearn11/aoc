
# --- Day 7: Some Assembly Required ---



# work with the example for now 
'''     
    # example circuit
    x = 123
    y = 456
    d = x & y
    e = x | y
    f = x << 2
    g = y >> 2
    h = (2**16) - x-1
    i = (2**16) - y-1 
    
    test = "123 -> x"
    print(test[::-1])


    print("d: ", d) 
    print("e: ", e) 
    print("f: ", f) 
    print("g: ", g) 
    print("h: ", h) 
    print("i: ", i) 
    print("x: ", x) 
    print("y: ", y)
'''

def p1(f):
    # create hash table to store wires
    ciruit = {}
    data = [line for line in f.read().splitlines()]
    
    for i in data:
        ciruit['{}'.format(i.split("->")[-1].replace(" ", ""))] = i
    # print(ciruit)

   

    



p1(f=open("input.txt", "r"))

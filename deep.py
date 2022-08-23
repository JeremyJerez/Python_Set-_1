#Problem Set 1
"""
A series of exercises for CS50 hands-on projects
this it's my approach on the Deep Thought problem
"""
x = input("what is the answer to the Great Question of Life, the Universe and Everything? ")
# an option looking for equality      x = int(x)
x = x.strip()
if x == "42": 
    print("yes")
elif x.lower() == "forty-two":
    print("yes")
elif x.lower() == "forty two":
    print("yes")    
else:
    print("no")

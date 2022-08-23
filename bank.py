#Problem set 01
"""
this it's my solution to the Home Federal Savings Bank problem
"""
x = input("Greeting: ")
x = x.strip().lower()
if "hello" in x:
    print("$0")
elif "h" == x[0]:
    print("$20")
else:
    print("$100")

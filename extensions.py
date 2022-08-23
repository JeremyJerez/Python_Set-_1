#Problem set 01
"""
this it's my solution to the file extensions problem
it might require to add more filetypes...
"""
x = input("File name: ")
x = x.strip().lower()
if ".jpg" in x:
    print("image/jpeg")
elif ".pdf" in x:
    print("application/pdf")
else:
    print("appliccation/octet-stream")

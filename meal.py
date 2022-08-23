#Problem set 01
"""
this it's my solution to the meal time problem
"""
def main():
    x = input("what time is it? ")
    time = convert(x)
    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
    elif time >= 18.0 and time <= 19.0:
        print("dinner time")

            
def convert(time):
    hours, minutes = time.split(":")
    new_minute = float(minutes) / 60 #to make minutes a decimal
    return float(hours) + new_minute

main()

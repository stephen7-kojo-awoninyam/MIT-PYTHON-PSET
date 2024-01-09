import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    
    if Match := re.match(r"^((?:[1-9]|1[0-2]):?(?:[0-5][0-9])? ?(?:AM|PM)) to ((?:[1-9]|1[0-2]):?(?:[0-5][0-9])?) ?(?:PM|AM)$",s):
        morn = Match.group(1)
        even = Match.group(2)
        if "PM" in morn :
            morn = morn.replace("PM","")
            if ":" in morn:
                hour,minute = morn.split(":")

                hour = int(hour)

                hour = hour + 12

                return f"{hour}:{minute} to {'0'+even}"
            else:
                morn = int(morn)
                morn = morn + 12
                return f"{morn}:00 to {'0'+even}:00"
        else:
            morn = morn.replace("AM","")
            
            if  ":" in even:
                hour,minute = even.split(":")

                hour = int(hour)

                hour = hour + 12

                return f"{'0'+morn} to {hour}:{minute}"
            else:

                even = int(even)

                even = even + 12

                return f"{'0'+morn}:00 to {even}:00"

    else:

        raise ValueError   
       

if __name__ == "__main__":
    main()
 
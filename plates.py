import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #  CHECK IF THE LENGTH OF THE STRING IS LESS THAN 2 AND GREATER THAN 6 AND RETURN FALSE
    if len(s) > 6 or len(s) < 2:
        return False
    # CHECK IF THE FIRST TWO LETTERS OF THE STRING IS NOT ALPHABET AND RETURN FALSE
    elif not (s[0].isalpha() and s[1].isalpha()):
        return False
    
    # ASSIGNING A DEFAULT VALUE TO INITIALISE THE VARIABLE
    first_num = 0
    # LOOP THROUGH THE STRING
    for char in s:
        # IF THE CHARACTERS CONTAIN A PUNCTUATION MARK, RETURN FALSE
        if char in string.punctuation:
            return False
        #  IF IT IS A NUMBER 
        if char.isnumeric():
            # AND THE NUMBER IS ZERO RETURN FALSE
            if char == "0":
                return False
            # ELSE OTHERTHAN ZERO ASSIGN THE INDEX OF THAT NUMBER TO THE VARIABLE AND BREAK
            first_num = s.index(char)
            break
    #  LOOP THROUGH THE STRING AGAIN
    for char in s:
        # IF THE CHARACTER'S INDEX IS LESS THAN THE INDEX OF THE FIRST NUMBER DONT TAKE ANY ACTION
        if s.index(char) <= first_num:
            pass
        else:
            #  IF OTHERWISE CHECK IF IT CONTAINS PUNCTUATION, RETURN FALSE
             if char in string.punctuation:
                 return False
            # AND IF ANY CHARACTER APPEAR AFTER THE NUMBER RETURN FALSE
             if char.isalpha():
                 return False
    #  AFTER SUCCESSFUL EXECUTION RETURN TRUE 
    return True                    


if __name__== "__main__":
      main()
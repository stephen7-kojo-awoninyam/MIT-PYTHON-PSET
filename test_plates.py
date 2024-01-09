from plates import is_valid

def test_is_valid():
    try:
        assert is_valid("HELLO") == True

        assert is_valid("HELLO, WORID") == False

        assert is_valid("GOODBYE")  == False

        assert is_valid("CS50") == True

        assert is_valid("CS05") == True

        assert is_valid("50") == True
    except AssertionError:
            print("function does not work appropriately")    
 
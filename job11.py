

def check_E_char(string):
    if 'e' in string:
        return True
    else:
        return False
while True:
    input_string = input("Enter a string: ")
    if check_E_char(input_string):
        print("The string contains the character 'E'.")
        break
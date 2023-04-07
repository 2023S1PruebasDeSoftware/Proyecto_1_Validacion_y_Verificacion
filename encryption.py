def encryption(message, mode):
    result = ""
    key = 30

    # Ensure key is within range
    key = key % 26

    # Iterate through each character in the message
    for char in message:
        if char.isalpha():
            # Determine the ASCII code for the character
            code = ord(char)

            # Shift the code by the key value
            if mode == "encrypt":
                code += key
            elif mode == "decrypt":
                code -= key

            # Ensure the code is within the range of A-Z or a-z
            if char.isupper():
                if code > ord("Z"):
                    code -= 26
                elif code < ord("A"):
                    code += 26
            elif char.islower():
                if code > ord("z"):
                    code -= 26
                elif code < ord("a"):
                    code += 26

            # Convert the new code to a character and add it to the result string
            result += chr(code)
        else:
            # Non-alphabetic characters are added to the result string as-is
            result += char

    return result

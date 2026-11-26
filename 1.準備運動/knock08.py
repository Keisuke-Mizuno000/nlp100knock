def cipher(text):
    result = ""

    for char in text:
        if char.islower():
            result += chr(219 - ord(char))
        else:
            result += char

    return result

message = "I am a student."

encrypted = cipher(message)
print("暗号化:", encrypted)

decrypted = cipher(encrypted)
print("復号化:", decrypted)
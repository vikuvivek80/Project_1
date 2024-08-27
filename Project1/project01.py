def encrypt_caesar_cipher(plaintext, shift):
encrypted_text = ""
for char in plaintext:
if char.isalpha():
shift_amount = shift % 26
shifted_char = chr((ord(char) + shift_amount - 65) % 26 + 65)
if char.isupper() else chr((ord(char) + shift_amount - 97) % 26 + 97)
encrypted_text += shifted_char
else:
encrypted_text += char
return encrypted_text
def decrypt_caesar_cipher(encrypted_text, shift):
return encrypt_caesar_cipher(encrypted_text, -shift)
def main():
print("Welcome to the Caesar Cipher Project!")
while True:
choice = input("Do you want to (E)ncrypt or (D)ecrypt a
message? (Q to quit): ").upper()
if choice == 'Q':
print("Goodbye!")
break
elif choice not in ['E', 'D']:
print("Invalid choice. Please choose E to encrypt, D to
decrypt, or Q to quit.")
continue
message = input("Enter your message: ")
shift = int(input("Enter the shift value: "))
if choice == 'E':
encrypted_message = encrypt_caesar_cipher(message, shift)
print(f"Encrypted message: {encrypted_message}")
else:
decrypted_message = decrypt_caesar_cipher(message, shift)
print(f"Decrypted message: {decrypted_message}")
if __name__ == "__main__":
main()
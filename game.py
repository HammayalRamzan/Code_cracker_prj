import streamlit as st

st.title("🕵️‍♂️ Secret Agent's Code Crack 🤫")
st.write("Welcome to the Code Cracker! Enter a cipher text and let's decode it 🎯")
# Add cipher selection
cipher_type = st.selectbox(
    "Select Cipher Type:",
    ["Caesar Cipher", "Vigenère Cipher"]
)

cipher_text = st.text_input("Enter your cipher text:")


# Add specific inputs based on cipher type
if cipher_type == "Caesar Cipher":
    shift = st.slider("Shift value", 1, 25, 3)
else:
    key = st.text_input("Enter Vigenère key (letters only):")

# Add Vigenère Cipher implementation
def vigenere_decrypt(text, key):
    if not key.isalpha():
        return "Error: Key must contain only letters"
    
    key = key.upper()
    decrypted_text = ""
    key_length = len(key)
    key_as_int = [ord(i) - ord('A') for i in key]
    key_index = 0
    
    for char in text:
        if char.isalpha():
            # Determine the shift based on the key character
            shift = key_as_int[key_index % key_length]
            # Get the proper base (uppercase or lowercase)
            shift_base = ord('A') if char.isupper() else ord('a')
            # Decrypt the character
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text

def caesar_cipher_decrypt(text, shift):
    """
    Decrypt a Caesar cipher text with the given shift value.
    """
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift the character back by the shift amount
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            # Keep non-alphabetic characters unchanged
            decrypted_text += char
    return decrypted_text

if st.button("Crack the Code"):
    if cipher_text:
        st.write("🔓 Decryption in progress...✅")
        
        if cipher_type == "Caesar Cipher":
            result = caesar_cipher_decrypt(cipher_text, shift)
            st.success(f"Decrypted text (shift={shift}): {result}")
        else:
            if key:
                result = vigenere_decrypt(cipher_text, key)
                st.success(f"Decrypted text (key='{key}'): {result}")
            else:
                st.error("Please enter a key for Vigenère cipher")
    else:
        st.error("Please enter some text to decrypt ⚠")

# Add explanation section
with st.expander("How it works?"):
    if cipher_type == "Caesar Cipher":
        st.write("""
        The Caesar cipher is a simple substitution cipher that shifts each letter in the plaintext by a fixed number of positions in the alphabet.
        For example, with a shift of 3:
        - A → D
        - B → E
        - C → F
        And so on...
        """)
    else:
        st.write("""
        The Vigenère cipher is a polyalphabetic substitution cipher that uses a keyword to determine the shift for each letter in the plaintext.
        The keyword is repeated to match the length of the plaintext, and each letter in the keyword determines the shift for the corresponding letter in the plaintext.
        """)
    
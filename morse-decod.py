# Dictionnaire de correspondance du code morse
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', 
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', 
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', 
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', 
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', 
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', 
    '----.': '9', '/': ' '  # L'espace est représenté par un slash "/"
}

def decode_morse(morse_code):
    """Décode un message en code morse"""
    words = morse_code.split(' / ')  # Chaque mot est séparé par " / "
    decoded_message = ''
    
    for word in words:
        # Décoder chaque lettre
        letters = word.split(' ')  # Séparation des lettres dans le mot
        decoded_word = ''.join([MORSE_CODE_DICT[letter] for letter in letters if letter in MORSE_CODE_DICT])
        decoded_message += decoded_word + ' '
    
    return decoded_message.strip()

# Exemple de message morse à décoder
morse_message = "…. .. –..– / — …. .- -. -.- … / — — / … .- — ..- . .-.. / — — .-. … . / — …. . / — .-. .- -. … — .. … … .. — -. / — ..-. / — . .-.. . –. .-. .- .--. .... .. -.-. / .. -. ..-. — .-. — .- — .. — -. / .– .- … / … — .- -. -.. .- .-. -.. .. –.. . -.. .-.-.-"
decoded_message = decode_morse(morse_message)
print(f"Message décodé : {decoded_message}")

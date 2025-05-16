def rot_n(message, n):
    """Applique un décalage ROT de n caractères à chaque lettre du message."""
    decrypted = ""
    for char in message:
        if 'A' <= char <= 'Z':  # Lettres majuscules
            decrypted += chr((ord(char) - ord('A') - n) % 26 + ord('A'))
        elif 'a' <= char <= 'z':  # Lettres minuscules
            decrypted += chr((ord(char) - ord('a') - n) % 26 + ord('a'))
        else:
            decrypted += char  # Garder les autres caractères intacts
    return decrypted

def test_all_rot(message):
    """Teste tous les décalages ROT (1 à 25) et affiche les résultats possibles."""
    for i in range(1, 26):
        decrypted_message = rot_n(message, i)
        print(f"ROT-{i} : {decrypted_message}")

# Exemple de message chiffré (remplace ceci par ton propre message)
message_chiffre = "Aipgsqi fego, xlmw pizip mw rsx ew iewc ew xli pewx fyx wxmpp rsx xss gleppirkmrk. Ws ks elieh erh irxiv xlmw teww: wlmjxxlexpixxiv"

print("Test des décalages ROT possibles :")
test_all_rot(message_chiffre)

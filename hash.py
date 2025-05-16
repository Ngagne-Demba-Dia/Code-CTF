def cesar_decrypt(message, shift):
    """Déchiffre un message avec un chiffrement César en utilisant un décalage donné."""
    decrypted = ""
    for char in message:
        if 'A' <= char <= 'Z':  # Pour les lettres majuscules
            decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif 'a' <= char <= 'z':  # Pour les lettres minuscules
            decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted += char  # Laisser les autres caractères inchangés
    return decrypted

def test_all_shifts(message):
    """Teste tous les décalages (1 à 25) pour le chiffrement César et affiche les résultats."""
    for shift in range(1, 26):
        decrypted_message = cesar_decrypt(message, shift)
        print(f"Shift {shift}: {decrypted_message}")

# Message chiffré à tester
message_chiffre = "Ayowe awxewr nwaalfw die tiy rgw fklf ua xgixiklrw ! Tiy lew qwkxinw."

# Tester tous les décalages possibles
test_all_shifts(message_chiffre)

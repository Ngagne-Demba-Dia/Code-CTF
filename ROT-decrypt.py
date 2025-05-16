def reverse_text(text):
    """
    Renverse la chaîne de caractères lettre par lettre.
    Exemple : "ABC" -> "CBA"
    """
    return text[::-1]

def reverse_words(text):
    """
    Renverse l'ordre des mots dans le texte.
    Exemple : "Hello world" -> "world Hello"
    """
    words = text.split()
    return " ".join(words[::-1])

# Le texte chiffré par inversion
cipher_text = ("qoymlNlpY :ccdf lpy yzJ .qoh ln lxigqoh qlxlm eeiw zot ydpy gmipylnoC ,zot gmiyqdncyzo ho ydpy ci lniqk tN .lsie sooe tlpy ydpw yom ,smipy amd tdc tlpy ydpw tj lefolf gmigazb ho ydpy ci lniqk tN .tyicoiqzk ho ydpy ci lniqk tN .edminiqk d nd i clT")

# Inversion lettre par lettre
reversed_by_letter = reverse_text(cipher_text)
print("Texte inversé lettre par lettre:")
print(reversed_by_letter)

print("\n------------------------\n")

# Inversion mot par mot
reversed_by_words = reverse_words(cipher_text)
print("Texte inversé mot par mot:")
print(reversed_by_words)


# def reverse_letters(text):
#     """Inverse l'ordre de tous les caractères du texte."""
#     return text[::-1]

# def reverse_words(text):
#     """Inverse l'ordre des mots tout en conservant leur orthographe."""
#     words = text.split()
#     return " ".join(words[::-1])

# # Ton texte chiffré par inversion
# cipher_text = ("qoymlNlpY :ccdf lpy yzJ .qoh ln lxigqoh qlxlm eeiw zot ydpy gmipylnoC ,zot gmiyqdncyzo ho ydpy ci lniqk tN .lsie sooe tlpy ydpw yom ,smipy amd tdc tlpy ydpw tj lefolf gmigazb ho ydpy ci lniqk tN .tyicoiqzk ho ydpy ci lniqk tN .edminiqk d nd i clT")

# # 1. Inversion complète (caractère par caractère)
# reversed_by_letters = reverse_letters(cipher_text)
# print("🔄 Texte inversé lettre par lettre:")
# print(reversed_by_letters)

# print("\n------------------------\n")

# # 2. Inversion des mots (chaque mot reste lisible)
# reversed_by_words = reverse_words(cipher_text)
# print("🔄 Texte inversé mot par mot:")
# print(reversed_by_words)

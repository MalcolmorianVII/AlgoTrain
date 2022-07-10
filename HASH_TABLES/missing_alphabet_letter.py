import string
def find_missing_alpha_letter(str):
    string_dict = {key:True for key in str}
    alphabet = string.ascii_lowercase

    for letter in alphabet:
        if not string_dict.get(letter):
            return letter

print(find_missing_alpha_letter("the quick brown box jumps over a lazy dog"))
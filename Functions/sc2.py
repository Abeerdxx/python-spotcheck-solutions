def remove_letter_from_text(text, letter):
    return filter(lambda c: c != letter, text)


def encode_text(text):
    return "-".join(map(lambda c: str(ord(c)), text))


def show_encoded_filter(text, letter):
    updated_text = remove_letter_from_text(text, letter)
    print("Updated text is " + updated_text)

    encrypted_text = encode_text(updated_text)
    print("Encrypted text is " + encrypted_text)


show_encoded_filter("sinusitis", "s")

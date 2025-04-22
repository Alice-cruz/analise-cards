def get_card_type(card_number):
    card_number = card_number.replace(" ", "")  # remove os espaços

    # lista das bandeiras
    card_types = {
        "MasterCard": {"prefixes": ["51", "52", "53", "54", "55"], "lengths": [16]},
        "Visa": {"prefixes": ["4"], "lengths": [13, 16, 19]},
        "American Express": {"prefixes": ["34", "37"], "lengths": [15]},
        "Diners Club": {"prefixes": ["36", "38"], "lengths": [14]},
        "Discover": {"prefixes": ["6011", "65"], "lengths": [16]},
        "enRoute": {"prefixes": ["2014", "2149"], "lengths": [15]},
        "JCB": {"prefixes": ["35"], "lengths": [16, 19]},
        "Voyager": {"prefixes": ["8699"], "lengths": [15]},
        "HiperCard": {"prefixes": ["38", "60"], "lengths": [13, 16, 19]},
        "Aura": {"prefixes": ["50"], "lengths": [16]},
    }

    # checa se bate e eh valido
    for card_type, details in card_types.items():
        prefixes = details["prefixes"]
        lengths = details["lengths"]

        if any(card_number.startswith(prefix) for prefix in prefixes) and len(card_number) in lengths:
            return card_type

    return "Unknown Card Type"


# Inputa o numero
card_number = input("Enter your credit card number: ")
card_type = get_card_type(card_number)
print(f"The card type is: {card_type}")
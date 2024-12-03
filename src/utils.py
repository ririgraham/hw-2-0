from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Transforming card number into str type"""
    card_number = str(card_number)
    """Formatting the card number"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
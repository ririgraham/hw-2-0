from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Transforming card number into str type"""
    card_number = str(card_number)
    """Formatting the card number"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Transforming account number into str type"""
    account_number = str(account_number)
    """Formatting the account number"""
    return f"**{account_number[-4:]}"


if __name__ == '__main__':
    print(get_mask_card_number('7000792289606361'))
    print(get_mask_account(73654108430135874305))

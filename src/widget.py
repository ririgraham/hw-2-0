import re
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Defining regex for cards and accounts"""
    card_pattern = r"(Visa|Visa Platinum|MasterCard|Maestro)[^0-9]*(\d{16})"
    account_pattern = r"(Счет)\s*(\d{20})"
    """Importing masking functions"""

    """Checking if input equals card regex"""
    card_match = re.search(card_pattern, data)
    if card_match:
        card_type = card_match.group(1)
        card_number = card_match.group(2)
        masked_card = get_mask_card_number(int(card_number))
        return f"{card_type} {masked_card}"
    """Checking if input equals account regex"""
    account_match = re.search(account_pattern, data)
    if account_match:
        account_type = account_match.group(1)
        account_number = account_match.group(2)
        masked_account = get_mask_account(int(account_number))
        return f"{account_type} {masked_account}"

    return "Incorrect Input"


def get_date(date_str: str) -> str:
    """Splitting string by year, month and day"""
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")

    """Returning date in the right format"""
    return f"{day}.{month}.{year}"


test_data = [
    "Visa Platinum 7000792289606361",
    "Maestro 1596837868705199",
    "MasterCard 7158300734726758",
    "Счет 73654108430135874305",
    "Счет 64686473678894779589",
]

test_date = "2024-03-11T02:26:18.671407"
if __name__ == "__main__":
    for data in test_data:
        # print(f'Processing: {data}')
        print(mask_account_card(data))
        # print('Processed successfully')
formatted_date = get_date(test_date)
print(formatted_date)

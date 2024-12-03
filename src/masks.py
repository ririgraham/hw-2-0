from typing import Union
from src.utils import get_mask_card_number


def get_mask_account(account_number: Union[int, str]) -> str:
    """Transforming account number into str type"""
    account_number = str(account_number)
    """Formatting the account number"""
    return f"**{account_number[-4:]}"


if __name__ == '__main__':
    print(get_mask_card_number('7000792289606378'))
    print(get_mask_account(73654108430135874305))

# validator.py
def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_phone(phone: str) -> bool:
 """Валидация российского номера телефона."""
 import re
 pattern = r'^\+?7\d{10}$'
 return bool(re.match(pattern, phone.replace('-', '').replace(' ', '')))

def test_validate_phone():
 assert validate_phone("+79991234567") == True
 assert validate_phone("89991234567") == False
 assert validate_phone("+7999123") == False

def validate_inn(inn: str) -> bool:
 """TODO: валидация ИНН."""
 pass
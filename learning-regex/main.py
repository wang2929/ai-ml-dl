import re

def match_alpha_only(s: str) -> bool:
    """
    Match strings that contain only alphabetic characters (uppercase or lowercase).
    """
    # \w matches word chars, and \W matches non-word chars
    regex = r"[a-zA-Z]+"
    if re.fullmatch(regex, s): 
        return True
    return False

def match_all_lowercase(s: str) -> bool:
    """
    Match strings that contain only lowercase letters.
    """
    regex = r'[a-z]+'
    if re.fullmatch(regex, s):
        return True
    return False

def match_all_uppercase(s: str) -> bool:
    """
    Match strings that contain only uppercase letters.
    """
    regex = r'[A-Z]+'
    if re.fullmatch(regex, s):
        return True
    return False

def match_email_format(s: str) -> bool:
    """
    Match a valid email address format (e.g., example@domain.com).
    """
    regex = r'\w+@\w+\.[a-zA-z]{2,3}'
    if re.fullmatch(regex, s):
        return True
    return False

def match_us_phone(s: str) -> bool:
    """
    Match a US phone number format: 123-456-7890
    """
    regex = r'\d{3}-\d{3}-\d{4}'
    if re.fullmatch(regex, s):
        return True
    return False

def match_date_mmddyyyy(s: str) -> bool:
    """
    Match a date in the format MM/DD/YYYY.
    """
    regex = r'[0-1]\d/[0-3]\d/[0-2]\d{3}'
    if re.fullmatch(regex, s):
        arr = s.split('/')
        month = int(arr[0])
        day = int(arr[1])
        if month <= 12 and day <= 31:
            return True
    return False

def match_postal_code(s: str) -> bool:
    """
    Match a 5-digit US ZIP code.
    """
    regex = r'\d{5}'
    if re.fullmatch(regex, s):
        return True
    return False

def match_hex_color(s: str) -> bool:
    """
    Match a hex color code (e.g., #FFF or #FFFFFF).
    """
    regex = r'#([\da-fA-F]{6}|[\da-fA-F]{3})'
    if re.fullmatch(regex, s):
        return True
    return False

def match_time_24h(s: str) -> bool:
    """
    Match a time in 24-hour format (e.g., 14:30).
    """
    regex = r'[0-2][0-9]:[0-5][0-9]'
    if re.fullmatch(regex, s):
        arr = s.split(':')
        if int(arr[0]) < 24 and int(arr[1]) < 60:
            return True
    return False

def match_valid_username(s: str) -> bool:
    """
    Match a username that contains only letters, numbers, and underscores, and is 3–16 characters long.
    """
    regex = r'\w{3,16}'
    if re.fullmatch(regex, s):
        return True
    return False

def match_url(s: str) -> bool:
    """
    Match a simple HTTP or HTTPS URL.
    """
    regex = r'^(http|https)://[a-zA-Z.]+\.[a-zA-z]{2,3}'
    if re.fullmatch(regex, s):
        return True
    return False

def match_credit_card(s: str) -> bool:
    """
    Match a credit card number format: 4 groups of 4 digits separated by spaces or hyphens.
    """
    regex = r'[0-9]{4}(\s|-)[0-9]{4}(\s|-)[0-9]{4}(\s|-)[0-9]{4}'
    if re.fullmatch(regex, s):
        return True
    return False

def match_hashtag(s: str) -> bool:
    """
    Match a valid hashtag that begins with # and is followed by alphanumeric characters.
    """
    regex = r'#[0-9a-zA-Z]+'
    if re.fullmatch(regex, s):
        return True
    return False

def match_ip_address(s: str) -> bool:
    """
    Match a valid IPv4 address.
    """
    regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    if re.fullmatch(regex, s):
        arr = s.split('.')
        if int(arr[0]) <= 255 and int(arr[1]) <= 255 and int(arr[2]) <= 255 and int(arr[3]) <= 255:
            return True
    return False

def match_strong_password(s: str) -> bool:
    """
    Match a strong password (at least 8 characters, one uppercase, one lowercase, one digit, and one special character).
    """
    regex = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^a-zA-Z\d]).{8,}'
    if re.fullmatch(regex, s):
        return True
    return False

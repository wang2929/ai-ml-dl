import pytest
from main import *

def test_match_alpha_only():
    assert match_alpha_only("HelloWorld") == True
    assert match_alpha_only("Hello123") == False
    assert match_alpha_only("!") == False

def test_match_all_lowercase():
    assert match_all_lowercase("hello") == True
    assert match_all_lowercase("Hello") == False
    assert match_all_lowercase("hello123") == False

def test_match_all_uppercase():
    assert match_all_uppercase("HELLO") == True
    assert match_all_uppercase("Hello") == False
    assert match_all_uppercase("123") == False

def test_match_email_format():
    assert match_email_format("user@example.com") == True
    assert match_email_format("user@.com") == False
    assert match_email_format("userexample.com") == False

def test_match_us_phone():
    assert match_us_phone("123-456-7890") == True
    assert match_us_phone("1234567890") == False
    assert match_us_phone("123-45-6789") == False

def test_match_date_mmddyyyy():
    assert match_date_mmddyyyy("12/31/2022") == True
    assert match_date_mmddyyyy("31/12/2022") == False
    assert match_date_mmddyyyy("12-31-2022") == False

def test_match_postal_code():
    assert match_postal_code("90210") == True
    assert match_postal_code("9021") == False
    assert match_postal_code("90210-1234") == False

def test_match_hex_color():
    assert match_hex_color("#FFF") == True
    assert match_hex_color("#ffffff") == True
    assert match_hex_color("123456") == False

def test_match_time_24h():
    assert match_time_24h("23:59") == True
    assert match_time_24h("12:60") == False
    assert match_time_24h("24:00") == False

def test_match_valid_username():
    assert match_valid_username("user_123") == True
    assert match_valid_username("us") == False
    assert match_valid_username("user@name") == False

def test_match_url():
    assert match_url("http://example.com") == True
    assert match_url("https://example.com") == True
    assert match_url("ftp://example.com") == False

def test_match_credit_card():
    assert match_credit_card("1234 5678 9012 3456") == True
    assert match_credit_card("1234-5678-9012-3456") == True
    assert match_credit_card("1234567890123456") == False

def test_match_hashtag():
    assert match_hashtag("#hello") == True
    assert match_hashtag("#123abc") == True
    assert match_hashtag("hello") == False

def test_match_ip_address():
    assert match_ip_address("192.168.1.1") == True
    assert match_ip_address("256.256.256.256") == False
    assert match_ip_address("192.168.1") == False

def test_match_strong_password():
    assert match_strong_password("Str0ng!Pass") == True
    assert match_strong_password("weakpass") == False
    assert match_strong_password("StrongPass") == False

import requests
import random as rnd
import re
import os

def fetch_words():
    # url = f"https://raw.githubusercontent.com/hingston/russian/refs/heads/master/10000-russian-words-cyrillic-only.txt" -- not really accurate words, use when ather ling is down
    url = f"http://dict.ruslang.ru/freq.php?act=show&dic=freq_s&title=%D7%E0%F1%F2%EE%F2%ED%FB%E9%20%F1%EF%E8%F1%EE%EA%20%E8%EC%E5%ED%20%F1%F3%F9%E5%F1%F2%E2%E8%F2%E5%EB%FC%ED%FB%F5"
    req = requests.get(url)
    pattern = r'<td>([А-Яа-яЁё]+)<\/td>'
    words = re.findall(pattern, req.text)
    cache_words(words)
    return words

def cache_words(content):
    with open('russian_words.txt', 'w',  encoding="utf-8") as f:
        content = ' '.join(content)
        f.write(content)

def get_words_from_cache(txt_path):
    with open(txt_path, 'r', encoding="utf-8") as f:
        content = f.read()
    return content.split()

def get_list():
    txt_path = 'russian_words.txt'
    if os.path.isfile(txt_path):
        words = get_words_from_cache(txt_path)
    else:
        words = fetch_words()
    return [word for word in words if len(word) > 5]

def random_word():
    return rnd.choice(get_list()) 
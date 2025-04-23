# categorizer.py

from config import CATEGORIES
from utils.cleaner import clean_text


def categorize_ad(ad):
    matched = set()
    content = clean_text(ad['title'] + " " + ad['description'] + " " + " ".join(ad['keywords']))

    for category, keywords in CATEGORIES.items():
        if any(kw in content for kw in keywords):
            matched.add(category)

    return list(matched)

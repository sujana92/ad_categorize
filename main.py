# main.py

import csv
import json
from categorizer import categorize_ad
from utils.logger import setup_logger

INPUT_FILE = "dataAds.csv"
OUTPUT_FILE = "output/categorized_ads.json"


def load_ads(file_path):
    ads = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ads.append({
                "title": row["title"],
                "description": row["description"],
                "keywords": [kw.strip() for kw in row["keywords"].split(",")]
            })
    return ads


def save_output(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    logger = setup_logger()

    logger.info("Starting ad categorization process.")
    ads = load_ads(INPUT_FILE)

    for ad in ads:
        ad["categories"] = categorize_ad(ad)
        logger.info(f"Categorized ad: {ad['title']} -> {ad['categories']}")

    save_output(ads, OUTPUT_FILE)
    logger.info("Ad categorization complete. Output saved to JSON.")

#  Ad Categorization & Labeling Workflow

This Python-based tool performs automated categorization of advertisements using keyword-based matching. It is built with a modular structure for easy maintenance and future enhancements (like ML integration or web deployment).

---

## Features

-  Reads ad metadata from CSV
- Cleans and preprocesses ad text
- Classifies ads based on predefined categories
- Outputs results as a formatted JSON file
- Logs each step to a log file
- Configurable and extendable structure

---

## 📁 Project Structure

ad_categorization/ 
     ├── data/
     │      └── ads.csv 
 #Input CSV with ad metadata 
     ├── output/  
     │     └── categorized_ads.json 
#Output JSON file 
     ├── logs/ 
     │     └── run.log 
#Log file for process tracking 
     ├── utils/ 
     │     ├── cleaner.py  
#Text preprocessing 
     │     └── logger.py 
#Logger setup 
 ├── categorizer.py  
#Categorization logic
 ├── config.py  
#Category-keyword config 
 └── main.py 


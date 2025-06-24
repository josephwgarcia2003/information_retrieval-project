# KSU Web Information Retrieval Project

This Web scraping and text analysis project was developed for the **CS4422 Information Retrieval** course at Kennesaw State University. It demonstrates web scraping, email extraction, and text analysis and visualization on real-world web content using Python.

---

## Project Overview

I built a Scrapy-based crawler to fetch and analyze pages from the `kennesaw.edu` domain. After extracting raw page text, I performed tokenization, stopword removal, and statistical analysis to explore vocabulary distribution and identify patterns such as Zipf’s Law.

---

## Project Structure

```
information_retrieval-project/
├── scraper/
│ └── ksu_spider.py # Scrapy spider
├── analysis/
│ ├── test.py # Email stats and token count
│ ├── word_freq.py # Word frequency before cleanup + Zipf plot
│ ├── stopwords_removed.py # Word frequency after cleanup
│ ├── word_freq_before.png # Frequency vs. rank (linear)
│ └── word_freq_before_loglog.png # Log-log Zipf plot
├── data/
│ └── ksu1000_sample.json # 50-page sample of crawled data
├── report.pdf # Final report for class submission
├── requirements.txt # Python dependencies
└── README.md # You're reading it
```

---

## Technologies Used

- Python
- Scrapy
- BeautifulSoup
- NLTK
- Matplotlib
- JSON

---

## Project Features

- Crawls Kennesaw State University pages using Scrapy
- Extracts page title, body text, and email addresses
- Identifies frequency of email addresses and common terms
- Removes stopwords and punctuation for clean vocabulary stats
- Plots word frequency distributions before and after cleanup
- Demonstrates Zipf's Law in web content

---

## Sample Output

### Email Stats:
- ~851 pages crawled
- % of pages with email addresses: XX%
- Top 10 email addresses extracted from real KSU domains

### Vocabulary Analysis:
- Top 30 most common words before cleanup
- Top 30 words after stopword + punctuation removal
- Visualized word distributions using log-log plots

---

## How to Run the Code

1. Clone this repository or download the ZIP
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run analysis scripts:
    - Run email and token statistics:
      ```bash
      python analysis/test.py
      ```
    - Run word frequency + plot (before cleanup):
      ```bash
      python analysis/word_freq.py
      ```
    - Run word frequency (after removing stopwords):
      ```bash
      python analysis/stopwords_removed.py
      ```


> ⚠️ Note: The full `ksu1000.json` dataset is not uploaded due to size. Instead, a `ksu1000_sample.json` with 50 pages is provided for demonstration.

---

## Contact

Built by **Joseph Garcia** for CS4422 @ Kennesaw State University.

Feel free to connect on [LinkedIn](https://www.linkedin.com/in/josephgarcia03) or reach out with questions.


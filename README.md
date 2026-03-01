# web-scraper-project
**Please note that this project has been created solely for academic evaluation and educational purposes within the scope of my university studies. It is a conceptual demonstration intended to fulfill specific learning objectives and should not be interpreted as a finished, market-ready, or production-ready product.

#  Web Scraping for Data Collection
### University Project 3 — Στέργιος Μουτζίκος 

A Python desktop application that scrapes websites, extracts key statistics, saves results to CSV, and visualizes the data in a bar chart — all through a clean GUI built with `tkinter`.

---

##  Preview

| GUI Input | Output Chart |
|-----------|-------------|
| Enter any URL and click **Retrieve Website Data** | Bar chart showing words, unique words, hyperlinks & images |

---

##  Features

-  **Web Scraping** — Fetches and parses any public webpage using `requests` + `BeautifulSoup`
-  **Data Extraction** — Collects word count, unique words, hyperlinks, images, title, description, and readability score
-  **CSV Export** — Saves all scraped data automatically to `website_data.csv`
-  **Visualization** — Displays an interactive bar chart of the extracted statistics
-  **GUI** — Simple, user-friendly interface built with `tkinter` and `ttk`

---

##  Tech Stack

| Library | Purpose |
|---|---|
| `tkinter` / `ttk` | GUI and styled widgets |
| `requests` | HTTP GET requests |
| `BeautifulSoup4` | HTML parsing |
| `matplotlib` | Data visualization |
| `textstat` | Flesch Reading Ease score |
| `csv` | Saving data to CSV files |

---

##  Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/web-scraper-project.git
cd web-scraper-project
```

### 2. (Optional) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

##  Usage

```bash
python inf2021149_Project_3.py
```

1. The GUI window will open
2. Paste any website URL (e.g. `https://en.wikipedia.org/wiki/Greece`)
3. Click **Retrieve Website Data**
4. A success message will confirm the CSV was saved
5. A bar chart will display the scraped statistics

---

##  Project Structure

```
web-scraper-project3/
│
├── inf2021149_Project_3.py   # Main application
├── requirements.txt           # Python dependencies
├── website_data.csv           # Output file (auto-generated on run)
├── Project_3_report.pdf       # Full project report (Greek)
└── README.md                  # You are here
```

---

##  requirements.txt

```
requests
beautifulsoup4
matplotlib
textstat
```

> `tkinter` and `csv` are part of Python's standard library — no installation needed.

---

##  Example URLs Tested

- `https://en.wikipedia.org/wiki/Greece`
- `https://www.bbc.com/weather`
- `https://blog.hubspot.com/sales/famous-quotes`
- `https://www.naftemporiki.gr/`

---

##  Report

The full project documentation (in Greek) is included as [`Project_3_report.pdf`](./Project_3_report.pdf), covering:
- Library explanations
- Function-by-function code walkthrough
- GUI screenshots and sample output chart

---

##  Author

**Στέργιος Μουτζίκος** 
University Project · Web Scraping for Data Collection

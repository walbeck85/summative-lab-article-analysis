# Summative Lab: Analyze a News Article

## Project Description
This project is the **Summative Lab** for *Flatiron School - Course 6: Python for Software Engineering*.  
The lab focuses on applying Python fundamentals (functions, loops, conditionals, regex, and file handling) to analyze a news article.

The program reads from `article.txt` and performs text analysis tasks, demonstrating practical Natural Language Processing (NLP) basics.

---

## Features
- **Count Specific Word**  
  Counts how many times a given word appears in the text (case-insensitive).

- **Identify Most Common Word**  
  Finds the most frequent word in the text using `collections.Counter`.

- **Calculate Average Word Length**  
  Computes the average length of words, excluding punctuation.

- **Count Paragraphs**  
  Counts text blocks separated by blank lines.  
  > *Note: Section headers are included as paragraphs, per instructions.*

- **Count Sentences**  
  Counts sentences based on `.`, `!`, and `?`.  
  > *Note: Abbreviations like `Inc.` and `Dr.` are counted as sentences, per instructions.*

---

## Installation
Clone the repository and navigate into the project folder:

```bash
git clone git@github.com:walbeck85/summative-lab-article-analysis.git
cd summative-lab-article-analysis
```

Python 3.8+ is required. No external dependencies are needed; only Python’s standard library (`re`, `collections.Counter`) is used.

---

## Usage
Run the program:

```bash
python3 pythonAssessment.py
```

You’ll be presented with an interactive menu:

```
1. Count a specific word
2. Identify the most common word
3. Calculate average word length
4. Count paragraphs
5. Count sentences
6. Exit
```

Follow the prompts to analyze the provided article (`article.txt`).

---

## Rubric Mapping
This implementation satisfies the rubric requirements:

- **Substring Match – Specific Word Count** → `count_specific_word`
- **Regex Match – Identify Most Common Word** → `identify_most_common_word`
- **Substring Match – Calculate Average Word Length** → `calculate_average_word_length`
- **Substring Match – Count Paragraphs** → `count_paragraphs`
- **Substring Match – Count Sentences** → `count_sentences`
- **Conditional – While Loop** → main interactive menu
- **Conditional – For Loop** → menu input validation
- **Conditional – If/Else** → article validation and menu branching

---

## Tech Stack
- **Language:** Python 3.8+  
- **Libraries:** Standard library only (`re`, `collections.Counter`)  

---

## Author
Developed by **Will Albeck** as part of the Flatiron School Full-Stack Software Engineering Bootcamp.

---
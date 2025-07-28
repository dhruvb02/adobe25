# Adobe Hackathon 2025 – Intelligent PDF Analysis

## Overview

This repository provides a two-part Python solution for **extracting structured outlines and performing persona-driven content ranking** on PDF documents. It consists of two independent modules:

| Challenge | Folder         | Purpose                                                          |
| --------- | -------------- | ---------------------------------------------------------------- |
| 1A        | `challenge1a/` | Extracts a hierarchical outline (H1–H3) from PDF files           |
| 1B        | `challenge1b/` | Cleans, analyzes, and ranks document sections based on a persona |

---

## Challenge 1A – Hybrid Outline Extractor

**Objective:** Build a robust outline generator that detects and classifies headings (H1–H3) even in noisy or multilingual PDFs.

## How It Works
* **PDF Analysis:** Extracts built-in table of contents or creates one by analyzing text formatting
* **Title Detection:** Identifies document title from largest font text on first page
* **Pattern Recognition:** Detects headings using numbered sections (1.2.3), uppercase text, and font size
* **Smart Filtering:** Removes duplicates, page numbers, and irrelevant content
* **Hierarchy Mapping:** Assigns H1-H3 levels based on numbering depth and visual cues

## Output
Each PDF generates a JSON file in `outputs/` containing:
* **title:** Inferred document title
* **outline:** Array with `level` (H1-H3), `text`, and `page` fields
* **clean structure:** Deduplicated and properly formatted outline

## ⚙️ **How to Run**

---

### 🔹 **1️⃣ Run locally (Python)**

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Run for a single PDF:**

```bash
python final_outline.py input/yourfile.pdf
```

**OR run for all PDFs in `input/`:**

```bash
python run.py
```

---

### 🔹 **2️⃣ Build Docker Image**

```bash
docker build -t pdf-outline-extractor .
```

---

### 🔹 **3️⃣ Run with Docker**

> ⚠️ **Important:**
> If you are on **Windows**, use the **full absolute path** for `-v` mounts!
> Example:

```bash
docker run --rm ^
  -v "C:/Users/YourUser/Desktop/pdf_outline_extractor/inputs:/app/input" ^
  -v "C:/Users/YourUser/Desktop/pdf_outline_extractor/outputs:/app/output" ^
  pdf-outline-extractor
```

**Linux/Mac example:**

```bash
docker run --rm \
  -v "$PWD/inputs:/app/input" \
  -v "$PWD/outputs:/app/output" \
  pdf-outline-extractor
```
---

## Challenge 1B – Persona-Based Section Extractor

**Objective:** Extract and rank the most relevant PDF sections according to a user-defined **persona** and **task**.

### How It Works

* **PDF Processing:** Extracts and analyzes text content from multiple PDFs using PyMuPDF
* **OCR Cleaning:** Applies comprehensive text cleaning with pre-compiled fixes for common OCR errors
* **Smart Keyword Extraction:** Generates relevant keywords from persona, job description, and document filenames
* **Font-Based Analysis:** Identifies sections using font size, formatting, and visual hierarchy
* **Pattern Recognition:** Detects quality titles using linguistic patterns and content structure
* **Relevance Scoring:** Combines query matching, keyword relevance, and content quality metrics
* **TF-IDF Enhancement:** Uses machine learning for final ranking and similarity scoring

## Features
* **Dual Extraction Methods:** Font analysis (primary) with pattern-based fallback
* **Quality Filtering:** Removes irrelevant content, OCR artifacts, and low-quality sections
* **Content Optimization:** Extracts best sentences based on query relevance and information density
* **Performance Monitoring:** Tracks processing time and provides score estimation
* **Comprehensive Output:** Ranked sections with metadata and refined subsection analysis

## Input Requirements
* **input/**: Directory containing PDF files to analyze
* **persona.json**: Configuration file with persona role, job description, and document list

### Output
```json
{
  "metadata": { ... },
  "sections": [
    { "title": "Introduction", "rank": 1, "page": 2 },
    ...
  ],
  "keywords": [ ["PDF","outline"], ... ]
}
```

---

## Folder Structure

```
root/
├── challenge1a/               # Outline extraction
│   ├── process.py                # 1a-main.py core script
│   ├── requirements.txt
│   ├── input/
│   └── output/
│
├── challenge1b/               # Persona-based section extractor
│   ├── process.py             # 1b-process.py core script
│   ├── requirements.txt
│   ├── persona.json
│   ├── input/
│   └── output/
│
└── README.md                  # This file
```



> On Windows PowerShell, replace paths with `$(Get-Location)` if needed.

---

## Summary

This repository presents a comprehensive two-stage solution that connects **document organization (Challenge 1A)** with **content intelligence (Challenge 1B)**. 

The system is engineered to **perform consistently and effectively with diverse document types**, encompassing multilingual content and varying structural formats. Through intelligent scoring algorithms, standalone functionality, and flexible architecture, this toolkit provides a powerful foundation for advanced document analysis—suitable for commercial, research, and organizational use cases.

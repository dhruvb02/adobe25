## 📄 **PDF Outline Extractor**

Extracts an outline (headings + hierarchy) from PDF files and saves the result as JSON.
Runs locally **or in Docker**.

---

### ✅ **Project Structure**

```
pdf_outline_extractor/
├── Dockerfile
├── final_outline.py
├── run.py
├── requirements.txt
├── inputs/         # Put your PDF files here
├── outputs/        # JSON files will be saved here
└── README.md
```

---

## ⚙️ **How to Run**

---

### 🔹 **1️⃣ Run locally (Python)**

**Install dependencies:**

```bash
pip install -r requirements.txt
```

**Run for a single PDF:**

```bash
python final_outline.py inputs/yourfile.pdf
```

**OR run for all PDFs in `inputs/`:**

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
  -v "C:/Users/YourUser/Desktop/pdf_outline_extractor/inputs:/app/inputs" ^
  -v "C:/Users/YourUser/Desktop/pdf_outline_extractor/outputs:/app/outputs" ^
  pdf-outline-extractor
```

**Linux/Mac example:**

```bash
docker run --rm \
  -v "$PWD/inputs:/app/inputs" \
  -v "$PWD/outputs:/app/outputs" \
  pdf-outline-extractor
```

---

## 🗂️ **Inputs & Outputs**

* **Input PDFs:** Place in `inputs/` folder.
* **Outputs:** JSON files saved in `outputs/` folder.

---
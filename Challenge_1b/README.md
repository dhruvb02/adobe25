# 📄 Document Section & Subsection Analyzer

Extracts relevant sections from a collection of PDF documents based on a persona and job description, then saves the analysis as a JSON file. Runs locally **or in Docker**.

## Project Structure

```
1-b/
├── Dockerfile
├── process.py
├── requirements.txt
├── persona.json
├── input/         # Put your PDF files here
├── output/        # The result.json file will be saved here
└── README.md
```

## ⚙️ How to Run

### 🔹 1️⃣ Run locally (Python)

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run the analysis:** Make sure your PDFs are in the `input/` directory and your `persona.json` is configured. Then run the main script:
```bash
python process.py
```

### 🔹 2️⃣ Build Docker Image

```bash
docker build -t my-project .
```

### 🔹 3️⃣ Run with Docker

The `input` directory is copied into the image during the build process. You only need to mount the `output` directory to retrieve the `result.json` file.

**Important:** If you are on **Windows**, use the **full absolute path** for the `-v` mount! Example:
```bash
docker run --rm ^
  -v "C:\Users\YourUser\Desktop\1-b\output:/app/output" ^
  my-project
```

**Linux/Mac example:**
```bash
docker run --rm \
  -v "$(pwd)/output:/app/output" \
  my-project
```

## 🗂️ Inputs & Outputs

* **Inputs:**
   * Place all your PDF documents into the `input/` folder.
   * Define the persona and job task in `persona.json`.
* **Output:**
   * The analysis results will be saved as `result.json` in the `output/` directory.

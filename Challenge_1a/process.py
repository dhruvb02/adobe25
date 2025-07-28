import os
import sys
import json
import fitz
import re
from collections import Counter

def extract_outline(pdf_path):
    with fitz.open(pdf_path) as doc:
        heading = guess_title(doc)
        outline = doc.get_toc()
        if not outline:
            outline = fake_outline(doc, heading)

    result = {
        "title": heading,
        "outline": []
    }

    seen = set()
    for item in outline:
        level = f"H{item[0]}"
        text = item[1].strip()
        page = item[2]

        if text.lower() == heading.lower():
            continue

        key = (level, text, page)
        if key in seen:
            continue
        seen.add(key)

        result["outline"].append({
            "level": level,
            "text": text,
            "page": page
        })

    return result


def guess_title(doc):
    first_page = doc[0]
    blocks = first_page.get_text("dict")["blocks"]

    spans = []
    for b in blocks:
        if "lines" in b:
            for l in b["lines"]:
                for s in l["spans"]:
                    text = s["text"].strip()
                    if len(text) > 5:
                        spans.append({"size": s["size"], "text": text})

    spans.sort(key=lambda x: -x["size"])
    if not spans:
        return ""

    top_size = spans[0]["size"]
    top_spans = [s["text"] for s in spans if s["size"] >= 0.9 * top_size]

    title = " ".join(top_spans).strip()

    if re.fullmatch(r"[-=]{3,}", title):
        return ""

    return title



def fake_outline(doc, heading):
    fake = []
    is_form = "application form" in heading.lower() or "form" in heading.lower()

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for b in blocks:
            spans = []
            max_size = 0
            top_y = 1000

            for l in b.get("lines", []):
                for s in l.get("spans", []):
                    text = s["text"].strip()
                    if text:
                        spans.append(s)
                        if s["size"] > max_size:
                            max_size = s["size"]
                        if s["bbox"][1] < top_y:
                            top_y = s["bbox"][1]

            line_text = " ".join(s["text"].strip() for s in spans).strip()
            if not line_text:
                continue

           
            if line_text.lower() == heading.lower():
                continue

            if len(line_text.split()) > 30:
                continue

            m = re.match(r"^(\d+(?:\.\d+)*)(?:\.)?\s+(.+)", line_text)
            if m:
                numbering = m.group(1)
                body = m.group(2).strip()

                if is_form and numbering.isdigit():
                    continue

                if page_num == 0 and numbering.isdigit() and len(body.split()) < 8:
                    continue

                if re.search(r"\s+\d+$", body) and page_num <= 3:
                    continue

                if numbering.count('.') == 0:
                    fake.append([1, line_text, page_num])
                elif numbering.count('.') == 1:
                    fake.append([2, line_text, page_num])
                else:
                    fake.append([3, line_text, page_num])
                continue

            if line_text.isupper() and len(line_text.split()) < 8:
                fake.append([1, line_text, page_num])
                continue

            if (
                len(line_text.split()) <= 6 and
                line_text[0].isupper() and
                max_size >= 10 and
                top_y < 200
            ):
                fake.append([1, line_text, page_num])

    return fake




def save_outline(pdf_path, result):
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    basename = os.path.splitext(os.path.basename(pdf_path))[0]
    output_file = f"{basename}_outline.json"
    output_path = os.path.join(output_dir, output_file)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"JSON saved to: {output_path}")
    return output_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python final_outline.py <pdf_file>")
        sys.exit(1)

    pdf_file = sys.argv[1]
    if not os.path.exists(pdf_file):
        print(f"File not found: {pdf_file}")
        sys.exit(1)

    result = extract_outline(pdf_file)
    save_outline(pdf_file, result)

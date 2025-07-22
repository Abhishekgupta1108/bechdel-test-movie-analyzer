# 🎥 Bechdel Test Movie Script Analyzer

Hi, I’m Abhishek Gupta 👋  
This project is a Python-based tool that analyzes movie scripts to check whether they pass the **Bechdel Test**, a basic measure of female representation in films.

---

## 📌 About This Project

The Bechdel Test is simple yet insightful:
1. The movie must have at least two named female characters.
2. They must talk to each other.
3. Their conversation must be about something other than a man.

This tool:
- Parses movie scripts (plain text).
- Detects characters and their dialogues.
- Applies rule-based logic to evaluate if the script passes the Bechdel Test.
- Outputs results in a readable format and stores them in a file.

---

## 🚀 Features

- 📑 Automatic script parsing.
- 🎭 Detection of female characters.
- 🎬 Bechdel Test evaluation with PASS/FAIL result.
- 📂 Results are saved automatically for record-keeping.

---

## 📂 Project Structure

bechdel-test-movie-analyzer/
│
├── data/
│ └── script.txt
│
├── scripts/
│ ├── script_parser.py
│ └── bechdel_test.py
│
├── README.md


## ▶️ How to Use

1. Place your movie script (plain text) inside the `/data/` folder as `script.txt`.
2. Run the parser:
```bash
python scripts/script_parser.py

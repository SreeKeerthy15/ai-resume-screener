# 🔍 AI Resume Screener

This is an AI-powered Resume Screener built using **Streamlit**, designed to automatically analyze and compare candidate resumes against a given job description using **Natural Language Processing (spaCy)**, **WordNet synonyms**, and optional **GPT-based skill categorization**.

---

## 🚀 Features

- 📄 Upload multiple resumes (PDF/DOCX)  
- 📝 Upload a Job Description (JD) (PDF/DOCX)  
- 🧠 Extracts keywords using spaCy NLP  
- 🧩 Skill Categorization:  
  - Built-in categories: Technical, Tools, Soft Skills, Certifications  
  - Unmatched skills auto-categorized via **OpenAI GPT-3.5**  
- ✅ Match Scoring between JD and Resume(s)  
- 📊 Visual Match Score Meter  
- 📌 View per-category Matched & Missing Skills  
- 📥 Downloadable AI-generated Reports: PDF and DOCX formats  

---

## 💻 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/SreeKeerthy15/ai-resume-screener.git
cd ai-resume-screener
````

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # for Windows PowerShell
# OR
source venv/bin/activate     # for macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🧠 Technologies Used

* Python
* Streamlit
* spaCy (`en_core_web_sm`)
* NLTK & WordNet
* OpenAI GPT-3.5 (`text-davinci-003`)
* PDFMiner & python-docx
* fpdf (PDF report generation)

---

## 📄 Outputs

* 🎯 Overall match score for each resume
* 🗂️ Categorized skills: matched and missing
* 📁 Downloadable report: PDF & DOCX

---

## ⚠️ Challenges Faced

* Handling different resume formats and noisy text extraction
* Balancing keyword-based and AI-based skill categorization
* Avoiding false positives in skill matching (e.g., matching "Java" to "JavaScript")
* Designing clean PDF/DOCX output with summaries
* Handling OpenAI API rate limits during batch resume evaluation

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

**Sree Keerthy**
[GitHub Profile](https://github.com/SreeKeerthy15)

````

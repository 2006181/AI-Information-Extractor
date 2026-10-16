# 🎬 AI Information Extractor

An AI-powered Information Extraction application that converts unstructured text into structured JSON using Google Gemini, LangChain, Pydantic, and Streamlit.

Simply enter a paragraph, and the application extracts important information, organizes it into predefined fields, and generates validated JSON output.

## ✨ Features

- 🤖 **AI-Powered Extraction:** Extract relevant information from any paragraph using Google Gemini.
- 📝 **Basic Information:** Identify the main subject, title, category, and release year.
- 👥 **Entity Extraction:** Extract people, cast members, directors, creators, authors, and organizations.
- 🏷️ **Classification:** Identify genres, subgenres, and themes.
- ✅ **Pydantic Validation:** Validate structured output using Pydantic and PydanticOutputParser.
- 📊 **Interactive UI:** Explore extracted information through a Streamlit interface.
- 💻 **JSON Output:** Display clean, formatted JSON.
- ⬇️ **Download Results:** Download extracted information as a JSON file.
- 🔒 **Missing Information Handling:** Handle unavailable information using predefined default values.

## 🛠️ Tech Stack

- **Python** – Core programming language
- **Streamlit** – Interactive web interface
- **Google Gemini** – Large language model
- **LangChain** – Prompt management and model integration
- **Pydantic** – Data validation and schema definition
- **PydanticOutputParser** – Structured output parsing
- **python-dotenv** – Environment variable management

## 📂 Project Structure

```text
AI-Information-Extractor/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

## 🚀 Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/2006181/AI-Information-Extractort
```

Navigate to the project directory:

```bash
cd YOUR_REPOSITORY
```

Replace `YOUR_USERNAME` and `YOUR_REPOSITORY` with your GitHub username and repository name.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API Key

Create a `.env` file in the project root directory and add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Get your API key from Google AI Studio:

https://aistudio.google.com/apikey

**Important:** Never upload your `.env` file or expose your API key publicly.

### 5. Run the Application

Execute the following command:

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 🧪 Example Input

```text
Inception is a science fiction movie released in 2010.
It was directed by Christopher Nolan and stars Leonardo DiCaprio.
```

## 📤 Example JSON Output

```json
{
    "main_subject": "Inception",
    "title_name": "Inception",
    "category_type": "Movie",
    "release_year_date": 2010,
    "people_cast": [
        "Leonardo DiCaprio"
    ],
    "director_creator_author": [
        "Christopher Nolan"
    ],
    "organizations_companies": [],
    "genre_category": "Science Fiction",
    "subgenres": [],
    "themes_topics": []
}
```

*Note: The actual output depends on the input paragraph. The model extracts only the information it identifies in the supplied text.*

## ⚙️ How It Works

1. The user enters a paragraph in the Streamlit application.
2. LangChain's `PromptTemplate` prepares the prompt and formatting instructions.
3. Google Gemini analyzes the paragraph and generates structured information.
4. `PydanticOutputParser` parses and validates the response against the `MovieInfo` schema.
5. The validated result is displayed in the Streamlit interface.
6. The user can view the formatted JSON and download it as a `.json` file.

## 🧠 Key Concepts Demonstrated

- Prompt Engineering
- Large Language Model Integration
- Information Extraction
- Structured Outputs
- Pydantic Data Models
- Output Parsing and Validation
- LangChain Expression Language (LCEL)
- Streamlit UI Development
- Environment Variable Management

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | API key required to access Google Gemini |

## 📌 Future Improvements

- Support for additional information extraction schemas.
- Export extracted results to CSV.
- Batch processing for multiple paragraphs.
- Improved error handling and validation feedback.
- Support for extracting information from uploaded documents.

## 👨‍💻 Author

RAHUL GUPTA
---

⭐ If you find this project useful, consider giving the repository a star!

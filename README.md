# 📘 Blood Sacs detector Microservice

<!-- This project provides a lightweight microservice that receives an image, forwards it to Google Gemini using the `google-genai` SDK, and returns the generated caption. -->

## 🚀 1. Environment Setup (Using uv)

This project uses **uv** (fast Python package manager). Make sure you have uv installed:  
👉 https://docs.astral.sh/uv/getting-started/

### Install all required dependencies

The repository already includes a `pyproject.toml`, so simply run:
```bash
uv venv
uv sync
```

This creates a virtual environment and installs all dependencies automatically.

## 🔐 2. Create Your `.env` File

You must obtain the `.env` file from the author of the repository.

Place it in the project root:
```
.env
```

A valid `.env` file contains:
```env
API_KEY=your_actual_api_key_here
```

**(Do NOT commit this file to GitHub.)**

## ▶️ 3. Running the FastAPI Server

To start the microservice:
```bash
uv run uvicorn main:app --reload
```

The server will run at:
```
http://127.0.0.1:8000
```

Interactive API docs (Swagger):
```
http://127.0.0.1:8000/docs
```

## 🧪 4. Testing the API (test.py)

You can test the microservice using the included `test.py` script. Run it using regular Python on your machine:
```bash
python test.py
```

This script sends an image to the running FastAPI server and prints the caption returned by Gemini.

## 📂 Project Structure
```
.
├── main.py                # FastAPI microservice
├── test.py                # Client to test the API
├── pyproject.toml         # uv dependency file
├── README.md              # Documentation
└── .env                   # API keys (not included in repo)
```

## 💡 Notes

* Your `.env` file must contain a valid Google API key.
<!-- * The microservice receives an image using `UploadFile` and forwards it to Gemini via `types.Part.from_bytes`. -->
* `uv sync` ensures deterministic dependency installation.

## 📧 Need Help?

Contact the author or open an issue in the repository.
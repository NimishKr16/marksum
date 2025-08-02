# Marksum

**Marksum** is a modern, developer-friendly CLI tool that summarizes Markdown files using Google's Gemini AI (via the `gemini-2.0-flash` model). It supports TL;DR summaries, bullet-point formats, directory-wide processing, and stylish terminal output using `rich`.

Ideal for:
- Technical writers
- Documentation maintainers
- Developers working with large Markdown repositories

---

## ✨ Features

- Summarize single or multiple `.md` files
- Choose between **TL;DR** and **bullet point** output
- Save summaries to files or folders
- Clean terminal UI with colorized formatting
- Graceful error handling
- Modular backend (Gemini; OpenAI coming soon)

---

## ⚙️ Installation

### ✅ Recommended (via PyPI)

```bash
pip install marksum
```

Then run:

```bash
marksum README.md --summary
```

### 🔧 From Source (for development)

```bash
git clone https://github.com/NimishKr16/marksum.git
cd marksum
poetry install
```

---

## 🔐 Gemini API Key Setup

Marksum requires a Gemini API key to access Google's LLMs.

### Option 1: Use `.env` file (recommended)

Create a `.env` file in the project root with:

```env
GOOGLE_API_KEY=your_api_key_here
```

### Option 2: Set as environment variable

```bash
export GOOGLE_API_KEY=your_api_key_here
```

You can persist this in your shell profile (`.bashrc`, `.zshrc`, etc.).

---

## 🚀 Usage Examples

### 🔹 TL;DR Summary of One File

```bash
marksum README.md --summary
```

### 🔹 Bullet Point Summary

```bash
marksum README.md --bullets
```

### 🔹 Save Output to a File

```bash
marksum README.md --summary --output summary.md
```

### 🔹 Process All `.md` Files in a Folder

```bash
marksum docs/ --summary
```

### 🔹 Save Summaries to a Folder

```bash
marksum docs/ --bullets --output summaries/
```

> Each `.md` file will generate a `.summary.md` file in `summaries/`, preserving subfolder structure.

---

## 📁 Project Structure

```
marksum/
├── src/
│   └── marksum/
│       ├── cli.py
│       ├── llm_provider.py
│       └── prompts/
│           ├── default.txt
│           └── bullets.txt
├── README.md
├── .env
├── pyproject.toml
```

---

## 🧠 Customizing Prompts

Marksum uses prompt templates stored in:

```
src/marksum/prompts/
├── default.txt  # TL;DR style
├── bullets.txt  # Bullet point style
```

You can edit these to change the tone, depth, or formatting of your AI summaries.

---

## 🛠 Error Handling

- ✅ Skips empty files
- ✅ Detects invalid or missing paths
- ✅ Reports Gemini API issues per file
- ✅ Warns on multi-file output conflicts

---

## 🧪 Roadmap & Ideas

- [ ] Unified `--mode` flag (`summary` or `bullets`)
- [ ] Custom prompt file via CLI
- [ ] Language translation support
- [ ] Markdown-to-plain-text option
- [ ] JSON metadata output
- [ ] Interactive chat mode for Markdown docs

---

## 🤝 Contributing

Want to help improve Marksum?  
Feel free to open issues, suggest features, or submit a pull request!

---

## 🪪 License

Apache 2.0 License © 2025 Nimish Kumar
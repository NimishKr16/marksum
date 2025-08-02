

# Marksum

**Marksum** is a modern and developer-friendly CLI tool that summarizes Markdown files using Google's Gemini AI (via the `gemini-2.0-flash` model). It supports both TL;DR and bullet-point summaries, works on single files or entire directories, and includes clean output formatting and detailed error handling.

Built with modularity and extensibility in mind, Marksum is ideal for:
- Technical writers
- Documentation maintainers
- Developers working with large Markdown repositories

---

## ✨ Features

- 🔹 Summarize single or multiple `.md` files
- 🔹 Choose between **TL;DR summary** and **bullet point** modes
- 🔹 Automatically save summaries to structured output directories
- 🔹 Clean terminal display with `rich`
- 🔹 Friendly error handling and helpful prompts
- 🔹 Modular LLM integration via `llm_provider.py`
- 🔹 Powered by Gemini's `gemini-2.0-flash` model

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/NimishKr16/marksum.git
cd marksum
```

### 2. Install dependencies using Poetry

```bash
poetry install
```

### 3. Set up your Gemini API key

You can provide your Gemini API key in one of two ways:

#### Option 1: Set an environment variable

```bash
export GOOGLE_API_KEY=your_api_key_here
```

#### Option 2: Use a `.env` file

Create a `.env` file in the project root and add:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## 🚀 Usage

Run the CLI via:

```bash
poetry run marksum [OPTIONS] PATH
```

---

### 🔹 Summarize a Single File (TL;DR)

```bash
poetry run marksum README.md --summary
```

### 🔹 Bullet Point Summary

```bash
poetry run marksum README.md --bullets
```

### 🔹 Save Output to File

```bash
poetry run marksum README.md --summary --output summary.md
```

---

### 🔹 Summarize All Markdown Files in a Folder

```bash
poetry run marksum docs --summary
```

### 🔹 Save Summaries for Multiple Files

```bash
poetry run marksum docs --bullets --output summaries/
```

> Each `.md` file inside `docs/` will generate a `.summary.md` file in `summaries/`, preserving folder structure.

---

## 📁 Project Structure

```
marksum/
├── src/
│   └── marksum/
│       ├── cli.py               # CLI logic
│       ├── llm_provider.py      # Gemini wrapper
├── prompts/
│   ├── default.txt              # TL;DR prompt
│   └── bullets.txt              # Bullet points prompt
├── samples/                     # Example markdowns
├── README.md
├── .env                         # API key (not committed)
├── pyproject.toml
```

---

## 🧠 Prompt Customization

Prompts are stored in the `prompts/` folder:
- `default.txt`: for summary output
- `bullets.txt`: for point-wise output

> You can edit these prompt templates to better suit your use case.

---

## 🛠 Error Handling

- Graceful handling of empty files or folders
- Errors from Gemini are reported per file
- Invalid paths, file I/O, and multi-file conflicts are clearly communicated

---

## 🔐 Setting Up Your Gemini API Key

Marksum requires a Gemini API key to work. You can generate one from [Google AI Studio](https://makersuite.google.com/app/apikey).

### ✅ Recommended

Use a `.env` file in your project folder:
```env
GOOGLE_API_KEY=your_api_key_here
```

This will be automatically loaded when the CLI runs.

### 🌐 Alternatively

Set it directly in your shell session:
```bash
export GOOGLE_API_KEY=your_api_key_here
```

To persist this, add it to your `~/.zshrc` or `~/.bashrc`.

> If the key is missing, Marksum will alert you to set it before running any commands.

---

## 🔧 Coming Soon

- [ ] Unified `--mode` flag (e.g. `--mode summary|bullets`)
- [ ] Custom prompt file support
- [ ] Markdown-to-plaintext output toggle
- [ ] Language translation of summaries
- [ ] JSON output metadata
- [ ] Interactive Q&A mode (chat with a markdown doc)

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to open issues, suggest new prompt styles, or improve performance.

---

## 🪪 License

Apache 2.0 License © 2025 Nimish Kumar
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
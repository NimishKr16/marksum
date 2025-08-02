# Marksum

Marksum is a command-line tool that uses large language models (LLMs) to generate concise summaries of Markdown files. It supports multiple output styles such as TL;DR summaries, bullet point extraction, and Q&A-style breakdowns. Marksum is designed for developers, technical writers, and anyone who wants to quickly understand documentation or notes written in Markdown.

## Features

• Summarize individual or multiple Markdown files  
• Output options: TL;DR summary, bullet points, Q&A format  
• Supports OpenAI, Mistral, LM Studio, and other LLM APIs  
• Chunking logic to handle large files by splitting on headings  
• Command-line interface built with Typer  
• Optional interactive mode for asking questions about the content  
• Save summaries to file or print to stdout

## Installation

1. Clone the repository:

```bash
git clone https://github.com/nimishkumarkan/marksum.git
cd marksum
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Set your LLM API key (e.g., OpenAI):

```bash
export OPENAI_API_KEY=your-api-key
```

## Usage

Basic usage:

```bash
python marksum.py README.md
```

Generate a bullet-point summary:

```bash
python marksum.py README.md --bullets
```

Process an entire folder of Markdown files:

```bash
python marksum.py ./docs --summary --output summaries/
```

Use a different model or API:

```bash
python marksum.py notes.md --provider mistral --api-url http://localhost:11434
```

## Roadmap

• Add support for more file types (e.g., plain text, HTML)  
• Implement interactive CLI mode  
• Add options for outline-style summaries  
• Package as a pip-installable module  
• Add support for local models (e.g., llama.cpp integration)

## License

This project is licensed under the Apache 2.0 License. See the LICENSE file for details.

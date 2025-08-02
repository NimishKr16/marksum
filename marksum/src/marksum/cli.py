from string import Template
from pathlib import Path
import typer
from marksum.llm_provider import summarize_with_gemini

app = typer.Typer()

@app.command()
def summarize(
    path: str,
    summary: bool = typer.Option(False, help="Generate TL;DR summary"),
    bullets: bool = typer.Option(False, help="Generate bullet points"),
    output: str = typer.Option(None, help="Optional output file or directory")
):
    typer.echo(f"Processing {path}")
    typer.echo(f"Options -> summary: {summary}, bullets: {bullets}, output: {output}")
    # Step 1: Read the Markdown file
    file_path = Path(path)
    if not file_path.exists() or not file_path.is_file():
        typer.echo("Error: File not found.")
        raise typer.Exit(code=1)

    markdown_text = file_path.read_text(encoding="utf-8")
    typer.echo(f"Loaded {len(markdown_text.split())} words from {file_path.name}")

    # Step 2: Load and fill prompt template
    template_path = Path(__file__).resolve().parent.parent / "prompts" / "default.txt"
    if not template_path.exists():
        typer.echo("Prompt template not found.")
        raise typer.Exit(code=1)

    template_str = template_path.read_text(encoding="utf-8")
    prompt = Template(template_str).substitute(markdown=markdown_text)
    typer.echo("Prompt prepared successfully.")

    typer.echo("Sending prompt to Gemini...")
    summary_text = summarize_with_gemini(prompt)

    # Output the result
    if output:
        Path(output).write_text(summary_text, encoding="utf-8")
        typer.echo(f"Summary saved to {output}")
    else:
        typer.echo("\n" + summary_text)

if __name__ == "__main__":
    app()
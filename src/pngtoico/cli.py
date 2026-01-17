import typer
from pathlib import Path
from typing import List, Optional
from pngtoico.core import convert_png_to_ico_collection

app = typer.Typer(add_completion=False, help="Convert PNG to multiple individual ICO files.")

@app.command()
def convert(
    input_file: Path = typer.Argument(..., help="Source PNG", exists=True, dir_okay=False),
    output: Optional[Path] = typer.Option(
        None, "--output", "-o", 
        help="Target directory for icons (defaults to CWD)"
    ),
    sizes: List[int] = typer.Option(
        [16, 32, 48, 64, 128, 256], 
        "--size", "-s", 
        help="Resolutions to generate"
    )
):
    """
    Generate a set of individual .ico files with clean naming.
    """
    # Pure logic: if no output provided, use CWD
    target_dir = output or Path.cwd()
    
    try:
        typer.echo(f"🚀 Processing: {input_file.name}")
        created = convert_png_to_ico_collection(input_file, target_dir, sizes)
        
        for p in created:
            typer.secho(f"  CLEAN: {p.name}", fg=typer.colors.CYAN)
            
        typer.secho(f"\n✨ Done! {len(created)} icons exported to {target_dir}", fg=typer.colors.GREEN, bold=True)
    except Exception as e:
        typer.secho(f"💥 Error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)

if __name__ == "__main__":
    app()

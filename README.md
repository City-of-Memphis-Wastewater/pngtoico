# pngtoico

A lightweight internal utility to convert PNG images into a collection of transparent, cleanly-named Windows `.ico` files using **Pillow** and **Typer**.

## 🛠 Installation & Setup

This project uses `uv` for dependency management. To set up your local development environment:

```bash
# Clone the repository (if you haven't already)
git clone https://github.com/City-of-Memphis-Wastewater/pngtoico.git
cd pngtoico

# Sync dependencies and create the virtual environment
uv sync

```

Once synced, the `pngtoico` command will be available within your environment.

## 🚀 Usage

The CLI allows you to convert a source PNG into multiple individual icon files.

### Basic Conversion

By default, this generates icons for sizes: 16, 32, 48, 64, 128, and 256.

```bash
pngtoico pyhabitat.png

```

### Specify Output Directory

Use the `-o` or `--output` flag to send the generated icons to a specific folder (e.g., your build assets):

```bash
pngtoico pyhabitat.png -o ../pyhabitat/build_assets

```

### Custom Sizes

If you only need specific resolutions, use the `-s` or `--size` flag:

```bash
pngtoico pyhabitat.png --size 32 --size 256

```

## 📋 Options Summary

| Option | Shorthand | Description |
| --- | --- | --- |
| `--output` | `-o` | Target directory for icons (defaults to CWD) |
| `--size` | `-s` | Resolutions to generate (can be used multiple times) |
| `--help` |  | Show the help message and exit |

from pathlib import Path
from PIL import Image

def convert_png_to_ico_collection(input_path: Path, output_dir: Path, sizes: list[int]) -> list[Path]:
    """
    Creates individual .ico files for each resolution in the target directory.
    """
    img = Image.open(input_path).convert("RGBA")
    
    # Background removal (near-white to transparent)
    datas = img.getdata()
    new_data = [
        (255, 255, 255, 0) if all(c > 240 for c in item[:3]) else item 
        for item in datas
    ]
    img.putdata(new_data)
    
    output_dir.mkdir(parents=True, exist_ok=True)
    generated_files = []

    for size in sizes:
        output_name = f"{input_path.stem}_{size}x{size}.ico"
        target_path = output_dir / output_name
        
        # Resize using Lanczos for high-quality downsampling
        resized_img = img.resize((size, size), resample=Image.Resampling.LANCZOS)
        resized_img.save(target_path, format='ICO')
        generated_files.append(target_path)
        
    return generated_files

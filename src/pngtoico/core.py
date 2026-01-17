from pathlib import Path
from PIL import Image

def convert_png_to_ico_collection(
    input_path: Path, 
    output_dir: Path, 
    sizes: list[int], 
    #remove_bg: bool = False
) -> list[Path]:
    img = Image.open(input_path).convert("RGBA")

    # broken, sucks
    if False:# remove_bg:
        # Only run this if explicitly requested
        white_thresh = 245
        grayscale = img.convert("L")
        mask = grayscale.point(lambda x: 0 if x > white_thresh else 255)
        img.putalpha(mask)

    output_dir.mkdir(parents=True, exist_ok=True)
    generated_files = []

    for size in sizes:
        output_name = f"{input_path.stem}_{size}x{size}.ico"
        target_path = output_dir / output_name
        
        # Ensure we resize to the target dimensions
        resized_img = img.resize((size, size), resample=Image.Resampling.LANCZOS)
        
        # We explicitly pass the size to the ICO writer to ensure the header is correct
        resized_img.save(target_path, format='ICO', sizes=[(size, size)])
        generated_files.append(target_path)
        
    return generated_files

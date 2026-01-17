from pathlib import Path
from PIL import Image

def convert_png_to_ico_collection(input_path: Path, output_dir: Path, sizes: list[int]) -> list[Path]:
    # 1. Load with transparency preserved
    img = Image.open(input_path).convert("RGBA")
    
    # 2. Better Background Handling
    # Instead of a loop, we use 'point' or just rely on the PNG's existing alpha.
    # If the source PNG is from a generator, it likely has a white background.
    # To get smooth edges, we convert white to transparent while keeping anti-aliasing.
    
    # This is a cleaner way to handle transparency without "fizzy" edges:
    white_thresh = 245
    alpha = img.split()[-1] # Get existing alpha
    
    # Create a mask where white is transparent
    grayscale = img.convert("L")
    mask = grayscale.point(lambda x: 0 if x > white_thresh else 255)
    
    # Combine original alpha with our new mask
    img.putalpha(mask)

    output_dir.mkdir(parents=True, exist_ok=True)
    generated_files = []

    for size in sizes:
        output_name = f"{input_path.stem}_{size}x{size}.ico"
        target_path = output_dir / output_name
        
        # 3. Use LANCZOS + Image.Image.resize (higher quality than shortcut)
        resized_img = img.resize((size, size), resample=Image.Resampling.LANCZOS)
        
        # 4. Save
        resized_img.save(target_path, format='ICO')
        generated_files.append(target_path)
        
    return generated_files

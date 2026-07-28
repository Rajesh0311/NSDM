from pathlib import Path
from PIL import Image

source = Path("assets/upscale_nsdm_decision_boundary_primary_2.png")
target = Path("assets/nsdm_decision_boundary_primary_1600.webp")

target_width = 1600
target_height = 1986

with Image.open(source) as image:
    image.load()

    if image.mode in ("RGBA", "LA") or (
        image.mode == "P" and "transparency" in image.info
    ):
        rgba = image.convert("RGBA")
        background = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
        image = Image.alpha_composite(background, rgba).convert("RGB")
    else:
        image = image.convert("RGB")

    resized = image.resize(
        (target_width, target_height),
        Image.Resampling.LANCZOS
    )

    resized.save(
        target,
        format="WEBP",
        quality=88,
        method=6,
        lossless=False,
        exact=True
    )

print(f"Created: {target}")
print(f"Dimensions: {target_width} x {target_height}")
print(f"Size MB: {target.stat().st_size / 1024 / 1024:.2f}")

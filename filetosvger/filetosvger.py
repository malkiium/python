import os
import numpy as np
from skimage import io, color, filters, measure, segmentation, util
import svgwrite

BASE_PATH = r"C:\Users\eliha\Pictures"

def image_to_colored_svg(input_name, output_name="output.svg", num_colors=8):
    input_path = os.path.join(BASE_PATH, input_name)
    output_path = os.path.join(BASE_PATH, output_name)

    # Load image
    img = io.imread(input_path)
    if img.shape[-1] == 4:  # RGBA → RGB
        img = color.rgba2rgb(img)

    # Convert to LAB (better for clustering colors)
    lab_img = color.rgb2lab(img)

    # Quantize colors using SLIC superpixels
    segments = segmentation.slic(lab_img, n_segments=num_colors*100, compactness=20, start_label=1)

    # Prepare SVG canvas
    h, w = img.shape[:2]
    dwg = svgwrite.Drawing(output_path, size=(w, h))

    # Go over each region
    for region_id in np.unique(segments):
        mask = segments == region_id
        contours = measure.find_contours(mask, 0.5)

        # Get average color of this region
        mean_color = img[mask].mean(axis=0)
        rgb = tuple(int(c) for c in mean_color[:3])

        for contour in contours:
            points = [(float(x), float(y)) for y, x in contour]
            dwg.add(dwg.polygon(points, fill=svgwrite.utils.rgb(*rgb), stroke="none"))

    dwg.save()
    print(f"✅ Colored SVG saved at {output_path}")

# Example usage
image_to_colored_svg("PPNEW.jpg", "trial_colored.svg", num_colors=12)

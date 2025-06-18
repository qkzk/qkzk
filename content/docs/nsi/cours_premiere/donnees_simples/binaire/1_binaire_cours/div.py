from PIL import Image, ImageDraw, ImageFont
import os

# Load the original image
img_path = "./divisions.png"
original = Image.open(img_path).convert("RGBA")

# Create a list of crops corresponding to each step (manually defined by approximate coordinates)
# Coordinates format: (left, upper, right, lower)
steps = [
    (0, 0, 50, 20),  # 167 | 2
    (0, 0, 60, 40),  # + 83
    (0, 0, 80, 60),  # + 41
    (0, 0, 100, 80),  # + 20
    (0, 0, 120, 100),  # + 10
    (0, 0, 140, 120),  # + 5
    (0, 0, 160, 140),  # + 2
    (0, 0, 180, 160),  # + 1
    (0, 0, 200, 180),  # + 2
    (0, 0, 220, 200),  # + 0
]

# Create frames for the GIF
frames = [original.crop(box) for box in steps]

# Let's create a proper animated GIF showing each step by revealing more of the original image over time.
# We'll use the full image size and apply a progressive mask to show more content with each frame.

# Get the size of the original image
width, height = original.size

# Define vertical crop positions for each step (manually tuned based on image structure)
step_heights = [30, 55, 85, 115, 145, 170, 195, 220, 245, height]

# Create frames by cropping progressively more of the image
frames_full = [original.crop((0, 0, width, h)) for h in step_heights]

# Create a white background image to paste on (same size as full image)
white_bg = Image.new("RGBA", (width, height), "WHITE")
final_frames = []

# Paste the cropped step onto the white background to ensure consistent frame size
for frame in frames_full:
    full_frame = white_bg.copy()
    full_frame.paste(frame, (0, 0))
    final_frames.append(full_frame)

# Save the new animated GIF
fixed_gif_path = "/mnt/data/divisions_steps_fixed.gif"
final_frames[0].save(
    fixed_gif_path, save_all=True, append_images=final_frames[1:], duration=600, loop=0
)

fixed_gif_path

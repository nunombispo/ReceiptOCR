from PIL import Image

# Set filename
filename = "receipt-hotel-image"

# Open the image file
image = Image.open(f'{filename}.png')

# Convert image to RGB (in case it's RGBA or another mode)
image = image.convert('RGB')

# Save the image as a PDF
image.save(f'{filename}.pdf')


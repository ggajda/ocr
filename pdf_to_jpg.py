import os
from pypdf import PdfReader
from PIL import Image


def convert_pdfs_to_images(pdfs):
    print("Trwa pobieranie obrazów z pilku...")
    reader = PdfReader(pdfs[0])

    page = reader.pages[0]
    image_paths = []
    image_ext = None

    for count, image_file_object in enumerate(page.images):
        f_name = f'{count}{image_file_object.name}'
        image_paths.append(f_name)
        with open(f_name, "wb") as f:
            f.write(image_file_object.data)
        image_ext = f_name.split('.')[1]

    image_paths.sort(reverse=True)
    file_name = f"{pdfs[0].split('.')[0]}.{image_ext}"
    print(file_name)
    images_merege(image_paths, file_name)


def images_merege(image_paths, file_name):
    print("Trwa konwersja pilku PDF do obrazu...")
    images = [Image.open(img_path) for img_path in image_paths]

    max_width = max(img.width for img in images)
    total_height = sum(img.height for img in images)

    new_image = Image.new('RGB', (max_width, total_height))

    y_offset = 0
    for img in images:
        new_image.paste(img, (0, y_offset))
        y_offset += img.height

    new_image.save(file_name)

    for f in image_paths:
        os.remove(f)
    new_image.show()

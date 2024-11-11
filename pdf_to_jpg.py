import os
from pypdf import PdfReader
from PIL import Image
from ocr import get_ocr


def convert_pdfs_to_images(pdf):
    print("\nTrwa pobieranie obrazu z pliku PDF...")
    reader = PdfReader(pdf)

    image_paths = []
    # image_ext = None

    # page = reader.pages[0]
    for page in reader.pages:
        for count, image_file_object in enumerate(page.images):
            f_name = f'{count}{image_file_object.name}'
            image_paths.append(f_name)
            with open(f_name, "wb") as f:
                f.write(image_file_object.data)
            img = Image.open(f_name)
            rotated_img = img.rotate(90, expand=True)
            rotated_img.save(f_name)
            get_ocr(f_name)
            # image_ext = f_name.split('.')[1]

    # # image_paths.sort(reverse=True)
    # file_name = f"{pdf.split('.')[0]}.{image_ext}"
    # images_merge(image_paths, file_name)
    # images_merge(['0Im1.jpg', '0Im2.jpg', '0Im3.jpg', '0Im4.jpg',
    #              '0Im5.jpg', '0Im6.jpg', '0Im7.jpg', '0Im8.jpg', '0Im9.jpg'], 'umowa_zawiercie.jpg')


def images_merge(image_paths, file_name):
    print("Trwa konwersja pliku PDF do obrazu...")
    images = [Image.open(img_path) for img_path in image_paths]

    max_width = max(img.width for img in images)
    total_height = sum(img.height for img in images)

    new_image = Image.new('RGB', (max_width, total_height))

    y_offset = 0
    for img in images:
        new_image.paste(img, (0, y_offset))
        y_offset += img.height

    new_image.save(file_name)

    # for f in image_paths:
    #     os.remove(f)
    new_image.show()
    # get_ocr(file_name)

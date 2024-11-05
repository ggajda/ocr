from pdf2image import convert_from_path


def convert_to_jpg(pdf_file):
    images = convert_from_path(pdf_file)

    for i in range(len(images)):
        images[i].save('page' + str(i) + '.jpg', 'JPEG')

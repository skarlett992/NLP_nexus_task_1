import cv2
from pdf2image import convert_from_path

from src.help_functions import get_text_from_image, variant_1
from src.log import logger


def get_text(input_files):
    logger.info(f'run get_text., args: input_files: {input_files}')
    result_text = ''
    for file_name in input_files:
        # if '.pdf' in file_name:
        if file_name[-4:] == '.pdf':
            new_files = convert_pdf_to_jpg(file_name)
            result_text += get_text(new_files)
            # input_files = [*input_files, *new_files]
        else:
            result_text += prepare_file(file_name)

    logger.info(f"get_text., returns: {result_text}")

    return result_text


def prepare_file(file_name):
    logger.info(f'run prepare_file., args: file_name: {file_name}')

    image = cv2.imread(file_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    contours1, hierarchy1 = variant_1(gray)
    image_with_contours = cv2.drawContours(image.copy(), contours1, -1,
                                           (0, 255, 0), 3)
    result_text = get_text_from_image(contours1, image_with_contours,
                                      r'--oem 3 -l eng --psm 6')
    logger.info(f"finish prepare_file., returns: {result_text}")

    return result_text


def convert_pdf_to_jpg(file_name):
    logger.info(f'run convert_pdf_to_jpg., args: file_name: {file_name}')

    input_files = []
    pages = convert_from_path(file_name, 350)
    i = 1
    for page in pages:
        image_name = f'{file_name} page {i}.jpg'
        input_files.append(image_name)
        page.save(image_name, "JPEG")
        i = i + 1
    logger.info(f"finish convert_pdf_to_jpg., returns: {input_files}")

    return input_files

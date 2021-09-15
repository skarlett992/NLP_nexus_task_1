import cv2
import pytesseract

from src.log import logger


# find text contours
def variant_1(gray):
    logger.debug(f'run variant_1., args: file_name: {gray}')

    threshold_img = cv2.threshold(gray, 0, 255,
                                  cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)[1]
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    dilation = cv2.dilate(threshold_img, rect_kernel, iterations=50)
    dilation = cv2.GaussianBlur(dilation, (11, 11), 0)
    dilation = cv2.medianBlur(dilation, 9)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)
    logger.info(f"finish variant_1., returns: {contours, hierarchy}")

    return contours, hierarchy


def get_text_from_image(contours,
                        image_with_contours,
                        config=r'--oem 3 -l eng --psm 6'):
    logger.info(
        f'run get_text_from_image., args: contours: {contours}, '
        f'image_with_contours: {image_with_contours}, config: {config}')

    for cnt in contours:
        [x, y, w, h] = cv2.boundingRect(cnt)
        # Don't plot small false positives that aren't text
        if w < 35 and h < 35:
            continue
        # Cropping the text block for giving input to OCR
        cropped = image_with_contours[y:y + h, x:x + w]

        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(
            cropped,
            #         lang='eng',
            config=config,
            #         config='-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz -psm 6'
            #         config='-l eng --psm 6'
        ).strip()
        if (len(text) == 0):
            continue
        logger.info(text)

        logger.info(f"get_text_from_image., returns: {text}")

        return text

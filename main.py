import time
import pytesseract
import cv2
import pyautogui

# 'C:\Users\user\Desktop\Projects\Alarm_idirect\env\Lib\site-packages'

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# 1653, 597, 1704, 597
# 1653, 612, 1705, 612
#
# 1647, 612, 1691, 612
# 1647, 630, 1691, 630


def cut_images(img, location):
    images = []
    for points in location:
        y = points[1]
        x = points[0]
        h = 17
        w = 50
        crop = img[y:y + h, x:x + w]
        crop = cv2.resize(crop, None, fx=9, fy=9)  # Увеличение изображения в 9 раз
        # cv2.imshow('image', crop)
        # cv2.waitKey(0)

        images.append(crop)
    return images


def type_check(str):
    if string_ocr:
        return (float(str))
    else:
        return ('[-] Значения не найдены')



if __name__ == '__main__':
    for _ in range(20):
        time.sleep(1)
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')
        img = cv2.imread('screenshot.png')

        # location = [[1653, 597], [1647, 612]]
        location = [[1584, 537], [1578, 552]]

        for cuted_image in cut_images(img, location):
            # Распознавание, допустимы только цифры
            string_ocr = pytesseract.image_to_string(cuted_image, config='outputbase digits')
            print(type_check(string_ocr))

    time.sleep(3600)

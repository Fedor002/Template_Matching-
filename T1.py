# Python program to illustrate
# template matching
import cv2
import numpy as np

#Считывание фотографии
img_rgb = cv2.imread('Stock/StockC3.jpg')

#Перегонка фотки из цветного в оттенки черого
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

#Создание tample и перегонка туда требуемой фотки
template = cv2.imread('Tmpl/Tmpl8.jpg', 0)

# Сохраним показатели высоты и ширины tample, чтобы в дальнейшем делать обводку с такимиже показателями
w, h = template.shape[::-1]

# Произвести поиск совподения tample с img и сохранить все координаты совподения
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# Процент схождения
threshold = 0.34

# Отбор координат по требуемому threshold
loc = np.where(res >= threshold)

# Прорисовка прямоугольников в требуемых координатах
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

# Показать итог

cv2.imshow('Detected', img_rgb)
cv2.waitKey(0)
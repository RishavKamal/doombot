import cv2 as cv
import numpy as np

region_img = cv.imread('region.png', cv.IMREAD_COLOR)   # big image
shelter_img = cv.imread('shelter.png', cv.IMREAD_COLOR) # template

result = cv.matchTemplate(region_img, shelter_img, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
print(f"Best match confidence: {max_val}")

threshold = 0.7  # try lowering to 0.5 if needed
if max_val >= threshold:
    h, w = shelter_img.shape[:2]
    cv.rectangle(region_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)
else:
    print("No good match found.")

cv.imshow('result', region_img)
cv.waitKey(0)
cv.destroyAllWindows()
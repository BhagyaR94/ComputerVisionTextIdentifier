import cv2
import easyocr
import matplotlib.pyplot as plt

imgpath = './data/exitonly.jpg'

image = cv2.imread(imgpath)
reader = easyocr.Reader(['en'], gpu=False)
text = reader.readtext(image)
threshold = 0.25
for t in text:
    bbox, text, score = t
    if score > threshold:
        cv2.rectangle(image, bbox[0], bbox[2], (0, 255, 0), 5)
        cv2.putText(image, text, bbox[0], cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.65, (255, 0, 0), 1)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)
# cap.set(10,130)
# cap.set(3, value)  # تنظیم عرض تصویر (عرض پنجره)
# cap.set(4, value)  # تنظیم ارتفاع تصویر (ارتفاع پنجره)
# cap.set(10, value)  # تنظیم روشنایی
# cap.set(11, value)  # تنظیم کنتراست
# cap.set(5, value)  # تنظیم عرض فریم
# cap.set(6, value)  # تنظیم ارتفاع فریم
# cap.set(12, value)  # تنظیم غنی‌سازی رنگ
# cap.set(13, value)  # تنظیم حسگر سفید
# cap.set(14, value)  # تنظیم تراکم رنگ
# cap.set(28, value)  # تنظیم فوکوس
# cap.set(15, value)  # تنظیم سرعت شاتر
# cap.set(16, value)  # تنظیم نوردهی
# cap.set(27, value)  # تنظیم زوم
# cap.set(cv2.CAP_PROP_FPS, value)  # تنظیم FPS

while True:
    success, img = cap.read() #cap.read() میاد فریم جدید ویدیو رو میخونه و اونو برمیگردونه
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #اگر دکمه q رو بزنیم حلقه رو میشکنه
        break


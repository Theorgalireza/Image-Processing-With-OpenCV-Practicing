import cv2
import numpy as np
# Cascade به معنای "آبشاری" هست.
# این الگوریتم به صورت مرحله‌ای (آبشاری) بررسی می‌کنه که آیا توی یه ناحیه چهره هست یا نه. اول با فیلترهای ساده شروع می‌کنه، بعد اگه نتیجه مثبت بود، وارد مراحل پیچیده‌تر می‌شه. این باعث می‌شه سریع‌تر بشه تشخیص داد.
# haarcascade_frontalface_default.xml یک فایل آموزش‌دیده‌شده‌ست که می‌دونه چطور چهره‌های روبرو رو پیدا کنه.


# این خط یک کلاسه تشخیص چهره بارگذاری می‌کنه. 
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

widthImg = 640
heightImg = 480

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

# #تصویر رو خاکستری می‌کنه. چرا؟ چون الگوریتم cascade فقط با تصاویر خاکستری کار می‌کنه، نه رنگی.
# # خاکستری شدن تصویر باعث کاهش اطلاعات غیرضروری و سرعت بیشتر پردازش می‌شه.
# imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)



# # ینجا چهره‌ها شناسایی می‌شن. یعنی الگوریتم می‌گرده دنبال نواحی‌ای که مثل چهره باشن.
# # 1.1 ➤ ضریب scale. یعنی تصویر رو کمی‌ کمی کوچیک می‌کنه و در هر مقیاس دنبال چهره می‌گرده.
# # 4 ➤ تعداد مینیمم نواحی نزدیک به هم که باید پیدا بشن تا مطمئن بشه اون ناحیه واقعاً چهره‌ست.
# # faces لیستی از مختصات چهره‌هاست، مثلا: [(x1, y1, w1, h1), (x2, y2, w2, h2), ...]
# faces = faceCascade.detectMultiScale(imgGray,1.1,4)


# روی هر چهره‌ای که پیدا شد، یه کادر قرمز (مستطیل) می‌کشه.
# (x,y) نقطه‌ی بالا-چپ کادره
# (x+w,y+h) نقطه‌ی پایین-راستشه
# (255,0,0) رنگ آبی در BGR (چون OpenCV از BGR استفاده می‌کنه)
# 2 ضخامت خط

while True:
    success, img = cap.read() #cap.read() میاد فریم جدید ویدیو رو میخونه و اونو برمیگردونه
    imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #If You want to detect more objects theres a lot of cascades avalaible onlin
    
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #اگر دکمه q رو بزنیم حلقه رو میشکنه
        break


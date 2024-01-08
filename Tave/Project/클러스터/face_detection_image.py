import os
import glob
import cv2

fpath = r"C://Users//김예영//Documents//Tave//img_crow//Image_crow//여자배우//가득희*.jpg"
for fpath in glob.glob(fpath):
    fpath_r = fpath.replace('ga(','(')
    os.rename(fpath, fpath_r)
    
face_cascade = cv2.CascadeClassifier(r'C://Users//김예영//Documents//tomato//CV//data//haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'C://Users//김예영//Documents//tomato//CV//data//haarcascade_eye.xml')

imgnum = 44
img = cv2.imread(str(imgnum)+".jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3,5)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
    cropped = img[y - int(h/4):y + h + int(h/4), x - int(w/4):x + w + int(w/4)]
    cv2.imwrite("cropped"+str(imgnum)+".png", cropped)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),2)


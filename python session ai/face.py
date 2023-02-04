import cv2

video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
        face_gray = gray[y:y + h, x:x + w]
        face_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(face_gray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 3)
    return frame


while True:
    ret, frame = video_capture.read()
    print(ret, frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    output = detect(gray, frame)
    cv2.imshow('FACE detection', output)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
video_capture.release()
cv2.destroyAllWindows

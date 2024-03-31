import cv2 as cv

img = cv.imread('./images/people.jpg')
img = cv.resize(img,(700,700))
grey = cv.cvtColor(img,cv.COLOR_BGR2RGB)

# either import the haas cascade or keep it locally
# face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haascascade_frontalface_default.xml')

face_cascade = cv.CascadeClassifier('har_face.xml')


# returns a list 
faces = face_cascade.detectMultiScale(grey,scaleFactor=1.1 , minNeighbors=3)

print(f'number of faces = {len(faces)}')


# detectmultiscale returns the cordinated of the rectange where the face is found
# we are creating the recatagnel around the face using those cordinates
for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('face',img)

cv.waitKey(0)
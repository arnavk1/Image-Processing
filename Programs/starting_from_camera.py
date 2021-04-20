import cv2
import datetime
cap = cv2.VideoCapture(0)

# fourcc = cv2.VideoWriter_fourcc(*'XVID')

# out = cv2.VideoWriter('newVideo.avi', fourcc, 25.0, (640,480))

while True:
    ret, frame = cap.read()
    if ret == True:
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' +str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10,50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        # out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
# out.release()
cv2.destroyAllWindows()


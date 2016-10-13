import cv2, socket, numpy

host = 'localhost'
port = 5565

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    rval, imgencode = cv2.imencode(".jpg", frame, [1,90])
    data = numpy.array(imgencode)
    stringData = data.tostring()

    s = socket.socket()
    s.connect((host, port))
    s.sendall(stringData)
    s.close()

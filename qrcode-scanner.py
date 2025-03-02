import pyzbar.pyzbar as pyzbar
import cv2
import pyperclip

webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    validacao, frame = webcam.read()
    while validacao:
        validacao, frame = webcam.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        decoded = pyzbar.decode(gray)
        
        for d in decoded: 
            x, y, w, h = d.rect

            barcode_data = d.data.decode("utf-8")
            barcode_type = d.type
            
            print(f"Código detectado: {barcode_data} (Tipo: {barcode_type})")
            pyperclip.copy(barcode_data)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            text = '%s (%s)' % (barcode_data, barcode_type)
            cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            
        cv2.imshow("QR Code Scanner (WebCam) | 'ESC' to exit.", frame)
        
        key = cv2.waitKey(2)
        if key == 27:
            break
            
webcam.release()
cv2.destroyAllWindows()




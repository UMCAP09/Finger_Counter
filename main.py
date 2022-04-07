import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0) # подключение к камере
mp_Hands = mp.solutions.hands # распознавание рук 
hands = mp_Hands.Hands(max_num_hands = 2) # характеристики переменной
mpDraw = mp.solutions.drawing_utils # инициализируем утилиту для рисования узлов

finger_Coord = [(8, 6), (12, 10), (16, 14), (20, 18)] # координаты узлов
thumb_Coord = (4, 2) # координаты узла большого пальца
   
while cap.isOpened(): # проверка доступа к камере
    success, image = cap.read() # получение картинки и переменной True/False
    if not success: # в случае неудачи
        print('Не удалось получить кадр с web-камеры')
        continue
    image = cv2.flip(image, 1) # зеркалим картинку
    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # преобразуем BGR в RGB
    result = hands.process(RGB_image) # запуск распознавания рук
    multiLandMarks = result.multi_hand_landmarks # извлечение узлов

    if multiLandMarks: # если руки есть 
        for idx, handLms in enumerate(multiLandMarks):
            lbl = result.multi_handedness[idx].classification[0].label
            print(lbl)
            upcount = 0
        for handlms in multiLandMarks:
            mpDraw.draw_landmarks(image, handlms, mp_Hands.HAND_CONNECTIONS)
            fingerslist = []
            for idx, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                fingerslist.append((cx, cy))
            for coordinate in finger_Coord:
                if fingerslist[coordinate[0]][1] < fingerslist[coordinate[1]][1]:
                    upcount += 1
            if fingerslist[thumb_Coord[0]][0] < fingerslist[thumb_Coord[1]][0]:
                upcount += 1



        cv2.putText(image, str(upcount), (50, 150), cv2.FONT_HERSHEY_PLAIN, 10, (0,200, 100), 10)
        print(upcount)
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == 27: # выход
        break

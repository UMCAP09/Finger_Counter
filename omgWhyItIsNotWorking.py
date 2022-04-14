class handDetector():    
    def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionProbability=0.5, track=0.5):
       self.mp_Hands = mp.solutions.hands # распознавание рук 
       self.hands = self.mp_Hands.Hands(mode, maxHands, modelComplexity, detectionProbability, track) # характеристики переменной
       self.mpDraw = mp.solutions.drawing_utils # инициализируем утилиту для рисования узлов

    def findHands(self, img):
        RGB_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # преобразуем BGR в RGB
        self.result = self.hands.process(RGB_image) # запуск распознавания рук
        

    def findPositionPoints(self):
        pass


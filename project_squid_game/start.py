import mediapipe as mp
import cv2
import numpy as np
import time
import pyttsx3



class MyGameStart():
    def __init__(self, name_lvl = "Niveau 1"):

        self.name_lvl = name_lvl
        self.cap = cv2.VideoCapture(0)
        self.cPos = 0
        self.startT = 0
        self.endT = 0
        self.userSum = 0
        self.dur = 0
        self.isAlive = 1
        self.isInit = False
        self.cStart, self.cEnd = 0, 0
        self.isCinit = False
        self.tempSum = 0
        self.winner = 0
        self.inFrame = 0
        self.inFramecheck = False
        self.thresh = 180

        self.list_talk = ["un deux trois", "soleil"]

    def calc_sum(self, landmarkList):
        tsum = 0
        for i in range(11, 33):
            tsum += (landmarkList[i].x * 480)

        return tsum



    def calc_dist(self, landmarkList):
        return (landmarkList[28].y * 640 - landmarkList[24].y * 640)



    def isVisible(self, landmarkList):
        if (landmarkList[28].visibility > 0.7) and (landmarkList[24].visibility > 0.7):
            return True
        return False


    def start_level(self):
        mp_pose = mp.solutions.pose
        pose = mp_pose.Pose()
        drawing = mp.solutions.drawing_utils

        im1 = cv2.imread('../project_game_squid_game/media/image/blue.PNG')
        im2 = cv2.imread('../project_game_squid_game/media/image/red.PNG')

        currWindow = im1

        while True:

            _, frm = self.cap.read()
            rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
            res = pose.process(rgb)
            frm = cv2.blur(frm, (5, 5))
            drawing.draw_landmarks(frm, res.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            if not (self.inFramecheck):
                try:
                    if self.isVisible(res.pose_landmarks.landmark):
                        self.inFrame = 1
                        self.inFramecheck = True
                    else:
                        self.inFrame = 0
                except:
                    print("AUCUNE VUE D'ENSEMBLE DE VOTRE CORPS")

            if self.inFrame == 1:
                if not (self.isInit):

                    engine_voice = pyttsx3.init('sapi5')
                    engine_voice.say(self.list_talk[0])
                    engine_voice.runAndWait()
                    currWindow = im1
                    self.startT = time.time()
                    self.endT = self.startT
                    self.dur = np.random.randint(1, 5)
                    self.isInit = True

                if (self.endT - self.startT) <= self.dur:
                    try:
                        m = self.calc_dist(res.pose_landmarks.landmark)
                        if m < self.thresh:
                            self.cPos += 1

                        print("BARRE DE PROGRESSION COURANTE : ", self.cPos)
                    except:
                        print("INVISIBLE")

                    self.endT = time.time()

                else:

                    if self.cPos >= 100:
                        print("GAGNANT")
                        self.winner = 1

                    else:
                        if not (self.isCinit):
                            self.isCinit = True
                            self.cStart = time.time()
                            self.cEnd = self.cStart
                            currWindow = im2
                            engine_voice = pyttsx3.init('sapi5')
                            engine_voice.say(self.list_talk[1])
                            engine_voice.runAndWait()
                            self.userSum = self.calc_sum(res.pose_landmarks.landmark)

                        if (self.cEnd - self.cStart) <= 3:
                            self.tempSum = self.calc_sum(res.pose_landmarks.landmark)
                            self.cEnd = time.time()
                            if abs(self.tempSum - self.userSum) > 150:
                                print("VOUS AVEZ PERDU LA PARTIE ", abs(self.tempSum - self.userSum))

                                self.isAlive = 0

                        else:
                            self.isInit = False
                            self.isCinit = False

                cv2.circle(currWindow, ((55 + 6 * self.cPos), 280), 15, (0, 0, 255), -1)

                mainWin = np.concatenate((cv2.resize(frm, (800, 400)), currWindow), axis=0)
                cv2.imshow("DEMO SQUID GAME BY ZEN", mainWin)


            else:
                cv2.putText(frm, "Aucune corpulence dans le frame", (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                            (0, 255, 0), 4)
                cv2.imshow("DEMO SQUID GAME BY ZEN", frm)

            if cv2.waitKey(1) == 27 or self.isAlive == 0 or self.winner == 1:
                cv2.destroyAllWindows()
                self.cap.release()
                break

        frm = cv2.blur(frm, (5, 5))

        if self.isAlive == 0:
            cv2.putText(frm, "Vous avez PERDU", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
            cv2.imshow("DEMO SQUID GAME BY ZEN", frm)

        if self.winner == 1:
            cv2.putText(frm, "Vous avez GAGNES", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)
            cv2.imshow("DEMO SQUID GAME BY ZEN", frm)

        cv2.waitKey(0)











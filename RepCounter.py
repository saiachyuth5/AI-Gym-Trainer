import cv2
import mediapipe as mp
import time
import numpy as np

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    return angle

mpPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
pose = mpPose.Pose()
counter = 0
state = None
posture = None
capture = cv2.VideoCapture(0)
#capture = cv2.VideoCapture("C:\\Users\\saiac\\OneDrive\\Desktop\\bicepcurl2.mp4")
pTime = 0
while True:
    success, img = capture.read()
    #imagRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(img)
    #if results.pose_landmarks:
    #    for id, pos in enumerate(results.pose_landmarks.landmark):
    #        print(id, pos)
    try:
        landmarks = results.pose_landmarks.landmark
        print(landmarks)
    except:
        print("Error occured")
        pass

    shoulder = [landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].x,
                landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].y]
    elbow = [landmarks[mpPose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mpPose.PoseLandmark.LEFT_ELBOW.value].y]
    wrist = [landmarks[mpPose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mpPose.PoseLandmark.LEFT_WRIST.value].y]
    left_hip = [landmarks[mpPose.PoseLandmark.LEFT_HIP.value].x, landmarks[mpPose.PoseLandmark.LEFT_HIP.value].y]

    angle1 = calculate_angle(shoulder,elbow,wrist)
    angle2 = calculate_angle(wrist,shoulder,left_hip)
    #cv2.putText(img,str(int(fps)), (75,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

     # Curl counter logic
    if angle1 > 160:
         stage = "down"
    if angle1 < 30 and stage == 'down':
         stage = "up"
         counter += 1

    if angle2 > 30:
        posture = "bad"
    else:
        posture = "good"

    # Render curl counter
    # Setup status box
    cv2.rectangle(img, (0, 0), (150, 73), (150, 117, 16), -1)

    # if posture == "good":
    #     cv2.rectangle(img, (150, 0), (300, 73), (0, 200, 0), -1)
    #     cv2.putText(img, 'GOOD', (165, 12),
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    # elif posture == "bad":
    #     cv2.rectangle(img, (150, 0), (300, 73), (0, 0, 200), -1)
    #     cv2.putText(img, 'BAD', (165, 12),
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

    # Rep data
    cv2.putText(img, 'REPS:', (15, 12),
                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(img, str(counter),
                 (10, 60),
                 cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, str(angle1),
                tuple(np.multiply(elbow, [640, 480]).astype(int)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                )
    cv2.putText(img, str(angle2),
                tuple(np.multiply(shoulder, [640, 480]).astype(int)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                )

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    # Extract landmarks
    #try:
    #    landmarks = results.pose_landmarks.landmark
    #    print(landmarks)
    #except:
    #    pass
    #cv2.putText(img,str(int(fps)), (75,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

    mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    cv2.imshow("Image", img)

    cv2.waitKey(10)



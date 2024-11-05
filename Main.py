import threading

import cv2
from deepface import DeepFace

cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter=0
flag=0

face_match = False

reference_img= cv2.imread("reference.jpg")


def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True
        else: 
            face_match = False

    except ValueError:
        face_match = False



while True:
    ret, frame = cap.read()

    if ret: 
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()

            except ValueError:
                pass
        counter+=1

        if face_match:
            cv2.destroyAllWindows()
            flag=1
            print("Matched!")
            print(flag)
            break

        
        else:
            cv2.putText(frame, "NO MATCH.", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0,    255), 2)
        
        cv2.imshow("video", frame)


    key=cv2.waitKey(1)
    if key== ord("q"):
        break

cv2.destroyAllWindows()





if flag==1:
    import tkinter as tk
    from tkinter import messagebox

    # Function to validate the login
    def validate_login():
        userid = username_entry.get()
        password = password_entry.get()

        # You can add your own validation logic here
        if userid == "abcd" and password == "1234":
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
        else:
            messagebox.showerror("Login Failed", "Invalid userid and password")

    # Create the main window
    parent = tk.Tk()
    parent.title("Login Form")

    # Create and place the username label and entry
    username_label = tk.Label(parent, text="Userid:")
    username_label.pack()

    username_entry = tk.Entry(parent)
    username_entry.pack()

    # Create and place the password label and entry
    password_label = tk.Label(parent, text="Password:")
    password_label.pack()

    password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
    password_entry.pack()

    # Create and place the login button
    login_button = tk.Button(parent, text="Login", command=validate_login)
    login_button.pack()



    # Start the Tkinter event loop
    parent.mainloop()
    
else:
    print("Face not recognized.")

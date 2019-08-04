import threading
import time
def job():
    for i in range(5):
        print("Child thread:",i)
        time.sleep(1)

def cmdTHREADING():
    t=threading.Thread(target=job)
    t.start()
    for i in range(3):
        print("Main thread:",i)
        time.sleep(1)
    t.join()
    print("Done.")

GUI_TYPE="Button"
GUI_TEXT="THREADING"
GUI_COMMAND="cmdTHREADING"

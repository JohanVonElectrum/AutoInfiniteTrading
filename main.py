from subprocess import Popen, PIPE, STDOUT
from PIL import ImageGrab, Image
import sys
import pyautogui
import requests
import threading

joined = False

def read_from_popen(popen: Popen):
    for stdout_line in iter(client.stdout.readline, ""):
        if stdout_line:
            text = stdout_line.decode("utf-8").replace("\n", "")
            print(text)
            if "<login" == text:
                print("Logged In!")
                global joined
                joined = True
            elif ">!quartz" == text:
                print(f"We have {quartz} quartz blocks.")
                requests.post("http://localhost:404/message", json={"message": f"We have {quartz} quartz blocks."})


if __name__ == "__main__":
    client = Popen(["node", "run.js"] + sys.argv[1:], stdout=PIPE, stderr=STDOUT)

    quartz = int(sys.argv[7])

    read_th = threading.Thread(target=read_from_popen, args=(client,))
    read_th.start()

    while True:
        if not joined:
            continue

        pyautogui.rightClick()

        img: Image.Image = ImageGrab.grab().load()
        rgb = img[880, 400]
        if rgb == (198, 198, 198):
            requests.post("http://localhost:404/connect", json={"host": sys.argv[1], "port": sys.argv[2], "version": sys.argv[3]})
            print("Logged Out!")
            joined = False
            pyautogui.rightClick(x=600, y=790)
            pyautogui.press("esc")
            quartz += 12
            requests.post("http://localhost:404/message", json={"message": f"We have {quartz} quartz blocks."})

    read_th.join()
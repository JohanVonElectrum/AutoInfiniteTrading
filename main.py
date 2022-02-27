from subprocess import Popen, PIPE
from PIL import ImageGrab, Image
import sys
import pyautogui

if __name__ == "__main__":
    client = Popen(["MinecraftClient.exe"], stdout=PIPE, stdin=PIPE, stderr=PIPE)

    quartz = int(sys.argv[1])
    joined = False

    while True:
        for stdout_line in iter(client.stdout.readline, ""):
            if stdout_line:
                text = stdout_line.decode("utf-8").replace("\n", "")
                print(text)
                if "[MCC] Server was successfully joined." == text:
                    joined = True
                elif "!quartz":
                    client.communicate(input=f"We have {quartz} quartz blocks.".encode("utf-8"))

        if not joined:
            continue

        pyautogui.rightClick()

        img: Image.Image = ImageGrab.grab().load()
        rgb = img[880, 400]
        if rgb == (198, 198, 198):
            client.communicate(input="/reco".encode("utf-8"))[0].decode("utf-8")
            joined = False
            pyautogui.rightClick(x=600, y=790)
            pyautogui.press("esc")
            quartz += 12

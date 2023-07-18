import subprocess
import multiprocessing
import os
import time

def run_script(script):
    command = "eeg\Scripts\\activate.bat && python " + script
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    script1 = multiprocessing.Process(target=run_script, args=('start_stimulus.py',))
    script2 = multiprocessing.Process(target=run_script, args=('start_unicorn.py',))

    script1.start()
    script2.start()

    script1.join()

    os.system("taskkill /f /im python.exe") # Kill all python processes when stimulus is exited


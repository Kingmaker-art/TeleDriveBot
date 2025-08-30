# copyright 2025 © Kingmaker | https://github.com/Kingmaker-art

# @title 🖥️ Main Colab Leech Code (changed)


# @title Main Code
# @markdown <div><center><img src="https://github.com/user-attachments/assets/9aa1d07d-e3a5-411e-ae0f-e9108b1b1249" height=80></center></div>
# @markdown <center><h4><a href="https://github.com/Kingmaker-art/TeleDriveBot/wiki/INSTRUCTIONS">READ</a> How to use</h4></center>

# @markdown <br>

API_ID = 0  # @param {type: "integer"}
API_HASH = ""  # @param {type: "string"}
BOT_TOKEN = ""  # @param {type: "string"}
USER_ID = 0  # @param {type: "integer"}
DUMP_ID = 0  # @param {type: "integer"}


import subprocess, time, json, shutil, os
from IPython.display import clear_output
from threading import Thread

Working = True

banner = '''
  ______   __        ____             _       
 /_  __/  / /  ___  / __ ) ___   ____(_)____ _
  / /    / /  / _ \\/ __  |/ _ \\ / ___/ // __ `/
/ /    / /__/  __/ /_/ //  __// /   / // /_/ / 
/_/    /____/\\___/_____/ \\___//_/   /_/ \\__,_/  
                                               
'''
print(banner)

def Loading():
    white = 37
    black = 0
    while Working:
        print("\r" + "░"*white + "▒▒"+ "▓"*black + "▒▒" + "░"*white, end="")
        black = (black + 2) % 75
        white = (white -1) if white != 0 else 37
        time.sleep(2)
    clear_output()


_Thread = Thread(target=Loading, name="Prepare", args=())
_Thread.start()

if len(str(DUMP_ID)) == 10 and "-100" not in str(DUMP_ID):
    n_dump = "-100" + str(DUMP_ID)
    DUMP_ID = int(n_dump)

if os.path.exists("/content/sample_data"):
    shutil.rmtree("/content/sample_data")

cmd = "git clone https://github.com/Kingmaker-art/TeleDriveBot"
proc = subprocess.run(cmd, shell=True)
cmd = "apt update && apt install ffmpeg aria2"
proc = subprocess.run(cmd, shell=True)
cmd = "pip3 install -r /content/TeleDriveBot/requirements.txt"
proc = subprocess.run(cmd, shell=True)

credentials = {
    "API_ID": API_ID,
    "API_HASH": API_HASH,
    "BOT_TOKEN": BOT_TOKEN,
    "USER_ID": USER_ID,
    "DUMP_ID": DUMP_ID,
}

with open('/content/TeleDriveBot/credentials.json', 'w') as file:
    file.write(json.dumps(credentials))

Working = False

if os.path.exists("/content/TeleDriveBot/tg_drivebot.session"):
    os.remove("/content/TeleDriveBot/tg_drivebot.session") # Remove previous bot session
    
print("\rStarting Bot....")

!cd /content/TeleDriveBot/ && python3 -m tele_drive_bot #type:ignore

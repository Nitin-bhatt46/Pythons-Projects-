
## text to speak 
## for windows

import os


if __name__ == '__main__':

    while True:
           txt = str(input("Enter anything to pronounce it: "))
           if txt == "q":
                    print("Exited..")
                    break
           cmd = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{txt}')"
           os.system(cmd)

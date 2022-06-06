#!/usr/bin/env python3

##### LICENSE
# Copyright (C) 2021-22 Muhammed Abdurrahman (MuKonqi)

# You just DO WHAT THE FUCK YOU WANT TO.
# Sadece NE HALT EDERSEN ET.

import time
import os
def entry():
    print("Welcome to TEAfa (The Example App For apiutaller)!\nTEAfa (The Example App For apiutaller)'ya hoşgeldiniz!")
    main=input("Do you want exit TEAfa or restart TEAfa with root user?\nTEAfa'dan çıkmak ister misiniz ya da TEAFa'yı kök kullanıcıyla yeniden başlatmayı mı istersiniz?\nOptions / Seçenekler: y / n / r \nAnswer / Cevap: ")
    if main == "y":
        print("Wait! -----\nBekle! -----")
        time.sleep(1)
        print("Wait! ----\nBekle! ----")
        time.sleep(1)
        print("Wait! ---\nBekle! ---")
        time.sleep(1)
        print("Wait! --\nBekle! --")
        time.sleep(1)
        print("See you! -\nGörüşürüz! -")
        time.sleep(1)
        exit()
    if main == "n":
        print("Let's go!\nHaydi gidelim!")
        entry()
    if main == "r":
        print("Don't wait!\nBekleme!")
        os.system("pkexec python3 /usr/bin/teafa")
        exit()
    else:
        print("Stop, you can't go!\nDur, gidemezsin!")
        entry()
entry()
#!/usr/bin/env python3

##### LICENSE !!!!!
# Copyright (C) 2022 Muhammed Abdurrahman
# TEAfa is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# TEAfa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with TEAfa.  If not, see <https://www.gnu.org/licenses/>.

import time
import os
print("Copyright (C) 2022 Muhammed Abdurrahman")
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
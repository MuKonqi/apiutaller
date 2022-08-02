#!/usr/bin/env python3
#-*-coding:utf-8-*-

##### LICENSE !!!!!
# Copyright (C) 2022 Muhammed Abdurrahman
# TEAfunknown is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# TEAfunknown is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with TEAfunknown.  If not, see <https://www.gnu.org/licenses/>.

lang="" # Don't chnage this!
word_after_TEAf="apiutaller" # Don't forget change this!

import time
import getpass
username=getpass.getuser()

print("Copyright (C) 2022 Muhammed Abdurrahman")

def entry():
    def def_exit():
        if lang == "en":
            print("Wait! -----")
            time.sleep(1)
            print("Wait! ----")
            time.sleep(1)
            print("Wait! ---")
            time.sleep(1)
            print("Wait! --")
            time.sleep(1)
            print("See you! -")
        elif lang == "tr":
            print("Bekle! -----")
            time.sleep(1)
            print("Bekle! ----")
            time.sleep(1)
            print("Bekle! ---")
            time.sleep(1)
            print("Bekle! --")
            time.sleep(1)
            print("Görüşürüz! -")
        time.sleep(1)
        exit()

    def def_wrong_answer():
        if lang == "en":
            print("\n\n\n\n\n    FATAL ERROR!\n\n TEAf"+word_after_TEAf+" has encountered a fatal problem and needs to be closed and restarted.\n\nCurrently collecting some error information... %3 complete.")
            time.sleep(1)
            print("Currently collecting some error information... %21 complete.")
            time.sleep(1)
            print("Currently collecting some error information... %40 complete.")
            time.sleep(1)
            print("Currently collecting some error information... %63 complete.")
            time.sleep(1)
            print("Currently collecting some error information... %77 complete.")
            time.sleep(1)
            print("Currently collecting some error information... %99 complete.")
            time.sleep(1)
            print("Currently collecting some error information... %100 (completely) complete.")
            print("\nThese were a joke. Maybe it wasn't funny but since you gave 2 wrong answers this was triggered.\n\n\n\n\n")
        elif lang == "tr":
            print("\n\n\n\n\n     ÖLÜMCÜL HATA!\n\n TEAf"+word_after_TEAf+" önemli bir sorunla karşılaştı ve kapatılıp yeniden başlatılması gerekiyor.\n\nŞu anda bazı hata bilgileri toplanıyor... %3 tamamlandı.")
            time.sleep(1)
            print("Şu anda bazı hata bilgileri toplanıyor... %21 tamamlandı.")
            time.sleep(1)
            print("Şu anda bazı hata bilgileri toplanıyor... %40 tamamlandı.")
            time.sleep(1)
            print("Şu anda bazı hata bilgileri toplanıyor... %63 tamamlandı.")
            time.sleep(1)
            print("Şu anda bazı hata bilgileri toplanıyor... %77 tamamlandı.")
            time.sleep(1)
            print("Şu anda bazı hata bilgileri toplanıyor... %99 tamamlandı.")
            time.sleep(1)
            print("Şu anda bazı hata bilgileri toplanıyor... %100 (tamamen) tamamlandı.")
            print("\nBunlar şakaydı. Belki komik değildi ama 2 yanlış cevap verdiğiniz için bu tetiklendi.\n\n\n\n\n")
        entry()


    def en():
        wrong_answer=0 # Don't change this!

        question1=input("\nIs there a capital word i (İ) in English? Options: yes / no\nYour answer: ")
        if question1 == "n" or question1 == "no":
            print("Congratulations!")
        else:
            wrong_answer+=1
            print('Unfortunately your answer is wrong. The correct answer was no.')
        
        question2=input('\n"He gave a greeting to the world: Hello world!" How many words are in previous sentence?\nYour answer: ')
        if question2 == "9":
            print("Congratulations!")
        else:
            wrong_answer+=1
            print('Unfortunately your answer is wrong. The correct answer was 9.')
        
        if wrong_answer == 2:
            def_wrong_answer()

        question3=input("\nWhat is [(3+5).(1+4)+35+37]:4+16?\nYour answer: ")
        if question3 == "44":
            print("Congratulations!")
        else:
            wrong_answer+=1
            print('Unfortunately your answer is wrong. The correct answer was 44.')

        if wrong_answer == 2:
            def_wrong_answer()

        question4=input("\nWhich is sentence is spelled correctly:\n   A) I think you will be better in future.\n   B) i think u will be better in future\nYour answer: ")
        if question4 == "A)" or question4 == "a)" or question4 == "a" or question4 == "A":
            print("Congratulations!")
        else:
            wrong_answer+=1
            print('Unfortunately your answer is wrong. The correct option was A.')

        if wrong_answer == 2:
            def_wrong_answer()

        question5=input("\nWhat is your username?\nYour answer: ")
        if question5 == username:
            print("Congratulations, that's all!\n\nThank you for spending some of your time on this program.\n")
            def_exit()
        else:
            wrong_answer+=1
            print("Sorry, your answer is wrong. The correct answer was "+username+".")
            if wrong_answer == 2:
                def_wrong_answer()
            print("All questions are finished, thanks for spending some of your time on this program.")
            def_exit()   


    def tr():
        wrong_answer=0 # Don't change this!

        answer1=input("\nTürkçede q or Q var mı? Seçenekler: evet / hayır\nCevabınız: ")
        if answer1 == "h" or answer1 == "hayır":
            print("Tebrikler!")
        else:
            wrong_answer+=1
            print('Maalesef cevabınız yanlış. Doğru cevap hayır idi.')
        
        question2=input('\n"Dünyaya selam verdi: Merhaba dünya!" Bir önceki cümlede kaç kelime var?\nCevabınız: ')
        if question2 == "5":
            print("Tebrikler!")
        else:
            wrong_answer+=1
            print('Maalesef cevabınız yanlış. Doğru cevap 5 idi.')
        
        if wrong_answer == 2:
            def_wrong_answer()

        question3=input("\n[(3+5).(1+4)+35+37]:4+16 nedir?\nCevabınız: ")
        if question3 == "44":
            print("Tebrikler!")
        else:
            wrong_answer+=1
            print('Maalesef cevabınız yanlış. Doğru cevap 44 idi.')

        if wrong_answer == 2:
            def_wrong_answer()

        question4=input("\nHangi cümle doğru yazılmış:\n A) Bence gelecekte daha iyi olacaksınız.\n B) bence gelcekte daha ii olcaksınız\nCevabınız: ")
        if question4 == "A)" or question4 == "a)" or question4 == "a" or question4 == "A":
            print("Tebrikler!")
        else:
            wrong_answer+=1
            print('Maalesef cevabınız yanlış. Doğru seçenek A idi.')

        if wrong_answer == 2:
            def_wrong_answer()

        question5=input("\nKullanıcı adınız nedir?\nCevabınız: ")
        if question5 == username:
            print("Tebrikler, hepsi bu kadar!\n\nZamanınızın bir kısmını bu programa ayırdığınız için teşekkür ederiz.\n")
            def_exit() 
        else:
            wrong_answer+=1
            print("Maalesef cevabınız yanlış. Doğru cevap "+username+" idi.")
            if wrong_answer == 2:
                def_wrong_answer()
            print("Tüm sorular bitmiştir, zamanınızın bir kısmını bu programa ayaırdığınız için teşekkürler.")
            def_exit()          

    print("Welcome to TEAf"+word_after_TEAf+" (The Example App for "+word_after_TEAf+")!\nTEAf"+word_after_TEAf+" (The Example App for "+word_after_TEAf+")'a hoşgeldiniz!")
    langinput=input("\nPlease select a language.\nLütfen bir dil seçiniz.\nOptions / Seçenekler: en / tr: ")
    if langinput == "en":
        lang="en"
        print("English selected.")
        en()
    elif langinput == "tr":
        lang="tr"
        print("Türkçe seçildi.")
        tr()
entry()
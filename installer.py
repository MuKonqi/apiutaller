#!/usr/bin/env python3

##### LICENSE
# Copyright (C) 2021-22 Muhammed Abdurrahman (MuKonqi)

# You just DO WHAT THE FUCK YOU WANT TO.
# Sadece NE HALT EDERSEN ET.

##### English
## DEAR DEVELOPER,
# You can make comment lines if you want skip some steps.
# You must say or specify your program dependencies and supportted distros in README.md. apitaller don't control user's distros.
# You must say or specify installing dependencies in README.md. apitaller don't install dependencies.
# You must set up variables in installer.py.

##### Turkish
## Sevgili geliştirici,
# Siz bazı adımları atlamak istersen yorum satırları yapabilirsiniz.
# Siz programının bağımlılıklarını ve desteklediği dağıtımları README.md içinde demelisiniz veya belirtmelisiniz. apitaller, kullanıcının dağıtımını kontrol etmez.
# Siz bağımlılıkları kurmayı README.md'de demelisiniz veya belirtmelisiniz. apitaller, bağımlılıkları kurmaz.
# Siz installer.py'de değişkenleri ayarlamalısınız.

import os

appname="peytehow"
appfolder="/usr/bin/"
appfile="peytehow.py"
policyfile="python3.policy"
appdesktopfile="peytehow.desktop"
mainappfolder="/usr/local/bin/"
licensename="WTFPL"

def main_EN():
    os.system("chmod +x *")

    if os.path.isdir(appfolder):
        pass
    else:
        os.system("mkdir "+appfolder)
    os.system("cd app ; chmod +x "+appfile+" ; mv "+appfile+" "+appname+" ; mv "+appname+" "+appfolder)
    if os.path.isfile(appfolder+appname):
        pass
    else:
        print("Error! This step is first. Closing apitaller...")
        exit()
        
    if os.path.isdir("/usr/share/polkit-1/actions"):
        pass
    else:
        os.system("mkdir /usr/share/polkit-1/actions")
    os.system("cd app ; mv "+policyfile+" /usr/share/polkit-1/actions")
    if os.path.isfile("/usr/share/polkit-1/actions/"+policyfile):
        pass
    else:
        print("Error! This step is second. Closing apitaller...")
        exit()

    if os.path.isdir("/usr/share/applications"):
        pass
    else:
        os.system("mkdir /usr/share/applications")
    os.system("cd app ; mv "+appdesktopfile+" /usr/share/applications")
    if os.path.isfile("/usr/share/applications/"+appdesktopfile):
        pass
    else:
        print("Error! This step is third. Closing apitaller...")
        exit()

    if os.path.isdir(mainappfolder):
        pass
    else:
        if mainappfolder == "/usr/local/bin":
            os.system("mkdir /usr/local ; mkdir /usr/local/bin/")
        else:
            os.system("mkdir "+mainappfolder)
    os.system("mkdir "+mainappfolder+appname)
    os.system("cd app ; mv * "+mainappfolder+appname)
    os.system("mkdir "+mainappfolder+appname+"/apiutaller")
    os.system("rm -rf app ; mv * "+mainappfolder+appname+"/apiutaller")
    if os.path.isdir(mainappfolder+appname):
        print("Successful! You have this program "+appname+" at the moment. Thank you for choosing us!")
        exit()
    else:
        print("Error! This step is last. Closing apitaller...")
        exit()


def license_EN():
    license=input("Hello! I try installing "+appname+".\nI'm licensed with WTFPL!\n"+appname+" is under the "+licensename+"!\nDo you agree there?\nOptions: y or n\nAnswer: ")
    if license == "y":
        main_EN()
    if license == "n":
        print("I'm sorry, you can't use "+appname+" and apitaller, because you don't agree licenses!\nClosing apitaller...")
        exit()



def main_TR():
    os.system("chmod +x *")

    if os.path.isdir(appfolder):
        pass
    else:
        os.system("mkdir "+appfolder)
    os.system("cd app ; chmod +x "+appfile+" ; mv "+appfile+" "+appname+" ; mv "+appname+" "+appfolder)
    if os.path.isfile(appfolder+appname):
        pass
    else:
        print("Hata! Bu adım birinci. apitaller kapatılıyor...")
        exit()
        
    if os.path.isdir("/usr/share/polkit-1/actions"):
        pass
    else:
        os.system("mkdir /usr/share/polkit-1/actions")
    os.system("cd app ; mv "+policyfile+" /usr/share/polkit-1/actions")
    if os.path.isfile("/usr/share/polkit-1/actions/"+policyfile):
        pass
    else:
        print("Hata! Bu adım ikinci. apitaller kapatılıyor...")
        exit()

    if os.path.isdir("/usr/share/applications"):
        pass
    else:
        os.system("mkdir /usr/share/applications")
    os.system("cd app ; mv "+appdesktopfile+" /usr/share/applications")
    if os.path.isfile("/usr/share/applications/"+appdesktopfile):
        pass
    else:
        print("Hata! Bu adım üçüncü. apitaller kapatılıyor...")
        exit()

    if os.path.isdir(mainappfolder):
        pass
    else:
        if mainappfolder == "/usr/local/bin":
            os.system("mkdir /usr/local ; mkdir /usr/local/bin/")
        else:
            os.system("mkdir "+mainappfolder)
    os.system("mkdir "+mainappfolder+appname)
    os.system("cd app ; mv * "+mainappfolder+appname)
    os.system("mkdir "+mainappfolder+appname+"/apiutaller")
    os.system("rm -rf app ; mv * "+mainappfolder+appname+"/apiutaller")
    if os.path.isdir(mainappfolder+appname):
        print("Başarılı! Siz artık "+appname+" programına sahipsiniz. Bizi seçtiğiniz için teşekkürler!")
        exit()
    else:
        print("Hata! Bu adım sonuncu. apitaller kapatılıyor...")
        exit()

def license_TR():
    license=input("Merhabalar! Ben "+appname+" uygulamasını yüklemeyi deneyeceğim.\nBen WTFPL ile lisanslıyım!\nBunları kabul ediyor musunuz?\nSeçenekler: e ya da h\nCevap: ")
    if license == "e":
        main_TR()
    if license == "h":
        print("Üzgünüm, siz "+appname+" ile apitaller'i kullanamazsınız, çünkü siz lisansları kabul etmediniz!\napitaller kapatılıyor...")
        exit()




def entry():
    language=input("Choose English or Turkish as a language.\nLütfen İngilizce veya Türkçe'yi bir dil olarak seçiniz.\nOptions / Seçenekler: en / tr\nLanguage / Dil: ")
    if language == 'en':
        print("English selected.")
        license_EN()
    if language == 'tr':
        print("Türkçe seçildi.")
        license_TR()
entry()
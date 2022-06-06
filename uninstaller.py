#!/usr/bin/env python3

##### LICENSE
# Copyright (C) 2021-22 Muhammed Abdurrahman (MuKonqi)

# You just DO WHAT THE FUCK YOU WANT TO.
# Sadece NE HALT EDERSEN ET.

##### English
## DEAR DEVELOPER,
# You can make comment lines if you want skip some steps.
# You must say or specify supportted distros in README.md. apitaller don't control user's distros.
# You must set up variables in uninstaller.py.

##### Turkish
## Sevgili geliştirici,
# Siz bazı adımları atlamak istersen yorum satırları yapabilirsiniz.
# Siz desteklediği dağıtımları README.md içinde demelisiniz veya belirtmelisiniz. apitaller, kullanıcının dağıtımını kontrol etmez.
# Siz uninstaller.py'de değişkenleri ayarlamalısınız.

import os

appname="peytehow"
appfolder="/usr/bin/"
appfile="peytehow.py"
policyfile="python3.policy"
appdesktopfile="peytehow.desktop"
mainappfolder="/usr/local/bin/"
licensename="WTFPL"

def main_EN():
    os.system("cd "+appfolder+" ; rm "+appname)
    if os.path.isfile(appfolder+appname):
        print("Error! This step is first. Closing aputaller...")
        exit()
    else:
        pass
        
    os.system("cd /usr/share/polkit-1/actions ; rm "+policyfile)
    if os.path.isfile("/usr/share/polkit-1/actions/"+policyfile):
        print("Error! This step is second. Closing aputaller...")
        exit()
    else:
        pass

    os.system("cd /usr/share/applications ; rm "+appdesktopfile)
    if os.path.isfile("/usr/share/applications/"+appdesktopfile):
        print("Error! This step is third. Closing aputaller...")
        exit()
    else:
        pass

    os.system("cd "+mainappfolder+" ; rm -rf "+appname)
    if os.path.isdir(mainappfolder+appname):
        print("Error! This step is last. Closing aputaller...")
        exit()
    else:
        print("Successful! You haven't this "+appname+" at the moment. We are happy if you share uninstalling reason!")
        exit()


def license_EN():
    license=input("Hello! I try uninstalling "+appname+".\nI'm licensed with WTFPL!\n"+appname+" is under the "+licensename+"!\nDo you agree there?\nOptions: y or n\nAnswer: ")
    if license == "y":
        main_EN()
    if license == "n":
        print("I'm sorry, you can't use "+appname+" and aputaller, because you don't agree there!\nClosing aputaller...")
        exit()



def main_TR():
    os.system("cd "+appfolder+" ; rm "+appname)
    if os.path.isfile(appfolder+appname):
        print("Hata! Bu adım birinci. aputaller kapatılıyor...")
        exit()
    else:
        pass
        
    os.system("cd /usr/share/polkit-1/actions ; rm "+policyfile)
    if os.path.isfile("/usr/share/polkit-1/actions/"+policyfile):
        print("Hata! Bu adım ikinci. aputaller kapatılıyor...")
        exit()
    else:
        pass

    os.system("cd /usr/share/applications ; rm "+appdesktopfile)
    if os.path.isfile("/usr/share/applications/"+appdesktopfile):
        print("Hata! Bu adım üçüncü. aputaller kapatılıyor...")
        exit()
    else:
        pass

    os.system("cd "+mainappfolder+" ; rm -rf "+appname)
    if os.path.isdir(mainappfolder+appname):
        print("Hata! Bu adım sonuncu. aputaller kapatılıyor...")
        exit()
    else:
        print("Başarılı! Siz artık "+appname+" programına sahip değilsiniz. Kaldırma sebebini bizle paylaşırsanız seviniriz.")
        exit()

def license_TR():
    license=input("Merhabalar! Ben "+appname+" uygulamasını silmeyi deneyeceğim.\nBen WTFPL ile lisanslıyım!\nBunları kabul ediyor musunuz?\nSeçenekler: e ya da h\nCevap: ")
    if license == "e":
        main_TR()
    if license == "h":
        print("Üzgünüm, siz "+appname+" ile aputaller'i kullanamazsınız, çünkü siz onları kabul etmediniz!\naputaller kapatılıyor...")
        exit()




def entry():
    language=input("Choose English or Turkish as a language.\nLütfen İngilizce veya Türkçe'yi bir dil olarak seçiniz.\nOptions / Seçenekler: en / tr\nLanguage / Dil: ")
    if language == 'en':
        print("English selected.")
        license_EN()
    if language == 'tr':
        print("Türkçe seçildi.")#!/usr/bin/env python3

##### LICENSE
# Copyright (C) 2021-22 Muhammed Abdurrahman (MuKonqi)

# You just DO WHAT THE FUCK YOU WANT TO.
# Sadece NE HALT EDERSEN ET.

##### English
## DEAR DEVELOPER,
# You can make comment lines if you want skip some steps.
# You must say or specify supportted distros in README.md. apitaller don't control user's distros.
# You must set up variables in uninstaller.py.

##### Turkish
## Sevgili geliştirici,
# Siz bazı adımları atlamak istersen yorum satırları yapabilirsiniz.
# Siz desteklediği dağıtımları README.md içinde demelisiniz veya belirtmelisiniz. apitaller, kullanıcının dağıtımını kontrol etmez.
# Siz uninstaller.py'de değişkenleri ayarlamalısınız.

import os

appname="peytehow"
appfolder="/usr/bin/"
appfile="peytehow.py"
policyfile="python3.policy"
appdesktopfile="peytehow.desktop"
mainappfolder="/usr/local/bin/"
licensename="WTFPL"

def main_EN():
    os.system("cd "+appfolder+" ; rm "+appname)
    if os.path.isfile(appfolder+appname):
        print("Error! This step is first. Closing aputaller...")
        exit()
    else:
        pass
        
    os.system("cd /usr/share/polkit-1/actions ; rm "+policyfile)
    if os.path.isfile("/usr/share/polkit-1/actions/"+policyfile):
        print("Error! This step is second. Closing aputaller...")
        exit()
    else:
        pass

    os.system("cd /usr/share/applications ; rm "+appdesktopfile)
    if os.path.isfile("/usr/share/applications/"+appdesktopfile):
        print("Error! This step is third. Closing aputaller...")
        exit()
    else:
        pass

    os.system("cd "+mainappfolder+" ; rm -rf "+appname)
    if os.path.isdir(mainappfolder+appname):
        print("Error! This step is last. Closing aputaller...")
        exit()
    else:
        print("Successful! You haven't this "+appname+" at the moment. We are happy if you share uninstalling reason!")
        exit()


def license_EN():
    license=input("Hello! I try uninstalling "+appname+".\nI'm licensed with WTFPL!\nDo you agree there?\nOptions: y or n\nAnswer: ")
    if license == "y":
        main_EN()
    if license == "n":
        print("I'm sorry, you can't use aputaller, because you don't agree license!\nClosing aputaller...")
        exit()



def main_TR():
    os.system("cd "+appfolder+" ; rm "+appname)
    if os.path.isfile(appfolder+appname):
        print("Hata! Bu adım birinci. aputaller kapatılıyor...")
        exit()
    else:
        pass
        
    os.system("cd /usr/share/polkit-1/actions ; rm "+policyfile)
    if os.path.isfile("/usr/share/polkit-1/actions/"+policyfile):
        print("Hata! Bu adım ikinci. aputaller kapatılıyor...")
        exit()
    else:
        pass

    os.system("cd /usr/share/applications ; rm "+appdesktopfile)
    if os.path.isfile("/usr/share/applications/"+appdesktopfile):
        print("Hata! Bu adım üçüncü. aputaller kapatılıyor...")
        exit()
    else:
        pass

    os.system("cd "+mainappfolder+" ; rm -rf "+appname)
    if os.path.isdir(mainappfolder+appname):
        print("Hata! Bu adım sonuncu. aputaller kapatılıyor...")
        exit()
    else:
        print("Başarılı! Siz artık "+appname+" programına sahip değilsiniz. Kaldırma sebebini bizle paylaşırsanız seviniriz.")
        exit()

def license_TR():
    license=input("Merhabalar! Ben "+appname+" uygulamasını silmeyi deneyeceğim.\nBen WTFPL ile lisanslıyım!\nBunları kabul ediyor musunuz?\nSeçenekler: e ya da h\nCevap: ")
    if license == "e":
        main_TR()
    if license == "h":
        print("Üzgünüm, siz aputaller'i kullanamazsınız, çünkü siz lisansı kabul etmediniz!\naputaller kapatılıyor...")
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
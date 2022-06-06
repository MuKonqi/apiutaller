#!/usr/bin/env python3

##### LICENSE
# Copyright (C) 2021-22 Muhammed Abdurrahman (MuKonqi)

# You just DO WHAT THE FUCK YOU WANT TO.
# Sadece NE HALT EDERSEN ET.

##### English
## DEAR DEVELOPER,
# You can make comment lines if you want skip some steps.
# You must say or specify your program dependencies and supportted distros in README.md. apuitaller don't control user's distros.
# You must say or specify installing dependencies in README.md. apiutaller don't install dependencies.
# You must set up variables in apiutaller.py.

##### Turkish
## Sevgili geliştirici,
# Siz bazı adımları atlamak istersen yorum satırları yapabilirsiniz.
# Siz programının bağımlılıklarını ve desteklediği dağıtımları README.md içinde demelisiniz veya belirtmelisiniz. apiutaller, kullanıcının dağıtımını kontrol etmez.
# Siz bağımlılıkları kurmayı README.md'de demelisiniz veya belirtmelisiniz. apiutaller, bağımlılıkları kurmaz.
# Siz apiutaller.py'de değişkenleri ayarlamalısınız.

import os

appname="apiutaller"
appfolder="/usr/bin/"
appfile="apiutaller.py"
policyfile="python3.policy"
appdesktopfile="apiutaller.desktop"
mainappfolder="/usr/local/bin/"
licensename="WTFPL"

def main_install_EN():
    os.system("chmod +x *")

    if os.path.isdir(appfolder):
        pass
    else:
        os.system("mkdir "+appfolder)
    os.system("cd app ; chmod +x "+appfile+" ; mv "+appfile+" "+appname+" ; mv "+appname+" "+appfolder)
    if os.path.isfile(appfolder+appname):
        pass
    else:
        print("Error! This step is first. Closing apiutaller...")
        exit()
        
    if os.path.isdir("/usr/share/polkit-1/actions"):
        pass
    else:
        os.system("mkdir /usr/share/polkit-1/actions")
    os.system("cd app ; mv "+policyfile+" /usr/share/polkit-1/actions")
    if os.path.isfile("/usr/share/polkit-1/actions/"+policyfile):
        pass
    else:
        print("Error! This step is second. Closing apiutaller...")
        exit()

    if os.path.isdir("/usr/share/applications"):
        pass
    else:
        os.system("mkdir /usr/share/applications")
    os.system("cd app ; mv "+appdesktopfile+" /usr/share/applications")
    if os.path.isfile("/usr/share/applications/"+appdesktopfile):
        pass
    else:
        print("Error! This step is third. Closing apiutaller...")
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
        print("Error! This step is last. Closing apiutaller...")
        exit()


def main_uninstall_EN():
    os.system("cd "+appfolder+" ; rm "+appname)
    if os.path.isfile(appfolder+appname):
        print("Error! This step is first. Closing apiutaller...")
        exit()
    else:
        pass
        
    os.system("cd /usr/share/polkit-1/actions ; rm "+policyfile)
    if os.path.isfile("/usr/share/polkit-1/actions/"+policyfile):
        print("Error! This step is second. Closing apiutaller...")
        exit()
    else:
        pass

    os.system("cd /usr/share/applications ; rm "+appdesktopfile)
    if os.path.isfile("/usr/share/applications/"+appdesktopfile):
        print("Error! This step is third. Closing apiutaller...")
        exit()
    else:
        pass

    os.system("cd "+mainappfolder+" ; rm -rf "+appname)
    if os.path.isdir(mainappfolder+appname):
        print("Error! This step is last. Closing apiutaller...")
        exit()
    else:
        print("Successful! You haven't this "+appname+" at the moment. We are happy if you share uninstalling reason!")
        exit()


def operation_EN():
    oa=input("What do you want to do? \nOptions: install or uninstall\nAnswer: ")
    if oa == "install":
        main_install_EN()
    if oa == "uninstall":
        main_uninstall_EN()        


def license_EN():
    license=input("Hello! I try installing or uninstalling "+appname+".\nI'm licensed with WTFPL!\n"+appname+" is under the "+licensename+"!\nDo you agree there?\nOptions: y or n\nAnswer: ")
    if license == "y":
        operation_EN()
    if license == "n":
        print("I'm sorry, you can't use "+appname+" and apiutaller, because you don't agree licenses!\nClosing apiutaller...")
        exit()



def main_install_TR():
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


def main_uninstall_TR():
    os.system("cd "+appfolder+" ; rm "+appname)
    if os.path.isfile(appfolder+appname):
        print("Hata! Bu adım birinci. apiutaller kapatılıyor...")
        exit()
    else:
        pass
        
    os.system("cd /usr/share/polkit-1/actions ; rm "+policyfile)
    if os.path.isfile("/usr/share/polkit-1/actions/"+policyfile):
        print("Hata! Bu adım ikinci. apiutaller kapatılıyor...")
        exit()
    else:
        pass

    os.system("cd /usr/share/applications ; rm "+appdesktopfile)
    if os.path.isfile("/usr/share/applications/"+appdesktopfile):
        print("Hata! Bu adım üçüncü. apiutaller kapatılıyor...")
        exit()
    else:
        pass

    os.system("cd "+mainappfolder+" ; rm -rf "+appname)
    if os.path.isdir(mainappfolder+appname):
        print("Hata! Bu adım sonuncu. apiutaller kapatılıyor...")
        exit()
    else:
        print("Başarılı! Siz artık "+appname+" programına sahip değilsiniz. Kaldırma sebebini bizle paylaşırsanız seviniriz.")
        exit()        


def operation_TR():
    oa=input(appname+" programını kurmayı mı yoksa silmeyi mi istersiniz?\nSeçenekler: kur veya sil\nCevap: ")
    if oa == "kur":
        main_install_TR()
    if oa == "sil":
        main_uninstall_TR()


def license_TR():
    license=input("Merhabalar! Ben "+appname+" uygulamasını kurmayı ya da silmeyi deneyeceğim.\nBen WTFPL ile lisanslıyım!\n"+appname+" ise "+licensename+" ile lisanslı!\nBunları kabul ediyor musunuz?\nSeçenekler: e ya da h\nCevap: ")
    if license == "e":
        operation_TR()
    if license == "h":
        print("Üzgünüm, siz "+appname+" ile apiutaller'i kullanamazsınız, çünkü siz lisansları kabul etmediniz!\napuitaller kapatılıyor...")
        exit()




def entry():
    language=input("Choose English or Turkish as a language.\nLütfen İngilizce veya Türkçeyi bir dil olarak seçiniz.\nOptions / Seçenekler: en / tr\nLanguage / Dil: ")
    if language == 'en':
        print("English selected.")
        license_EN()
    if language == 'tr':
        print("Türkçe seçildi.")
        license_TR()
entry()
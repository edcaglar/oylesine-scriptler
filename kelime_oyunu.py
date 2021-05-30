#Belirli harfle baslayan kelimeleri sirayla soyledigimiz oyun.
#Bi zaman sonra hangilerini soyledigimizi unuttugumuz icin yazdim.

import os
def failure_show():
    os.system("cls")
    for i in range(player_count):
        print("{}\t\t".format(player_list[i]),end = "")
    print("\n\n")

    for i in range(player_count):
        print("{}\t\t".format(failure_list[i]),end="")

    print("\n\n")


os.system("cls")
player_count = int(input("Oyuncu sayisini girin."))
player_list = list()
failure_list = [0] * player_count
os.system("cls")

for i in range(player_count):
    player_list.append(input("{}. oyuncunun adini girin :".format(i+1)))



failure_show()


word_list = list()

while(1):
    for i in range(player_count):
        failure_show()


        if(failure_list[i] == 2):
            continue
        flag = 1
        while(flag == 1):
            word = input("{} kelimeyi soylesin.".format(player_list[i]))
            failure_show()
            if word in word_list:

                flag = 1
                failure_list[i] += 1
                failure_show()
                print("Kelime listede bulunuyor.Yeni bir kelime soyle\n")
                if(failure_list[i] == 2):

                    flag = 0
                    failure_show()
                    print("{} 2 hata yaptigi icin elendi.".format(player_list[i]))
                    input("Devam etmek icin entera bas")
            else:

                flag = 0
                word_list.append(word)

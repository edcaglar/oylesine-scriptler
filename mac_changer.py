import subprocess  # linux terminale ulasabilmek icin
import optparse  # programi calistirirken -i --iface ile degerler verebilmek icin
import re # kullaniciya maci gosterirken kullanicaz regex101.com

def get_input():  # terminalde kullanicidan -i ve -m degerlerinin alinip tuple ile return edildi
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--iface", dest="interface", help="Interface to change")
    parse_object.add_option("-m", "--mac", dest="mac_adress", help="new mac adress")
    return parse_object.parse_args()


def change_mac_adress(user_interface, user_mac_adress):  # mac adresi degistiren fonksiyon
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_adress])
    subprocess.call(["ifconfig", user_interface, "up"])


def control_new_mac(user_interface):    # yeni macimizi ifconfigin icinde test ettik
    ifconfig =str(subprocess.check_output(["ifconfig",user_interface]))
    new_mac = re.search(r"\S\S:\S\S:\S\S:\S\S:\S\S:\S\S",ifconfig)

    if new_mac:
        return new_mac.group(0)
    else:
        return None


user_input, arguments = get_input()  # tuplein icinde dictionary seklindeki verileri aldik

print("MacChanger started ...")
change_mac_adress(user_input.interface, user_input.mac_adress)
last_mac = control_new_mac(user_input.interface)
print("New mac :",last_mac)

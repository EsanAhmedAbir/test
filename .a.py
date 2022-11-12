import base64, sys, os
from rich import print as iprint
from rich.panel import Panel

clr = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def banner():
	iprint(Panel(f"╔╦╗┌─┐┌─┐┌─┐┌┬┐┌─┐┬┬  ┌─┐\n ║║├┤ │  │ ││││├─┘││  ├┤ \n═╩╝└─┘└─┘└─┘┴ ┴┴  ┴┴─┘└─┘ "))
    
def banner1():
	iprint(Panel(f"", subtitle="[black][on white] masukan file *.so yang ingin di decompile"))

def banner2():
	iprint(Panel("                            [!] Proses Decompile"))
	
def banner3():
	iprint(Panel("                            [!] Decompile Selesai"))


class Decrypt:
    def __init__(self, path):
        self.path = path
        self.max_trying = 99

    def decrypt(self, saveto):
        os.system(f"strings {self.path} > temp.txt")
        try:
            source_code = [i for i in str(open("temp.txt", "r", encoding="utf-8").read()).split("\nb64decode")[0].split("\n")[-1].split("\n") if len(i) > 5][0]
        except:
            print(" [!] Some package not installed\n [!] please make sure your device connected to internet")
            os.system("pkg update -y")
            os.system("pkg upgrade -y")
            os.system("pkg install binutils -y")
            os.system(f"strings {self.path} > temp.txt")
            source_code = [i for i in str(open("temp.txt", "r", encoding="utf-8").read()).split("\nb64decode")[0].split("\n")[-1].split("\n") if len(i) > 5][0]

        os.remove("temp.txt")
        for i in range(self.max_trying):
            source_code = self.b64(source_code)
            if "b64decode(" not in source_code: break
            source_code = source_code.split('("' if '("' in source_code else "('")[-1].split('"' if '"' in source_code else "'")[0]
        if "b64decode(" in source_code: print(f" [!] Filed decrypt {self.path}")
        open(saveto, "w", encoding="utf-8").write('# Decompile by : KangProf & Bilal Haider iD\n# Tools : Decompiled *so Base64\n'+source_code)

    def b64(self, code):
        return base64.b64decode(code).decode()

def main():
    clr()
    banner()
    banner1()
    while True:
        path = str(input(" [!] File: "))
        try:
            open(path, "r", encoding="utf-8").read()
        except FileNotFoundError:
            print(f" [!] File {path} Tidak Ada Harap Isi Yang Benar")
            continue
        except:
            pass
        decryptor = Decrypt(path)
        break

    while True:
        saveto = str(input(" [!] Simpan Hasil Ke (*.py) : "))
        if saveto.split(".")[-1] != "py": saveto+=".py"
        try:
            open(saveto, "r", encoding="utf-8").read()
            print(f" [!] File {saveto} sudah ada, silakan gunakan nama file lain")
            source_code = "# dec by main.py"
        except:
            break

    banner2()
    print(f" [+] Decrypting {path} ...")
    decryptor.decrypt(saveto)
#    os.system(f" cat {saveto} ")
    print(f" [+] Hasil Di Simpan Ke --> : {saveto}")
    banner3()


if __name__ == "__main__":
    main()

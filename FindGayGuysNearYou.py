import random
import os
import sys

# Başlığı değiştir
os.system("title Find Gay Guys Near You")

# Konsolu temizle
os.system("cls")

# Mor renk ANSI kodu
PURPLE = "\033[95m"
RESET = "\033[0m"

# Rastgele sayı üret
number = random.randint(0, 1000)

# Çıktıyı mor renkte yazdır
print(f"{PURPLE}Number of Gay Guys Near You = {number}{RESET}")

# Çıkmadan beklet
input("\nPress Enter to exit...")

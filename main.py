#для полной работы программы вам нужно скачать и разместить все mp3 файлы в нужную директорию и не забудьте установить библиотеку pygame
import pygame
import time
import sys
pygame.mixer.init()
while True:
    bukva = str(input())
    if bukva == "a" or bukva == "A":
        print('███████████████')
        print('██╔═════════╗██')
        print('██║▓▓▓╔═╗▓▓▓║██')
        print('██║▓▓▓║█║▓▓▓║██')
        print('██║▓▓▓╚═╝▓▓▓║██')
        print('██║▓▓▓╔═╗▓▓▓║██')
        print('██╚═══╝▓╚═══╝██')
        print('███████████████')

        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "b" or bukva == "B":
        print('███████████████')
        print('██╔════════╗███')
        print('██║▓▓▓╔╗▓▓▓║███')
        print('██║▓▓▓╚╝▓▓▓╚╗██')
        print('██║▓▓▓╔═╗▓▓▓║██')
        print('██║▓▓▓╚═╝▓▓▓║██')
        print('██╚═════════╝██')
        print('███████████████')

    elif bukva == "c" or bukva == "C":
        print('███████████████')
        print('██╔════════╗███')
        print('██║▓▓▓╔═╗▓▓║███')
        print('██║▓▓▓║█╚══╝███')
        print('██║▓▓▓║█╔══╗███')
        print('██║▓▓▓╚═╝▓▓║███')
        print('██╚════════╝███')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "d" or bukva == "D":
        print('███████████████')
        print('██╔═════════╗██')
        print("██╚╗▓▓▓╔╗▓▓▓║██")
        print('███║▓▓▓║║▓▓▓║██')
        print('███║▓▓▓║║▓▓▓║██')
        print('██╔╝▓▓▓╚╝▓▓▓║██')
        print('██╚═════════╝██')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "e" or bukva == "E":
        print("███████████████")
        print('████╔══════╗███')
        print('████║▓▓▓╔══╝███')
        print('████║▓▓▓╚══╗███')
        print('████║▓▓▓╔══╝███')
        print('████║▓▓▓╚══╗███')
        print('████╚══════╝███')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "f" or bukva == "F":
        print('███████████████')
        print('███╔══════╗████')
        print('███║▓▓▓╔══╝████')
        print("███║▓▓▓╚══╗████")
        print('███║▓▓▓╔══╝████')
        print("███║▓▓▓║███████")
        print('███╚═══╝███████')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "g" or bukva == "G":
        print('███████████████')
        print('██╔═════════╗██')
        print('██║▓▓▓╔═╗▓▓▓║██')
        print('██║▓▓▓║█╚═══╝██')
        print('██║▓▓▓║╔═══╗███')
        print('██║▓▓▓╚╩═▓▓║███')
        print('██╚════════╝███')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "h" or bukva == "H":
        print('███████████████')
        print('██╔═══╗█╔═══╗██')
        print('██║▓▓▓║█║▓▓▓║██')
        print('██║▓▓▓╚═╝▓▓▓║██')
        print('██║▓▓▓╔═╗▓▓▓║██')
        print('██║▓▓▓║█║▓▓▓║██')
        print('██╚═══╝█╚═══╝██')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "i" or bukva == "I":
        print('███████████████')
        print('█████╔════╗████')
        print('█████╚╣▓▓╠╝████')
        print('██████║▓▓║█████')
        print('██████║▓▓║█████')
        print('█████╔╣▓▓╠╗████')
        print('█████╚════╝████')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "j" or bukva == "J":
        print('███████████████')
        print('███████╔═══╗███')
        print('███████║▓▓▓║███')
        print('███████║▓▓▓║███')
        print('██╔═══╗║▓▓▓║███')
        print('██║▓▓▓╚╝▓▓▓║███')
        print('██╚════════╝███')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "k" or bukva == "K":
        print('███████████████')
        print('███╔═══╗╔═══╗██')
        print('███║▓▓▓║║▓▓╔╝██')
        print('███║▓▓▓╚╝▓▓╝███')
        print('███║▓▓▓╔╗▓▓║███')
        print('███║▓▓▓║║▓▓╚╗██')
        print('███╚═══╝╚═══╝██')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "l" or bukva == "L":
        print('███████████████')
        print('███╔═══╗███████')
        print('███║▓▓▓║███████')
        print('███║▓▓▓║███████')
        print('███║▓▓▓║█╔══╗██')
        print('███║▓▓▓╚═╝▓▓║██')
        print('███╚════════╝██')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "m" or bukva == "M":
        print('███████████████')
        print('██╓───╖█╓───╖██')
        print('██║▓▓▓╙─╜▓▓▓║██')
        print('██║▓╓─╖▓╓─╖▓║██')
        print('██║▓║█║▓║█║▓║██')
        print('██║▓║█║▓║█║▓║██')
        print('██╙─╜█╙─╜█╙─╜██')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "n" or bukva == "N":
        print('███████████████')
        print('███╓──╖███╓─╖██')
        print('███║▓▓╙─╖█║▓║██')
        print('███║▓╓─╖╙─╜▓║██')
        print('███║▓║█╙─╖▓▓║██')
        print('███║▓║███║▓▓║██')
        print('███╙─╜███╙──╜██')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "o" or bukva == "O":
        print('███████████████')
        print('██╔═════════╗██')
        print('██║   ╔═╗   ║██')
        print('██║   ║ ║   ║██')
        print('██║   ║ ║   ║██')
        print('██║   ╚═╝   ║██')
        print('██╚═════════╝██')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "p" or bukva == "P":
        print('███████████████')
        print('█╔═════════╗███')
        print('█║▓▓▓╔═╗▓▓▓║███')
        print('█║▓▓▓╚═╝▓▓▓║███')
        print('█║▓▓╔══════╝███')
        print('█║▓▓║██████████')
        print('█╚══╝██████████')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "q" or bukva == "Q":
        print('███████████████')
        print('██╔═════════╗██')
        print('██║▓▓▓╔═╗▓▓▓║██')
        print('██║▓▓▓║█║▓▓▓║██')
        print('██║▓▓▓║█║▓▓▓║██')
        print('██║▓▓▓╚═╝▓▓▓║██')
        print('██╚═════──═╗║██')
        print('███████████╚╝██')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "r" or bukva == "R":
        print('███████████████')
        print('██╔═════════╗██')
        print('██║▓▓▓╔═╗▓▓▓║██')
        print('██║▓▓▓╚═╝▓▓▓║██')
        print('██║▓▓▓╔╗▓▓╔═╝██')
        print('██║▓▓▓║║▓▓╚═╗██')
        print('██╚═══╝╚════╝██')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "s" or bukva == "S":
        print('███████████████')
        print('███╓───────╖███')
        print('███║▓▓╓────╜███')
        print('███║▓▓╙────╖███')
        print('███╙───╖▓▓▓║███')
        print('███╓───╜▓▓▓║███')
        print('███╙───────╜███')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "t" or bukva == "T":
        print('███████████████')
        print('██╔════════╗███')
        print('██║▓╔╗▓▓╔╗▓║███')
        print('██╚═╝║▓▓║╚═╝███')
        print('█████║▓▓║██████')
        print('█████║▓▓║██████')
        print('█████╚══╝██████')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "u" or bukva == "U":
        print('███████████████')
        print('██╔═══╗█╔═══╗██')
        print('██║▓▓▓║█║▓▓▓║██')
        print('██║▓▓▓║█║▓▓▓║██')
        print('██║▓▓▓║█║▓▓▓║██')
        print('██║▓▓▓╚═╝▓▓▓║██')
        print('██╚═════════╝██')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "v" or bukva == "V":
        print('███████████████')
        print('██╓─╖████╓─╖███')
        print('██║▓╙╖██╓╜▓║███')
        print('██║▓▓║██║▓▓║███')
        print('██╙─╖╙──╜╓─╜███')
        print('████╙╖▓▓╓╜█████')
        print('█████╙──╜██████')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "w" or bukva == "W":
        print('███████████████')
        print('███╔═╗╔═╗╔═╗███')
        print('███║▓║║▓║║▓║███')
        print('███║▓║║▓║║▓║███')
        print('███║▓╚╝▓╚╝▓║███')
        print('███╚═╗╔═╗╔═╝███')
        print('█████╚╝█╚╝█████')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "x" or bukva == "X":
        print('███████████████')
        print('██╔═══╗╔═══╗███')
        print('██╚╗▓▓╚╝▓▓╔╝███')
        print('███╚╗▓▓▓▓╔╝████')
        print('███╔╝▓▓▓▓╚╗████')
        print('██╔╝▓▓╔╗▓▓╚╗███')
        print('██╚═══╝╚═══╝███')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "y" or bukva == "Y":
        print('███████████████')
        print('██╔═══╗██╔═══╗█')
        print('██║▓▓▓╚╗╔╝▓▓▓║█')
        print('██╚══╗▓╚╝▓╔══╝█')
        print('█████╚╗▓▓╔╝████')
        print('██████║▓▓║█████')
        print('██████╚══╝█████')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    elif bukva == "z" or bukva == "z":
        print('███████████████')
        print('████╔═════╗████')
        print('████╚══╗▓▓║████')
        print('██████╔╝╔═╝████')
        print('█████╔╝╔╝██████')
        print('████╔╝▓╚══╗████')
        print('████╚═════╝████')
        print('███████████████')
        pygame.mixer.music.load(bukva + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    else:
       time.sleep(1)
       print("На этом мои полномочия все.")
       pygame.mixer.music.load("полномочия.mp3")
       pygame.mixer.music.play()
       while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        sys.exit()
    time.sleep(0.3)
    print("Хотите продолжить(yes - y or no - n) ?")
    pygame.mixer.music.load( "продолжить.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    b = str(input())
    if  b != "y" and b != "n":
        time.sleep(0.3)
        print("вы инвалид , так вы хотите продолжить ? ")
        pygame.mixer.music.load("оскорбления.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    if b == "n":
        time.sleep(0.3)
        print('Не очень то и хотелось.')
        pygame.mixer.music.load( "не очень то и хотелось.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        sys.exit()
    if b == "y":
        time.sleep(0.3)
        print("Спасибо, что пользуетесь нашими услугами!")
        pygame.mixer.music.load( "услуги.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        continue

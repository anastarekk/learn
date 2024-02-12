# Anas Tarek Fathi Ali       20236019



def menu1():
    print("** numbering system converter **")
    print("A) insert a new number")
    print("B) Exit program")

def menu2():
    print("** please select the base you want to convert a number from **")
    print("A) Decimal")
    print("B) binary")
    print("C) octal")
    print("D) hexadecimal")

def menu3():
    print("** please select the base you want to convert a number to **")
    print("A) Decimal")
    print("B) binary")
    print("C) octal")
    print("D) hexadecimal")

def dec_to_bin():
    s = ""
    n = Num
    while(n>0):
        r = n % 2
        s = str(r) + s
        n = n // 2
    print(int(s))

def dec_to_dec():
    print(Num)

def dec_to_oct():
    s1 = ""
    n1 = Num
    while(n1>0):
        r = n1 % 8
        s1 = str(r) + s1
        n1 = n1 // 8
    print(int(s1))

def dec_to_hex():
    s2 = ""
    n = Num
    while (n>0):
        r = n % 16
        s2 = str(r) + s2
        n = n // 16
    print(int(s2))

def bin_to_dec():
    dec = 0
    power = 0
    binNum = Num
    while binNum>0:
        digit = binNum%10
        dec = dec + digit*pow(2,power)
        binNum = binNum//10
        power = power + 1
    print(dec)

def bin_to_bin():
    print(Num)

def bin_to_oct():
    BinNum = Num
    octaldigit = 0
    count = 1
    i = 0
    pos = 0
    octalarray = [0] * 32
    while BinNum > 0:
        digit = BinNum%10
        octaldigit = octaldigit + digit * pow(2,i)
        i = i+1
        BinNum = BinNum//10
        octalarray[pos] = octaldigit
        if count % 3 == 0:
            octaldigit = 0
            i = 0
            pos = pos +1
        count = count +1
    for x in range(pos, -1, -1):
        print(octalarray[x], end="")

def bin_to_hex():
    BinNum = Num
    hexadigit = 0
    count = 1
    i = 0
    pos = 0
    hexaarray = [0] * 32
    while BinNum > 0:
        digit = BinNum%10
        hexadigit = hexadigit + digit * pow(2,i)
        i = i + 1
        BinNum = BinNum//10
        hexaarray[pos] = hexadigit
        if count % 4 == 0:
            hexadigit = 0
            i = 0
            pos = pos +1
        count = count +1
    for x in range(pos, -1, -1):
        print(hexaarray[x], end="")
def octal_to_dec():
    octNum = Num
    dec = 0
    i = 0
    while octNum > 0:
        digit = octNum%10
        dec = dec + digit*pow(8,i)
        i +=1
        octNum = octNum//10
    print(dec)

#def octal_to_dec2():
    octNum = Num
    dec = 0
    i = 0
    while octNum > 0:
        digit = octNum%10
        dec = dec + digit*pow(8,i)
        i +=1
        octNum = octNum//10
        d = dec

#def dec_to_bin2():
    s = ""
    n = d
    while (n > 0):
        r = n % 2
        s = str(r) + s
        n = n // 2
    print(int(s))

#def dec_to_hex2():
    s2 = ""
    n = d
    while (n > 0):
        r = n % 16
        s2 = str(r) + s2
        n = n // 16
    print(int(s2))

def hex_to_dec():
    hexNum = Num
    dec = 0
    i = 0
    while hexNum > 0:
        digit = hexNum % 10
        dec = dec + digit*pow(16, i)
        hexNum = hexNum//10
        i += 1
    print(dec)

#def hex_to_dec2():
    hexNum = Num
    dec = 0
    i = 0
    while hexNum > 0:
        digit = hexNum % 10
        dec = dec + digit * pow(16, i)
        hexNum = hexNum // 10
        i += 1
        d = dec
menu1()
option = str(input())
while option != "b":
    if option == "a":
        print("Please insert a number")
        try:
            print()
            Num = int(input())
            menu2()
            option2 = str(input())
            if option2 == "a":
                print()
                menu3()
                option3 = str(input())
                if option3 == "b":
                    dec_to_bin()
                elif option3 == "a":
                    dec_to_dec()
                elif option3 == "c":
                    dec_to_oct()
                elif option3 == "d":
                    dec_to_hex()
                else:print("Please select a valid option")
            elif option2 == "b":
                print()
                menu3()
                option3 = str(input())
                if option3 == "a":
                    bin_to_dec()
                elif option3 == "b":
                    bin_to_bin()
                elif option3 == "c":
                    bin_to_oct()
                elif option3 == "d":
                    bin_to_hex()
                else:print("Please select a valid option")
            elif option2 == "c":
                print()
                menu3()
                option3 = str(input())
                if option3 == "a":
                    octal_to_dec()
                elif option3 == "b":
                    octNum = Num
                    dec = 0
                    i = 0
                    while octNum > 0:
                        digit = octNum % 10
                        dec = dec + digit * pow(8, i)
                        i += 1
                        octNum = octNum // 10
                        d = dec
                    s = ""
                    n = d
                    while (n > 0):
                        r = n % 2
                        s = str(r) + s
                        n = n // 2
                    print(int(s))
                elif option3 == "c":
                    print(Num)
                elif option3 == "d":
                    octNum = Num
                    dec = 0
                    i = 0
                    while octNum > 0:
                        digit = octNum % 10
                        dec = dec + digit * pow(8, i)
                        i += 1
                        octNum = octNum // 10
                        d = dec
                    s2 = ""
                    n = d
                    while (n > 0):
                        r = n % 16
                        s2 = str(r) + s2
                        n = n // 16
                    print(int(s2))
            elif option2 == "d":
                print()
                menu3()
                option3 = str(input())
                if option3 == "a":
                    hex_to_dec()
                elif option3 == "b":
                    hexNum = Num
                    dec = 0
                    i = 0
                    while hexNum > 0:
                        digit = hexNum % 10
                        dec = dec + digit * pow(16, i)
                        hexNum = hexNum // 10
                        i += 1
                        d = dec
                    s = ""
                    n = d
                    while (n > 0):
                        r = n % 2
                        s = str(r) + s
                        n = n // 2
                    print(int(s))
                elif option3 =="c":
                    hexNum = Num
                    dec = 0
                    i = 0
                    while hexNum > 0:
                        digit = hexNum % 10
                        dec = dec + digit * pow(16, i)
                        hexNum = hexNum // 10
                        i += 1
                        d = dec
                    s1 = ""
                    n1 = d
                    while (n1 > 0):
                        r = n1 % 8
                        s1 = str(r) + s1
                        n1 = n1 // 8
                    print(int(s1))
                elif option3 =="d":
                    print(Num)
            else:
             print("Please select a valid option")
        except ValueError:
            print("Please insert a valid number")
    else:
        print("Please select a valid option")
    print()
    menu1()
    option = str(input())
print("Thanks for using this program")



def main():
    while True:
        print('options:')
        print('Tempreture(T)\nLength(L)\nMass/Weight(M)\nArea(A)\nQuit(Q)')
        option = input('What dimension would you like to convert: ')
        option = option.upper().strip()
        if option == 'T':
            tempreture()
        elif option == 'L':
            length()
        elif option == 'M':
            mass1=mass()
            mass1.m()
        elif option == 'A':
            area()
        elif option == 'Q':
            print('exiting system now:')
            exit(0)
        else:
            print('incorrect input (must only input what is in brackets)')


class mass:
    def __int__(self):
        self.convertto=0
        self.convertfrom=0
    def m(self):
        while True:
            try:
                print("\nOptions:")
                print("Kg) Kilogram \nLbs) pounds\nOz) Ounces\nSt) Stone)\nT) Tons")
                self.convertfrom = input("What are you converting from: ")
                self.convertfrom = self.convertfrom.upper().strip()
                if self.convertfrom == 'KG' or self.convertfrom == 'LBS' or self.convertfrom == 'OZ' or self.convertfrom == 'ST' or self.convertfrom == 'T':
                    while True:
                        self.convertto = input("What are you converting to: ")
                        self.convertto = self.convertto.strip().upper()
                        if self.convertto == 'KG' or self.convertto == 'LBS' or self.convertto == 'OZ' or self.convertto == 'ST' or self.convertto == 'T':
                            num1 = float(input("Enter the value: "))
                            kg = mass.converttokg(num1, self.convertfrom)
                            mass.convertfromkg(kg, self.convertfrom, num1, self.convertto)
                        else:
                            print("Invalid option, try again")
                elif self.convertfrom == 'Q':
                    print("\nExiting program\n")
                    break
                else:
                    print("Invalid option, try again")
            except KeyboardInterrupt:
                print("\nExiting program\n")
                break  # You can also use exit(0) to quit
    def converttokg(self,num1, convertfrom):
        if convertfrom == 'LBS':
            kg = num1 / 2.205
        elif convertfrom == 'KG':
            kg = num1
        elif convertfrom == 'OZ':
            kg = num1 / 35.274
        elif convertfrom == 'ST':
            kg = num1 / 6.35
        else:
            kg = num1 / 1000
        return kg


    def convertfromkg(self,kg, convertfrom, num1, convertto):
        if convertto == 'LBS':
            mass = kg * 2.205
        elif convertto == 'KG':
            mass = kg
        elif convertto == 'OZ':
            mass = kg * 35.274
        elif convertto == 'ST':
            mass = kg * 6.35
        else:
            mass = kg * 1000
        print(f'The length from {num1}{convertfrom} to {round(mass, 2)}{convertto}\n')
        main()


def area():
    while True:
        try:
            print("\nOptions:")
            print(
                "M) Metre^2 (m^2)\nI) Inch^2 (in^2)\nF) Feet^2 (ft^2)\nHa) Hectare (Ha)\nY) Yard^2 (y^2)\nKm) KM^2 (Km)\nA) Acre (A)")
            convertfrom = input("What are you converting from: ")
            convertfrom = convertfrom.upper().strip()
            if convertfrom == 'M' or convertfrom == 'I' or convertfrom == 'F' or convertfrom == 'Y' or convertfrom == 'HA' or convertfrom == 'KM' or convertfrom == 'A':
                while True:
                    convertto = input("What are you converting to: ")
                    convertto = convertto.strip().upper()
                    if convertto == 'M' or convertto == 'I' or convertto == 'F' or convertto == 'Y' or convertto == 'HA' or convertfrom == 'KM' or convertfrom == 'A':
                        num1 = float(input("Enter the value: "))
                        metresquared = converttometresquared(num1, convertfrom)
                        convertfrommetresquared(metresquared, convertfrom, num1, convertto)
                    else:
                        print("Invalid option, try again")
            elif convertfrom == 'Q':
                print("\nExiting program\n")
                break
            else:
                print("Invalid option, try again")
        except KeyboardInterrupt:
            print("\nExiting program\n")
            break  # You can also use exit(0) to quit


def converttometresquared(num1, convertfrom):
    if convertfrom == 'F':
        metresquared = num1 / (10.764)
    elif convertfrom == 'M':
        metresquared = num1
    elif convertfrom == 'I':
        metresquared = num1 / 1550
    elif convertfrom == 'Y':
        metresquared = num1 / 1.196
    elif convertfrom == 'KM':
        metresquared = num1 * 1000000
    elif convertfrom == 'HA':
        metresquared = num1 * 10000
    else:
        metresquared = num1 * 4047
    return metresquared


def convertfrommetresquared(metresquared, convertfrom, num1, convertto):
    if convertto == 'F':
        area = metresquared * 10.764
    elif convertto == 'M':
        area = metresquared
    elif convertto == 'I':
        area = metresquared * 1550
    elif convertto == 'Y':
        area = metresquared * 1.196
    elif convertto == 'KM':
        area = metresquared / 1000000
    elif convertto == 'HA':
        area = metresquared / 10000
    else:
        area = metresquared / 4047
    print(f'The length from {num1}{convertfrom}(^2) to {round(area, 2)}{convertto}(^2)\n')
    main()


def length():
    while True:
        try:
            print("\nOptions:")
            print("M) Metre (m)\nI) Inch (in)\nF) Feet (ft)\nY) Yard (yd)\nMi) Mile (mi)\nNm) Nautical Mile (nm)\n")
            convertfrom = input("What are you converting from: ")
            convertfrom = convertfrom.upper().strip()
            if convertfrom == 'M' or convertfrom == 'I' or convertfrom == 'F' or convertfrom == 'Y' or convertfrom == 'MI' or convertfrom == 'NM':
                while True:
                    convertto = input("What are you converting to: ")
                    convertto = convertto.strip().upper()
                    if convertto == 'M' or convertto == 'I' or convertto == 'F' or convertto == 'Y' or convertto == 'MI' or convertfrom == 'NM':
                        num1 = float(input("Enter the value: "))
                        metre = converttometre(num1, convertfrom)
                        convertfrommetre(metre, convertfrom, num1, convertto)
                    else:
                        print("Invalid option, try again")
            elif convertfrom == 'Q':
                print("\nExiting program\n")
                break
            else:
                print("Invalid option, try again")
        except KeyboardInterrupt:
            print("\nExiting program\n")
            break  # You can also use exit(0) to quit


def converttometre(num1, convertfrom):
    if convertfrom == 'F':
        metre = num1 / (3.281)
    elif convertfrom == 'M':
        metre = num1
    elif convertfrom == 'I':
        metre = num1 / 39.37
    elif convertfrom == 'Y':
        metre = num1 / 1.094
    elif convertfrom == 'MI':
        metre = num1 * 1609
    else:
        metre = num1 * 1852
    return metre


def convertfrommetre(metre, convertfrom, num1, convertto):
    if convertto == 'F':
        length = metre * 3.281
    elif convertto == 'M':
        length = metre
    elif convertto == 'I':
        length = metre * 39.37
    elif convertto == 'Y':
        length = metre * 1.094
    elif convertto == 'MI':
        length = metre / 1609
    else:
        length = metre / 1852
    print(f'The length from {num1}{convertfrom} to {round(length, 2)}{convertto}\n')
    main()


def tempreture():
    while True:
        try:
            print("\nOptions:")
            print("K)Kelvin (K)\n"
                  "C)Celsius (°C)\n"
                  "F)Fahrenheit (°F)\n"
                  "R)Rankine (°R)\n"
                  "D)Delisle (°D)\n"
                  "Q) Exit program\n")
            convertfrom = input("What are you converting from: ")
            convertfrom = convertfrom.upper().strip()
            if convertfrom == 'K' or convertfrom == 'C' or convertfrom == 'F' or convertfrom == 'R' or convertfrom == 'D':
                while True:
                    convertto = input("What are you converting to: ")
                    convertto = convertto.strip().upper()
                    if convertto == 'K' or convertto == 'C' or convertto == 'F' or convertto == 'R' or convertto == 'D':
                        num1 = float(input("Enter the value: "))
                        kelvin = converttokelvin(num1, convertfrom)
                        convertfromkelvin(kelvin, convertfrom, num1, convertto)
                    else:
                        print("Invalid option, try again")
            elif convertfrom == 'Q':
                print("\nExiting program\n")
                break
            else:
                print("Invalid option, try again")
        except KeyboardInterrupt:
            print("\nExiting program\n")
            break  # You can also use exit(0) to quit


def converttokelvin(num1, convertfrom):
    if convertfrom == 'C':
        kelvin = num1 + 273.15
    elif convertfrom == 'K':
        kelvin = num1
    elif convertfrom == 'F':
        kelvin = (num1 - 32) * (5 / 9) + 273.15
    elif convertfrom == 'R':
        kelvin = num1 * 5 / 9
    else:
        kelvin = (num1 + 100) / 1.5 + 273.15
    return kelvin


def convertfromkelvin(kelvin, convertfrom, num1, convertto):
    if convertto == 'K':
        tempreture = kelvin
    elif convertto == 'C':
        tempreture = kelvin - 273.15
    elif convertto == 'F':
        tempreture = (kelvin - 273.15) * (9 / 5) + 32
    elif convertto == 'R':
        tempreture = kelvin * 9 / 5
    else:
        tempreture = (kelvin - 273.15) * 1.5 - 100
    print(f'The tempreture from {num1}°{convertfrom} to {round(tempreture, 2)}°{convertto}\n')
    main()


if __name__ == "__main__":
    main()

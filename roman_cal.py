#rom_val = {'M': 1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}

import sys

rom_val = {"M":1000, "CM":900, "D":500, "CD":400,"C":100, "XC":90, "L":50, "XL":40,"X":10, "IX":9, "V":5,"IV":4,"I":1}


def rom_to_dec(rom_no):
    i=0
    l=len(rom_no)
    value=0
    while(i<l):
        n1 = rom_val[rom_no[i]]
        if(i+1<l):
            n2=rom_val[rom_no[i+1]]
            if(n1>=n2):
                value=value+n1
                i=i+1
            else:
                value=value+n2-n1
                i=i+2
        else:
            value=value+n1
            i=i+1
    return value


def dec_to_rom(num):
    roman=''
    while num>0:
        for k,v in rom_val.items():
            while num>=v:
                roman=roman+k
                num=num-v
    return roman


def dec_to_rom2(num):
    num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman = ''
    while num > 0:
        for k, v in num_map:
            while num >= k:
                roman += v
                num -= k
    return roman



def find(number_decimal_1,number_decimal_2, op):
    eq_number_decimal_1 =  rom_to_dec(number_decimal_1)
    eq_number_decimal_2 =  rom_to_dec(number_decimal_2)
    if op == "+":
        decimal_equivalent  = eq_number_decimal_1 + eq_number_decimal_2
    elif op == "-":
        decimal_equivalent  = eq_number_decimal_1 - eq_number_decimal_2
    elif op == "*" or op.lower()=="x" :
        decimal_equivalent  = eq_number_decimal_1 * eq_number_decimal_2
    else:
        print("invalid operator")
        return
    print(decimal_equivalent)
    roman_result = dec_to_rom2(decimal_equivalent)
    print("The Result \n########################\n{} {} {} = {}\n".format(number_decimal_1,op,number_decimal_2, roman_result))


if __name__ == "__main__":
    print("Running the roman calculator")
    print(sys.argv)
    if len(sys.argv) > 3:
        roman_1 = sys.argv[1].upper()
        roman_2 = sys.argv[3].upper()
        op = sys.argv[2]
        find(roman_1, roman_2, op)
    else:
        print("\nInvalid Input...Please give input in the format \n\nroman_number_1<space>operator<space>roman_number_2 \n")
        print("For e.g. XV + IX \n")


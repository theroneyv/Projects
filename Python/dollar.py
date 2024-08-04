import sys

PRL = 41.7
BCD = 36.65

def convert_dollar(dollar):
    print('(PRL) ' + str(dollar) + ' $ --> ' + str(dollar * PRL) + ' Bs')
    print('(BCD) ' + str(dollar) + ' $ --> ' + str(dollar * BCD) + ' Bs')

def convert_bolivar(bolivar):
    print('(PRL) ' + str(bolivar) + ' Bs --> ' + str(bolivar / PRL) + ' $')
    print('(BCD) ' + str(bolivar) + ' Bs --> ' + str(bolivar / BCD) + ' $')

def main():
    if len(sys.argv) > 1:
        if len(sys.argv) > 2 and sys.argv[2] == "-b":
            convert_bolivar(float(sys.argv[1]))
        else:
            convert_dollar(float(sys.argv[1]))
    else:
        convert_dollar(1)

if __name__=="__main__":
    main()

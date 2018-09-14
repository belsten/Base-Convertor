import math

def welcome_print():
    print("\n####################################################")
    print("##   _______                 _______   ________   ##")
    print("##  | _____ \       /\      /______/  |  ______|  ##")
    print("##  ||     | |     //\\\    //         | |         ##")
    print("##  ||____/ /     //  \\\   \\\______   | |_____    ##")
    print("##  | ____ <     //====\\\   \______\  |  _____|   ##")
    print("##  ||     \ \\  //      \\\         \\\ | |         ##")
    print("##  ||_____| | //        \\\________// | |______   ##")
    print("##  |_______/ //          \________/  |________|  ##")
    print("##                                                ##")
    print("##                 CONVERTER                      ##")
    print("##                                                ##")
    print("##  MADE POSSIBLE BY:                             ##")
    print("##         ALEX BELSTEN                           ##")
    print("####################################################")
    
def print_error():
    print("Error. Input not valid")

def main():
    welcome_print()
    dec     = 0
    index   = 0    
    new_str = ''
    base = ['0','1','2','3','4','5','6',  \
            '7','8','9','A','B','C','D',  \
            'E','F','G','H','I','J','K',  \
            'L','M','N','O','P','Q','R',  \
            'S','T','U','V','W','X','Y','Z']
    
    while True:
        string_num = input('\nEnter number => ').upper()
        old_base   = input('Enter number base (36 max) => ')
        new_base   = input('Enter base to convert to (36 max) => ')
        try:
            old_base = int(old_base)
            new_base = int(new_base)
            if old_base > 36 or new_base > 36:
                raise ValueError("Not valid input")
        except ValueError:
            print_error()
            continue
        
        valid = True
        for i in reversed(string_num):
            if base.index(i) > old_base:
                print_error()
                valid = False
                break
            else:
                dec += int(base.index(i)) * old_base**index
                index += 1
        if valid:
            while dec != 0:
                bit = int(dec%new_base)
                new_str = base[bit] + new_str
                dec -= bit
                dec = dec / new_base
            print('Base',new_base,': ', new_str)
            new_str = ''
        valid = True
        dec   = 0
        index = 0

if __name__ == "__main__":
    main()
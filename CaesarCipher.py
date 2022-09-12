from ascii import logo
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
status = input("What you want to do?\nType 'encode' or 'decode'.\n")
stri = input(f"Please enter your Text to {status.capitalize()}:\n")
inpShift = int(input("Please enter your Shift Number:\n"))


enc_stri = ""


def encryp(str, shift):
    enc_stri = ""
    for s in str:
        for a in range(26):
            if(s == alp[a]):
                if(shift >= (26-a)):
                    enc_stri = enc_stri+alp[(26-a)+(shift - (26-a)) - 1]
                else:
                    enc_stri = enc_stri+alp[a+shift]
            else:
                pass
    print(enc_stri)


def decryp(str, shift):
    dec_stri = ""
    for s in str:
        for a in range(26):
            if(s == alp[a]):
                if(a <= shift):
                    dec_stri = dec_stri + alp[26-shift+1]
                else:
                    dec_stri = dec_stri + alp[a-shift]
            else:
                pass
    print(dec_stri)


if status.lower() == "encode":
    encryp(stri, inpShift)
elif status.lower() == "decode":
    decryp(stri, inpShift)
else:
    print("Command Not Found")

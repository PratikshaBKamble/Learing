Mesha=["A","L","E","I","O"]
Vrishabha=["B","V","U","W"]
Mithun=["K","CHH","GH","Q","C"]
Karka=["DD","H"]
Simha=["M","TT"]
Kanya=["P","TTHH"]
Tula=["R","T"]
Vruschika=["N","Y"]
Dhanu=["BH","F","DH"]
Makar=["KH","J"]
Kumbha=["G","S","Sh"]
Meena=["D","CH","Z","TH"]

name=str(input("Please enter your name:")).upper()
#print(name)
one=name[0:1]
two=name[0:2]
three=name[0:3]
four=name[0:4]

if one in Mesha:
    print(name,"Your rashifal is Mesha")
elif one in Vrishabha:
    print(name,"Your rashifal is Vrishabha")
elif one in Mithun or two in Mithun or three in Mithun:
    print(name,"Your rashifal is Mithun")
elif one in Karka or two in Karka:
    print(name,"Your rashifal is Karka")
elif one in Simha or two in Simha:
    print(name,"Your rashifal is Simha")
elif one in Kanya or four in Kanya:
    print(name,"Your rashifal is Kanya")
elif one in Tula:
    print(name,"Your rashifal is Tula")
elif one in Vruschika:
    print(name,"Your rashifal is Vruschika")
elif one in Dhanu or two in Dhanu:
    print(name,"Your rashifal is Dhanu")
elif one in Makar or two in Makar:
    print(name,"Your rashifal is Makar")
elif one in Kumbha or two in Kumbha:
    print(name,"Your rashifal is Kumbha")
elif one in Meena or two in Meena:
    print(name,"Your rashifal is Meena")
else:
    print("wrong output")
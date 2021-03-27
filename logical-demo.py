kilo = float(input("Kilonuz: "))
boy = float(input("Boyunuz: "))
formul = (kilo / (boy**2))
zayif = formul>0 and formul<18.4
normal = formul>18.5 and formul<26
fazlakilo = formul>27 and formul<29.9
obez = formul>30 and formul<34.9 
print(f"kilo indeksiniz: {formul} ve grubunuz zayıf :{zayif} ")
print(f"kilo indeksiniz: {formul} ve grubunuz normal :{normal} ")
print(f"kilo indeksiniz: {formul} ve grubunuz fazla kilolu :{fazlakilo} ")
print(f"kilo indeksiniz: {formul} ve grubunuz obez :{obez}")


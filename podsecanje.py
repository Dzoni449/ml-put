s = "  Python  "
s.upper()
print(f"[{s}]")
# [  Python  ] nista se ne desi jer nije dodeljena vrednost
s = "  Python  "
s = s.strip()
print(len(s))
# 6
ime = "marko"
ime.capitalize()
ime = ime + "!"
print(ime)
# marko!
naslov = "  #shorts Trik  "
naslov.replace("#shorts", "")
naslov = naslov.strip()
print(f"[{naslov}]")
# #shorts Trik
t = "  ok  "
u = t.strip()
print(len(t), len(u))
# 6 i 2
#------------------------- 5/5
print(f"{0.5:.0%}")
# 50%
print(f"{0.075:.1%}")
# 7.5%
print(f"{7.5:.1%}")
# 750%
print(int(9.99))
# 9
print(round(9.99))
# 10
print(int(-3.7))
# -3
print(20 / 100)
# 0.2
print(int(20 / 100))
# 0
# ------------------------- 4/5
#int("abc")
# ValueError
#"5" + 5
#typeError
#"Python"[10]
#indexError
#10 / 0
#ZeroDivisionError
#prit("x")
#NameError
#float("4,5")
#valueerror
#len(5)
#-------------------- 5/7
print("a", "b")
#2 razmaka
print("x:", 5)
#2 razmaka
print("x: ", 5)
print(f"x: {5}")
print("a", "b", "c", sep=", ")
#--------------------------- 5/5
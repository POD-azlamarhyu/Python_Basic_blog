val_string = "貯金は割合が全てです."
val_25 = "25%以上貯められればいいですね."
val_etf = "ETF!"

print(val_string+val_25)
print(val_etf*10)
val_parcent = "%以上貯められればいいですね."
rate = 35.0
print("%s %.1f%s" %(val_string,rate,val_parcent))

print("{0} {1}{2}".format(val_string,rate,val_parcent))

print(val_etf.capitalize())
print(val_etf.casefold())
print(val_25.encode(encoding="utf-8",errors="strict"))

print(val_string.isalpha())
print(val_parcent.upper())
print(val_25.replace("25%","40%"))
print(str(int(rate)).zfill(5))

for i in val_25:
    print(i)
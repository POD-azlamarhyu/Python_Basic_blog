from decimal import Decimal as dec

x = 3.0
y = 2.0
print(x+y)
print(dec(x)+dec(y))
print(0.1+0.1)

print(dec(str(x))*dec(str(y)))

account_cash = 940_939_000
use_cash = 1_330_323
print(dec(str(account_cash)) - dec(str(use_cash)))

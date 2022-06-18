"""
if
"""

is_bool = 0

if is_bool == 0:
    print("株式会社です")
elif is_bool == 1:
    print("合同会社です")
else:
    print("有限会社です。今は設立できません")
    
    
input_score = int(input("数字を入力してください : "))

if input_score >= 100:
    print("Perfect!!")
elif input_score > 90:
    print("Great!!")
elif input_score > 70:
    print("Good!")
else:
    print("Jesus!!")
    
value = 100

if value is not 100:
    print("true")
else:
    print("false")
    
bool = True

print("true" if bool is True else "false")

bool_list = None

if bool_list is not None:
    print("true")
else:
    print("false")
    
stock_owner = 2199
trading_stock_rate = 35.7
market_value = 2500

if stock_owner >= 2200 and trading_stock_rate >= 35.0 and market_value >= 250:
    print("上場条件の一部を満たしています")
elif stock_owner >= 2200 or trading_stock_rate >= 35.0 or market_value >= 250:
    print("上場条件の一部を満たせていません")
else:
    print("上場条件を満たせていません")
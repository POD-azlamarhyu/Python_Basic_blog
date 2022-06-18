def obj_func():
     print("""
          ----------------------------
               print func
          ----------------------------
          """)

obj_func()

def null_func():
     pass

def calc_func(x1,x2):
     y = x1**2 + 3*x2 +1
     print(y)

calc_func(2,4)

def get_account_info(id):
     return {"id":1001,"name":'jiro'}

user = get_account_info(1001)
print(user)
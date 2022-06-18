var_x = 3
var_y = 2.3

def calc_func():
     var_local__x = 2
     var_x=6
     print(var_local__x)
     print(var_x)

     var_x = 2
     print(var_x)

calc_func()

print(var_x)

def calc_func_float():
     global var_y

     var_y = 1.345

     print(var_y)

calc_func_float()
print(var_y)
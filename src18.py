def except_func():
     try:
          input_number=int(input('input number : '))
          input_divide_number=int(input('input divide number : '))
          print("\n")
          print(input_number//input_divide_number)
     except ValueError:
          print("not number")
     except ZeroDivisionError:
          print("dont divide 0")
     finally:
          print("end")

except_func()

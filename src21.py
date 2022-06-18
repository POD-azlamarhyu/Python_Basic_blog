from pydoc import cli
import sys

print(sys.version)

print(sys.platform)

def cli_input_args():
     args = sys.argv

     if len(args) == 2:
          print(args)
          print(type(args))

          id = args[0]
          pw = args[1]

     else:
          print('error. please input id and pw')

cli_input_args()

print(sys.float_info)
print(sys.int_info)

print(sys.prefix)




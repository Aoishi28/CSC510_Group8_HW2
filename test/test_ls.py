from xxlimited import Str
from test_list import test_list
def ls():
  print("\nExamples lua csv -e ...")
  for k in (test_list()):
      print(Str.format("\t%s",k))
  return True
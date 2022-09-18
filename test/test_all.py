from test_list import test_list
from test_engine import TestEngine
def all_tests():
  for k in(test_list()):
    if k != "ALL":
      print("\n-----------------------------------")
      if not TestEngine.runs(k):
          fails=fails+ 1 
  return True
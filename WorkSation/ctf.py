#两两字符串分割
def long_to_2(str_):
  for i in range(0,len(str_)+1,2):
      print(str_[i:i+2])
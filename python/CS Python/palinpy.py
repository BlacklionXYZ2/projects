
def format(data):
   out = []
   idx = []
   for x in str(data):
      out.append(x)
   if data % 2 == 0:
      idx = [0, len(out) / 2]
   else:
      idx = [0, len(data) / 2, round(len(data) / 2)]
   return out, idx
def front_times(str, n):
  sum=""
  re=""
  if(len(str)<3):
    sum=str
  else:
    sum=str[:3]
  for i in range(n):
    re=re+sum
  return re
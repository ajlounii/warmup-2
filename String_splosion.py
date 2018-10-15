def string_splosion(str):
  sum=""
  for i in range(len(str)):
    sum=sum+str[:i+1]
    
  return sum
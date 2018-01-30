
# coding: utf-8

# In[21]:



n = 0
a = 0
b = 0
i = 1
avg = 0
total = 0
avgPairList = []
tempR = 0
tempG = 0
tempB = 0
with open('check.ppm', 'r') as fin:
  
  first_line = fin.readline()
  second_line = fin.readline()
  third_line = fin.readline()
  print ("The first line is "+ first_line)
  print ("The second line is " + second_line)
  print ("The third line is "+ third_line)
  for line in fin:
   
      num = int(line) 
      if i == 1:
        tempR = num
        i = i+1
      elif i == 2:
        tempG = num
        i = i+1
      elif i ==3:
        tempB = num
        i = i+1
      elif i == 4:
        avg = (tempR+num)/2
        avgPairList.append(int(avg))
        i = i+1
      elif i == 5:
        avg = (tempG+num)/2
        avgPairList.append(int(avg))
        i = i+1
      elif i == 6:
        avg = (tempB+num)/2
        avgPairList.append(int(avg))
        i = 1
    
      #print (num)
      
      n = n+1  
print("There are " + str(n) +" numbers")
print(len(avgPairList))

#for i in range(len(avgPairList)):
#     print( avgPairList[i] )

print("done")
        
with open('output.ppm', 'w') as fout:
    fout.write(first_line)
    fout.write("128 256\n")
    fout.write(third_line)
    for i in range(len(avgPairList)):
        fout.write(str(avgPairList[i])+"\n")
        
print("done writing")


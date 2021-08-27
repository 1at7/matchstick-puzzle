'''
Correcting matchstick euation by replacing only one matchstick.

possible equations type is "int" "+ or -" "int" "=" "int"
where all the integers are between 0-9
for example "4-1=6"
'''

#import pdb
#pdb.set_trace()

def solution(eqn,map_matchsticks,all_,plus_one,zero,minus_one):
  print("Given equation is : ",eqn)
  first = int(eqn[0])
  sign = eqn[1]
  second = int(eqn[2])
  third = int(eqn[4])
  total_sticks = map_matchsticks[first]+map_matchsticks[sign]+map_matchsticks[second]+map_matchsticks[third]

  choices_first = all_[first]
  choices_second = all_[second]
  choices_third = all_[third]
  choices_sign = ["+","-"]
  
  possible  = []
  added = 0
  moved = 0
  removed = 0

  for i in choices_first:
    for j in choices_second:
      for k in choices_third:
        for l in choices_sign:
          sticks = map_matchsticks[i]+map_matchsticks[j]+map_matchsticks[k]+map_matchsticks[l]
          if sticks == total_sticks:

            try:
              if i in plus_one[first]: added+=1
            except: 
              pass
            try:
              if i in zero[first]: moved+=1
            except: 
              pass
            try:
              if i in minus_one[first]: removed+=1
            except: 
              pass
            try:
              if j in plus_one[second]: added+=1
            except: 
              pass
            try:
              if j in zero[second]: moved+=1
            except: 
              pass
            try:
              if j in minus_one[second]: removed+=1
            except: 
              pass
            try:
              if k in plus_one[third]: added+=1
            except: 
              pass
            try:
              if k in zero[third]: moved+=1
            except: 
              pass
            try:
              if k in minus_one[third]: removed+=1
            except: 
              pass
            try:
              if l in plus_one[sign]: added+=1
            except: 
              pass
            try:
              if l in minus_one[sign]: removed+=1
            except: 
              pass
            #print(added, removed, '\t', [i,l,j,k])
            if added==1 and removed==1 and moved==0:              
              possible.append([i,l,j,k]) 
            elif moved==1 and removed==0 and added==0:
              possible.append([i,l,j,k]) 
            added=0
            removed=0
            moved=0
  #print("Possible solutions : ",possible)     
  correct=0      
  for i in possible:
    #print(i)
    results = eval(str(i[0])+i[1]+str(i[2]))
    if results==i[3]:
      correct+=1
      print("Corrected equation is : "+str(i[0])+i[1]+str(i[2])+"="+str(i[3]))
  if correct==0:
    print("No possible solution to equation.")
  return None
      

map_matchsticks = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6,"+":2,"-":1}

plus_one = {0:[8],1:[7],2:[],3:[],4:[],5:[6,9],6:[8],7:[],8:[],9:[8],"-":["+"]}
zero = {0:[6,9],1:[],2:[3],3:[5,2],4:[],5:[3],6:[0,9],7:[],8:[],9:[0,6]}
#can_not = {4:4}
minus_one = {0:[],1:[],2:[],3:[],4:[],5:[],6:[5],7:[1],8:[0,9,6],9:[5,3],"+":["-"]}

all_ = {0:[0,6,9,8],1:[1,7],2:[2,3],3:[3,5,2],4:[4],5:[5,3,6,9],6:[6,0,5,8,9],7:[7,1],8:[8,0,6,9],9:[9,0,3,5,6,8]}

eqn1 = "5+7=2" # 9 - 7 = 2
eqn2 = "4-1=6" # 4 + 1 = 5
eqn3 = "6+4=4" #  0 + 4 = 4 and 8 - 4 = 4
eqn4 = "6-2=1"  # no solution
eqn5 = "6+8=8" # 8 + 0 = 8 or 0 + 8 = 8
eqn6 = "3+3=5" # 3+2=5 or 5+2=3
eqn7 = "5+9=9" # 5+3=8 or 6+3=9 or 6-0=6 or 6-6=0 or 6-6=0 or 9-9=0 or 9-0=9

solution(eqn1, map_matchsticks, all_, plus_one, zero, minus_one)
  
  
  
  
  
  
    
    


#This code is incorrect,but I don't want to fix this thing anymore

import random

numls=[1,2,3,4,5,6,7,8,9,10,"J","Q","K"]


class master:
  random.seed()
  cards=random.sample(numls,5)
  static_cards=cards
  for i in range(0,5):
    if static_cards[i] == "J" or static_cards[i] == "Q" or static_cards[i] == "K":
        cards[i]=10

  if sum(cards)%10==0:
    ten_flag=True
  else:
    ten_flag=False
  is_ngau=[]
  print(cards)
  ansls=[]
  point=[]
  
class guest:
  random.seed()
  cards=random.sample(numls,5)
  static_cards=cards
  for i in range(0,5):
    if static_cards[i] == "J" or static_cards[i] == "Q" or static_cards[i] == "K":
        cards[i]=10

  if sum(cards)%10==0:
    ten_flag=True
  else:
    ten_flag=False
  is_ngau=[]
  print(cards)
  ansls=[]
  point=[]

def is_set_ngau(object):

    n = 5
    a = object.cards
    k = [10,20,30]

    cnt = 0

    for i in range(1<<len(a)):
      l = []
      for j in range(len(a)):
        if (i>>j & 1) == 1:
          l.append(a[j])
          if len(l)==3:
            object.ansls.append(l)
        
    for ansls in object.ansls:

      if sum(ansls)==k[0]:
        if object.ten_flag:
          object.is_ngau.append("NYU_NYU")
          break
        else:
          left_number=sum(object.cards)-k[0]
          object.point.append(int(left_number))
      elif sum(ansls)==k[1]:
        if object.ten_flag:
          object.is_ngau.append("NYU_NYU")
        else:
          left_number=sum(object.cards)-k[1]
          object.point.append(int(left_number))      
      elif sum(ansls)==k[2]:
        if object.ten_flag:
          object.is_ngau.append("NYU_NYU")
        else:
          left_number=sum(object.cards)-k[2]
          object.point.append(int(left_number))

      else:
        object.is_ngau.append("TON_TON")

def game():
    if "NYU_NYU" in master.is_ngau and guest.is_ngau:
        print("draw")
    elif "TON_TON" in master.is_ngau and guest.is_ngau:
        print("draw")
    elif "NYU_NYU" in master.is_ngau:
        print("master win")
    elif "NYU_NYU" in guest.is_ngau:
        print("guest win")
    elif "TON_TON" in master.is_ngau:
        print("master lose")
    elif "TON_TON" in guest.is_ngau:
        print("guest lose")
    else:
        master_point=max(master.point)
        guest_point=max(guest.point)
        if master_point > guest_point:
            print("master win")
        elif master_point < guest_point:
            print("guest win")
        else:
            print("draw")

is_set_ngau(master)
is_set_ngau(guest)
game()

"""

n=3
k=10
a=[1,2,8]
for bit in range(2**n):
    sum2 = 0

    for i in range(n):
        if bit & (1 << i):
            sum2 += a[n-1-i]

    if sum2 == k:
        print("Yes")
        exit()
print("No")

n = int(input())
a = list(map(int, input().split()))
k = int(input())

cnt = 0

for i in range(1<<len(a)):
    l = []
    for j in range(len(a)):
        if (i>>j & 1) == 1:
            l.append(a[j])
    if sum(l) == k:
        cnt += 1
print('Yes' if cnt>=1 else 'No')

"""

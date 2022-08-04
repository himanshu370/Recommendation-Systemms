import pickle
from math import*
 
def euclidean_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))


with open('topwear_database','rb') as f:
    topwear_database = pickle.load(f)

with open('bottomwear_database','rb') as f:
    bottomwear_database = pickle.load(f)

def similar_k(image_id,k):

  toprecommended = []
  bottomrecommended = []
  output1 = topwear_database[image_id]
  output2 = bottomwear_database[image_id]
  
  dis_dict = {}
  for key in topwear_database:
    dis_dict[key] = euclidean_distance(topwear_database[key],output1)

  sorted_dis_dict = dict(sorted(dis_dict.items(), key=lambda item: item[1]))
  i = 0

  for key in sorted_dis_dict:
    if i == k:
      break
    if key == image_id:
      continue;
    else:
        toprecommended.append(key)

    i = i+1

  dis_dict = {}
  for key in bottomwear_database:
    dis_dict[key] = euclidean_distance(bottomwear_database[key],output2)

  sorted_dis_dict = dict(sorted(dis_dict.items(), key=lambda item: item[1]))
  i = 0

  for key in sorted_dis_dict:
    if i == k:
      break
    if key == image_id:
      continue;
    else:
        bottomrecommended.append(key)

    i = i+1
  

  return toprecommended,bottomrecommended

#print(main_database)
#rec = similar_k('SEBANDITIN_OPTICAL WHITE (5).jpg',5)
#print(rec)
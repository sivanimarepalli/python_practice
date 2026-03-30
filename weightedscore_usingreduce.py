# Calculate Weighted Score Aggregationusing reduce when given lists of scores and weights.
from functools import reduce
weight=[65,25,35,48,50]
score=[99,85,56,65,52]
weighted_score=reduce(lambda x,y:x+y,map(lambda x,y:x*y,weight,score))
print(weighted_score)
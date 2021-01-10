# =============================================================================
# Nom : GNANASEELAN BENEDICT Jathurshan
#       TCHAKAH Koffi Kafui
# Master SEP
# 2020/2021
# =============================================================================

from random import *
import findspark
findspark.init("C:/spark")
import pyspark
import random
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from time import time
import numpy as np
from operator import add

conf = SparkConf().setAppName("PI").setMaster("local")
sc = SparkContext(conf=conf)

def is_point_inside_unit_circle(p):
 x, y = random(), random()
 return 1 if x*x + y*y < 1 else 0

inside = is_point_inside_unit_circle()
#inside permet de determiner si le point selectionné est dans le cercle où pas, le résultat affiche 1 si oui 0 sinon
## Calcul de pi
count = sc.parallelize(range(0, num_samples)).filter(inside).count()

pi = 4 * count / num_samples
print(pi)

sc.stop()
### Calcul du temps d'exécution 
t_0 = time()


count = sc.parallelize(range(0, num_samples)) \
             .map(inside).reduce(add)
print(np.round(time()-t_0, 3), "temps d'exécution avec n=", num_samples)
print("Pi is roughly %f" % (4.0 * count / num_samples))



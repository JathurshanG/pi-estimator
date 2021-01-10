# =============================================================================
# Nom : GNANASEELAN BENEDICT Jathurshan
#       TCHAKAH Koffi Kafui
# Master SEP
# 2020/2021
# =============================================================================

from random import random
from pyspark import SparkContext, SparkConf
from time import time
import numpy as np
from operator import add
import math

#initialisation de Spark
conf = SparkConf().setAppName("PI").setMaster("local")
sc = SparkContext(conf=conf)

def is_point_inside_unit_circle(_):
    x, y = random(), random()
    return 1 if x*x + y*y < 1 else 0
#Cette Fonction permet de determiner si le point choisit aléatoirement va être dans notre cercle. si 1 alors le point
#figure dans le cercle 0 sinon

#1) Définissons une fonction Permettant de Calculer Spark en utilisant Spark


def pi_spark(n):
      t_0=time()
      #1) Création d'un RDD avec la fonction is_point_inside_unit_circle
      count = sc.parallelize(range(0, n)).map(is_point_inside_unit_circle) \
      .reduce(add)
      # 2) reduce(add) permet de faire la somme des tous les RDD ainsi nous aurons le nombre total de point qui sont
      # présent dans coun#3) Calcul de PI
      spi=(4.0 * count / n)
      print("############ Spark ###################")
      print("Pi est environ egale à avec Spark ", spi )
      #4) estimation du temps afin d'executer le timer
      print(time() - t_0, "temps d'execution avec n=", n)
      print("La différence avec math.pi est de ", (spi-math.pi))


def numpy_pi(n):
    t_0=time()
    matrix = np.zeros((n,1))
    for i in range(0,n):
        matrix[i,:] = is_point_inside_unit_circle(1)
    count=np.sum(matrix)
    npi=4*(count/n)
    print("######## Numpy ###########")
    print("pi est environ egale avec numpy",npi)    
    print(time() - t_0, "temps d'execution avec n=", n)
    print("la difference avec math.pi est de ",(npi-math.pi ))
     

n_sample=100000
pi_spark(n_sample)
numpy_pi(n_sample)

#pour n=1.000.000
n1_sample= 1000000
pi_spark(n1_sample)
numpy_pi(n1_sample)

#arreter Spark
sc.stop()

<h1><center> Pi - Estimator </center></h1>

Le projet a pour but de determiner la valeur de Pi en utilisant Spark et Numpy. La finalité du projet est de faire une étude comparative entre ces derniers et déterminer le plus performant.
Le projet a donné les résultats suivants :

- Pour n=100.000

 Pour n=100000       | Spark                 |        Numpy       |
| :-----------------: |:-------------------: | :-----------------:|
| Temps d'exécution  | 1.152  Secondes       | 0.128 Secondes     |
| Valeur de Pi       | 3.14136               | 3.13512            |
| Ecart % Math.pi    | -0.000232             | -0.00647           |

- Pour n=1000000

 Pour n=1000000      | Spark                 |        Numpy       |
| :----------------: |:--------------------: | :-----------------:|
| Temps d'exécution  | 2.238  Secondes       | 1.172 Secondes     |
| Valeur de Pi       | 3.14222               | 3.143324           |
| Ecart % Math.pi    | 0.000635              | 0.001731           |


Les résultats sont visibles en exécutant run.py

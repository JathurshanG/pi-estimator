# =============================================================================
# Nom : GNANASEELAN BENEDICT Jathurshan
#       TCHAKAH Koffi Kafui
# Master SEP
# 2020/2021
# =============================================================================

from random import *

def is_point_inside_unit_circle():
 x, y = random(), random()
 return 1 if x*x + y*y < 1 else 0

nin = is_point_inside_unit_circle()
#nin permet de determiner si le point selectionner est dans le cercle où pas, le résultat affiche 1 si oui 0 sinon


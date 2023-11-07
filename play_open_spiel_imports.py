from absl import app

from open_spiel.python.algorithms import cfr
from open_spiel.python.algorithms import expected_game_score
import pyspiel
import numpy as np

import sys
import os

# cwd = os.getcwd()
# pyspiel_function_names = dir(pyspiel)
# for pyspiel_function_name in pyspiel_function_names:
#     print(pyspiel_function_name)

sys.path.append('.')
sys.path.append('/home/rick_shilling/open_spiel')
sys.path.append('/home/rick_shilling/open_spiel/open_spiel/python/examples/meta_cfr/sequential_games')

import game_tree_utils
import open_spiel_typing
import world_representation
import meta_learning
# import cfr
# import openspiel_api

# from typing import GameTree
# from open_spiel.python.examples.meta_cfr.sequential_games.typing import HistoryNode
# from open_spiel.python.examples.meta_cfr.sequential_games.typing import InfostateMapping
# from open_spiel.python.examples.meta_cfr.sequential_games.typing import InfostateNode

# from cfr import Players
# from game_tree_utils import HistoryTreeNode

# open_spiel_functions = dir(open_spiel)
# from open_spiel.python.egt. import 

print('end')

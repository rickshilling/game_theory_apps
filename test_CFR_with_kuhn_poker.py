
"""Tests counterfactual regret minimization."""

from absl.testing import absltest
from absl.testing import parameterized

import sys
import importlib.util
spec = importlib.util.find_spec('open_spiel')
print(spec.origin)
sys.path.append(spec.origin)
print(sys.path)

from open_spiel.python.algorithms import cfr
from open_spiel.python.examples isequential_games
# from open_spiel.python.examples.meta_cfr.sequential_games import game_tree_utils as trees

# from open_spiel.open_spiel.python.examples.meta_cfr.sequential_games import cfr

# from open_spiel.python.examples.meta_cfr.sequential_games import cfr
# from open_spiel.python.examples.meta_cfr.sequential_games import game_tree_utils as trees
# from open_spiel.python.examples.meta_cfr.sequential_games import openspiel_api

def _uniform_policy(size):
  if size > 0:
    return [1./size]*size
  return []
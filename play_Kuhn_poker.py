from absl import app

from open_spiel.python.algorithms import cfr
from open_spiel.python.algorithms import expected_game_score
import pyspiel
import numpy as np

import sys
import os

cwd = os.getcwd() 

# /home/rick_shilling/open_spiel/open_spiel/python/examples/meta_cfr/sequential_games/game_tree_utils.py
sys.path.append('.')
sys.path.append('/home/rick_shilling/open_spiel')
sys.path.append('/home/rick_shilling/open_spiel/open_spiel/python/examples/meta_cfr/sequential_games')
print(sys.path)
# import game_tree_utils
import open_spiel.python.games.tic_tac_toe as t3

def main(_):
  game = pyspiel.load_game("kuhn_poker")

  cfr_solver = cfr.CFRSolver(game)
  iterations = 1000

  for i in range(iterations):
    cfr_value = cfr_solver.evaluate_and_update_policy()
    print("Game util at iteration {}: {}".format(i, cfr_value))

  average_policy = cfr_solver.average_policy()
  average_policy_values = expected_game_score.policy_value(
      game.new_initial_state(), [average_policy] * 2)
  print("Computed player 0 value: {}".format(average_policy_values[0]))
  print("Expected player 0 value: {}".format(-1 / 18))

  # ----
  game = pyspiel.load_game("kuhn_poker")
  state = game.new_initial_state()
  while not state.is_terminal():
    legal_actions = state.legal_actions()
    if state.is_chance_node():
        # Sample a chance event outcome.
        outcomes_with_probs = state.chance_outcomes()
        action_list, prob_list = zip(*outcomes_with_probs)
        action = np.random.choice(action_list, p=prob_list)
        state.apply_action(action)
    else:
        # The algorithm can pick an action based on an observation (fully observable
        # games) or an information state (information available for that player)
        # We arbitrarily select the first available action as an example.
        action = legal_actions[0]
        state.apply_action(action)

if __name__ == "__main__":
  app.run(main)
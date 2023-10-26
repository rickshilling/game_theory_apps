import numpy as np

from jax import grad
import jax.numpy as jnp

from open_spiel.python.observation import IIGObserverForPublicInfoGame
import pyspiel

# Based on http://modelai.gettysburg.edu/2013/cfr/cfr.pdf
_NUM_PLAYERS = 2
_S = 10
_N = 4
_GAME_TYPE = pyspiel.GameType(
    short_name="Colonel Blotto",
    long_name="Colonel Blotto",
    dynamics=pyspiel.GameType.Dynamics.SIMULTANEOUS,
    chance_mode=pyspiel.GameType.ChanceMode.DETERMINISTIC,
    information=pyspiel.GameType.Information.PERFECT_INFORMATION,
    utility=pyspiel.GameType.Utility.GENERAL_SUM,
    reward_model=pyspiel.GameType.RewardModel.REWARDS,
    max_num_players=_NUM_PLAYERS,
    min_num_players=_NUM_PLAYERS,
    provides_information_state_string=True,
    provides_information_state_tensor=False,
    provides_observation_string=True,
    provides_observation_tensor=True,
    parameter_specification={})

def enumerate_battelfields(s,n):
    if n<=0 or s<0:
        return np.array([])
    elif n == 1 and s>=0:
        return np.array([[s]])
    else: #n>1 and s>0
        battlefields = []
        for i in range(s+1):
            first_battlefield = [i]
            remaining_battlefields = enumerate_battelfields(s = s-i,n = n - 1)
            for remaining_battlefield in remaining_battlefields:
                battlefield = first_battlefield + remaining_battlefield
                battlefields.append(battlefield)
        return np.array(battlefields)

battlefields = enumerate_battelfields(s=_S,n=_N)
num_battlefields = len(battlefields)
print(f"Battlefields, S = {_S}, N = {_N}, # of battlefields = {num_battlefields}")

_GAME_INFO = pyspiel.GameInfo(
    num_distinct_actions=num_battlefields,
    max_chance_outcomes=0,
    num_players=2,
    min_utility=0,
    max_utility=_N,
    max_game_length=1)
    # utility_sum=0.0)

# class Colonel_Blotto(pyspiel.Game):
#     def __init__(self,params=None):
#         super().__init__(_GAME_TYPE, _GAME_INFO, params or dict())

class Colonel_Blotto(pyspiel.State):
  def __init__(self, game):
    """Constructor; should only be called by Game.new_initial_state."""
    super().__init__(game)
    self._cur_player = 0
    self._player0_score = 0.0
    self._player1_score = 0.0
    self._is_terminal = False
    self.board = np.full( (2,_N), 0)
    self._S0 = _S
    self._S1 = _S

    def _legal_actions(self):
        """Returns a list of legal actions"""
        actions = []
        battlefields = enumerate_battelfields(_S,_N)
        for battlefield1 in battlefields:
            for battlefield2 in battlefields:
                current_board = np.stack(battlefield1,battlefield2,axis=0)
                actions.append(current_board)
        return actions
    
    def _apply_action(self, action):
        self.board = action
        self._is_terminal = True
        self._player0_score = np.count_nonzero(self.board[0] > self.board[1])
        self._player1_score = np.count_nonzero(self.board[1] > self.board[0])

  def is_terminal(self):
    """Returns True if the game is over."""
    return self._is_terminal
  
  def returns(self):
      return [self._player0_score, self._player1_score] 
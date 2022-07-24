import torch
import random
import numpy as np
from collections import deque
from game import SnakeGameAI, Direction, Point

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001 # learning rate

class Agent:
    
    def __init__(self) -> None:
        self.n_games = 0
        self.epsilon = 0 # controls randomnewss
        self.gamma = 0 # discount rate
        self.memory = deque(maxlen=MAX_MEMORY) # popleft() callled when max mem is reached

        # TODO: model, trainer

    def get_state(self, game):
        pass

    def remember(self, state, action, reward, next_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self, state, action, reward, next_state, done):
        pass

    def get_action(self, state):
        pass

def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()
    while True:
        # get the current state
        state_old = agent.get_state(game)

        # get move
        final_move = agent.get_action(state_old)

        # perform a move and get a new state
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)

        # train the short mem of the agent
        agent.train_short_memory(state_old, final_move, reward, state_new, done)

        # remember all
        agent.remember(state_old, final_move, reward, state_new, done)

        if done: #game over
            # train the long memory, plot result
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                # TODO: agent.model.save()
                print('GAME: ', agent.n_games, 'SCORE: ', score, 'RECORD: ', record)

                # TODO: plot data

if __name__ == '__main__':
    train()
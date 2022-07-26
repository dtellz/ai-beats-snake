<p align='center'>
    <img src=assets/python.png width='150'/>
    <img src=assets/anaconda.png width='150'/>
    <img src=assets/pytorch.png width='150'/>
</p>

# AI Learns To Play Snake! Reinforcement Learning With PyTorch and Pygame

In this Python Reinforcement Learning Project I build an AI and then teach it to play Snake! I build everything using Pygame and PyTorch.

Key steps:

- Implement the Snake game.
- Implement the Agent that controls the game.
- Implement the neural network to predict the moves and train it.

## After 500+ games on V1

<p align='center'>
    <img src=assets/stats/v1_555_games.png width='350'/>
</p>
<p align='center'>
    <img src=assets/stats/v1_555_games_data_plot.png width='450'/>
</p>

## After 1000+ games on V1

Model haven't beat its own record but it gets better averaged results every game

<p align='center'>
    <img src=assets/stats/v1_1000_games.png width='350'/>
</p>
<p align='center'>
    <img src=assets/stats/v1_1000_games_data_plot.png width='450'/>
</p>

TODO:

- Avoid the AI to trap itself
- Don't let her get in a loop for too long
- Increase game speed to increase training speed

## Dependencies

I have used Anaconda to create the python env

```
conda create -n pygame_env python=3.7
```

I used pyGame to create the game environment

```
pip install pygame
```

I used pyTorch to create the model

```
pip install torch torchvision
```

Extra deps:

```
pip install matplotlib ipython
```

Partitioned A3C for RogueInABox
==========
  
This software is a fork of:
* [RogueInABox](https://github.com/rogueinabox/rogueinabox)
* [Miyosuda's UNREAL implementation](https://github.com/miyosuda/unreal)

This project has been tested on Debian 9. The setup.sh script installs the necessary dependencies and compiles [Rogue](http://www.anthive.com/project/rogue/). Before running setup.sh you must have installed virtualenv, python3-dev, python3-pip and make. 
The train.sh script starts the training. The test.sh script starts testing.
During training the agent produces real-time statistics on the its perfomance. Among the statistics reported there are: 
* the success rate: the percentage of episodes in which the final state is reached (an equivalent of the accuracy)
* the number of new tiles found during the exploration process
* the number of steps taken to win an episode

For each thread, the statistics are printed as the average of the last 200 simulations. The results.log file contains the average of the average of each thread.
Through the options.py file you can change most of the architecture parameters, including: the number of threads to use, whether to use the GPU or not, the initial learning rate, the log directories and much more.
The framework is composed of the following classes:
* Application (train.py): the global A3C agent, which contains the methods for starting the local workers.
* Trainer (trainer.py): a local A3C worker.
* RMSPropApplier (rmsprop_applier.py): the class for asynchronously computing the gradient.
* MultiAgentModel and A3CModel (multi_agent_model.py and a3c_model.py): within these classes the structure of the neural network is specified (LSTM, policy layer, value layer, CNN, FC, ecc..).
* Environment (environment.py): class that handles the interface between the agent and the environment. The Environment class has been extended with RogueEnvironment (rogue_environment.py). RogueEnvironment contains methods for calculating rewards, obtaining statuses and statistics on episodes, etc.

Training Video
-------

[![Youtube video of the training](https://img.youtube.com/vi/1j6_165Q46w/0.jpg)](https://www.youtube.com/watch?v=1j6_165Q46w)


License
-------

This software is a fork of:
* [RogueInABox](https://github.com/rogueinabox/rogueinabox)
* [Miyosuda's UNREAL implementation](https://github.com/miyosuda/unreal)
Those parts of this software that are not inherited from the aforementioned repositories are released under the GPL v3.0 licence.
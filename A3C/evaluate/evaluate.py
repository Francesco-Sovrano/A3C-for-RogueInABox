import sys
import json

from agent import A3C_Agent
import options
flags = options.get()


agent = A3C_Agent({'gui': False})

nruns = flags.match_count_for_evaluation
steps = flags.steps_per_episode

for run in range(nruns):
    agent.environment.reset()
    
    if run % (nruns // 20) == 0:
        print("run number: %s..." % run, file=sys.stderr)
    
    for step in range(steps):
        terminal = agent.act()
        
        if terminal:
            break

agent.environment.game.stop()
stats = agent.environment.get_statistics()

json.dump(stats, sys.stdout, indent=4)



from agent import A3C_Agent


configs = {
   'userinterface': 'curses',
   'verbose': 3,
   'gui': True,
   'memory_size': 0,
   'test': False,
   'timer_ms': 50
}

agent = A3C_Agent(configs)
agent.run()


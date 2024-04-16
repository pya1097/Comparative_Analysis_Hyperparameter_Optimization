import subprocess
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
scripts = [os.path.join(script_dir,'optuna_src.py'), os.path.join(script_dir,'hyperopt_src.py'),os.path.join(script_dir,'skopt_src.py')]

for script in scripts:
    subprocess.run(['python', script])
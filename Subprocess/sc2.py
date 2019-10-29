import subprocess

subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'partial commit'])
subprocess.call(['git', 'push', 'origin', 'master'])
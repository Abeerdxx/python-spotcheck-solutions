from subprocess import Popen, PIPE

Popen(['git', 'commit', '-m', "'hello, world'"]) # watch out for quotes
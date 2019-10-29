from subprocess import call

call(['git', 'add', '.'])
call(['git', 'commit', '-m', 'partial commit'])
call(['git', 'push', 'origin', 'master'])
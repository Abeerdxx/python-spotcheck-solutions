from subprocess import Popen, PIPE

# Part 1, creates the result_n.txt files:
for i in range(1, 4):
    file_name = 'result_' + str(i) + '.txt'
    Popen(['touch', file_name])  # for Mac
    Popen(['copy', 'nul', file_name])  # for Windows

# Part 2, checks if files exist based off Popen results
process = Popen(['ls'], stdout=PIPE, text=True)  # for Mac
process = Popen(['dir'], stdout=PIPE, text=True)  # for Windows
results, err = process.communicate()

for i in range(1, 11):
    file_name = 'result_' + str(i) + '.txt'

    if file_name in stdout:
        print(file_name + " successfully created")
    else:
        print(file_name + " not created")

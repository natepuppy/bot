

import win32com.shell.shell as shell

conglomerate_of_cmd = ''

cmd_part_1 = 'C:\WINDOWS\system32\\net.exe user user' 
cmd_part_2 = ' 0223 /add '
cmd_part_3 = '&& '

start = 901
stop = 1001
for i in range(start, stop):
    conglomerate_of_cmd += cmd_part_1
    conglomerate_of_cmd += str(i)
    conglomerate_of_cmd += cmd_part_2

    if i != stop - 1:
        conglomerate_of_cmd += cmd_part_3

    print(i)

print(conglomerate_of_cmd)

shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+conglomerate_of_cmd)


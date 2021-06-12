

import win32com.shell.shell as shell

def create_range(start, stop):
    conglomerate_of_cmd = ''
    cmd_part_1 = 'C:\WINDOWS\system32\\net.exe user user' 
    cmd_part_2 = ' 0223 /add '
    cmd_part_3 = '&& '

    for i in range(start, stop):
        conglomerate_of_cmd += cmd_part_1
        conglomerate_of_cmd += str(i)
        conglomerate_of_cmd += cmd_part_2

        if i != stop - 1:
            conglomerate_of_cmd += cmd_part_3

    print(conglomerate_of_cmd)

    shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+conglomerate_of_cmd)


def run_in_segments(start, stop):
    start_ = 0
    stop_ = 0
    for i in range(start, stop):
        if (i % 100 == 0 and i != 0) or i == stop - 1:
            start_ = stop_ + 1
            stop_ = i
            print(start_, " ", stop_)
            create_range(start_, stop_)

start = 1
stop = 1001
run_in_segments(start, stop)
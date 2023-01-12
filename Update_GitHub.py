import os,time


def GetTime():
    return time.strftime("%y-%m-%d %H:%M:%S", time.localtime())


if __name__ == '__main__':
    commit_msg = f" \"Code updated {GetTime()}\" "
    result = 128
    cmd_2 = "git add ."
    cmd_3 = "git commit -m" + commit_msg
    cmd_4 = "git push -u origin main"
    os.system(cmd_2)
    os.system(cmd_3)

    while (result != 0):
        result = os.system(cmd_4)


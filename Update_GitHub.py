import os,time



def GetTime():
    return time.strftime("%y-%m-%d %H:%M:%S", time.localtime())

commit_msg = f" \"Code updated {GetTime()}\" "


cmd_2 = "git add ."
cmd_3 = "git commit -m" + commit_msg
cmd_4 = "git push"

os.system(cmd_2)

os.system(cmd_3)

result = 128
while (result != 0):
    print("[CMD]", cmd_4)
    result = os.system(cmd_4)
    print(result)

print("END")

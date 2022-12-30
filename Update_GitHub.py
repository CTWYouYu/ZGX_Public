import os,time



def GetTime():
    return time.strftime("%y-%m-%d %H:%M:%S", time.localtime())

commit_msg = f" \"Code updated {GetTime()}\" "

# cmd_1 = "git status"
cmd_2 = "git add ."
cmd_3 = "git commit -m" + commit_msg
cmd_4 = "git push"
# cmd_1 = ""

# git pull origin main --allow-unrelated-histories

# print("start")
# os.system("cd..")
# print("[CMD]",cmd_1)
# os.system(cmd_1)
# print("[CMD]",cmd_2)
os.system(cmd_2)
# print("[CMD]",cmd_3)
os.system(cmd_3)

result = 128
while (result != 0):
    print("[CMD]", cmd_4)
    result = os.system(cmd_4)
    print(result)

print("END")
# time.sleep(100000)
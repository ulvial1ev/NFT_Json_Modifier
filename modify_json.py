import os


os.environ['dir_name'] = input("Input directory of the json files(example: C:\\Users\\user1\\project\\json ) ")

os.chdir(os.environ['dir_name'])
print(os.getcwd())

fp = 3

print("BACK UP YOUR JSON FILES FIRST, THIS SCRIPT WILL ERASE ALL THE CONTENT BEFORE INITIATING. "
      " THEREFORE, IF SOMETHING WAS WRONG YOU WILL LOSE YOUR INITIAL FILE CONTENT")

for fp in os.listdir(os.getcwd()):
    if fp.endswith('.json'):
        f = open(fp, 'r+')
        text1 = input("Input new phrase");
        text2= input("Input the phrase that should be replaced ( if it is a link, input the full length link(https://example.com/ )")

        content = f.read().replace(text2, text1)
        f.seek(0)
        f.truncate()
        f.write(content)
        print("Done JSON number " + str(fp.strip(".json")))

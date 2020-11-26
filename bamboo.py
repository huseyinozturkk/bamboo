import random,os,argparse


parser=argparse.ArgumentParser()
parser.add_argument("-f","--file",dest="file_name")
parser.add_argument("-o","--o",dest="output_file_name",default="output.py")
parser.add_argument("-l","-list",dest="var_name_gen_list",default="ninja")
parser.add_argument("-vl","--vl",dest="var_name_len",default="10")
args=parser.parse_args()

file_name=args.file_name
var_name_gen_list=args.var_name_gen_list
var_name_len=int(args.var_name_len)
output_file_name=args.output_file_name


#Fixed Def.
s_n='\n'
code_exec=""
code_vars_str=""
code_vars_list=[]
code_list=[]
ninja_list=("Il1Li")
normal_list=("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789_")
var_list=[]

if (args.var_name_gen_list=="ninja"):
    var_name_gen_list=ninja_list
else:
    var_name_gen_list=normal_list


#Functions
def clr():
    os.system('cls' if os.name=='nt' else 'clear')
    os.system("color a" if os.name=='nt' else "printf '\033[32m'")

def random_name(input_list):
    name="l"
    for i in range(random.randint(1,var_name_len)):
        name=name+random.choice(input_list)

    return name

def split_line(line,code):
    for i in range(len(line)):
        code_list.append(line[i])

#Main
clr()

file=open(file_name,"r")
lines=file.readlines()

os.system("echo reading file..")

for i in range(len(lines)):
    line_str=lines[i]
    split_line(line_str,code_list)

os.system("echo generating var names...")
#birden fazla tekrar eden karakterleri bulmak

char_qnt=len(code_list)
duplicates_removed=list(dict.fromkeys(code_list))
char_qnt_duplicates_removed=len(duplicates_removed)#chars with duplicates removed

#dict içerisine değişken adlarını atamak
while(1):
    var_name=random_name(var_name_gen_list)
    if var_name not in var_list:
        var_list.append(var_name)
    if (len(var_list)==char_qnt_duplicates_removed):
        break

pre_dict={}

for i in range(len(duplicates_removed)):
    for x in range(len(var_list)):
        pre_dict[duplicates_removed[i]]=var_list[i]

os.system("echo generating code...")

for i in code_list:
    if i in pre_dict:
        code_exec=code_exec+pre_dict[i]+"+"

code_exec=code_exec[:-1]

        
a1=list(pre_dict.items())
random.shuffle(a1)
pre_dict=dict(a1)

for i in pre_dict:

    #code_vars_list.append(str("{}='{}''").format(pre_dict[i],i))
    code_vars_str=code_vars_str+pre_dict[i]+","

code_vars_str=code_vars_str[:-1]+"="

for i in pre_dict:
    if i=='\n':
        code_vars_str=code_vars_str+"'"+"\\n"+"'"+","
    else:    
        code_vars_str=code_vars_str+"'"+i+"'"+","

code_vars_str=code_vars_str[:-1]
os.system("echo writing code to file..")

out=open(output_file_name,"w+")
out.write(code_vars_str)
out.write("\n"+"exec"+"("+code_exec+")")
out.close()
os.system("echo file is ready..")

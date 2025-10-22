import os
import sys
import time

if len(sys.argv) != 2:
    sys.exit('too many arguments')
else:
    def_path = sys.argv[1]

lang_dict = {
              "cpp" : "C/C++",
              "php" : "PHP",
              "py"  : "PYTHON",
              "sh"  : "BASH",
              "oth" : "OTHERS"
            }
line_dict = {
               "C/C++"  : int(),
               "PYTHON" : int(),
               "BASH"   : int(),
               "PHP"    : int(),
               "OTHERS" : int()
    
}    

def how_much():
    for path,_,files in os.walk(def_path):
        for file in files:
            format_end = os.path.splitext(file)[-1].split('.')[-1]
            if format_end not in lang_dict.keys():
                format_end = 'oth'
            full_name = f"{path}/{file}"
            try:
                with open(full_name,'r') as f:
                    content = f.readlines()
                    for line in content:
                        
                        if len(line.strip()) !=0:
                            line_dict[lang_dict[format_end]] += 1
            except UnicodeDecodeError:
                pass
       
def erase_dict(dictionary):
    for key,_ in dictionary.items():
        if type(dictionary[key]) == int:
            dictionary[key] = 0


def visulation():
    global line_dict
    max_dict_val = max(line_dict.values())
    line_dict = dict(sorted(line_dict.items(),key= lambda x: x[1],reverse=True))
    for key,value in line_dict.items():
        if value == 0:
            continue
        col, _ = os.get_terminal_size()
        if value == max_dict_val:
            val = int((value/max_dict_val)*col - len(f"{key}:{value} ") -1 )
        else:
            val = int((value/max_dict_val)*col)
        bar = "\x1b[1;32m"+round(val)*"\u2588"+"\x1b[0m"
        print(f"{key}:{value} {bar}\n")
    

def main():
    while True:
        how_much()
        visulation() 
        erase_dict(line_dict)
        time.sleep(10)
        
main()

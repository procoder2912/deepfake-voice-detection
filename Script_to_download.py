import requests as re
import os as o
import time
li = [1,5,10,20,50,100]
output_folder = 'Cloned_Train'


for j in range(0,4):
    url = f"https://audiodemos.github.io/set{j}"
    print("Set Changed")
    org = "ground_truth.wav"
    original = url+"/"+org
    resp = re.get(original)
    path = o.path.join("Original_Train",str(j)+"speaker2"+org)
    if resp.status_code == 200:
        with open(path,'wb') as f:
            f.write(resp.content)
        print(f"\rfile {str(j)+org} downloaded")
    else:
        print("Error in downloading orginal")

    for i in range(0,18):
    
    
        if i<6:
            new = f"embedadapt_{li[i]}sample.wav"
        elif i<12 and i>6:
            new = f"wholemodel_{li[i%6]}sample.wav"
        else:
            new = f"withoutfinetuning_{li[i%6]}sample.wav"
     
        resp = re.get(url+"/"+new)
        path = o.path.join(output_folder,str(j)+"speaker2"+new)
        if resp.status_code == 200:
            with open(path,'wb') as f:
                f.write(resp.content)
            print(f"\rfile {str(j)+new} downloaded")
            time.sleep(1) 
        else:
            print("Some error occured")



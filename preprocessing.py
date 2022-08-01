import os 
import json
import re 
import numpy as np 


def create_data(datapath, outputpath):
    files = os.listdir(datapath)
    labels = []
    with open('./benchmarkList.md', 'r') as f:
        DRBlabel = f.read()
    
        labels = re.findall(r'(DRB\w*)\S+\s+\|([Y|N])', DRBlabel)
    
    
    labels = np.array(labels)
    print(len(labels))

    # print(files) 
    dataset = []
    ids = [] 
    for f in files: 
        data = {}
        with open(os.path.join(datapath, f), 'r') as fl: 
            id = f.split('-',1)[0]
            print(id)
            code = str(fl.read()) 
            data["func"] = remove_comments(code) 
            # print(data["func"])
            data["comment"] = extract_comments(code)
            data["idx"] = id
            try:
                idx = np.argwhere(labels == id)[0][0]
                print(labels[idx][0], labels[idx][1])
                data["label"] = labels[idx][1]
            except: 
                pass 
            ids.append(id)
        dataset.append(data) 

    
    with open(os.path.join(outputpath, "data.jsonl"), 'w') as outfile: 
        for data in dataset:
            json.dump(data, outfile)
            outfile.write('\n')

def remove_comments(func): 
    pattern = r'(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)'  
    regex = re.compile(pattern, re.MULTILINE | re.DOTALL) 
    
    def _replacer(match): 
        # print(match)
        if match.group(2) is not None: 
            return ""
        else: 
            return match.group(1) 

    return regex.sub(_replacer, func)


def extract_comments(func): 
    comments = re.findall(r'(//[^\n]*|/\*[\s\S]*?\*/)', func)
    comments = [ c.strip('/*') for c in comments]
    # print(comments)
    return '\n'.join(comments[1:]) 
    
def create_train(path): 
    ids = []
    labels = dict()
    with open(os.path.join(path, "data.jsonl"), 'r') as f:
        lines = f.readlines() 

        for line in lines: 
            data = json.loads(line) 
            ids.append(data['idx']) 
            labels[data['idx']] = data['label'] 

    comb_array = np.array(np.meshgrid(ids, ids)).T.reshape(-1, 2) 

    with open(os.path.join(outputpath, "train.txt"), 'w') as outfile: 
        for pair in comb_array:
            if pair[0] == pair[1]:
                outfile.write(pair[0] + '\t' + pair[1] + '\t' + '1' + '\n')
            else: 
                outfile.write(pair[0] + '\t' + pair[1] + '\t' + '0' + '\n')
        print(len(comb_array))


        


    pass

def create_valid(path): 
    pass


def create_test(outputpath): 
    ids = [] 
    with open(os.path.join(outputpath, "data.jsonl"), 'r') as f: 
        lines = f.readlines() 
        # print(lines)
        for line in lines: 
            data = json.loads(line) 
            ids.append(data['idx'])

    comb_array = np.array(np.meshgrid(ids, ids)).T.reshape(-1, 2)
    # print(ids)
    # print(comb_array) 

    # ids1 = np.random.permutation(ids)
    with open(os.path.join(outputpath, "test.txt"), 'w') as outfile: 
        for pair in comb_array:
            if pair[0] == pair[1]:
                outfile.write(pair[0] + '\t' + pair[1] + '\t' + '1' + '\n')
            else: 
                outfile.write(pair[0] + '\t' + pair[1] + '\t' + '0' + '\n')
        print(len(comb_array))
        
    # return ids




def main(): 
    outputpath = './dataset'
    datapath = './micro-benchmarks' 
    # create data.jsonl 
    create_data(datapath, outputpath)


    # create train.txt 
    # create_train(outputpath)

    # create valid.txt 
    # create_valid(outputpath) 

    # create test.txt 
    create_test(outputpath)
    

if __name__ == "__main__": 
    main()


import pweave
import argparse
import os
import shutil

parser = argparse.ArgumentParser(description="Report generator script")

parser.add_argument("--m", required=True, help="path to metadata file")
parser.add_argument("--n", required=True, help="path to notes file")
parser.add_argument("--r", required=True, help="path to recall info file")

args=parser.parse_args()

metadata_file = str(args.m)
notes_file = str(args.n)
recall_file = str(args.r)

fd = "./figures"
name_stem = "README"

pmd_file = open(name_stem + ".pmd", 'w')
pmd_string = name_stem + ".pmd"

with open("state_glob_lineages_template.pmd") as f:
    for l in f:
        if "##CHANGE" in l:
            if "metadata" in l:
                new_l = 'metadata = "' + metadata_file + '"\n' 
            if "input_file" in l:
                new_l = 'input_file = "' + notes_file + '"\n' 
            if "recall_file" in l:
                new_l = 'recall_file = "' + recall_file + '"\n' 
            
        else:
            new_l = l
        
        pmd_file.write(new_l)
    
    
pmd_file.close()

pweave.weave(pmd_string, doctype = "pandoc", figdir=fd)

new_file = name_stem + ".md"
index_file = "index.md"

path_to_dir = os.path.dirname(__file__)
source = os.path.join(path_to_dir, new_file)
destination = os.path.join(path_to_dir, "../../", new_file)
destination2 = os.path.join(path_to_dir, "../../docs", index_file)

shutil.copyfile(source, destination)  
shutil.move(source, destination2)

os.remove(name_stem + ".pmd")
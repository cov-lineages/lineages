import pweave
import argparse
import os
import shutil

parser = argparse.ArgumentParser(description="Lineage notes script")

parser.add_argument("--n", required=True, help="path to notes file")

args=parser.parse_args()

notes_file = str(args.n)

name_stem = "lineage_notes"

pmd_file = open(name_stem + ".pmd", 'w')
pmd_string = name_stem + ".pmd"

with open("lineage_notes_template.pmd") as f:
    for l in f:
        if "##CHANGE" in l:
            if "input_file" in l:
                new_l = 'input_file = "' + notes_file + '"\n' 
            
        else:
            new_l = l
        
        pmd_file.write(new_l)
    
    
pmd_file.close()


pweave.weave(pmd_string, doctype = "pandoc")

new_file = name_stem + ".md"

path_to_dir = os.path.dirname(__file__)
source = os.path.join(path_to_dir, new_file)
destination = os.path.join(path_to_dir, "../../docs", new_file)

shutil.move(source, destination)  

os.remove(name_stem + ".pmd")
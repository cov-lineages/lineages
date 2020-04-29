import pweave
import argparse

parser = argparse.ArgumentParser(description="Report generator script")

parser.add_argument("--m", required=True, help="path to metadata file")

args=parser.parse_args()

metadata_file = str(args.m)

fd = "./figures"
name_stem = "README"

pmd_file = open(name_stem + ".pmd", 'w')
pmd_string = name_stem + ".pmd"

with open("state_glob_lineages_template.pmd") as f:
    for l in f:
        if "##CHANGE" in l:
            if "metadata" in l:
                new_l = 'metadata = "' + metadata_file + '"\n' 
            
        else:
            new_l = l
        
        pmd_file.write(new_l)
    
    
pmd_file.close()



pweave.weave(pmd_string, doctype = "pandoc", figdir=fd)

import argparse
import collections
import os
cwd = os.getcwd()



def parse_args():
    parser = argparse.ArgumentParser(description='Find all snps.')
    parser.add_argument("-i", action="store", type=str, dest="description_text")
    parser.add_argument("-o", action="store", type=str, dest="description_out")
    return parser.parse_args()


def generate_report():
    args= parse_args()
    fw = open(args.description_out,"w")
    fw.write("# Lineage Notes 2020-05-07\n\n")
    fw.write("""This document describes each lineage that was called during the manual curation of GISAID data and a\
brief justification of why this lineage was called. Each week as more data is produced and analysed, new lineages may \
be called and it may turn out that older lineages are in fact not lineages. This document will provide information about each \
lineage and clarify the decision making process. We take into account both phylogenetic and \
epidemiological information and use all available evidence to informed lineage calls weekly.\n\n""")
    fw.write("| Lineage | Notes |\n|:-----|:-----|\n")

    with open(args.description_text,"r") as f:
        for l in f:
            l = l.rstrip("\n")
            if l.startswith("Lineage"):
                pass
            else:
                lineage,notes = l.split('\t')
                fw.write(f"| {lineage} | {notes} |\n")
    fw.write("\n*Lineages that are no longer being assigned.\n")
    fw.close()


if __name__ == '__main__':

    generate_report()






**A dynamic nomenclature proposal for SARS-CoV-2 to assist genomic epidemiology**
Andrew Rambaut, Edward C. Holmes, Verity Hill, Áine O’Toole, JT McCrone, Chris Ruis, Louis du Plessis, Oliver G. Pybus

This is a companion repository to the paper describing a dynamic lineage nomenclature system for SARS-CoV-2.

A pre-print of the paper can be found here: https://doi.org/10.1101/2020.04.17.046086

This contains the following files:

A table of acknowledgements for the GISAID genome sequences used to develop this paper:
https://raw.githubusercontent.com/hCoV-2019/lineages/master/gisaid_acknowledgements.tsv

<img src="https://github.com/hCoV-2019/pangolin/blob/master/docs/logo.png" width="100">**P**hylogenetic **A**ssignment of **N**amed **G**lobal **O**utbreak **LIN**eages

Software to help assign your own SARS-CoV-2 genomes to these lineages is available:
http://github.com/hCoV-2019/pangolin

## lineages data release 2020-05-19

### Updates:

This weeks data release has some substantial changes. 

- We've implemented a system of "putative" lineages. Any lineages that have a recall value of < 95% are given `p` flag. E.g. `B.1.16` becomes `B.1.p16`. 

- A large lineage within B.1 with `28881GA`,`28882GA`,`28883GC` defining SNPs has been called as B.1.1. Any lineages that existed within this that would have previously been called B.1.X have been renamed as B.1.1.X, with the count restarted. Details on which lineages have been renamed can be found in the lineage descriptions.

## Lineage summary

[[Introduction](#introduction)]

[[Additional notes](#descriptions)] on justification and descriptions are available after the following table, and can also be accessed by clicking on the lineage name in the table.

Each week as more data is produced and analysed, new lineages may be called and it may turn out that older lineages are in fact not lineages. We take into account both phylogenetic and 
epidemiological information and use all available evidence to informed lineage calls weekly.





---------------------------------------------------------------------------ValueError                                Traceback (most recent call last)<ipython-input-1-c68459e1eba7> in <module>
----> 1 lin_obj_dict, taxa, most_recent_sample = parse.make_objects(metadata)
      2 week = most_recent_sample
      3 
      4 print("This report gives summaries of globally circulating lineages as of " + str(week) + ". ")
      5 
~/Documents/GitHub/lineages/lineages/scripts/utils/parse_data.py in make_objects(metadata_file)
     73             metadata = [country, date, epiweek]
     74 
---> 75             new_taxon = classes.taxon(tax_name, lin_string, metadata)
     76             taxa.append(new_taxon)
     77             if new_taxon.date_dt != "NA":
~/Documents/GitHub/lineages/lineages/scripts/utils/class_defs.py in __init__(self, record_id, lineage, metadata)
     16         epiweek_prep = metadata[2]
     17         if epiweek_prep != "":
---> 18             if float(epiweek_prep) != 0.0:
     19                 self.epiweek = Week(2020, int(float(epiweek_prep)))
     20             else:
ValueError: could not convert string to float: '2020-03-02'

Sequences which were replicates or too error-prone were removed from this analysis.




---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-427e1617e061> in <module>
----> 1 status_counts, reactivated_lineages, continuining_lineages = parse.describe_lineages(lin_obj_dict.values())
      2 
      3 reactivateds = status_counts["Reactivated"]
      4 actives = status_counts["Reactivated"] + status_counts["Continuing"]
      5 continuous = status_counts["Continuing"]
NameError: name 'lin_obj_dict' is not defined


Note that the status of a lineage is highly likely to be due to heterogeneity in sampling, and not necessarily indicative of the real decline of lineages.

The table below shows summary information of each lineage. 

The "most common countries" column shows the three countries with the most sequences from each lineage, and the percentages by the country represent the percentage of sequences in that lineage taken from that location.

Again, please interpret this with caution. Some countries are sequencing much more than others, and so locations of lineages may be at least partially due to this. It does not imply direction of transmission from one country to another. 
Sometimes we have been able to examine lineages which we know are circulating in one country by looking at sequences from another country due to associated epidemiological information.





---------------------------------------------------------------------------NameError                                 Traceback (most recent call last)<ipython-input-1-7c514fa6d45a> in <module>
----> 1 df = parse.make_dataframe(lin_obj_dict)
      2 
      3 df.sort_values(by=["Lineage name"], ascending=True, inplace=True)
      4 df.set_index("Lineage name", inplace=True)
      5 #df.sort_values(by=["Number of taxa"], ascending=False, inplace=True)
NameError: name 'lin_obj_dict' is not defined

## Lineage descriptions <a name="descriptions"></a>


BS = bootstrap







### A

Root of the pandemic lies within lineage A. Many sequences originating from China and many global exports; including to South East Asia, Japan, South Korea, Australia, the USA and Europe, represented in this lineage


### A.1

A North American lineage, with some sequences from Australia in (BS=95)


### A.1.1

Iceland lineage (BS:100->79)


### *A.1.2

Reassigned to A.1 (low BS two weeks running)


### A.1.3

Australian lineage (BS=100)


### A.2

Spain/ Chile/ Australia/ Europe (BS=93)


### A.3

USA and Australian lineage (BS: 100 -> 44). Low BS likely due to India/NCDC-3279/2020, which was misassigned and likely jumps around the tree.


### A.4

Lineage circulating in USA (all sequences Wisconsin) (BS=100)


### A.5

A lineage with a lot of representation from Spanish-speaking countries. A majoritively Spain/ South-American lineage, lower bootstrap this week BS 87->20. 


### A.6

Lineage in Thailand (BS=87)


### A.p7

Potential lineage: Saudi Arabia, Russia, Turkey, India (BS=50)


### B

Base of this lineage also lies in China, with many global exports, two distinct SNPs `8782TC` and `28144CT` define this lineage


### B.1

A large European lineage that corresponds to the Italian outbreak.


### B.1.45

Australian lineage (more support this week BS=91), all Australian sequences within a background of European and Asian


### B.1.49

Scotland (BS=92)


### B.1.1

New European lineage that's been assigned due to high support and 3 clear SNPs `28881GA`,`28882GA`,`28883GC`. Note: Sub-lineages that previously existed within this lineage have been reassigned a new lineage name.


### B.1.1.1

Formerly B.1.1, UK/ Europe (BS=80)


### B.1.1.2

Formerly B.1.24, Welsh lineage (BS=100->47 this week)


### B.1.1.3

Formerly B.1.65, English lineage (BS=100)


### B.1.1.4

Formerly B.1.55, UK (BS=100)


### B.1.1.5

Formerly B.1.54, Iceland/ Belgium/ UK (BS=100)


### B.1.1.6

Formerly B.1.62, Austrian lineage (BS=100)


### B.1.1.7

Formerly B.1.1.56, UK/ Australia/ Iceland (BS=100)


### B.1.1.8

Formerly B.1.63, UK/ USA/ Australia (BS=100)


### B.1.1.9

Formerly B.1.53, England / USA (BS=83)


### B.1.1.10

Formerly B.1.10, UK/ Iceland (BS lower this week 70 -> 11), a lot of diversity in this lineage, now has a Turkish sequence. 


### B.1.1.p11

Formerly B.1.50, Portugal/ Wales (BS=55 this week)


### B.1.1.p12

Formerly B.1.49, Scottish lineage (BS=48)


### B.1.1.13

Formerly B.1.61, UK lineage (BS=95)


### B.1.1.14

Formerly B.1.60, Scottish lineage (BS=89)


### B.1.1.p15

Formerly B.1.46, Luxembourg (BS=11, but internal nodes all 100 and all Luxembourg)


### B.1.1.p16

Formerly B.1.59, Wales lineage (BS=70)


### B.1.1.17

Formerly B.1.58, Iceland lineage (BS=100)


### B.1.1.18

Formerly B.1.57, Austrian lineage (BS=97)


### B.1.1.p19

Formerly B.1.45, Australian lineage (BS=91)


### B.1.p2

USA (low BS=9)


### B.1.3

USA(BS=39)


### B.1.5

England/ Spain/ Turkey/ Australia/ USA/ Brasil. Low support at parent node now, potentially as a result of homoplasies (BS=5)


### B.1.5.1

Iceland (BS=27), but all sequences suggest an Icelandic lineage


### B.1.5.2

Netherlands (BS=100)


### B.1.5.3

England (now containing an Australian & Swedish seqeuence) (BS=96)


### B.1.5.4

Spain (BS=100)


### B.1.5.5

England (BS=100)


### B.1.5.6

UK (BS=100)


### B.1.6

Belgian lineage (BS=55)


### *B.1.7

Low support (BS=9), reassigned B.1


### B.1.8

Netherlands/ Europe (BS=47)


### B.1.p9

Netherlands/ Belgium/ Turkey/ DRC (BS=9)


### B.1.p11

UK lineage but low support and splitting up, pruned down quite a lot, but may need to be removed next time (BS=31)


### B.1.12

BeNeLux (BS=18 this week, lots of internal 100)


### B.1.13

England/ Australia, may need refining parent node BS=59, internal node of 100


### B.1.p16

Belgium, low support (BS=19), keep an eye on this with new data 


### B.1.19

USA (BS=100)


### *B.1.20

Low support (BS=5), reassigned B.1


### B.1.p21

Washington (USA) (Low BS=9)


### B.1.22

Netherlands (BS=100)


### B.1.23

Australia (BS=68)


### B.1.p25

Australian lineage, some low internal bootstrap values and parent node BS=16. However all sequences within it are Australian and that's with quite a lot of diversity as well.


### B.1.26

USA lineage (BS=83)


### B.1.27

USA/ Argentina (BS=74)


### *B.1.28

Denmark/ USA new parent node BS=9, reassigned B.1


### B.1.29

USA (BS=86)


### B.1.30

England (BS=100)


### B.1.31

Australia (BS=100)


### B.1.32

Swedish lineage (BS=95)


### B.1.33

Australian lineage (BS=100)


### B.1.34

England (BS=100)


### B.1.35

Wales (BS=9)


### B.1.36

Turkey/ Saudi Arabia/ Egypt / Finland & England (BS=100)


### B.1.37

USA lineage (BS=93)


### B.1.38

USA (BS=100)


### B.1.39

Denmark (BS=100)


### B.1.40

Scotland (BS=90)


### B.1.41

USA lineage (BS=100)


### B.1.p42

Sweden/ Denmark lineage, split up in the tree this week


### B.1.43

USA (BS=100)


### B.1.44

Wales (BS=100)


### *B.1.47

England, caused a lot of problems last release and many misassignments (BS=100)


### *B.1.48

England (BS=39)


### *B.1.51

UK (BS=11, got split in half)


### *B.1.52

England (BS=30)


### B.1.64

English lineage (BS=100)


### B.1.66

English lineage (BS=100)


### B.1.67

Wales lineage (BS=96)


### B.1.p68

USA lineage (UT) (BS=100)


### B.1.69

Scottish lineage (BS=100)


### B.1.70

Scottish lineage (BS=70)


### B.1.71

UK lineage (BS=100)


### B.1.72

UK lineage (BRIS) (BS=100)


### B.1.p73

Scotland lineage (BS=5, so very low)


### B.2

A previously defined large European/ Australian lineage that with new data has low support (BS=13). This lineage and its sublineage will need to be re-examined and perhaps refined quite significantly in next weeks data


### B.2.1

Large lineage with representation from UK, Europe, Jordan, Australia, USA, India, Ghana (BS=11) 


### B.2.2

BeNeLux/ UK/ Singapore /Australia /USA (BS=85)


### *B.2.3

Reassigned B.2 (No good internal BS, misassignments)


### B.2.4

Australian lineage, took a subset of previously defined B.2.4 and reassigning them B.2


### B.2.5

Spain/ England / Australia (BS=17) *flagged because of low bootstrap


### B.2.6

UK/ Singapore/ Jordan/ Iceland, previously just UK & Australia (BS=11, low support)


### B.2.7

Iceland lineage (BS=60)


### B.3

A European lineage, including a large set of sequences from Wales, low parent node support (BS=14)


### B.4

Iran lineage, many sequences we have of this lineage are associated with travel histories from Iran (BS=43)


### B.5

Japanese lineage (BS=75) 


### B.6

India/ Philippines/ UK/ North America/ Australia/ Singapore (BS=100)


### B.7

Hong Kong lineage (BS 73 -> 27)


### *B.8

Reassigned to B (BS 27 -> 14, got split into two clades with low support in this weeks tree)


### B.9

Australian/ England lineage (BS=100)


### B.10

Northern Ireland/ England/ Scotland (BS=89)


### B.p11

Netherlands lineage (BS=100)


### B.p12

Japan lineage (BS=99, but only a few sequences)


### B.13

USA (WI) lineage (BS=100)


### B.14

USA (CA) lineage (BS=100)


### B.15

UK lineage (BS=100)


### B.16

Mostly Scottish lineage (BS=95)
















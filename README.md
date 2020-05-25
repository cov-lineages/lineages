





# **A dynamic nomenclature proposal for SARS-CoV-2 to assist genomic epidemiology**
Andrew Rambaut, Edward C. Holmes, Verity Hill, Áine O’Toole, JT McCrone, Chris Ruis, Louis du Plessis, Oliver G. Pybus

This is a companion repository to the paper describing a dynamic lineage nomenclature system for SARS-CoV-2.

A pre-print of the paper can be found here: https://doi.org/10.1101/2020.04.17.046086

This contains the following files:

A table of acknowledgements for the GISAID genome sequences used to develop this paper:
https://raw.githubusercontent.com/hCoV-2019/lineages/master/gisaid_acknowledgements.tsv

<img src="https://github.com/hCoV-2019/pangolin/blob/master/docs/logo.png" width="100">**P**hylogenetic **A**ssignment of **N**amed **G**lobal **O**utbreak **LIN**eages

Software to help assign your own SARS-CoV-2 genomes to these lineages is available:
http://github.com/hCoV-2019/pangolin

### Updates in data release 2020-05-19:

This weeks data release has some substantial changes. 

- We've implemented a system of "putative" lineages. Any lineages that have a recall value of < 95% are given `p` flag. E.g. `B.1.16` becomes `B.1.p16`. 

- A large lineage within B.1 with `28881GA`,`28882GA`,`28883GC` defining SNPs has been called as B.1.1. Any lineages that existed within this that would have previously been called B.1.X have been renamed as B.1.1.X, with the count restarted. Details on which lineages have been renamed can be found in the lineage descriptions.

## Lineage summary


[Additional notes](#descriptions) on justification and descriptions are available after the following table, and can also be accessed by clicking on the lineage name in the table.

Each week as more data is produced and analysed, new lineages may be called and it may turn out that older lineages are in fact not lineages. We take into account both phylogenetic and 
epidemiological information and use all available evidence to informed lineage calls weekly.




This report gives summaries of globally circulating lineages as of 2020-05-10. 
27763 sequences have been included in this analysis.
98 lineages have been assigned in this dataset.

Sequences which were replicates or too error-prone were removed from this analysis.



30 are pending extinction ie last seen three weeks ago.
34 have not been seen for more than one month, and so are viewed as extinct, but will continue to be monitored.
21 lineages have gone quiet, ie haven't been seen this week.
13 lineages have been continuously circulating.


Note that the status of a lineage is highly likely to be due to heterogeneity in sampling, and not necessarily indicative of the real decline of lineages.

The table below shows summary information of each lineage. 

The "most common countries" column shows the three countries with the most sequences from each lineage, and the percentages by the country represent the percentage of sequences in that lineage taken from that location.

Again, please interpret this with caution. Some countries are sequencing much more than others, and so locations of lineages may be at least partially due to this. It does not imply direction of transmission from one country to another. 
Sometimes we have been able to examine lineages which we know are circulating in one country by looking at sequences from another country due to associated epidemiological information.




| Lineage name            | Most common countries                             | Date range                 |   Number of taxa |   Days since last sampling | Known Travel                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |   Recall value |
|:------------------------|:--------------------------------------------------|:---------------------------|-----------------:|---------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------:|
| [A](#A)                 | China (57%), South_Korea (9%), USA (8%)           | January 05 to April 23     |              223 |                         17 | China to Taiwan, Australia, Belgium, Vietnam, India (6)<br/> USA to New_Zealand (1)<br/> Saudia_Arabia to Turkey (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |          87.76 |
| [A.1](#A.1)             | USA (87%), Australia (7%), Canada (4%)            | February 22 to April 30    |             1116 |                         10 | USA to Iceland (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |         100    |
| [A.1.1](#A.1.1)         | Iceland (100%)                                    | March 11 to March 20       |               14 |                         51 | USA to Iceland (10)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |         100    |
| [A.1.3](#A.1.3)         | Australia (90%), Taiwan (10%)                     | March 19 to April 02       |               10 |                         38 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [A.2](#A.2)             | UK (34%), Spain (28%), Australia (28%)            | February 26 to April 27    |              295 |                         13 | Spain to Brazil (1)<br/> Italy to Chile, Spain (2)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |         100    |
| [A.3](#A.3)             | USA (71%), Australia (21%), UK (7%)               | January 28 to April 21     |              191 |                         19 | USA to Taiwan, New_Zealand (2)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |          99.48 |
| [A.4](#A.4)             | USA (100%)                                        | March 13 to April 10       |               25 |                         30 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [A.5](#A.5)             | Spain (39%), UK (35%), Uruguay (6%)               | February 23 to April 26    |              118 |                         14 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          95.93 |
| [A.6](#A.6)             | Thailand (100%)                                   | January 23 to March 28     |               31 |                         43 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [A.p7](#A.p7)           | Saudi_Arabia (70%), USA (7%), Russia (7%)         | March 06 to April 27       |               27 |                         13 | Saudia_Arabia to Turkey (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |         100    |
| [B](#B)                 | UK (43%), USA (16%), China (13%)                  | December 24 to May 03      |             1713 |                          7 | China to Taiwan, Cambodia, Italy, Canada, France, Thailand, India, Singapore (9)<br/> Italy to Finland, Iceland (2)<br/> UK to Iceland (4)<br/> Netherlands to Ecuador, Iceland (2)<br/> Austria to Iceland (1)<br/> USA to Kuwait, China, Iceland (3)<br/> Switzerland to Iceland (1)<br/> Japan to Taiwan (1)<br/> Saudia_Arabia to Turkey (1)<br/>                                                                                                                                                                                                                                                                                                                             |          97.99 |
| [B.1](#B.1)             | UK (41%), USA (26%), Australia (5%)               | January 24 to May 08       |             7438 |                          2 | Egypt;United_Arab_Emirates to Taiwan (1)<br/> UK to Iceland (16)<br/> Iran to Finland, Turkey (2)<br/> Netherlands to Iceland (3)<br/> Spain to Argentina, Iceland (6)<br/> Germany to Iceland (2)<br/> Switzerland to Iceland (2)<br/> Austria to Taiwan, Iceland (43)<br/> USA to Costa_Rica, Taiwan, Iceland (3)<br/> Italy to Finland, Czech_Republic, Brazil, Iceland (16)<br/> Croatia to Iceland (1)<br/> France to Turkey, Taiwan, Iceland (5)<br/> Egypt to Taiwan (2)<br/> USA;Czech_Republic to Taiwan (1)<br/> Czech_Republic to Taiwan (1)<br/> Poland to Taiwan (1)<br/> Israel to Argentina (1)<br/> Brazil to Argentina (1)<br/> Saudia_Arabia to Turkey (1)<br/> |          98.47 |
| [B.1.1](#B.1.1)         | UK (79%), Australia (2%), USA (2%)                | February 15 to May 09      |             6286 |                          1 | Italy to Nigeria, New_Zealand, Iceland, Brazil, Chile, Thailand, Mexico (36)<br/> Finland to Iceland (1)<br/> UK to Kuwait, Iceland (5)<br/> Germany to Iceland (1)<br/> USA to Brazil (1)<br/> Spain to Taiwan, Iceland (3)<br/> Germany;Austria;Spain;Italy to Brazil (1)<br/> Austria to Iceland (4)<br/> Switzerland to Iceland (1)<br/> Mexico to Argentina (1)<br/> France to Argentina (1)<br/>                                                                                                                                                                                                                                                                            |          99.86 |
| [B.1.1.1](#B.1.1.1)     | UK (93%), DRC (1%), Iceland (1%)                  | March 02 to May 08         |              952 |                          2 | Austria to Iceland (5)<br/> UK to Argentina, Iceland (3)<br/> Peru;Argentina to Costa_Rica (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |         100    |
| [B.1.1.2](#B.1.1.2)     | UK (100%)                                         | March 20 to April 20       |              107 |                         20 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          99.07 |
| [B.1.1.3](#B.1.1.3)     | UK (100%)                                         | March 18 to May 06         |               53 |                          4 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.1.4](#B.1.1.4)     | UK (100%)                                         | March 26 to May 08         |               50 |                          2 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.1.5](#B.1.1.5)     | UK (59%), Iceland (17%), Belgium (17%)            | March 16 to April 09       |               29 |                         31 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.1.6](#B.1.1.6)     | Austria (100%)                                    | February 26 to March 25    |               45 |                         46 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.1.7](#B.1.1.7)     | UK (94%), Iceland (3%), Australia (2%)            | March 07 to April 28       |              108 |                         12 | USA to Iceland (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |         100    |
| [B.1.1.8](#B.1.1.8)     | UK (89%), Australia (8%), Gambia (2%)             | March 17 to April 28       |               65 |                         12 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.1.9](#B.1.1.9)     | UK (84%), USA (13%), France (1%)                  | March 11 to April 18       |               67 |                         22 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.1.10](#B.1.1.10)   | UK (92%), Iceland (3%), Australia (2%)            | March 06 to May 01         |              171 |                          9 | UK to Iceland (1)<br/> USA to Iceland (1)<br/> Saudia_Arabia to Turkey (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          99.42 |
| [B.1.1.p11](#B.1.1.p11) | UK (89%), Portugal (11%)                          | March 17 to April 16       |               28 |                         24 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          80    |
| [B.1.1.p12](#B.1.1.p12) | UK (100%)                                         | March 21 to April 22       |               16 |                         18 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          80    |
| [B.1.1.13](#B.1.1.13)   | UK (100%)                                         | March 28 to April 15       |               16 |                         25 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.1.14](#B.1.1.14)   | UK (100%)                                         | April 16 to May 08         |               15 |                          2 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.1.p15](#B.1.1.p15) | Luxembourg (75%), UK (17%), Australia (8%)        | March 19 to April 17       |               12 |                         23 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          52.17 |
| [B.1.1.p16](#B.1.1.p16) | UK (100%)                                         | April 06 to April 16       |               11 |                         24 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          91.67 |
| [B.1.1.17](#B.1.1.17)   | Iceland (100%)                                    | March 06 to March 28       |               29 |                         43 | Italy to Iceland (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |         100    |
| [B.1.1.18](#B.1.1.18)   | Austria (100%)                                    | March 22 to April 07       |                8 |                         33 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.1.p19](#B.1.1.p19) | Australia (100%)                                  | March 23 to March 26       |                5 |                         45 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          71.43 |
| [B.1.p2](#B.1.p2)       | USA (96%), Australia (3%), Canada (1%)            | March 08 to April 25       |              364 |                         15 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          94.04 |
| [B.1.3](#B.1.3)         | USA (94%), Argentina (2%), Australia (1%)         | March 05 to April 30       |              174 |                         10 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          99.42 |
| [B.1.5](#B.1.5)         | UK (75%), Spain (8%), Australia (5%)              | February 26 to May 10      |              710 |                          0 | Spain to Iceland (2)<br/> Switzerland to Iceland (3)<br/> Portugal to Taiwan (1)<br/> Saudia_Arabia to Turkey (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |          71.41 |
| [B.1.5.1](#B.1.5.1)     | Iceland (100%)                                    | March 12 to March 28       |               93 |                         43 | Argentina to Iceland (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |         100    |
| [B.1.5.2](#B.1.5.2)     | Netherlands (86%), Belgium (7%), UK (7%)          | March 24 to April 06       |               14 |                         34 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.5.3](#B.1.5.3)     | UK (94%), Australia (3%), Sweden (3%)             | March 18 to April 16       |               33 |                         24 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.5.4](#B.1.5.4)     | Spain (75%), Mexico (6%), USA (6%)                | March 11 to April 06       |               16 |                         34 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.5.5](#B.1.5.5)     | UK (100%)                                         | April 08 to May 06         |               33 |                          4 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.5.6](#B.1.5.6)     | UK (100%)                                         | March 19 to May 01         |               32 |                          9 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.6](#B.1.6)         | Belgium (68%), DRC (18%), UK (9%)                 | March 11 to April 13       |               22 |                         27 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.8](#B.1.8)         | Netherlands (63%), Iceland (12%), Austria (6%)    | March 04 to April 11       |               83 |                         29 | Austria to Iceland (10)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |          98.81 |
| [B.1.p9](#B.1.p9)       | Belgium (56%), Turkey (13%), Netherlands (13%)    | March 14 to April 17       |               39 |                         23 | Saudia_Arabia to Turkey (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |          94.44 |
| [B.1.p11](#B.1.p11)     | UK (98%), USA (2%), Australia (0%)                | March 02 to May 08         |              584 |                          2 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          64.82 |
| [B.1.12](#B.1.12)       | Luxembourg (59%), Belgium (37%), Switzerland (2%) | March 04 to April 14       |               46 |                         26 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.13](#B.1.13)       | UK (95%), Australia (4%), Poland (0%)             | March 09 to May 07         |              248 |                          3 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.p16](#B.1.p16)     | Belgium (100%)                                    | March 01 to March 20       |               18 |                         51 | Italy to Belgium (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |          94.74 |
| [B.1.19](#B.1.19)       | USA (100%)                                        | March 19 to April 17       |               29 |                         23 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.p21](#B.1.p21)     | USA (100%)                                        | March 08 to April 27       |              265 |                         13 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          91.38 |
| [B.1.22](#B.1.22)       | Netherlands (55%), Australia (29%), Austria (6%)  | March 09 to April 17       |               31 |                         23 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.23](#B.1.23)       | Australia (100%)                                  | March 18 to April 12       |               78 |                         28 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.p25](#B.1.p25)     | Australia (100%)                                  | March 19 to March 27       |               16 |                         44 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          75    |
| [B.1.26](#B.1.26)       | USA (94%), Australia (3%), Taiwan (3%)            | March 12 to April 20       |               31 |                         20 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.29](#B.1.29)       | USA (96%), Australia (4%)                         | March 15 to May 03         |               27 |                          7 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.30](#B.1.30)       | UK (100%)                                         | March 17 to May 03         |               60 |                          7 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.31](#B.1.31)       | Australia (100%)                                  | March 21 to March 27       |               10 |                         44 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.32](#B.1.32)       | Sweden (100%)                                     | March 04 to March 10       |               17 |                         61 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.33](#B.1.33)       | Australia (100%)                                  | March 21 to April 11       |               19 |                         29 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.34](#B.1.34)       | UK (100%)                                         | March 17 to April 26       |               22 |                         14 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.35](#B.1.35)       | UK (100%)                                         | March 07 to April 22       |              112 |                         18 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.36](#B.1.36)       | Saudi_Arabia (46%), UK (25%), Turkey (9%)         | March 10 to May 07         |              159 |                          3 | Saudia_Arabia to Turkey (6)<br/> Iran to Turkey (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |          98.75 |
| [B.1.37](#B.1.37)       | USA (100%)                                        | March 12 to April 04       |               23 |                         36 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.38](#B.1.38)       | USA (100%)                                        | March 17 to April 09       |               18 |                         31 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.39](#B.1.39)       | Denmark (89%), UK (8%), Australia (3%)            | March 13 to April 07       |               36 |                         33 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          97.3  |
| [B.1.40](#B.1.40)       | UK (100%)                                         | March 18 to May 08         |               22 |                          2 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.41](#B.1.41)       | USA (100%)                                        | March 19 to April 09       |               31 |                         31 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          96.55 |
| [B.1.p42](#B.1.p42)     | Denmark (83%), Iceland (8%), Sweden (8%)          | March 03 to April 02       |               63 |                         38 | Faroe_Islands to Iceland (1)<br/> Denmark to Iceland (2)<br/> UK to Iceland (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |          77.78 |
| [B.1.43](#B.1.43)       | USA (100%)                                        | March 18 to April 02       |               58 |                         38 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.44](#B.1.44)       | UK (100%)                                         | March 25 to April 21       |               47 |                         19 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          97.87 |
| [B.1.66](#B.1.66)       | UK (100%)                                         | March 29 to April 29       |               30 |                         11 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.67](#B.1.67)       | UK (100%)                                         | March 25 to April 12       |               14 |                         28 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.p68](#B.1.p68)     | USA (100%)                                        | March 19 to April 15       |               13 |                         25 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          92.86 |
| [B.1.69](#B.1.69)       | UK (100%)                                         | March 06 to March 20       |               16 |                         51 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.70](#B.1.70)       | UK (100%)                                         | March 13 to April 20       |               19 |                         20 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.71](#B.1.71)       | UK (100%)                                         | March 18 to April 18       |               22 |                         22 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.72](#B.1.72)       | UK (100%)                                         | March 16 to April 05       |               29 |                         35 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.1.p73](#B.1.p73)     | UK (100%)                                         | March 16 to April 28       |              125 |                         12 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          96.9  |
| [B.2](#B.2)             | UK (74%), USA (8%), Netherlands (5%)              | February 13 to May 01      |              917 |                          9 | Germany to Iceland (1)<br/> UK to China, Iceland (3)<br/> Italy to Brazil (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |          95.31 |
| [B.2.1](#B.2.1)         | UK (93%), Australia (3%), USA (1%)                | February 09 to May 02      |             1568 |                          8 | UK to Iceland (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |         100    |
| [B.2.2](#B.2.2)         | UK (85%), Australia (5%), Iceland (3%)            | February 25 to April 22    |              208 |                         18 | Spain to Iceland (1)<br/> Switzerland to Iceland (1)<br/> Ireland to Taiwan (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |         100    |
| [B.2.4](#B.2.4)         | Australia (83%), UK (12%), Uruguay (4%)           | March 11 to April 02       |               24 |                         38 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.2.5](#B.2.5)         | UK (86%), Australia (10%), Slovenia (1%)          | February 27 to April 27    |              143 |                         13 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          99.3  |
| [B.2.6](#B.2.6)         | UK (77%), Australia (9%), Iceland (6%)            | March 05 to May 04         |               47 |                          6 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          97.92 |
| [B.2.7](#B.2.7)         | Iceland (100%)                                    | March 12 to March 29       |               46 |                         42 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          97.87 |
| [B.3](#B.3)             | UK (84%), Germany (3%), Denmark (3%)              | February 23 to April 23    |              752 |                         17 | UK to Iceland, Brazil (2)<br/> Austria to Iceland (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |         100    |
| [B.4](#B.4)             | Australia (35%), UK (18%), Turkey (8%)            | January 18 to April 14     |              258 |                         26 | Iran to Kuwait, Australia, New_Zealand, Turkey, Canada, Pakistan, Germany (12)<br/> Turkey to Taiwan (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |          99.61 |
| [B.5](#B.5)             | Japan (94%), Australia (6%)                       | February 10 to February 24 |               18 |                         76 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.6](#B.6)             | India (36%), Singapore (27%), Australia (19%)     | March 04 to April 30       |              221 |                         10 | Philippines to Taiwan (1)<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |         100    |
| [B.7](#B.7)             | Hong_Kong (97%), Canada (3%)                      | January 30 to March 04     |               37 |                         67 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.9](#B.9)             | UK (80%), Australia (20%)                         | March 12 to May 01         |               35 |                          9 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.10](#B.10)           | UK (100%)                                         | March 13 to April 22       |               66 |                         18 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.p11](#B.p11)         | Netherlands (100%)                                | March 02 to March 24       |               14 |                         47 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          93.33 |
| [B.p12](#B.p12)         | Japan (100%)                                      | March 25 to March 27       |                4 |                         44 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.13](#B.13)           | USA (100%)                                        | April 03 to April 17       |               19 |                         23 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.14](#B.14)           | USA (100%)                                        | March 16 to May 01         |               38 |                          9 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |          97.44 |
| [B.15](#B.15)           | UK (100%)                                         | March 11 to April 14       |               37 |                         26 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |
| [B.16](#B.16)           | UK (100%)                                         | March 13 to April 28       |               86 |                         12 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         100    |

## Lineage descriptions <a name="descriptions"></a>


BS = bootstrap







### A<a name=A></a>

Root of the pandemic lies within lineage A. Many sequences originating from China and many global exports; including to South East Asia, Japan, South Korea, Australia, the USA and Europe, represented in this lineage


### A.1<a name=A.1></a>

A North American lineage, with some sequences from Australia in (BS=95)


### A.1.1<a name=A.1.1></a>

Iceland lineage (BS:100->79)


### *A.1.2<a name=*A.1.2></a>

Reassigned to A.1 (low BS two weeks running)


### A.1.3<a name=A.1.3></a>

Australian lineage (BS=100)


### A.2<a name=A.2></a>

Spain/ Chile/ Australia/ Europe (BS=93)


### A.3<a name=A.3></a>

USA and Australian lineage (BS: 100 -> 44). Low BS likely due to India/NCDC-3279/2020, which was misassigned and likely jumps around the tree.


### A.4<a name=A.4></a>

Lineage circulating in USA (all sequences Wisconsin) (BS=100)


### A.5<a name=A.5></a>

A lineage with a lot of representation from Spanish-speaking countries. A majoritively Spain/ South-American lineage, lower bootstrap this week BS 87->20. 


### A.6<a name=A.6></a>

Lineage in Thailand (BS=87)


### A.p7<a name=A.p7></a>

Potential lineage: Saudi Arabia, Russia, Turkey, India (BS=50)


### B<a name=B></a>

Base of this lineage also lies in China, with many global exports, two distinct SNPs `8782TC` and `28144CT` define this lineage


### B.1<a name=B.1></a>

A large European lineage that corresponds to the Italian outbreak.


### B.1.45<a name=B.1.45></a>

Australian lineage (more support this week BS=91), all Australian sequences within a background of European and Asian


### B.1.49<a name=B.1.49></a>

Scotland (BS=92)


### B.1.1<a name=B.1.1></a>

New European lineage that's been assigned due to high support and 3 clear SNPs `28881GA`,`28882GA`,`28883GC`. Note: Sub-lineages that previously existed within this lineage have been reassigned a new lineage name.


### B.1.1.1<a name=B.1.1.1></a>

Formerly B.1.1, UK/ Europe (BS=80)


### B.1.1.2<a name=B.1.1.2></a>

Formerly B.1.24, Welsh lineage (BS=100->47 this week)


### B.1.1.3<a name=B.1.1.3></a>

Formerly B.1.65, English lineage (BS=100)


### B.1.1.4<a name=B.1.1.4></a>

Formerly B.1.55, UK (BS=100)


### B.1.1.5<a name=B.1.1.5></a>

Formerly B.1.54, Iceland/ Belgium/ UK (BS=100)


### B.1.1.6<a name=B.1.1.6></a>

Formerly B.1.62, Austrian lineage (BS=100)


### B.1.1.7<a name=B.1.1.7></a>

Formerly B.1.1.56, UK/ Australia/ Iceland (BS=100)


### B.1.1.8<a name=B.1.1.8></a>

Formerly B.1.63, UK/ USA/ Australia (BS=100)


### B.1.1.9<a name=B.1.1.9></a>

Formerly B.1.53, England / USA (BS=83)


### B.1.1.10<a name=B.1.1.10></a>

Formerly B.1.10, UK/ Iceland (BS lower this week 70 -> 11), a lot of diversity in this lineage, now has a Turkish sequence. 


### B.1.1.p11<a name=B.1.1.p11></a>

Formerly B.1.50, Portugal/ Wales (BS=55 this week)


### B.1.1.p12<a name=B.1.1.p12></a>

Formerly B.1.49, Scottish lineage (BS=48)


### B.1.1.13<a name=B.1.1.13></a>

Formerly B.1.61, UK lineage (BS=95)


### B.1.1.14<a name=B.1.1.14></a>

Formerly B.1.60, Scottish lineage (BS=89)


### B.1.1.p15<a name=B.1.1.p15></a>

Formerly B.1.46, Luxembourg (BS=11, but internal nodes all 100 and all Luxembourg)


### B.1.1.p16<a name=B.1.1.p16></a>

Formerly B.1.59, Wales lineage (BS=70)


### B.1.1.17<a name=B.1.1.17></a>

Formerly B.1.58, Iceland lineage (BS=100)


### B.1.1.18<a name=B.1.1.18></a>

Formerly B.1.57, Austrian lineage (BS=97)


### B.1.1.p19<a name=B.1.1.p19></a>

Formerly B.1.45, Australian lineage (BS=91)


### B.1.p2<a name=B.1.p2></a>

USA (low BS=9)


### B.1.3<a name=B.1.3></a>

USA(BS=39)


### B.1.5<a name=B.1.5></a>

England/ Spain/ Turkey/ Australia/ USA/ Brasil. Low support at parent node now, potentially as a result of homoplasies (BS=5)


### B.1.5.1<a name=B.1.5.1></a>

Iceland (BS=27), but all sequences suggest an Icelandic lineage


### B.1.5.2<a name=B.1.5.2></a>

Netherlands (BS=100)


### B.1.5.3<a name=B.1.5.3></a>

England (now containing an Australian & Swedish seqeuence) (BS=96)


### B.1.5.4<a name=B.1.5.4></a>

Spain (BS=100)


### B.1.5.5<a name=B.1.5.5></a>

England (BS=100)


### B.1.5.6<a name=B.1.5.6></a>

UK (BS=100)


### B.1.6<a name=B.1.6></a>

Belgian lineage (BS=55)


### *B.1.7<a name=*B.1.7></a>

Low support (BS=9), reassigned B.1


### B.1.8<a name=B.1.8></a>

Netherlands/ Europe (BS=47)


### B.1.p9<a name=B.1.p9></a>

Netherlands/ Belgium/ Turkey/ DRC (BS=9)


### B.1.p11<a name=B.1.p11></a>

UK lineage but low support and splitting up, pruned down quite a lot, but may need to be removed next time (BS=31)


### B.1.12<a name=B.1.12></a>

BeNeLux (BS=18 this week, lots of internal 100)


### B.1.13<a name=B.1.13></a>

England/ Australia, may need refining parent node BS=59, internal node of 100


### B.1.p16<a name=B.1.p16></a>

Belgium, low support (BS=19), keep an eye on this with new data 


### B.1.19<a name=B.1.19></a>

USA (BS=100)


### *B.1.20<a name=*B.1.20></a>

Low support (BS=5), reassigned B.1


### B.1.p21<a name=B.1.p21></a>

Washington (USA) (Low BS=9)


### B.1.22<a name=B.1.22></a>

Netherlands (BS=100)


### B.1.23<a name=B.1.23></a>

Australia (BS=68)


### B.1.p25<a name=B.1.p25></a>

Australian lineage, some low internal bootstrap values and parent node BS=16. However all sequences within it are Australian and that's with quite a lot of diversity as well.


### B.1.26<a name=B.1.26></a>

USA lineage (BS=83)


### B.1.27<a name=B.1.27></a>

USA/ Argentina (BS=74)


### *B.1.28<a name=*B.1.28></a>

Denmark/ USA new parent node BS=9, reassigned B.1


### B.1.29<a name=B.1.29></a>

USA (BS=86)


### B.1.30<a name=B.1.30></a>

England (BS=100)


### B.1.31<a name=B.1.31></a>

Australia (BS=100)


### B.1.32<a name=B.1.32></a>

Swedish lineage (BS=95)


### B.1.33<a name=B.1.33></a>

Australian lineage (BS=100)


### B.1.34<a name=B.1.34></a>

England (BS=100)


### B.1.35<a name=B.1.35></a>

Wales (BS=9)


### B.1.36<a name=B.1.36></a>

Turkey/ Saudi Arabia/ Egypt / Finland & England (BS=100)


### B.1.37<a name=B.1.37></a>

USA lineage (BS=93)


### B.1.38<a name=B.1.38></a>

USA (BS=100)


### B.1.39<a name=B.1.39></a>

Denmark (BS=100)


### B.1.40<a name=B.1.40></a>

Scotland (BS=90)


### B.1.41<a name=B.1.41></a>

USA lineage (BS=100)


### B.1.p42<a name=B.1.p42></a>

Sweden/ Denmark lineage, split up in the tree this week


### B.1.43<a name=B.1.43></a>

USA (BS=100)


### B.1.44<a name=B.1.44></a>

Wales (BS=100)


### *B.1.47<a name=*B.1.47></a>

England, caused a lot of problems last release and many misassignments (BS=100)


### *B.1.48<a name=*B.1.48></a>

England (BS=39)


### *B.1.51<a name=*B.1.51></a>

UK (BS=11, got split in half)


### *B.1.52<a name=*B.1.52></a>

England (BS=30)


### B.1.64<a name=B.1.64></a>

English lineage (BS=100)


### B.1.66<a name=B.1.66></a>

English lineage (BS=100)


### B.1.67<a name=B.1.67></a>

Wales lineage (BS=96)


### B.1.p68<a name=B.1.p68></a>

USA lineage (UT) (BS=100)


### B.1.69<a name=B.1.69></a>

Scottish lineage (BS=100)


### B.1.70<a name=B.1.70></a>

Scottish lineage (BS=70)


### B.1.71<a name=B.1.71></a>

UK lineage (BS=100)


### B.1.72<a name=B.1.72></a>

UK lineage (BRIS) (BS=100)


### B.1.p73<a name=B.1.p73></a>

Scotland lineage (BS=5, so very low)


### B.2<a name=B.2></a>

A previously defined large European/ Australian lineage that with new data has low support (BS=13). This lineage and its sublineage will need to be re-examined and perhaps refined quite significantly in next weeks data


### B.2.1<a name=B.2.1></a>

Large lineage with representation from UK, Europe, Jordan, Australia, USA, India, Ghana (BS=11) 


### B.2.2<a name=B.2.2></a>

BeNeLux/ UK/ Singapore /Australia /USA (BS=85)


### *B.2.3<a name=*B.2.3></a>

Reassigned B.2 (No good internal BS, misassignments)


### B.2.4<a name=B.2.4></a>

Australian lineage, took a subset of previously defined B.2.4 and reassigning them B.2


### B.2.5<a name=B.2.5></a>

Spain/ England / Australia (BS=17) *flagged because of low bootstrap


### B.2.6<a name=B.2.6></a>

UK/ Singapore/ Jordan/ Iceland, previously just UK & Australia (BS=11, low support)


### B.2.7<a name=B.2.7></a>

Iceland lineage (BS=60)


### B.3<a name=B.3></a>

A European lineage, including a large set of sequences from Wales, low parent node support (BS=14)


### B.4<a name=B.4></a>

Iran lineage, many sequences we have of this lineage are associated with travel histories from Iran (BS=43)


### B.5<a name=B.5></a>

Japanese lineage (BS=75) 


### B.6<a name=B.6></a>

India/ Philippines/ UK/ North America/ Australia/ Singapore (BS=100)


### B.7<a name=B.7></a>

Hong Kong lineage (BS 73 -> 27)


### *B.8<a name=*B.8></a>

Reassigned to B (BS 27 -> 14, got split into two clades with low support in this weeks tree)


### B.9<a name=B.9></a>

Australian/ England lineage (BS=100)


### B.10<a name=B.10></a>

Northern Ireland/ England/ Scotland (BS=89)


### B.p11<a name=B.p11></a>

Netherlands lineage (BS=100)


### B.p12<a name=B.p12></a>

Japan lineage (BS=99, but only a few sequences)


### B.13<a name=B.13></a>

USA (WI) lineage (BS=100)


### B.14<a name=B.14></a>

USA (CA) lineage (BS=100)


### B.15<a name=B.15></a>

UK lineage (BS=100)


### B.16<a name=B.16></a>

Mostly Scottish lineage (BS=95)
















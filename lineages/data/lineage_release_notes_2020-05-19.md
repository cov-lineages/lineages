## lineages data release 2020-05-19

### Updates:

This weeks data release has some substantial changes. 

- We've implemented a system of "putative" lineages. Any lineages that have a recall value of < 95% are given `p` flag. E.g. `B.1.16` becomes `B.1.p16`. 

- A large lineage within B.1 with `28881GA`,`28882GA`,`28883GC` defining SNPs has been called as B.1.1. Any lineages that existed within this that would have previously been called B.1.X have been renamed as B.1.1.X, with the count restarted. Details on which lineages have been renamed can be found in the lineage descriptions.

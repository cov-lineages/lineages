# Data preparation

### Source

All GISAID data is downloaded and run through [`grapevine`](https://github.com/cov-ert/grapevine) which excludes records without proper dates, removes duplicate sequences (taking the earliest sample of the duplicates), omits some sequences with known issues, filters by length and coverage, and trims the sequences to CDS.

It also aligns the sequences using `mafft` and builds an ML tree using `iqtree`. A lineages is assigned to each sequence using `pangolin` with the previous data release.

### Lineage Curation

The phylogeny is annotated with lineage and then in `FigTree` the lineages are manually curated, drawing together a number of pieces of information including monophyly in the ML phylogeny (generally a bootstrap > 70 is required) and epidemiological data such as country and travel history. Any changes to lineage definitions and new lineages are documented during this process.

Occasionally, a bootstrap lower than 70 may be at the parent node of a lineage. This can be for one of a number of reasons.

- The lineage may have been defined earlier in the outbreak and with added sequence data, there is less support for that lineage. In these cases the associated epidemiological metadata is examined and the lineage may be refined or even dropped entirely. The lineage number will not be 'recycled', but the members will get reassigned the parent lineage designation.
- The lineage may have very clear epidemiological support and ambiguities or homoplasies in the sequences/ tree could contribute to low bootstrap values. In these cases, if the support is strong, the lineages are called. Recall rates for these lingeages within `pangolin` may be lower however.

### pangolin data preparation pipeline

The new tip annotations are extracted from the tree files and passed to the [prepare_package_data](https://github.com/hCoV-2019/pangolin/blob/master/pangolin/scripts/prepare_package_data.smk) pipeline, alongside the GISAID fasta file and metadata, and the following steps are performed:

- find_representatives

    Reads in the alignment, gets SNPs in the sequence relative to the reference (`WH04`).
    For each lineage, it identifies singleton SNPs (which will be masked), SNPs that should be represented within the tree (>10% of tips within the lineage have this SNP) and lineage-defining SNPs (100% of tips have these SNPs, or if there isn't one, relax to 90% inclusion). Representative sequences are selected based on N-content and having the SNPs flagged for representation. A target of 5 sequences per lineage at a minimum (may lower this to three as more lienages are defined) is aimed for.

- extract_representative_sequences

    Extracts the representative sequences from the big GISAID alignment and masks the singleton SNPs. Writes a metadata csv with the representative sequences indicated.

- mafft representative sequences

- iqtree representative sequences

- anonymise headers & encrypt sequences

    Anonymise the headers in the fasta file to fit with GISAID data sharing guidelines and encrypt the sequence data so it isn't searchable.

import pandas as pd

configfile: "config.yaml"

sample_sheet = pd.read_table(config["sample_sheet"], sep="\s+")

# groups = list(sample_sheet.Group.drop_duplicates())
groups = config["groups"]
region_types = config["region_types"]

to_include = ["subread/featurecounts", "download/annotation", "quantiles/quantiles",
              "bed/gff3_to_bed", "bed/bed"]
              # "bed/bed"]


for rule in to_include:
    include: "rules/{rule}.rules".format(rule=rule)


wildcard_constraints:
    group = "({})".format("|".join(groups)),
    region_type = "({})".format("|".join(region_types))


rule expression_quantiles:
    input:
        expand("data/deeptools/{group}.{region_type}.bed",
               region_type=region_types, group=groups)

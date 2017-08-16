import pandas as pd
from os.path import basename


def compute_quantiles(df, quantiles=[.25, .5, .75]):

    kb_lengths = df.Length / 1000
    df = df.drop("Chr Start End Strand Length".split(), axis=1)
    df = df.set_index("Geneid")
    df.columns = [basename(c) for c in df.columns]

    norm_df = df / df.sum() * 1e6

    s = norm_df.sum(axis=1)
    s = s / kb_lengths.values

    z = s[s == 0]
    z.name = "Value"
    z = z.to_frame()
    z.insert(0, "Quantile", "0")
    z = z.drop("Value", 1)

    nz = s[s != 0]

    qs, qs2 = iter([0] + quantiles), iter([0] + quantiles + [1])
    next(qs2)

    results = [z]
    for q, q2 in zip(qs, qs2):
        quantile = nz.quantile(q, interpolation="lower")
        quantile2 = nz.quantile(q2, interpolation="lower")
        result = nz[(nz >= quantile) & (nz <= quantile2)]

        # print("Length:", len(result))

        result.name = "Value"
        result = result.to_frame()
        result.insert(0, "Quantile", "-".join(
            [str(int(s * 100)) for s in (q, q2)]))
        result = result.drop("Value", axis=1)

        results.append(result)

    return pd.concat(results)


if __name__ == "__main__":

    df = pd.read_table(snakemake.input[0], header=1)

    outdf = compute_quantiles(df, snakemake.config["quantiles"])

    outdf.to_csv(snakemake.output[0], sep=" ")

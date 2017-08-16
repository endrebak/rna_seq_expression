import pytest

import pandas as pd
from io import StringIO

from scripts.compute_quantiles import compute_quantiles

@pytest.mark.unit
def test_compute_quantiles(matrix, expected_result):
    result = compute_quantiles(matrix)

    # result.to_csv("result.csv", sep=" ")
    # expected_result.to_csv("expected_result.csv", sep=" ")

    # print(result.to_csv(sep=" "))
    # print(result.head())
    # print(result.tail())
    # print(result.dtypes)
    # print(len(result))
    # print(type(result))

    # print(expected_result.head())
    # print(expected_result.tail())
    # print(expected_result.dtypes)
    # print(len(expected_result))
    # print(type(expected_result))

    assert expected_result.equals(result)


@pytest.fixture
def expected_result():

    contents = """Geneid Quantile
ENSG00000284332.1 0
ENSG00000237613.2 0
ENSG00000268020.3 0
ENSG00000240361.1 0
ENSG00000186092.4 0
ENSG00000233750.3 0
ENSG00000268903.1 0
ENSG00000269981.1 0
ENSG00000222623.1 0
ENSG00000241599.1 0
ENSG00000279928.2 0
ENSG00000279457.4 0
ENSG00000273874.1 0
ENSG00000236679.2 0
ENSG00000236743.1 0
ENSG00000236601.2 0
ENSG00000237094.11 0
ENSG00000269732.1 0
ENSG00000278566.1 0
ENSG00000224813.3 0
ENSG00000233653.3 0
ENSG00000250575.1 0
ENSG00000278757.1 0
ENSG00000235146.2 0
ENSG00000225972.1 0
ENSG00000225630.1 0
ENSG00000237973.1 0
ENSG00000278791.1 0
ENSG00000229344.1 0
ENSG00000240409.1 0
ENSG00000248527.1 0
ENSG00000198744.5 0
ENSG00000268663.1 0
ENSG00000273547.1 0
ENSG00000283574.1 0
ENSG00000223181.1 0
ENSG00000229905.1 0
ENSG00000225880.5 0
ENSG00000187642.9 0
ENSG00000188290.10 0
ENSG00000231702.2 0
ENSG00000224969.1 0
ENSG00000242590.1 0
ENSG00000217801.9 0
ENSG00000273443.1 0
ENSG00000237330.2 0
ENSG00000207730.3 0
ENSG00000207607.3 0
ENSG00000186827.10 0
ENSG00000176022.4 0
ENSG00000238009.6 0-25
ENSG00000241860.6 0-25
ENSG00000228463.9 0-25
ENSG00000230092.7 0-25
ENSG00000177757.2 0-25
ENSG00000230368.2 0-25
ENSG00000283040.1 0-25
ENSG00000230699.2 0-25
ENSG00000188976.10 0-25
ENSG00000188157.14 0-25
ENSG00000131591.17 0-25
ENSG00000230415.1 0-25
ENSG00000223972.5 25-50
ENSG00000243485.5 25-50
ENSG00000239945.1 25-50
ENSG00000239906.1 25-50
ENSG00000177757.2 25-50
ENSG00000272438.1 25-50
ENSG00000241180.1 25-50
ENSG00000223764.2 25-50
ENSG00000187961.13 25-50
ENSG00000272512.1 25-50
ENSG00000223823.1 25-50
ENSG00000205231.1 25-50
ENSG00000162571.13 25-50
ENSG00000239906.1 50-75
ENSG00000241670.3 50-75
ENSG00000230021.8 50-75
ENSG00000229376.3 50-75
ENSG00000228327.3 50-75
ENSG00000228794.8 50-75
ENSG00000234711.1 50-75
ENSG00000187634.11 50-75
ENSG00000187583.10 50-75
ENSG00000187608.8 50-75
ENSG00000184163.3 50-75
ENSG00000169972.11 50-75
ENSG00000240731.1 50-75
ENSG00000227232.5 75-100
ENSG00000278267.1 75-100
ENSG00000237491.8 75-100
ENSG00000234711.1 75-100
ENSG00000198976.1 75-100
ENSG00000272141.1 75-100
ENSG00000186891.13 75-100
ENSG00000078808.16 75-100
ENSG00000260179.1 75-100
ENSG00000160087.20 75-100
ENSG00000162572.20 75-100
ENSG00000131584.18 75-100
ENSG00000127054.20 75-100"""

    return pd.read_table(StringIO(contents), sep=" ", header=0, index_col=0)

@pytest.fixture
def matrix():
    contents = """# Program:featureCounts v1.5.0-p3; Command:"featureCounts" "-C" "-O" "-a" "data/annotation/annotation.gff3" "-t" "gene" "-s" "2" "-T" "8" "-f" "-g" "gene_id" "-o" "data/featurecounts/WT.csv" "/local/home/lenecho/Biocore/002_Barbara/data/WTCas9_1.bam" "/local/home/lenecho/Biocore/002_Barbara/data/WTCas9_2.bam" "/local/home/lenecho/Biocore/002_Barbara/data/WTCas9_3.bam"
Geneid	Chr	Start	End	Strand	Length	/local/home/lenecho/Biocore/002_Barbara/data/WTCas9_1.bam	/local/home/lenecho/Biocore/002_Barbara/data/WTCas9_2.bam	/local/home/lenecho/Biocore/002_Barbara/data/WTCas9_3.bam
ENSG00000223972.5	chr1	11869	14409	+	2541	0	1	1
ENSG00000227232.5	chr1	14404	29570	-	15167	82	111	116
ENSG00000278267.1	chr1	17369	17436	-	68	1	6	5
ENSG00000243485.5	chr1	29554	31109	+	1556	1	0	0
ENSG00000238009.6	chr1	89295	133723	-	44429	1	0	1
ENSG00000239945.1	chr1	89551	91105	-	1555	0	0	1
ENSG00000239906.1	chr1	139790	140339	-	550	0	1	0
ENSG00000241860.6	chr1	141474	173862	-	32389	2	2	2
ENSG00000228463.9	chr1	257864	297502	-	39639	6	2	0
ENSG00000241670.3	chr1	258568	259024	-	457	2	0	0
ENSG00000230021.8	chr1	585989	827796	-	241808	136	190	240
ENSG00000229376.3	chr1	722092	724903	+	2812	5	9	9
ENSG00000228327.3	chr1	725885	778626	-	52742	40	39	61
ENSG00000237491.8	chr1	778770	810060	+	31291	369	349	348
ENSG00000230092.7	chr1	800879	817712	-	16834	0	0	1
ENSG00000177757.2	chr1	817371	819837	+	2467	0	0	1
ENSG00000228794.8	chr1	825138	859446	+	34309	102	205	192
ENSG00000230368.2	chr1	868071	876903	-	8833	0	1	2
ENSG00000234711.1	chr1	873292	874349	+	1058	4	8	6
ENSG00000283040.1	chr1	874529	877234	-	2706	0	0	1
ENSG00000272438.1	chr1	904834	915976	+	11143	1	6	4
ENSG00000230699.2	chr1	911435	914948	+	3514	0	1	0
ENSG00000241180.1	chr1	914171	914971	+	801	0	1	0
ENSG00000223764.2	chr1	916865	921016	-	4152	0	1	2
ENSG00000187634.11	chr1	923928	944581	+	20654	49	121	131
ENSG00000188976.10	chr1	944204	959309	-	15106	0	0	1
ENSG00000187961.13	chr1	960587	965715	+	5129	0	1	2
ENSG00000187583.10	chr1	966497	975865	+	9369	21	36	57
ENSG00000272512.1	chr1	995966	998051	-	2086	0	1	0
ENSG00000187608.8	chr1	1001138	1014541	+	13404	7	16	12
ENSG00000188157.14	chr1	1020123	1056118	+	35996	2	1	0
ENSG00000131591.17	chr1	1081818	1116361	-	34544	1	0	0
ENSG00000223823.1	chr1	1137017	1144056	+	7040	2	3	0
ENSG00000198976.1	chr1	1169005	1169087	+	83	108	73	65
ENSG00000272141.1	chr1	1169357	1170343	+	987	141	182	197
ENSG00000205231.1	chr1	1173056	1179555	-	6500	0	1	2
ENSG00000162571.13	chr1	1173884	1197935	+	24052	3	10	11
ENSG00000186891.13	chr1	1203508	1206691	-	3184	21	46	46
ENSG00000078808.16	chr1	1216908	1232031	-	15124	79	224	220
ENSG00000184163.3	chr1	1242446	1246722	-	4277	8	14	15
ENSG00000260179.1	chr1	1249777	1251334	-	1558	106	198	155
ENSG00000160087.20	chr1	1253909	1273885	-	19977	406	842	761
ENSG00000230415.1	chr1	1275223	1280420	+	5198	0	1	1
ENSG00000162572.20	chr1	1280436	1292029	+	11594	33	108	90
ENSG00000131584.18	chr1	1292376	1309609	-	17234	272	644	562
ENSG00000169972.11	chr1	1308567	1311677	+	3111	5	1	8
ENSG00000127054.20	chr1	1311585	1324691	-	13107	612	1111	1081
ENSG00000240731.1	chr1	1317581	1318689	-	1109	1	2	1
ENSG00000284332.1	chr1	30366	30503	+	138	0	0	0
ENSG00000237613.2	chr1	34554	36081	-	1528	0	0	0
ENSG00000268020.3	chr1	52473	53312	+	840	0	0	0
ENSG00000240361.1	chr1	62948	63887	+	940	0	0	0
ENSG00000186092.4	chr1	69091	70008	+	918	0	0	0
ENSG00000233750.3	chr1	131025	134836	+	3812	0	0	0
ENSG00000268903.1	chr1	135141	135895	-	755	0	0	0
ENSG00000269981.1	chr1	137682	137965	-	284	0	0	0
ENSG00000222623.1	chr1	157784	157887	-	104	0	0	0
ENSG00000241599.1	chr1	160446	161525	+	1080	0	0	0
ENSG00000279928.2	chr1	182696	184174	+	1479	0	0	0
ENSG00000279457.4	chr1	185217	195411	-	10195	0	0	0
ENSG00000273874.1	chr1	187891	187958	-	68	0	0	0
ENSG00000236679.2	chr1	347982	348366	-	385	0	0	0
ENSG00000236743.1	chr1	357383	359681	-	2299	0	0	0
ENSG00000236601.2	chr1	358857	366052	+	7196	0	0	0
ENSG00000237094.11	chr1	365389	501617	-	136229	0	0	0
ENSG00000269732.1	chr1	439870	440232	+	363	0	0	0
ENSG00000278566.1	chr1	450740	451678	-	939	0	0	0
ENSG00000224813.3	chr1	485026	485208	-	183	0	0	0
ENSG00000233653.3	chr1	487101	489906	+	2806	0	0	0
ENSG00000250575.1	chr1	491225	493241	-	2017	0	0	0
ENSG00000278757.1	chr1	516376	516479	-	104	0	0	0
ENSG00000235146.2	chr1	587629	594768	+	7140	0	0	0
ENSG00000225972.1	chr1	629062	629433	+	372	0	0	0
ENSG00000225630.1	chr1	629640	630683	+	1044	0	0	0
ENSG00000237973.1	chr1	631074	632616	+	1543	0	0	0
ENSG00000278791.1	chr1	632325	632413	-	89	0	0	0
ENSG00000229344.1	chr1	632757	633438	+	682	0	0	0
ENSG00000240409.1	chr1	633535	633741	+	207	0	0	0
ENSG00000248527.1	chr1	633696	634376	+	681	0	0	0
ENSG00000198744.5	chr1	634376	634922	+	547	0	0	0
ENSG00000268663.1	chr1	674842	675265	+	424	0	0	0
ENSG00000273547.1	chr1	685716	686654	-	939	0	0	0
ENSG00000283574.1	chr1	720024	720206	-	183	0	0	0
ENSG00000223181.1	chr1	758233	758336	-	104	0	0	0
ENSG00000229905.1	chr1	760911	761989	+	1079	0	0	0
ENSG00000225880.5	chr1	826206	827522	-	1317	0	0	0
ENSG00000187642.9	chr1	975204	982093	-	6890	0	0	0
ENSG00000188290.10	chr1	998962	1000172	-	1211	0	0	0
ENSG00000231702.2	chr1	1008076	1008229	-	154	0	0	0
ENSG00000224969.1	chr1	1011997	1013193	-	1197	0	0	0
ENSG00000242590.1	chr1	1055033	1056116	+	1084	0	0	0
ENSG00000217801.9	chr1	1059734	1069355	+	9622	0	0	0
ENSG00000273443.1	chr1	1062208	1063288	-	1081	0	0	0
ENSG00000237330.2	chr1	1070966	1074307	-	3342	0	0	0
ENSG00000207730.3	chr1	1167104	1167198	+	95	0	0	0
ENSG00000207607.3	chr1	1167863	1167952	+	90	0	0	0
ENSG00000186827.10	chr1	1211326	1214138	-	2813	0	0	0
ENSG00000176022.4	chr1	1232265	1235041	+	2777	0	0	0"""

    return pd.read_table(StringIO(contents), header=1)

@pytest.fixture
def large_dataframe():
    return pd.read_table("tests/test_data/WT.csv", header=1)

@pytest.mark.integration
def test_large_file(large_dataframe):

    result = compute_quantiles(large_dataframe)

    r = result.Quantile.value_counts().tail(4)

    # check that quartiles are of equal size
    assert r.max() - r.min() <= 1

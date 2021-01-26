# Benchmark of SNSPowderReduction with new Caching feature

The objective of this document is to record the benchmark of `SNSPowderReduction` with
new Caching feature.
The testing was performed on analysis cluster with the following script

```python
SNSPowderReduction("/SNS/PG3/IPTS-2767/nexus/PG3_46214.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_01_04_PAC_limit_1.4MW.txt,/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_05_06-HighRes-PAC_1.4 MW.txt",
                   Binning=-0.001,
                   SaveAs="nexus",
                   TypeOfCorrection="SampleAndContainer",
                   SampleFormula="La-(B11)5.94-(B10)0.06",
                   MeasuredMassDensity=2.36,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='SC_absorption_',
                   OutputDirectory=".",
                   CacheDir=".",
                   )
```

> NOTE: the type of correction is changed to corresponding abs_method for testing.

# Benchmark

The testing following the procedure below:

- Run the code from a fresh workbench instance with no harddrive cache, record the run time as `No Cache`.
- Clear the workspace completely, then rerun the testing code and record the time as `Cache (disk)`.
- Keep the two abs workspace (_acc, and _ass) and remove all others, then run again and record the time as `Cache (memory)`.

> ENV: analysis-node11

> Units: seconds

> NOTE: `AlignAndFocusPowderFromFiles` also has a cache feature, which we choose not to include by removing the corresponding memory cache at step three

## SampleOnly

| Test Number | No Cache | Cache (disk)   | Cache (memory) |
| :---------: | :------: | :------------: | :------------: |
| 1           | 367.390  | 185.980        | 169.680        |
| 2           | 327.340  | 199.040        | 197.620        |
| 3           | 344.640  | 146.380        | 147.430        |
| 4           | 247.110  | 136.580        | 151.950        |
| 5           | 313.280  | 158.590        | 238.210        |
| 6           | 401.540  | 200.370        | 223.210        |
| avg.        | 333.550  | 171.157        | 188.017        |

## SampleAndContainer

| Test Number | No Cache | Cache (disk)   | Cache (memory) |
| :---------: | :------: | :------------: | :------------: |
| 1           | 325.550  | 165.580        | 152.320        |
| 2           | 312.020  | 151.530        | 143.380        |
| 3           | 306.640  | 159.780        | 152.960        |
| 4           | 325.100  | 150.340        | 139.090        |
| 5           | 330.520  | 158.700        | 143.700        |
| 6           | 324.690  | 166.600        | 156.750        |
| avg.        | 320.753  | 158.755        | 148.033        |

## FullPaalmanPings

| Test Number | No Cache | Cache (disk)   | Cache (memory) |
| :---------: | :------: | :------------: | :------------: |
| 1           |
| 2           | 
| 3           |
| 4           |
| 5           |
| 6           |
| avg.        |

# Summary

Here is the summary of speed comparison using case `No Cache` as baseline
for each method

| Method Name        | No Cache | Cache (disk) | Cache (memory) |
| :----------------: | :------: | :----------: | :------------: |
| SampleOnly         | 100%     | **194.880%** | 177.404%       |
| SampleAndContainer | 100%     | 202.043%     | **216.677%**   |
| FullPaalmanPings   | 100%     |              |                |

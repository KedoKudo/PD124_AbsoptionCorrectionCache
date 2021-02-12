from mantid.simpleapi import *

# first pass to generate the cache
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


# second pass to use the cache
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
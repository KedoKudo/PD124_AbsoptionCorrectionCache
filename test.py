from mantid.simpleapi import *

# 
SNSPowderReduction("data/PG3_46214.nxs.h5",
                   CalibrationFile="data/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="data/PG3_char_2020_01_04_PAC_limit_1.4MW.txt,data/PG3_char_2020_05_06-HighRes-PAC_1.4MW.txt",
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
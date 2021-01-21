from mantid.simpleapi import SNSPowderReduction, mtd

# No Absorption Correction
SNSPowderReduction("PG3_46214.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_01_04_PAC_limit_1.4MW.txt,/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_05_06-HighRes-PAC_1.4 MW.txt",
                   Binning=-0.001,
                   SaveAs="nexus",
                   OutputDirectory="LaB6_reduction_out")

mtd.clear()

# Sample Only Absorption Correction
SNSPowderReduction("PG3_46214.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_01_04_PAC_limit_1.4MW.txt,/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_05_06-HighRes-PAC_1.4 MW.txt",
                   Binning=-0.001,
                   SaveAs="nexus",
                   TypeOfCorrection="SampleOnly",
                   SampleFormula="La-(B11)5.94-(B10)0.06",
                   MeasuredMassDensity=2.36,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='Sample_absorption_',
                   OutputDirectory="LaB6_reduction_out")

mtd.clear()

# Sample and Container Absorption Correction
SNSPowderReduction("PG3_46214.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_01_04_PAC_limit_1.4MW.txt,/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_05_06-HighRes-PAC_1.4 MW.txt",
                   Binning=-0.001,
                   SaveAs="nexus",
                   TypeOfCorrection="SampleAndContainer",
                   SampleFormula="La-(B11)5.94-(B10)0.06",
                   MeasuredMassDensity=2.36,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='SC_absorption_',
                   OutputDirectory="LaB6_reduction_out")

mtd.clear()

# Full-PP Absorption Correction
SNSPowderReduction("PG3_46214.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_01_04_PAC_limit_1.4MW.txt,/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_05_06-HighRes-PAC_1.4 MW.txt",
                   Binning=-0.001,
                   SaveAs="nexus",
                   TypeOfCorrection="FullPaalmanPings",
                   SampleFormula="La-(B11)5.94-(B10)0.06",
                   MeasuredMassDensity=2.36,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='PP_absorption_',
                   OutputDirectory="LaB6_reduction_out")

mtd.clear()

# No Absorption Correction
SNSPowderReduction("PG3_46214.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_01_04_PAC_limit_1.4MW.txt,/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_05_06-HighRes-PAC_1.4 MW.txt",
                   Binning=-0.001,
                   FinalDataUnits="MomentumTransfer",
                   SaveAs="nexus",
                   OutputDirectory="LaB6_reduction_out_Q")

mtd.clear()

# Sample Only Absorption Correction
SNSPowderReduction("PG3_46214.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_01_04_PAC_limit_1.4MW.txt,/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_05_06-HighRes-PAC_1.4 MW.txt",
                   Binning=-0.001,
                   FinalDataUnits="MomentumTransfer",
                   SaveAs="nexus",
                   TypeOfCorrection="SampleOnly",
                   SampleFormula="La-(B11)5.94-(B10)0.06",
                   MeasuredMassDensity=2.36,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='Sample_absorption_',
                   OutputDirectory="LaB6_reduction_out_Q")

mtd.clear()

# Sample and Container Absorption Correction
SNSPowderReduction("PG3_46214.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_01_04_PAC_limit_1.4MW.txt,/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_05_06-HighRes-PAC_1.4 MW.txt",
                   Binning=-0.001,
                   FinalDataUnits="MomentumTransfer",
                   SaveAs="nexus",
                   TypeOfCorrection="SampleAndContainer",
                   SampleFormula="La-(B11)5.94-(B10)0.06",
                   MeasuredMassDensity=2.36,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='SC_absorption_',
                   OutputDirectory="LaB6_reduction_out_Q")

mtd.clear()

# Full-PP Absorption Correction
SNSPowderReduction("PG3_46214.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_01_04_PAC_limit_1.4MW.txt,/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_05_06-HighRes-PAC_1.4 MW.txt",
                   Binning=-0.001,
                   FinalDataUnits="MomentumTransfer",
                   SaveAs="nexus",
                   TypeOfCorrection="FullPaalmanPings",
                   SampleFormula="La-(B11)5.94-(B10)0.06",
                   MeasuredMassDensity=2.36,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='PP_absorption_',
                   OutputDirectory="LaB6_reduction_out_Q")

mtd.clear()

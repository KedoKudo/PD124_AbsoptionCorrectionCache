from mantid.simpleapi import SNSPowderReduction, mtd

# No Absorption Correction
SNSPowderReduction("PG3_40644.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_07_05.txt,/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_06_11-HighRes-PAC.txt",
                   Binning=-0.001,
                   SaveAs="nexus",
                   OutputDirectory="NaCl_reduction_out")

mtd.clear()

# Sample Only Absorption Correction
SNSPowderReduction("PG3_40644.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_07_05.txt,/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_06_11-HighRes-PAC.txt",
                   Binning=-0.001,
                   SaveAs="nexus",
                   TypeOfCorrection="SampleOnly",
                   SampleFormula="Na Cl",
                   MeasuredMassDensity=1.085,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='Sample_absorption_',
                   OutputDirectory="NaCl_reduction_out")

mtd.clear()

# Sample and Container Absorption Correction
SNSPowderReduction("PG3_40644.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_07_05.txt,/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_06_11-HighRes-PAC.txt",
                   Binning=-0.001,
                   SaveAs="nexus",
                   TypeOfCorrection="SampleAndContainer",
                   SampleFormula="Na Cl",
                   MeasuredMassDensity=1.085,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='SC_absorption_',
                   OutputDirectory="NaCl_reduction_out")

mtd.clear()

# Full-PP Absorption Correction
SNSPowderReduction("PG3_40644.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_07_05.txt,/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_06_11-HighRes-PAC.txt",
                   Binning=-0.001,
                   SaveAs="nexus",
                   TypeOfCorrection="FullPaalmanPings",
                   SampleFormula="Na Cl",
                   MeasuredMassDensity=1.085,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='PP_absorption_',
                   OutputDirectory="NaCl_reduction_out")

mtd.clear()

# No Absorption Correction
SNSPowderReduction("PG3_40644.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_07_05.txt,/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_06_11-HighRes-PAC.txt",
                   FinalDataUnits="MomentumTransfer",
                   Binning=-0.001,
                   SaveAs="nexus",
                   OutputDirectory="NaCl_reduction_out_Q")

mtd.clear()

# Sample Only Absorption Correction
SNSPowderReduction("PG3_40644.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_07_05.txt,/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_06_11-HighRes-PAC.txt",
                   FinalDataUnits="MomentumTransfer",
                   Binning=-0.001,
                   SaveAs="nexus",
                   TypeOfCorrection="SampleOnly",
                   SampleFormula="Na Cl",
                   MeasuredMassDensity=1.085,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='Sample_absorption_',
                   OutputDirectory="NaCl_reduction_out_Q")

mtd.clear()

# Sample and Container Absorption Correction
SNSPowderReduction("PG3_40644.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_07_05.txt,/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_06_11-HighRes-PAC.txt",
                   FinalDataUnits="MomentumTransfer",
                   Binning=-0.001,
                   SaveAs="nexus",
                   TypeOfCorrection="SampleAndContainer",
                   SampleFormula="Na Cl",
                   MeasuredMassDensity=1.085,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='SC_absorption_',
                   OutputDirectory="NaCl_reduction_out_Q")

mtd.clear()

# Full-PP Absorption Correction
SNSPowderReduction("PG3_40644.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_07_05.txt,/SNS/PG3/shared/CALIBRATION/2018_2_11A_CAL/PG3_char_2018_06_11-HighRes-PAC.txt",
                   FinalDataUnits="MomentumTransfer",
                   Binning=-0.001,
                   SaveAs="nexus",
                   TypeOfCorrection="FullPaalmanPings",
                   SampleFormula="Na Cl",
                   MeasuredMassDensity=1.085,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='PP_absorption_',
                   OutputDirectory="NaCl_reduction_out_Q")

mtd.clear()
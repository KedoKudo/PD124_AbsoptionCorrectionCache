from mantid.simpleapi import SNSPowderReduction, mtd

# No Absorption Correction
SNSPowderReduction("PG3_46577.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_01_04_PAC_limit_1.4MW.txt,/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_05_06-HighRes-PAC_1.4 MW.txt",
                   Binning=-0.001,
                   SaveAs="topas",
                   OutputDirectory="Si_reduction_out")

mtd.clear()

# Sample Only Absorption Correction
SNSPowderReduction("PG3_46577.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_01_04_PAC_limit_1.4MW.txt,/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_05_06-HighRes-PAC_1.4 MW.txt",
                   Binning=-0.001,
                   SaveAs="topas",
                   TypeOfCorrection="SampleOnly",
                   SampleFormula="Si",
                   MeasuredMassDensity=1.1645,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='Sample_absorption_',
                   OutputDirectory="Si_reduction_out")

mtd.clear()

# Sample and Container Absorption Correction
SNSPowderReduction("PG3_46577.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_01_04_PAC_limit_1.4MW.txt,/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_05_06-HighRes-PAC_1.4 MW.txt",
                   Binning=-0.001,
                   SaveAs="topas",
                   TypeOfCorrection="SampleAndContainer",
                   SampleFormula="Si",
                   MeasuredMassDensity=1.1645,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='SC_absorption_',
                   OutputDirectory="Si_reduction_out")

mtd.clear()

# Full-PP Absorption Correction
SNSPowderReduction("PG3_46577.nxs.h5",
                   CalibrationFile="/SNS/PG3/shared/CALIBRATION/2020_1_11A_CAL/PG3_PAC_HR_d46168_2020_05_06.h5",
                   CharacterizationRunsFile="/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_01_04_PAC_limit_1.4MW.txt,/SNS/PG3/shared/CALIBRATION/2020_2_11A_CAL/PG3_char_2020_05_06-HighRes-PAC_1.4 MW.txt",
                   Binning=-0.001,
                   SaveAs="topas",
                   TypeOfCorrection="FullPaalmanPings",
                   SampleFormula="Si",
                   MeasuredMassDensity=1.1645,  # Need to verify 'packing density' = 'measured mass density'?
                   ContainerShape="PAC06",
                   OutputFilePrefix='PP_absorption_',
                   OutputDirectory="Si_reduction_out")

mtd.clear()

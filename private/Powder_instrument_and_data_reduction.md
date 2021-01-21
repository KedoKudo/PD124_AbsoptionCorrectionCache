Here is what I can think of about powder instrument in general, which I hope may be helpful.

Detector arrangement
===

Neutrons coming out from sources (spallation) may go through moderator and probably beam monitor before they arrive at samples to be scattered. The scattered neutrons will then bump into detectors arranged in panels. For NOMAD, those panels are arranged in a manner of physical banks while for POWGEN there is no physical banks (I believe). But the thing is, you can specify however many of pixels as a group and treat them as a 'bank' - that's, I believe, what we see in the POWGEN characterization file - I mean the five banks that we see in the bank column.

PS: A little demo for NOMAD banks can be found in this link: [https://code.ornl.gov/sns-hfir-scse/diffraction/powder/powder-diffraction/-/issues/157](https://code.ornl.gov/sns-hfir-scse/diffraction/powder/powder-diffraction/-/issues/157). I don't have one for POWGEN unfortunately.

Background subtraction
===

What detectors see is scattered neutron, for sure. But the thing is neutrons are not only scattered by our sample (which is, however, the only thing we are interested in) but also scattered from sample container and background (i.e. the empty instrument) as well. That's why we need to measure sample container and background along with the measurement for sample in container. Then we can subtract the signal from container and background from the signal for sample in container (which basically contains everything everything).

Calibration
===

The fundamental equation behind the scene is $`2d\,sin\theta = n\lambda`$ - $`d`$ is basically something we care about for our sample so we want to know $`\lambda`$ and $`\theta`$ simultaneously to get $`d`$. For time-of-flight (TOF) technique, we fix $`\theta`$ and vary $`\lambda`$ to basically scan through $`d`$-space. Furthermore, TOF is linked to $`\lambda`$ (fundamentally it is neutron velocity that is directly linked to $`\lambda`$. But suppose we know the flying path of neutrons, we can establish the link between TOF and $`\lambda`$ without problem) so we can scan through TOF to scan through $`d`$. In practice, for each single pixel (the smallest unit of the detector), we will get an intensity .vs. TOF pattern. In principle, we know where each pixel is located physically so we should know exactly $`\theta`$ in the equation. Also, holding the TOF-$`\lambda`$ relation, we should be able to transform the intensity .vs. TOF pattern into intensity .vs. $`d`$ pattern (which is something we fundamentally want to get from scattering experiment). However in practice, it is not that straightforward. We don't know exactly where our sample is located which means that we don't know the exact flying path of neutrons. That indicates we don't know the exact correspondence between TOF and $`\lambda`$. Also, the $`\theta`$ value is not accurate as well. That's the reason why we need to do the so-called calibration to enable us to transform the intensity .vs. TOF to intensity .vs. $`d`$ properly. We grab a standard sample for which we know exactly what $`d`$ is. We measure it to obtain its intensity .vs. TOF pattern. Because in this case we know exactly our intensity .vs. d patterns (basically, where diffraction peaks are located), it becomes possible that we can establish a direct link between TOF and $`d`$ through such a calibration with standard sample (usually, diamond).

Normalization
===

Calibration concerns about the TOF-$`d`$ transformation which can basically tell us where peaks are located in $`d`-space for our sample. But peak position is not the only thing we are interested in. The other thing of importance here is the intensity. Intensity is fundamentally the number of neutrons hitting detectors. But the thing is the number of neutrons detected by detectors is not equal to the number of neutrons hitting detectors because our detectors efficiency is not 100 percent - some neutrons hitting detectors are just not picked up by detectors. That means the 'intensity' we obtain when measuring our sample is not the actual intensity. To solve this problem, we need vanadium measurement. Without mentioning any technological terminologies, vanadium can be thought of as a sort of 'standard' sample with which we can normalize our diffraction pattern to correct for the detector efficiency issue.

Absorption, multiple scattering, etc.
===

When neutrons hit our sample (real sample, vanadium, container, or even our instrument), scattering is not the only event that will happen. Neutrons can also be absorbed. That's definitely something we want to correct for, per intensity concerned. Multiple scattering is another thing that could happen - neutrons can be scattered multiple times before they fly out of our sample and again that's something we want to correct. Absorption correction is something we have been working on and multiple scattering is something we want to worry about in the near future (in Mantid).

Final remarks
===

Statements presented above should be applicable generally to any TOF powder instrument, e.g. NOMAD and POWGEN at SNS. So ideally, we should have a uniform data reduction routine that is universally applicable on, e.g. both NOMAD and POWGEN. But in practice, that's unfortunately something we haven't got to yet.

Yuanpeng Zhang @ Wed Jan 20 17:17:27 2021 EST
CIS-PD, SNS at ORNL
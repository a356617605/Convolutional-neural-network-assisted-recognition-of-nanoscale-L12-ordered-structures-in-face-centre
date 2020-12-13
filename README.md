# Convolutional neural network-assisted recognition of nanoscale L12 ordered structures in face-centred cubic alloys

Cite: npj Computational Materials, 2020: https://doi.org/10.1038/s41524-020-00472-7

Nanoscale L12-type ordered structures are widely used in face-centered cubic (FCC) alloys to exploit their hardening capacity and thereby improve
mechanical properties. These fine-scale particles are typically fully coherent with matrix with the same atomic configuration disregarding chemical
species, which makes them challenging to be characterized. Spatial distribution maps (SDMs) are used to probe local order by interrogating the
three-dimensional (3D) distribution of atoms within reconstructed atom probe tomography (APT) data. However, it is almost impossible to
manually analyze the complete point cloud (>10 million) in search for the partial crystallographic information retained within the data. Here, we
proposed an intelligent L12-ordered structure recognition method based on convolutional neural networks (CNNs). The SDMs of a simulated L12-
ordered structure and the FCC matrix were firstly generated. These simulated images combined with a small amount of experimental data were
used to train a CNN-based L12-ordered structure recognition model. Finally, the approach was successfully applied to reveal the 3D distribution of
L12–type δ′–Al3(LiMg) nanoparticles with an average radius of 2.54nm in a FCC Al-Li-Mg system. The minimum radius of detectable nanodomain
is even down to 5 Å. The proposed CNN-APT method is promising to be extended to recognize other nanoscale ordered structures and even
more-challenging short-range ordered phenomena in the near future.

The first step is to build the simulated datasets as an input to train CNNs. Please refer to the Simulation of zx-SDMs folder.

Then, the obtained SDMs (used as inputs) combined with their corresponding crystal structures (used as outputs) were divided into training, validation, and test datasets, which were then used to train CNNs with the help of a small amount of experimental data in order to generate an L12 ordered structure recognition model. 

Finally, the experimentally-obtained SDMs from an Al-Li-Mg alloy were input into this recognition model to identify the 3D distributions of the L12–type Al3(LiMg) particles in the FCC matrix with a high accuracy. 

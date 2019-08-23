# Reaction network optimisation
This repository describes two models for reaction network optimisation. One is the **Flux Balances Analysis (FBA)** and the other a **Petri net optimisation (PNO)**


## Description of reaction network

We look at the following sample reaction system. It is representative of real chemical networls as it:
- it has more reactions than participating molecules
- equality reactions introduce bidirectionalities
- cycles are present

<p>Reaction 1 (R1): A + B →2C<br>
Reaction 2 (R2):C→B<br>
Reaction 3 (R3): A + C →2D+E<br>
Reaction 4 (R4): 3A→E<br>
Reaction 5 (R5):  B →D<br>
Reaction 6 (R6): D →B<br>
Reaction 7 (R7): 5A→B <p/>  

The following image shows a petri net representation of the system. Molecules are represented by circular nodes and reactions are shwon as bars. The stoichiometry of the reaction system is contained by the numbers on the edges.
![alt text][logo]  



[logo]: https://github.com/Jana-Marie-Weber/Reaction_network_optimisation/blob/master/sample_net.png "Logo Title Text 2"

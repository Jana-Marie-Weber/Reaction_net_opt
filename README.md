# Reaction network optimisation
This repository describes two models for reaction network optimisation. One is the **Flux Balances Analysis (FBA)** and the other a **Petri net optimisation (PNO)**


## Description of reaction network

We look at the following sample reaction system. It is representative of real chemical networks as it:
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

## Solving reaction network problems
The question of finding an optimal reaction pathway may be described through two simple scenarios. Given a certain amount of feedstock, what are the optimal reaction paths and products resultimg from it? Given a certain target molecule, what are the optimal feedstocks and reaction paths to produce it? Hence, the underlying question is one concerning optimality. Optimility in the objective function can be defined based on e.g. the prices of the compounds and costs involved in reactions.

The two approaches to solve such problems are the [RNFA], where stationary material balances model a steady-state of the system and constrain the network, and [petri nets] or [PNO], where tokens move through the network simulating the molecular flow.
In this work we show implementations of both systems for the case study described above. The main finding is, that the PNO allows a greater level of system control at the cost of higher model complexity. 


## Organisation of this repository



[logo]: https://github.com/Jana-Marie-Weber/Reaction_network_optimisation/blob/master/sample_net.png "Logo Title Text 2"
[RNFA]: https://onlinelibrary.wiley.com/doi/abs/10.1002/aic.12704
[petri nets]: https://onlinelibrary.wiley.com/doi/pdf/10.1002/minf.201000086
[PNO]: https://reader.elsevier.com/reader/sd/pii/009813549185029T?token=61AEF084C496C3044C2E9ECB56EB3427EAE8E2C8EB132172843F3839F376CB3B453833256C5EB9CB15501FC7A6031BB7

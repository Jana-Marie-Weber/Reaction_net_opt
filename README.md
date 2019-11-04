# Reaction network optimisation
This repository describes two models for reaction network optimisation. One is the **Reaction Network Flux Analysis (RNFA)** adopted from [Voll et al.](https://aiche.onlinelibrary.wiley.com/doi/full/10.1002/aic.12704) and the other a **Petri net optimisation (PNO)**. This study serves to guide decision-making on the modelling approach for reaction networks. For further information and to cite this work please refer to [this paper](https://pubs.rsc.org/en/content/articlehtml/2019/re/c9re00213h).


## Reaction network optimisation 

When optimising flux distributions in reaction networks, we wish to find the best reaction sequences with regard to prior specifications such as cost per reactions or revenue per molecules. This is difficult because of multiple reasons such as data availability, accuracy of the data, assembly of all relevant reactions, and complex structures within these reaction dependencies. Thsi work targets the models' behaviour with regard to circular substructures in the networks, which have shown to be common elements in chemical reaction networks.


We look at the following sample reaction system. R1 is an irreversible bimolecular reaction producing intermediate C, whereas R2 is an irreversible bimolecular reaction leading to the formation of product D and regeneration of a specie B. The chemical meaning of substance B could be for instance a homogeneous catalyst or a protecting group (PG). A and E are reactants. 

<p>Reaction 1 (R1): A + B → C<br>
Reaction 2 (R2): C +E → B + D<br>
 <p/>  

The following image shows a petri net representation of the system. Molecules are represented by circular nodes and reactions are shwon as bars. The stoichiometry of the reaction system is contained by the numbers on the edges.
![alt text][logo]  

### Model formulation 

The two approaches to solve such problems are the [RNFA], where stationary material balances model a steady-state of the system and constrain the network, and [petri nets] or [PNO], where tokens move through the network simulating the molecular flow.
In this work we show implementations of both systems for the case study described above. The main finding is, that the PNO allows a greater level of system control at the cost of higher model complexity. 


## Organisation of this repository



[logo]: https://github.com/Jana-Marie-Weber/Reaction_net_opt/blob/master/Reaction_system_circular.png "Logo Title Text 2"
[RNFA]: https://onlinelibrary.wiley.com/doi/abs/10.1002/aic.12704
[petri nets]: https://onlinelibrary.wiley.com/doi/pdf/10.1002/minf.201000086
[PNO]: https://reader.elsevier.com/reader/sd/pii/009813549185029T?token=61AEF084C496C3044C2E9ECB56EB3427EAE8E2C8EB132172843F3839F376CB3B453833256C5EB9CB15501FC7A6031BB7

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



## Organisation of this repository

Within the folder [models], you will find an abstract model formualtion for the RNFA model and one for the PNO. The folder [case_study] contains data input files and results for three different scenarios.

## How to..

Please ensure you fulfil the system requirements. Then, run following command in the command line in your terminal.

```
pyomo solve MODEL_XXX.py INPUT_FILE_XXX.dat --solver=cplex 
```
Your result will be saved in ```results.yml file```. 



[logo]: https://github.com/Jana-Marie-Weber/Reaction_net_opt/blob/master/Reaction_systrem_circular.png "Logo Title Text 2"
[RNFA]: https://onlinelibrary.wiley.com/doi/abs/10.1002/aic.12704
[petri nets]: https://onlinelibrary.wiley.com/doi/pdf/10.1002/minf.201000086
[PNO]: https://reader.elsevier.com/reader/sd/pii/009813549185029T?token=61AEF084C496C3044C2E9ECB56EB3427EAE8E2C8EB132172843F3839F376CB3B453833256C5EB9CB15501FC7A6031BB7

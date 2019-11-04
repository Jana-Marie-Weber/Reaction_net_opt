# Reaction network optimisation
This repository describes two models for reaction network optimisation. One is the **Reaction Network Flux Analysis (RNFA)** adopted from [Voll et al.](https://aiche.onlinelibrary.wiley.com/doi/full/10.1002/aic.12704) and the other a **Petri net optimisation (PNO)**. This study serves to guide decision-making on the modelling approach for reaction networks. For further information and to cite this work please refer to [this paper](https://pubs.rsc.org/en/content/articlehtml/2019/re/c9re00213h).

## Organisation of this repository

We outline soem background information and links to related paper in this ReadMe. Within the folder [models] we outline implemented equations for both approaches. One finds an abstract model formualtion for the RNFA model and one for the PNO. An abstract model is a general form of the problem and can be used for multiple data inputs. The folder [case_study] contains data input files and the results for three tested scenarios.


## Reaction network optimisation 

When optimising flux distributions in reaction networks, we wish to find the best reaction sequences with regard to prior specifications such as cost per reactions or revenue per molecules. This is difficult because of multiple reasons such as data availability, accuracy of the data, assembly of all relevant reactions, and complex structures within these reaction dependencies. Thsi work targets the models' behaviour with regard to circular substructures in the networks, which have shown to be common elements in chemical reaction networks.


We look at the following sample reaction system. R1 is an irreversible bimolecular reaction producing intermediate C, whereas R2 is an irreversible bimolecular reaction leading to the formation of product D and regeneration of a specie B. The chemical meaning of substance B could be for instance a homogeneous catalyst or a protecting group (PG). A and E are reactants. 

<p>Reaction 1 (R1): A + B → C<br>
Reaction 2 (R2): C +E → B + D<br>
 <p/>  

The following image shows a petri net representation of the system. Molecules are represented by circular nodes and reactions are shwon as bars. The stoichiometry of the reaction system is contained by the numbers on the edges.
![alt text][logo]  

### Model formulation 

The two approaches to solve such problems are the [RNFA], where stationary material balances model a steady-state of the system and constrain the network, and [petri nets] or [PNO], where tokens move through the network simulating the molecular flow. Please consult the [models] folder for the implemented equations and the [case_study] folder for data input. 

### Scenarios 

In this work, we test the following three scenarios.
1. Case 1: 100 mol of A, B, and E are present. Both reaction costs 5 and the revenue of the desired moelcule D is 50/mol. 
2. Case 2: 100 mol of A and E are present. Both reaction costs 5 and the revenue of the desired moelcule D is 50/mol. 
3. Case 3: 100 mol of A and B are present. Both reaction costs 5 and the revenue of the desired moelcule D is 50/mol. 

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
[models]:
https://github.com/Jana-Marie-Weber/Reaction_net_opt/tree/master/models
[case_study]:
https://github.com/Jana-Marie-Weber/Reaction_net_opt/tree/master/case_study


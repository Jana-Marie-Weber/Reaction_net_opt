# Case study for reaction network optimisation

## Reaction network optimisation 


We look at the following sample reaction system. R1 is an irreversible bimolecular reaction producing intermediate C, whereas R2 is an irreversible bimolecular reaction leading to the formation of product D and regeneration of a specie B. The chemical meaning of substance B could be for instance a homogeneous catalyst or a protecting group (PG). A and E are reactants. 

<p>Reaction 1 (R1): A + B → C<br>
Reaction 2 (R2): C +E → B + D<br>
 <p/>  

The following image shows a petri net representation of the system. Molecules are represented by circular nodes and reactions are shwon as bars. The stoichiometry of the reaction system is contained by the numbers on the edges.
![alt text][logo]  

## Scenarios 

In this work, we test the following three scenarios.

| Scenario | Input A       | Input B       | Input C | Input D | Input E       | Reaction cost  | Revenue D |
|----------|---------|---------|---|---|---------|----------------|-----------|
| Case 1   | 100 mol | 100 mol |   |   | 100 mol | 5              | 50/mol    |
| Case 2   | 100 mol |         |   |   | 100 mol | 5              | 50/mol    |
| Case 3   | 100 mol | 100 mol |   |   |         | 5              | 50/mol    |


### RNFA input file parameters

- param S: the number of substances in the system 
- param R: the number of total reactions (this includes one pseudo supply reaction per compound and all stoichiometric reactions in the system)
- param c: a cost/penalty per reaction (again the first reactions a pseudo supply reactions which do not need a cost)
- param p: the selling price of each substance
- param a: the stoichiometric relationships 
- param bound: the pseudo input reaction matrix 
- param input: defines the amount of mol given to the system of each substance

### PNO input file parameters

- param places: the number of substances
- param transitions: the number of stoichiometric reactions
- param c: the selling price for each substance
- param s: the cost/penalty per reaction 
- param d: the stoichiometric relationships
- param a: the input of the substances (marking of places with tokens in the initial state k)


[logo]: https://github.com/Jana-Marie-Weber/Reaction_net_opt/blob/master/Reaction_systrem_circular.png "Logo Title Text 2"
[RNFA]: https://onlinelibrary.wiley.com/doi/abs/10.1002/aic.12704
[petri nets]: https://onlinelibrary.wiley.com/doi/pdf/10.1002/minf.201000086
[PNO]: https://reader.elsevier.com/reader/sd/pii/009813549185029T?token=61AEF084C496C3044C2E9ECB56EB3427EAE8E2C8EB132172843F3839F376CB3B453833256C5EB9CB15501FC7A6031BB7
[models]:
https://github.com/Jana-Marie-Weber/Reaction_net_opt/tree/master/models
[case_study]:
https://github.com/Jana-Marie-Weber/Reaction_net_opt/tree/master/case_study


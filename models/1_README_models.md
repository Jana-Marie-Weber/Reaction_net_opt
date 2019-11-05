# Models for reaction network optimisation

## Model formulation 

The two approaches to solve such problems are the [RNFA], where stationary material balances model a steady-state of the system and constrain the network, and [petri nets] or [PNO], where tokens move through the network simulating the molecular flow. Please consult the [models] folder for the implemented equations and the [case_study] folder for data input. 

### PNO model 
See below the equations for the PNO model formulation.
![alt text][PNO_model]  

For further description of the model formualtion, please refer to [this paper](https://pubs.rsc.org/en/content/articlehtml/2019/re/c9re00213h).

### RNFA model 
See below the equations for the RNFA model formualtion. 
![alt text][RNFA_model]  

For further description of the model formualtion, please refer to [Voll et al.](https://aiche.onlinelibrary.wiley.com/doi/full/10.1002/aic.12704)


## How to run abstract models in pyomo..

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
[PNO_model]:  https://github.com/Jana-Marie-Weber/Reaction_net_opt/blob/master/models/PNO_model_formulation.png 
[RNFA_model]:  
https://github.com/Jana-Marie-Weber/Reaction_net_opt/blob/master/models/RNFA_model_formulation.png 

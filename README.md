# Reaction network optimisation
This repository describes two models for reaction network optimisation. One is the **Reaction Network Flux Analysis (RNFA)** adopted from [Voll et al.](https://aiche.onlinelibrary.wiley.com/doi/full/10.1002/aic.12704) and the other a **Petri net optimisation (PNO)**. This study serves to guide decision-making on the modelling approach for reaction networks. For further information and to cite this work please refer to [this paper](https://pubs.rsc.org/en/content/articlehtml/2019/re/c9re00213h).

## Organisation of this repository

Within the folder [models] we show implemented equations for both approaches. One finds an abstract model formualtion for the RNFA model and one for the PNO. An abstract model is a general form of the problem and can be used for multiple data inputs. The folder [case_study] contains data input files and the results for three tested scenarios.


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



# coding: utf-8

# import the required packages and introduce the abstract model through pyomo environment


from pyomo.environ import *
model = AbstractModel()


# Here, we set the overall parameters, e.g. the number of places (substances) and the number of transitions (reactions)


model.places = Param(within=NonNegativeIntegers)
model.transitions = Param(within=NonNegativeIntegers)


# The following part defines the control variables. Here we have p from 1 to places and t from 1 to transitions.


model.P = RangeSet(1, model.places)
model.T = RangeSet(1, model.transitions)


# We define further fixed parameters below. For further information consult the readme in the input file folder.


model.c = Param(model.P)
model.s = Param(model.T)
model.b = Param(model.T)
model.d = Param(model.P,model.T)
model.a = Param(model.P)


# This part sets up the optimisation variables. All variables here (m,q, and y) could be used as a matrix, but are split into vectors here to facilitate the set-up of the abstract model. If one wishes to change the overall allowed steps, one needs to add vectors below. Here we have 2 steps bringing m from its initial state m1 to m3. Where the fluxes and the activation of transition per step are recorded in q and y respectively. !!!NEED FOR MODIFICATION WHEN USED FOR MORE STEPS!!!


model.m1 = Var(model.P, domain=NonNegativeReals)
model.m2 = Var(model.P, domain=NonNegativeReals)
model.m3 = Var(model.P, domain=NonNegativeReals)

model.q1 = Var(model.T, domain=NonNegativeReals)
model.q2 = Var(model.T, domain=NonNegativeReals)

model.y1 = Var(model.T, domain=Binary)
model.y2 = Var(model.T, domain=Binary)


# We define the objectve function below. Only m3 is counted here because we wish to value only the final production of the substances, where for q and y reactions at each step are of interest. In this example, the cost associated to y was specified to 0 to enable a fair comaprison between the two approaches. !!!NEED FOR MODIFICATION WHEN USED FOR MORE STEPS!!!


def obj_expression(model):
    return (-summation(model.c, model.m3)+ summation(model.s,model.q1)+ summation(model.s,model.q2) + summation(model.b, model.y1)+ summation(model.b, model.y2))
model.OBJ = Objective(rule=obj_expression)


# The following constraint allows only one reaction to happen at each time. All elements of y are summed up in each vector. !!!NEED FOR MODIFICATION WHEN USED FOR MORE STEPS!!!


def bi1_constraint_rule(model):
    return sum(model.y1[t] for t in model.T)<=1
model.binary1Constraint = Constraint(rule=bi1_constraint_rule)

def bi2_constraint_rule(model):
    return sum(model.y2[t] for t in model.T)<=1
model.binary2Constraint = Constraint(rule=bi2_constraint_rule)


# The following constraint enables an ordering of the active transitions. It defines that all active transitions should take place at the beginning, while inactive ones take place at the end. !!!NEED FOR MODIFICATION WHEN USED FOR MORE STEPS!!!


def sy_constraint_rule(model):
    return sum(model.y1[t] for t in model.T) <= sum(model.y2[t] for t in model.T)
model.symmeryConstraint = Constraint( rule=sy_constraint_rule)


# The gib M constraint couples y and q with each other, so that only if y is active the flux can take place and so that y is only active if a flux is allowed due to the stoichiometric relationships. Please change the big M value accordingly if you modify teh system. !!!NEED FOR MODIFICATION WHEN USED FOR MORE STEPS!!!


def bM1_constraint_rule(model,t):
    return model.q1[t] <= 500 * model.y1[t]
model.bM1Constraint = Constraint(model.T,rule=bM1_constraint_rule)

def bM2_constraint_rule(model,t):
    return model.q2[t] <= 500 * model.y2[t]
model.bM2Constraint = Constraint(model.T,rule=bM2_constraint_rule)

def bM3_constraint_rule(model,t):
    return model.y1[t] <= 500 * model.q1[t]
model.bM3Constraint = Constraint(model.T,rule=bM3_constraint_rule)

def bM4_constraint_rule(model,t):
    return model.y2[t] <= 500 * model.q2[t]
model.bM4Constraint = Constraint(model.T,rule=bM4_constraint_rule)



# This part defines the initial system. Here we specifiy the amount of mol (tokens) that we introduce at the initial state. This is done by using a pyomo constraint formalism, while it could probbaly be done in a much better way.


def bo_constraint_rule(model,p):
    return model.m1[p] == model.a[p]
model.boundConstraint = Constraint(model.P, rule=bo_constraint_rule)


# Here we update the marking and we make sure that only transitions that can fire based on the previous token distributions are active. This works as we have previously defined that all markings m nee dto be positive at each step.!!!NEED FOR MODIFICATION WHEN USED FOR MORE STEPS!!!


def ma1_constraint_rule(model,p):
    return model.m2[p]   == (model.m1[p]+sum(model.q1[t]*model.d[p,t] for t in model.T))
model.marking1Constraint = Constraint(model.P, rule=ma1_constraint_rule)

def ma2_constraint_rule(model,p):
    return model.m3[p]   == (model.m2[p]+sum(model.q2[t]*model.d[p,t] for t in model.T))
model.marking2Constraint = Constraint(model.P, rule=ma2_constraint_rule)


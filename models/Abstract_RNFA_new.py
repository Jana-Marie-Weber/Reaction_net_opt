
# coding: utf-8

# # RNFA Abstract model 

# Import all packages needed


from pyomo.environ import *


# setting up a abstract model in pyomo


model = AbstractModel()


# This part defines the number of substances and reactions and the control variables within that space. Hence, we have k from 1 to S and j from 1 to R.


model.S = Param(within=NonNegativeIntegers)
model.R = Param(within=NonNegativeIntegers)
model.K = RangeSet(1, model.S)
model.J = RangeSet(1, model.R)


# This part defines the constant parameters for the problem.
# `model.c` are the flux costs, `model.p` the price for selling a molecule, `model.a` the stoichiometric matrix, and `model.bound` and `model.input` define the inital mol distribution. 



model.c = Param(model.J)
model.p = Param(model.K)
model.a = Param(model.K, model.J)
model.bound = Param(model.K,model.J)
model.input = Param(model.K)


# Here, we set up the models variables `model.f` and `model.b`. The first `S` fluxes will be specified to guarantee that the system is bounded (Pseudo input fluxes). The following reaction fluxes are degrees of freedom. 


model.f = Var(model.J, domain=NonNegativeReals)
model.b = Var(model.K, domain=NonNegativeReals)


# This pyomo expression defines the objective function. All reaction fluxes are multiplied with the respective costs and all output fluxes with possible revenues per molecule. 


def obj_expression(model):
    return (summation(model.c, model.f) - summation(model.p,model.b))

model.OBJ = Objective(rule=obj_expression)


# This pyomo expression defines the stoichemtric constraints: \begin{equation}A \cdot \textbf{f}=\textbf{b}\end{equation}

def ax_constraint_rule(model, k):
    # return the expression for the constraint for i
    return sum(model.a[k,j] * model.f[j] for j in model.J) == model.b[k]

model.AxbConstraint = Constraint(model.K, rule=ax_constraint_rule)


# Here we specify the input parameters (input fluxes to the system). We use a constraint formalism, there might be anotehr way to do this.



def Boundary_constraint(model,k):
    return sum(model.bound[k,j]*model.f[j] for j in model.J) == model.input[k]
model.BoundConstraint = Constraint(model.K, rule=Boundary_constraint)


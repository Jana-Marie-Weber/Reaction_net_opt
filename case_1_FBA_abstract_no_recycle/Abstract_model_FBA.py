
# coding: utf-8

# # PYOMO FBA MODEL 
# We build a simple abstract model. First, we need to load all required packages. Second, we give an example of an abstract objective function and constraint formulation. 

# In[37]:


from pyomo.environ import *


# ## Formulation of the optimisation problem
# 
# \begin{equation}
# \begin{aligned}
# \min_{x_{j}} \quad & \sum_{j=1}^{R}{c_{j}f_{j}} -\sum_{k=1}^{S}{p_{k}b_{k}}\\
# \textrm{s.t.} \quad & \sum_{j=1}^{R}{a_{kj}f_{j}} = b_{k} \quad \forall k=1 ... S  \\
#   &f_{j}\geq0 \quad \forall j=1 ... R    \\
# \end{aligned}
# \end{equation}

# ## Formulation of the Pyomo model: step by step
# We declare the model to be an abstract model. The name "model" may be varied. 

# In[38]:


model = AbstractModel()


# We set up parameters *m* and *n* as limits for the sum. Specifiation to nonNegativeIntegers allows the data input only to be nonNegativeIntegers. Any other input type will result in an error messeage. 

# In[39]:


model.S = Param(within=NonNegativeIntegers)
model.R = Param(within=NonNegativeIntegers)
model.BoundSupply = Param (within=NonNegativeIntegers)


# Next, we define index sets. It is not required but good practice to define the index parameters further. We declare here that it will be a range starting from 1 and ending at the values specified by `model.m` and `model.n`.

# In[40]:


model.K = RangeSet(1, model.S)
model.J = RangeSet(1, model.R)
model.H = RangeSet(1, model.BoundSupply)


# We now define the coefficients for both constraint and objective expression. We can make use of the indices specified before for that purpose. Also, the indices indicate the dimension of the input coefficients, E.g. `model.a` is a matrix, while `model.b` and `model.c` are vectors. 

# In[41]:


model.c = Param(model.J)
model.f = Param(model.J)
model.p = Param(model.K)
model.b = Param(model.K)
model.a = Param(model.K, model.J)
model.bound = Param(model.H,model.J)
model.input = Param(model.H)


# Now, we need to declare decision variables with the `Var` function. The first argument gives an index set and therewith the dimension of the decision variable. The second argument specifies the domain. These domains give the differences between e.g. LP and MILP, as we can introduce integer variables here. 

# In[42]:


model.f = Var(model.J, domain=NonNegativeReals)
model.b = Var(model.K, domain=NonNegativeReals)


# We wish to determine the objective function now. A python function is used to create the vector addition over all decision variables. He we add the coefficients. Following we need to declare the expression as objective function to the model. For that, we use the rule argument which intakes a function and we work with the default sense which is a minimisation problem. For maximisation problems, either `sense=maximize` or the coefficients of the objective functions can be adjusted. The name `OBJ` can be almost any name.  

# In[43]:


def obj_expression(model):
    return (summation(model.c, model.f) - summation(model.p,model.b))

model.OBJ = Objective(rule=obj_expression)


# We now wish to constrain the problem in a similar way as down with the objective function. In order to allow multiple constraints we parameterize the function with *i*, which states that we need a constraint for each value of *i* in *m*. we declare this as a constraint by using the Pyomo `Constraint` function. The model says that we can have more than one constraint of the same form and we have created the set `model.I` over which the constraints are indexed. The second argument gives the rule for the constraint fucntion. 

# In[44]:


def ax_constraint_rule(model, k):
    # return the expression for the constraint for i
    return sum(model.a[k,j] * model.f[j] for j in model.J) == model.b[k]

model.AxbConstraint = Constraint(model.K, rule=ax_constraint_rule)


# In[ ]:


def Boundary_constraint(model,h):
    return sum(model.bound[h,j]*model.f[j] for j in model.J) == model.input[h]
model.BoundConstraint = Constraint(model.H, rule=Boundary_constraint)


# ## Next step: data input
# 
# We have now sucessfully build an abstract pyomo model. The next step is to input data to the model. 

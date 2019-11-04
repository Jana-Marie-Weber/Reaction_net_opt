
# coding: utf-8

# In[3]:


from pyomo.environ import *
model=ConcreteModel()


# In[4]:


model = ConcreteModel()

model.x = Var([1,2], domain=NonNegativeReals)

model.OBJ = Objective(expr = 2*model.x[1] + 3*model.x[2])

model.Constraint1 = Constraint(expr = 3*model.x[1] + 4*model.x[2] >= 1)


# In[5]:


SolverFactory('cplex').solve(model, tee=True)
model.display()
model.pprint()



# coding: utf-8

# In[1]:


from pyomo.environ import *
model = AbstractModel()


# In[2]:


model.places = Param(within=NonNegativeIntegers)
model.transitions = Param(within=NonNegativeIntegers)


# In[3]:


model.P = RangeSet(1, model.places)
model.T = RangeSet(1, model.transitions)


# In[4]:


model.c = Param(model.P)
model.s = Param(model.T)
model.b = Param(model.T)
model.d = Param(model.P,model.T)
model.a = Param(model.P)


# In[5]:


model.m1 = Var(model.P, domain=NonNegativeReals)
model.m2 = Var(model.P, domain=NonNegativeReals)
model.m3 = Var(model.P, domain=NonNegativeReals)

model.q1 = Var(model.T, domain=NonNegativeReals)
model.q2 = Var(model.T, domain=NonNegativeReals)

model.y1 = Var(model.T, domain=Binary)
model.y2 = Var(model.T, domain=Binary)


# In[6]:


def obj_expression(model):
    return (-summation(model.c, model.m3)+ summation(model.s,model.q1)+ summation(model.s,model.q2) + summation(model.b, model.y1)+ summation(model.b, model.y2))
model.OBJ = Objective(rule=obj_expression)


# In[7]:


def bi1_constraint_rule(model):
    return sum(model.y1[t] for t in model.T)<=1
model.binary1Constraint = Constraint(rule=bi1_constraint_rule)

def bi2_constraint_rule(model):
    return sum(model.y2[t] for t in model.T)<=1
model.binary2Constraint = Constraint(rule=bi2_constraint_rule)


# In[8]:


def sy_constraint_rule(model):
    return sum(model.y1[t] for t in model.T) <= sum(model.y2[t] for t in model.T)
model.symmeryConstraint = Constraint( rule=sy_constraint_rule)


# In[9]:


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



# In[10]:


def bo_constraint_rule(model,p):
    return model.m1[p] == model.a[p]
model.boundConstraint = Constraint(model.P, rule=bo_constraint_rule)


# In[11]:


def ma1_constraint_rule(model,p):
    return model.m2[p]   == (model.m1[p]+sum(model.q1[t]*model.d[p,t] for t in model.T))
model.marking1Constraint = Constraint(model.P, rule=ma1_constraint_rule)

def ma2_constraint_rule(model,p):
    return model.m3[p]   == (model.m2[p]+sum(model.q2[t]*model.d[p,t] for t in model.T))
model.marking2Constraint = Constraint(model.P, rule=ma2_constraint_rule)


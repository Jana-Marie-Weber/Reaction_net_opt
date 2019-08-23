
# coding: utf-8

# In[1]:


from pyomo.environ import *
model=ConcreteModel()


# In[2]:


#adding the lists does not wor yet 
mu_list=list(range(21))
print(mu_list)
q_list=list(range(29))
print(q_list)


# In[3]:


model.mu=Var([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],domain=NonNegativeReals)
model.q=Var([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28],domain=NonNegativeReals)


model.OBJ=Objective(expr=-50*model.mu[20]+model.q[1]+model.q[2]+model.q[3]+model.q[4]+model.q[5]+model.q[6]+model.q[7]+model.q[8]+model.q[9]+model.q[10]+model.q[11]+model.q[12]+model.q[13]+model.q[14]+model.q[15]+model.q[16]+model.q[17]+model.q[18]+model.q[19]+model.q[20]+model.q[21]+model.q[22]+model.q[23]+model.q[24]+model.q[25]+model.q[26]+model.q[27]+model.q[28])

model.Constraint1=Constraint(expr=model.mu[1]==100)
model.Constraint2=Constraint(expr=model.mu[2]==0)
model.Constraint3=Constraint(expr=model.mu[3]==0)
model.Constraint4=Constraint(expr=model.mu[4]==0)
model.Constraint5=Constraint(expr=model.mu[5]==0)


# In[4]:


#updating marking constraints
model.Constraint6 = Constraint(expr = model.mu[6]==model.mu[1]+model.q[1]*(-1)+model.q[2]*(0)+model.q[3]*(-1)+model.q[4]*(-3)+model.q[5]*(0)+model.q[6]*(0)+model.q[7]*(-5))
model.Constraint7 = Constraint(expr = model.mu[7]==model.mu[2]+model.q[1]*(-1)+model.q[2]*(1)+model.q[3]*(0)+model.q[4]*(0)+model.q[5]*(-1)+model.q[6]*(1)+model.q[7]*(1))
model.Constraint8 = Constraint(expr = model.mu[8]==model.mu[3]+model.q[1]*(2)+model.q[2]*(-1)+model.q[3]*(-1)+model.q[4]*(0)+model.q[5]*(0)+model.q[6]*(0)+model.q[7]*(0))
model.Constraint9 = Constraint(expr = model.mu[9]==model.mu[4]+model.q[1]*(0)+model.q[2]*(0)+model.q[3]*(2)+model.q[4]*(0)+model.q[5]*(1)+model.q[6]*(-1)+model.q[7]*(0))
model.Constraint10 = Constraint(expr = model.mu[10]==model.mu[5]+model.q[1]*(0)+model.q[2]*(0)+model.q[3]*(1)+model.q[4]*(1)+model.q[5]*(0)+model.q[6]*(0)+model.q[7]*(0))


# In[5]:


model.Constraint11= Constraint(expr = model.mu[11]==model.mu[6]+model.q[8]*(-1)+model.q[9]*(0)+model.q[10]*(-1)+model.q[11]*(-3)+model.q[12]*(0)+model.q[13]*(0)+model.q[14]*(-5))
model.Constraint12= Constraint(expr = model.mu[12]==model.mu[7]+model.q[8]*(-1)+model.q[9]*(1)+model.q[10]*(0)+model.q[11]*(0)+model.q[12]*(-1)+model.q[13]*(1)+model.q[14]*(1))
model.Constraint13= Constraint(expr = model.mu[13]==model.mu[8]+model.q[8]*(2)+model.q[9]*(-1)+model.q[10]*(-1)+model.q[11]*(0)+model.q[12]*(0)+model.q[13]*(0)+model.q[14]*(0))
model.Constraint14= Constraint(expr = model.mu[14]==model.mu[9]+model.q[8]*(0)+model.q[9]*(0)+model.q[10]*(2)+model.q[11]*(0)+model.q[12]*(1)+model.q[13]*(-1)+model.q[14]*(0))
model.Constraint15= Constraint(expr = model.mu[15]==model.mu[10]+model.q[8]*(0)+model.q[9]*(0)+model.q[10]*(1)+model.q[11]*(1)+model.q[12]*(0)+model.q[13]*(0)+model.q[14]*(0))


# In[6]:


model.Constraint16= Constraint(expr = model.mu[16]==model.mu[11]+model.q[15]*(-1)+model.q[16]*(0)+model.q[17]*(-1)+model.q[18]*(-3)+model.q[19]*(0)+model.q[20]*(0)+model.q[7]*(-5))
model.Constraint17= Constraint(expr = model.mu[17]==model.mu[12]+model.q[15]*(-1)+model.q[16]*(1)+model.q[17]*(0)+model.q[18]*(0)+model.q[19]*(-1)+model.q[20]*(1)+model.q[7]*(1))
model.Constraint18= Constraint(expr = model.mu[18]==model.mu[13]+model.q[15]*(2)+model.q[16]*(-1)+model.q[17]*(-1)+model.q[18]*(0)+model.q[19]*(0)+model.q[20]*(0)+model.q[7]*(0))
model.Constraint19= Constraint(expr = model.mu[19]==model.mu[14]+model.q[15]*(0)+model.q[16]*(0)+model.q[17]*(2)+model.q[18]*(0)+model.q[19]*(1)+model.q[20]*(-1)+model.q[7]*(0))
model.Constraint20= Constraint(expr = model.mu[20]==model.mu[15]+model.q[15]*(0)+model.q[16]*(0)+model.q[17]*(1)+model.q[18]*(1)+model.q[19]*(0)+model.q[20]*(0)+model.q[7]*(0))


# In[7]:


#firing constraints
model.Constraint21 = Constraint(expr = (-1)*model.mu[1]<=model.q[1]*(-1))
model.Constraint22 = Constraint(expr = (-1)*model.mu[2]<=model.q[1]*(-1))
model.Constraint23 = Constraint(expr = (-1)*model.mu[3]<=model.q[1]*(2))
model.Constraint24 = Constraint(expr = (-1)*model.mu[4]<=model.q[1]*(0))
model.Constraint25 = Constraint(expr = (-1)*model.mu[5]<=model.q[1]*(0))
model.Constraint26 = Constraint(expr = (-1)*model.mu[6]<=model.q[8]*(-1))
model.Constraint27 = Constraint(expr = (-1)*model.mu[7]<=model.q[8]*(-1))
model.Constraint28 = Constraint(expr = (-1)*model.mu[8]<=model.q[8]*(2))
model.Constraint29 = Constraint(expr = (-1)*model.mu[9]<=model.q[8]*(0))
model.Constraint30 = Constraint(expr = (-1)*model.mu[10]<=model.q[8]*(0))
model.Constraint31 = Constraint(expr = (-1)*model.mu[11]<=model.q[15]*(-1))
model.Constraint32 = Constraint(expr = (-1)*model.mu[12]<=model.q[15]*(-1))
model.Constraint33 = Constraint(expr = (-1)*model.mu[13]<=model.q[15]*(2))
model.Constraint34 = Constraint(expr = (-1)*model.mu[14]<=model.q[15]*(0))
model.Constraint35 = Constraint(expr = (-1)*model.mu[15]<=model.q[15]*(0))


# In[8]:


model.Constraint36 = Constraint(expr = (-1)*model.mu[1]<=model.q[2]*(0))
model.Constraint37 = Constraint(expr = (-1)*model.mu[2]<=model.q[2]*(1))
model.Constraint38 = Constraint(expr = (-1)*model.mu[3]<=model.q[2]*(-1))
model.Constraint39 = Constraint(expr = (-1)*model.mu[4]<=model.q[2]*(0))
model.Constraint40 = Constraint(expr = (-1)*model.mu[5]<=model.q[2]*(0))
model.Constraint41 = Constraint(expr = (-1)*model.mu[6]<=model.q[9]*(0))
model.Constraint42 = Constraint(expr = (-1)*model.mu[7]<=model.q[9]*(1))
model.Constraint43 = Constraint(expr = (-1)*model.mu[8]<=model.q[9]*(-1))
model.Constraint44 = Constraint(expr = (-1)*model.mu[9]<=model.q[9]*(0))
model.Constraint45 = Constraint(expr = (-1)*model.mu[10]<=model.q[9]*(0))
model.Constraint46 = Constraint(expr = (-1)*model.mu[11]<=model.q[16]*(0))
model.Constraint47 = Constraint(expr = (-1)*model.mu[12]<=model.q[16]*(1))
model.Constraint48 = Constraint(expr = (-1)*model.mu[13]<=model.q[16]*(-1))
model.Constraint49 = Constraint(expr = (-1)*model.mu[14]<=model.q[16]*(0))
model.Constraint50 = Constraint(expr = (-1)*model.mu[15]<=model.q[16]*(0))


# In[9]:


model.Constraint51 = Constraint(expr = (-1)*model.mu[1]<=model.q[3]*(-1))
model.Constraint52 = Constraint(expr = (-1)*model.mu[2]<=model.q[3]*(0))
model.Constraint53 = Constraint(expr = (-1)*model.mu[3]<=model.q[3]*(-1))
model.Constraint54 = Constraint(expr = (-1)*model.mu[4]<=model.q[3]*(2))
model.Constraint55 = Constraint(expr = (-1)*model.mu[5]<=model.q[3]*(1))
model.Constraint56 = Constraint(expr = (-1)*model.mu[6]<=model.q[10]*(-1))
model.Constraint57 = Constraint(expr = (-1)*model.mu[7]<=model.q[10]*(0))
model.Constraint58 = Constraint(expr = (-1)*model.mu[8]<=model.q[10]*(-1))
model.Constraint59 = Constraint(expr = (-1)*model.mu[9]<=model.q[10]*(2))
model.Constraint60 = Constraint(expr = (-1)*model.mu[10]<=model.q[10]*(1))
model.Constraint61 = Constraint(expr = (-1)*model.mu[11]<=model.q[17]*(-1))
model.Constraint62 = Constraint(expr = (-1)*model.mu[12]<=model.q[17]*(0))
model.Constraint63 = Constraint(expr = (-1)*model.mu[13]<=model.q[17]*(-1))
model.Constraint64 = Constraint(expr = (-1)*model.mu[14]<=model.q[17]*(2))
model.Constraint65 = Constraint(expr = (-1)*model.mu[15]<=model.q[17]*(1))


# In[10]:


model.Constraint66 = Constraint(expr = (-1)*model.mu[1]<=model.q[4]*(-3))
model.Constraint67 = Constraint(expr = (-1)*model.mu[2]<=model.q[4]*(0))
model.Constraint68 = Constraint(expr = (-1)*model.mu[3]<=model.q[4]*(0))
model.Constraint69 = Constraint(expr = (-1)*model.mu[4]<=model.q[4]*(0))
model.Constraint70 = Constraint(expr = (-1)*model.mu[5]<=model.q[4]*(1))
model.Constraint71 = Constraint(expr = (-1)*model.mu[6]<=model.q[11]*(-3))
model.Constraint72 = Constraint(expr = (-1)*model.mu[7]<=model.q[11]*(0))
model.Constraint73 = Constraint(expr = (-1)*model.mu[8]<=model.q[11]*(0))
model.Constraint74 = Constraint(expr = (-1)*model.mu[9]<=model.q[11]*(0))
model.Constraint75 = Constraint(expr = (-1)*model.mu[10]<=model.q[11]*(1))
model.Constraint76 = Constraint(expr = (-1)*model.mu[11]<=model.q[18]*(-3))
model.Constraint77 = Constraint(expr = (-1)*model.mu[12]<=model.q[18]*(0))
model.Constraint78 = Constraint(expr = (-1)*model.mu[13]<=model.q[18]*(0))
model.Constraint79 = Constraint(expr = (-1)*model.mu[14]<=model.q[18]*(0))
model.Constraint80 = Constraint(expr = (-1)*model.mu[15]<=model.q[18]*(1))


# In[11]:


model.Constraint81 = Constraint(expr = (-1)*model.mu[1]<=model.q[5]*(0))
model.Constraint82 = Constraint(expr = (-1)*model.mu[2]<=model.q[5]*(-1))
model.Constraint83 = Constraint(expr = (-1)*model.mu[3]<=model.q[5]*(0))
model.Constraint84 = Constraint(expr = (-1)*model.mu[4]<=model.q[5]*(1))
model.Constraint85 = Constraint(expr = (-1)*model.mu[5]<=model.q[5]*(0))
model.Constraint86 = Constraint(expr = (-1)*model.mu[6]<=model.q[12]*(0))
model.Constraint87 = Constraint(expr = (-1)*model.mu[7]<=model.q[12]*(-1))
model.Constraint88 = Constraint(expr = (-1)*model.mu[8]<=model.q[12]*(0))
model.Constraint89 = Constraint(expr = (-1)*model.mu[9]<=model.q[12]*(1))
model.Constraint90 = Constraint(expr = (-1)*model.mu[10]<=model.q[12]*(0))
model.Constraint91 = Constraint(expr = (-1)*model.mu[11]<=model.q[19]*(0))
model.Constraint92 = Constraint(expr = (-1)*model.mu[12]<=model.q[19]*(-1))
model.Constraint93 = Constraint(expr = (-1)*model.mu[13]<=model.q[19]*(0))
model.Constraint94 = Constraint(expr = (-1)*model.mu[14]<=model.q[19]*(1))
model.Constraint95 = Constraint(expr = (-1)*model.mu[15]<=model.q[19]*(0))


# In[12]:


model.Constraint96 = Constraint(expr = (-1)*model.mu[1]<=model.q[6]*(0))
model.Constraint97 = Constraint(expr = (-1)*model.mu[2]<=model.q[6]*(1))
model.Constraint98 = Constraint(expr = (-1)*model.mu[3]<=model.q[6]*(0))
model.Constraint99 = Constraint(expr = (-1)*model.mu[4]<=model.q[6]*(-1))
model.Constraint100 = Constraint(expr = (-1)*model.mu[5]<=model.q[6]*(0))
model.Constraint101 = Constraint(expr = (-1)*model.mu[6]<=model.q[13]*(0))
model.Constraint102 = Constraint(expr = (-1)*model.mu[7]<=model.q[13]*(1))
model.Constraint103 = Constraint(expr = (-1)*model.mu[8]<=model.q[13]*(0))
model.Constraint104 = Constraint(expr = (-1)*model.mu[9]<=model.q[13]*(-1))
model.Constraint105 = Constraint(expr = (-1)*model.mu[10]<=model.q[13]*(0))
model.Constraint106 = Constraint(expr = (-1)*model.mu[11]<=model.q[20]*(0))
model.Constraint107 = Constraint(expr = (-1)*model.mu[12]<=model.q[20]*(1))
model.Constraint108 = Constraint(expr = (-1)*model.mu[13]<=model.q[20]*(0))
model.Constraint109 = Constraint(expr = (-1)*model.mu[14]<=model.q[20]*(-1))
model.Constraint110 = Constraint(expr = (-1)*model.mu[15]<=model.q[20]*(0))


# In[13]:


model.Constraint111 = Constraint(expr = (-1)*model.mu[1]<=model.q[7]*(-5))
model.Constraint112 = Constraint(expr = (-1)*model.mu[2]<=model.q[7]*(1))
model.Constraint113 = Constraint(expr = (-1)*model.mu[3]<=model.q[7]*(0))
model.Constraint114 = Constraint(expr = (-1)*model.mu[4]<=model.q[7]*(0))
model.Constraint115 = Constraint(expr = (-1)*model.mu[5]<=model.q[7]*(0))
model.Constraint116 = Constraint(expr = (-1)*model.mu[6]<=model.q[14]*(-5))
model.Constraint117 = Constraint(expr = (-1)*model.mu[7]<=model.q[14]*(1))
model.Constraint118 = Constraint(expr = (-1)*model.mu[8]<=model.q[14]*(0))
model.Constraint119 = Constraint(expr = (-1)*model.mu[9]<=model.q[14]*(0))
model.Constraint120 = Constraint(expr = (-1)*model.mu[10]<=model.q[14]*(0))
model.Constraint121 = Constraint(expr = (-1)*model.mu[11]<=model.q[21]*(-5))
model.Constraint122 = Constraint(expr = (-1)*model.mu[12]<=model.q[21]*(1))
model.Constraint123 = Constraint(expr = (-1)*model.mu[13]<=model.q[21]*(0))
model.Constraint124 = Constraint(expr = (-1)*model.mu[14]<=model.q[21]*(0))
model.Constraint125 = Constraint(expr = (-1)*model.mu[15]<=model.q[21]*(0))


# In[14]:


SolverFactory('cplex').solve(model, tee=True)
model.display()
model.pprint()


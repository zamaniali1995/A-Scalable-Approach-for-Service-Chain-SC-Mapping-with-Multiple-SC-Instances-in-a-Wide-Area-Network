#Author: Ali Zamnai
#import random  ## to generate the items
# Import PuLP modeler functions
from pulp import * ## import pulp-or functions
#import pandas
import json
import numpy
#topo=pandas.read_csv('NSFNET.csv')
#chains=pandas.read_csv('chains.csv')
#prompt the user for a file to import
#lsfkjs
#%%
#class Pattern:
#    def __init__(self,placement,rout,userAssign):
#        self.assignment=placement
#        self.rout=rout
#        self.userAssign=userAssign
        
        
#%%	
class MasterProblem:
    def __init__(self, input):
        self.nodes=input['networkTopology'][0]['nodes']
#        self.functionslist=input['functions']
        self.nodesNum=len(self.nodes)
        self.links=input['networkTopology'][0]['links']
        self.chainNum=len(input['chains'])
        self.chainName=[input['chains'][i]['name'] for i in range(self.chainNum)]  
        self.functions=[input['chains'][i]['functions'] for i in range(self.chainNum)] 
        self.users=[input['chains'][i]['users'] for i in range(self.chainNum)]
        self.traffic=[input['chains'][i]['traffic%'] for i in range(self.chainNum)]
#        for i in range(self.chainNum):
#            self.functionslist=self.functions
#            for j in range(self.functions[i]):
#%% init of placement matrix
        self.placement={} 
        for z,i in enumerate(self.chainName):
            self.placement[i]={}
            for x,j in enumerate(self.nodes):
                self.placement[i][j]={}
                for k in self.functions[z]:
                    if x==z:
                        self.placement[i][j][k]=1
                    else:
                        self.placement[i][j][k]=0
#%%init of routing matrix
        self.routing={}
        for i,j in enumerate(self.chainName):
            self.routing[j]={}
            for k,l in enumerate(self.functions[i]):
                if k == len(self.functions[i])-1:
                    break
                print(self.functions[i][k], self.functions[i][k+1])
                self.routing[j][(self.functions[i][k], self.functions[i][k+1])]=\
                
        print("space")
        for key in self.routing:
            print(self.routing[key].values())
            break

        self.patterns={}
#        self.placement=[{self.nodes[0]:{}},{self.nodes[1]:(0,0,0,0,0)}]
#        self.routing=
#        self.userassin=
#        self.initialPatterns=initialPatterns
        for i in self.chainName:
            self.patterns[i]=[]
            for j in range(1):
              self.patterns[i].append({('pattern',j):(self.placement[i],1,1)})
        self.patSelect_vars = LpVariable.dict("patSelect",[])      
        self.prob = LpProblem('ColumnGeneration',LpMinimize)	# set up the problem
        self.obj = LpConstraintVar("obj")   # generate a constraint variable that will be used as the objective
        self.prob.setObjective(self.obj)
        self.PatternVars=[]
        self.constraintList=[]   # list to save constraint variables in
#        self.prob += lpSum([ingredient_vars[i] for i in Ingredients]) == 1, "PercentagesSum"
#        self.PatternVars=LpVariable.dict("P"+str(i)+str(j) for i in range(self.chainNum)	, 0, None, LpContinuous)  # create decision variable: will determine how often pattern x should be produced
#          self.PatternVars.append(var)
#        The objective function is added to ’self.prob’ first
        self.prob += lpSum([])
#        self.obj = LpConstraintVar("obj")   # generate a constraint variable that will be used as the objective
#        self.prob.setObjective(self.obj)
#		
#        self.PatternVars=[]
#        self.constraintList=[]   # list to save constraint variables in
#        for i,x in enumerate(self.chainName):		# create variables & set the constraints, in other words: set the minimum amount of items to be produced
#          var=LpConstraintVar("C"+str(i),LpConstraintGE,x)  # create constraintvar and set to >= demand for item
#          self.constraintList.append(var)
#          self.prob+=var
#		
			
#        for i,x in enumerate(self.initialPatterns):  #save initial patterns and set column constraints 
#          temp=[]
#          for j,y in enumerate(x):
#            if y>0: 
#              temp.append(j)
#          var=LpVariable("P"+str(i)	, 0, None, LpContinuous, lpSum(self.obj+[self.constraintList[v] for v in temp]))  # create decision variable: will determine how often pattern x should be produced
#          self.PatternVars.append(var)
#		
#		
#		
#	def solve(self):
#		self.prob.writeLP('prob.lp')
#		self.prob.solve()  # start solve
#		
#		return [self.prob.constraints[i].pi for i in self.prob.constraints]
#		
#			
#		
#	def addPattern(self,pattern):  # add new pattern to existing model
#		
#		self.initialPatterns.append(pattern)
#		temp=[]
#		
#		for j,y in enumerate(pattern):
#			if y>0: 
#				temp.append(j)
#		
#		var=LpVariable("Pat"+str(len(self.initialPatterns))	, 0, None, LpContinuous, lpSum(self.obj+[pattern[v]*self.constraintList[v] for v in temp]))
#		self.PatternVars.append(var)
#		
#	
#	def startSlave(self,duals):  # create/run new slave and return new pattern (if available)
#		
#		newSlaveProb=SlaveProblem(duals,self.itemLengths,self.maxValue)
#				
#		pattern=newSlaveProb.returnPattern()
#		return pattern
#		
#	def setRelaxed(self,relaxed):  # if no new patterns are available, solve model as IP problem
#		if relaxed==False:
#			for var in self.prob.variables():
#				var.cat = LpInteger
#			
#	def getObjective(self):
#		return value(self.prob.objective)
#		
#	def getUsedPatterns(self):
#		usedPatternList=[]
#		for i,x in enumerate(self.PatternVars):
#			if value(x)>0:
#				usedPatternList.append((value(x),self.initialPatterns[i]))
#		return usedPatternList
##%%
#		
#class SlaveProblem:
#    def __init__(self,duals, itemLengths,maxValue):
#        self.slaveprob=LpProblem("Slave solver",LpMinimize)
#        self.varList=[LpVariable('S'+str(i),0,None,LpInteger) for i,x in enumerate(duals)]
#        self.slaveprob+=-lpSum([duals[i]*x for i,x in enumerate(self.varList)])  #use duals to set objective coefficients
#        self.slaveprob+=lpSum([itemLengths[i]*x for i,x in enumerate(self.varList)])<=maxValue 
#
#        self.slaveprob.writeLP('slaveprob.lp')
#        self.slaveprob.solve() 
#        self.slaveprob.roundSolution() #to avoid rounding problems
#
#        
#
#    def returnPattern(self):
#        pattern=False
#        if value(self.slaveprob.objective) < -1.00001:
#            pattern=[]
#            for v in self.varList:
#                pattern.append(value(v))
#        return pattern
	
#%%	main 	
#random.seed(2012)
with open("input.json", "r") as read_file:
    input = json.load(read_file)

#nrItems=5
#lengthSheets=20


#itemLengths=[]
#itemDemands=[]

#while len(itemLengths)!=nrItems:
#	length=random.randint(5, lengthSheets-2)
#	demand=random.randint(5, 100)
#	if length not in itemLengths:
#		itemLengths.append(length)
#		itemDemands.append(demand)
	
#print ("Item lengts  : %s" % itemLengths)
#print ("Item demands : %s\n\n" % itemDemands)


patterns=[]
print ("Generating start patterns:")
#print (input)
## generate simple start patterns
#placement=[1,]
#rout=
#userAssig=
#for x in range(nrItems):
#	temp=[0.0 for y in range(x)]
#	temp.append(1.0)
#	temp+=[0.0 for y in range(nrItems-x-1)]
#	patterns.append(temp)
#	print (temp)


#print ("\n\nTrying to solve problem")
CGprob=MasterProblem(input)
#print (CGprob.placement)
a=CGprob.placement
#print (CGprob.functions)
#print (CGprob.traffic)
#print (CGprob.users[0])
#	
#relaxed=True
#while relaxed==True:   # once no more new columns can be generated set relaxed to False
#	duals=CGprob.solve()
#	
#	newPattern=CGprob.startSlave(duals)
#	
#	print ('New pattern: %s' % newPattern)
#	
#	if newPattern:
#		CGprob.addPattern(newPattern)
#	else:
#		CGprob.setRelaxed(False)
#		CGprob.solve()
#		relaxed=False
#
#print ("\n\nSolution: %s sheets required" % CGprob.getObjective())
#
#t=CGprob.getUsedPatterns()
#for i,x in enumerate(t):
#	print ("Pattern %s: selected %s times	%s" % (i,x[0],x[1]))

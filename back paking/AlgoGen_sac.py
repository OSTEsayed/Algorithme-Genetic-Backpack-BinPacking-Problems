
import numpy as np 
import random
"""
[Start] Generate random population of n chromosomes (suitable solutions for the problem
[Fitness] Evaluate the fitness f(x) of each chromosome x in the population
[Test](in my case i didn't put conditions) If the end condition is satisfied, stop and return the population. If not, generate a new population.
[New population] Create a new population by repeating following steps until the new population is complete:
    [Selection] Select two parent chromosomes from a population according to their fitness (the better fitness, the bigger chance to be selected)
    [Crossover] With a crossover probability cross over the parents to form a new offspring (children). If no crossover was performed, offspring is an exact copy of parents.
    [Mutation] With a mutation probability mutate new offspring at each locus (position in chromosome).
    [Accepting] Place new offspring in a new population
[Replace] Use new generated population for a further run of algorithm
[Loop] Go to the Fitness step
"""
def Read_Args(data_set):            #Read The max Capacity of our "Sac A Dos"  ,Read The Weight of each product , Read The Profit of each product
    global Capacity,Objects_profits,Objects_weight,numbb      
    Capacity= np.loadtxt("po{}/p0{}_c.txt".format(data_set,data_set))
    Objects_weight=np.loadtxt("po{}/p0{}_w.txt".format(data_set,data_set))
    # np.loadtxt("po4/p04_s.txt)")
    Objects_profits=np.loadtxt("po{}/p0{}_p.txt".format(data_set,data_set))
    numbb=np.shape(Objects_weight)[0]               #this is the number of prodcut we got or in outher word the size of each chromosom

def Test_for_The_Capacity_contrainte(The_chromo):       #test if the sum of products Respect The max Capacity of "Sac A dos" 
    new_Capacity=np.dot(Objects_weight,The_chromo)      #The object accepted in the "The_chrome" have the value "1" we Multiply it with it's Weight Value in "Object_weight"And calculate the sum Of all products
    if (new_Capacity>Capacity):
        return False
    return True
def check_the_Capacity_for_each_chromo(Population):         # for checking the capacity for the final population to see if wich of the chromo  have the best capacity and best ones 
    List_of_width=[]
    for chromo in Population:
        List_of_width.append(np.dot(Objects_weight,chromo))
    return np.asarray(List_of_width)
def Generate_Population(number_chromo,data_set):             #The First Giniration We Randomly Select for the First Population we have
    Read_Args(data_set)                                             #the Data We Get (see The Read_args Comontaire)                                                  
    pop=[]                                          #List to add the population(chromosoms) we goona create 
    numberofInstict=np.shape(Objects_weight)[0]             #number of Instict(Product) 
    while number_chromo !=0:                                #repeat untile We Get N Valide Chromosom For our population
        chromo =np.zeros(numberofInstict)                   #intiale the Chromosom by all 0 [0.0.0.0...]
        for j in range(numberofInstict):                     #change The Insticit of the chromosome Randomly [0.1]
            chromo[j]=random.randint(0,1)                   
        if  Test_for_The_Capacity_contrainte(chromo):           #(check the test For capacity contaraint Comntair above)
            pop.append(chromo)                                  #if its valide we add it in the population
            number_chromo-=1
    pop=np.asarray(pop)                         #we change the list to numpay array for simplifying the affichage and the manupulation 
    return pop
def Evalute_Fittness_of_population(Population):     #Evaluate Each chromosom in the population and append the reasault in a list

    Evaluate_list=[]                                #list of evaluated chromo
    for chrom in Population:
        Evaluate_list.append(np.dot(Objects_profits,chrom))         #For each prodoct [1] in the chromo we multiply it by the  profit  and calculate the sum of them
    return np.asarray(Evaluate_list)                  #we change the list to numpay array for simplifying the affichage and the manupulation        

def Selection_with_probabilty(Population,Evaluate_list):        #SElection and Crossover and mutation staps
    half=int((np.shape(Objects_weight)[0] )/2 )          #The position that we gonna crossover for each child in this case it's the half 
    new_pop=[]                                  
    used=[]                             #
    ss=np.sum(Evaluate_list)
    for i in range(len(Population)):
        Evaluate_list[i]=Evaluate_list[i]/ss            #Give Each Parent his Propabilty {The Best and higher his fittnes the higher chances he got}
    while (len(Population)-len(used) > 1):              #repeat untile we use all the Fathers to creat new childs...

        first=np.random.choice(np.arange(0, len(Population)), p=Evaluate_list) # chose the first father{The Best and higher his fittnes the higher chances he got}
        if first  in used:
            while first in used :
                first=np.random.choice(np.arange(0, len(Population)), p=Evaluate_list)  #make sure we didn't already used this father
        used.append(first)
        second=first                                      
        while second ==first:
            second=np.random.choice(np.arange(0, len(Population)), p=Evaluate_list)   #chose the second father{The Best and higher his fittnes the higher chances he got}
        used.append(second)

        child1=np.concatenate((Population[first][0:half],Population[second][half:]),axis=0)             #for the first child First Half From First Father Second Half From the second father 
        mut=random.randint(0, np.shape(Objects_weight)[0]-1)                  #randomly chose the first point for mutation
        mut2=random.randint(0, np.shape(Objects_weight)[0]-1)                 #randomly chose the second point for mutation
        temp=child1[mut]
        child1[mut]=child1[mut2]
        child1[mut2]=temp                                   #The mutation for the first child

        if  Test_for_The_Capacity_contrainte(child1):           #Test if this child is valide and Respect The Capacity of "Sac A dos"
                new_pop.append(child1)
        child2=np.concatenate((Population[second][0:half],Population[first][half:]),axis=0)             #do The Same for second child with changing the halfs of the parent's
     
        temp=child2[mut]
        child2[mut]=child2[mut2]
        child2[mut2]=temp
        if  Test_for_The_Capacity_contrainte(child2):
                new_pop.append(child2)
    new_pop=np.asarray(new_pop)
    return new_pop
  
def Get_the_new_population(Poupulation,Population_evaluation,Child_population):         #Evaluate All the child than generate the new population with only the best Fathers and childs  
    Child_evaluation=Evalute_Fittness_of_population(Child_population)           
    All_the_population=np.concatenate((Poupulation,Child_population),axis=0) 
    Max_allowed=np.shape(Poupulation)[0]                #the max Number allowed for the new population (the same size of the old population)
    List_of_Evaluation=np.concatenate((Population_evaluation,Child_evaluation),axis=0) 
    all_the_population = [x for (y,x) in sorted(zip(List_of_Evaluation,All_the_population),key=lambda pair: pair[0],reverse=True)]   #sort the best Chromosoms "Fathers and sons"
    all_the_population=np.asarray(all_the_population)    #we change the list to numpay array for simplifying the affichage and the manupulation            
    all_the_population=all_the_population[:Max_allowed]     #keep only the first Allowed in the new populations
    return all_the_population
Tableu_Prefernce=[]             #Just for Saving result purpuse    
data_set=int(input("chose The Data set (chose betwen 4,7,8):"))
Size_Of_The_Population = int(input("Enter the Size Of The Population:"))
pop=Generate_Population(Size_Of_The_Population,data_set)         #The First Population 
Tableu_Prefernce.append(pop)
Number_of_itiration=int(input("Enter The Number Of itiration you want:"))
for i in range(Number_of_itiration):
    eva=Evalute_Fittness_of_population(pop)             #Evaluate the population
    eva_garder=eva.copy()
    new_pop=Selection_with_probabilty(pop,eva)          #Selection,Crossover ,Mutation
    pop=Get_the_new_population(pop,eva_garder,new_pop)  #The new Population


print("the first Population (Randomly Generated): \n",Tableu_Prefernce[0])
print("The Capacity of the 'Sac A Dos':",Capacity)
print("The Size Of population {} , The number of itiration {} ".format(Size_Of_The_Population,Number_of_itiration))
print("The Last Population (The Best Population): \n",pop)
eva=np.asarray(Evalute_Fittness_of_population(pop))
print("The Profits for each Chromos(by order):\n",eva)
listof_width=check_the_Capacity_for_each_chromo(pop)
print("The Weight of all the Products(for each chromosom(each solution by order)):\n",listof_width)

import random
import numpy as np
dataset={
    "p01":[100,[70,60,50,33,33,33,11, 7, 3]],
    "p02":[100,[99,94,79,64,50,46,43,37,32,19,18, 7,6,3]],
    "p04":[524,[442,252,252,252,252,252,252,252,127,127,127,127,127,106,106,106,106,85,84,46,37,37,12,12,12,10,10,10,10,10,10,9,9]]
}
#ki t7abo tkhdmo b dataset mbedla expl p02 :wayn telga p01 ltaht eglboha p02
def test_contraint(chromo): #bah ntastiw l contraint tal capacity tales bin bah ascou na9blo l chromosom ou nn 
    for i in range(len(chromo)):
        tem=0                       
        for j in range(len(chromo)):    #Lkool bin nejm3o lwazen tales produit les fl bin adak kool  lkan fato l capacity nraj3o false (mach ma9bol)
            if chromo[i]==chromo[j]:
                tem=tem+dataset["p01"][1][j]                
        if tem > dataset["p01"][0]:         #hay lahna g3d ntastiw lkn fatet lcapacity
            return False
    return True                 #lkan les bin kool madepassawch les produit tahom lcapacity rj3na true (ma9boul)
def making_the_suit_ofbins_correct(chromo):     #adi lfunction ki ngeniriw les chromosom lowala mdayrin 3adad les bin how ged 3adad les produit kichgoul abcha3 i7timal whow rah ykhyr randomly apres 9ader yesotiw 3adad ta bin(expml 9ader tji hk 5 1 2 (wysoti lbin 3 w 4 )) hna normaliziwhm bah yjiw betartib (3 1 2) psk n7tajo l3adad tales bin fl function objectife
    tem=1
    tem2=1
    for i in range(len(dataset["p01"][1])):
            for j in range (len(dataset["p01"][1])):
                if chromo[j]==tem:
                    for r in range (len(dataset["p01"][1])):
                        if chromo[r]==tem:
                            chromo[r]=tem2
                    tem2=tem2+1
                    break
            tem=tem+1
    return chromo 
def evaluate_pop(population):   #hna nevalue kola chromosom (evaluation simple tkon egal 3adad tales bin li 3ndo )exmpl 3ndo 5 bin les evaluation ta3o 5 (ged matkon sghir ged makhir)
    evaluated_list=[]
    for i in range(len(population)):    #for les chromosom kool les fl population (ps : 3ambali complexity ta3o lcode hek twila bsh kadetni ndir solution khlaf gasro brk)
        max=1
        for j in range(len(population[i])):
            if population[i][j]>max:
                max=population[i][j]
        evaluated_list.append(max)
    return evaluated_list



    #hna yebda lcode yakhdem kima golt  lfoug derna max 3adad tales bin how 3adad tales produit (worst exmpl kola produit fi bin)
Max_number_of_bin_possible=len(dataset["p01"][1])
#generate_first_population
#
taill_of_population=10

population=[]           #nebdaw bl pupulation fargha 
while taill_of_population>0:    #n3mrouha b3adad tales chromosom
    chromo=[]
    for i in range(len(dataset["p01"][1])): #n7ato kola gane wla kola produit fi bin aleator
            chromo.append(random.randint(1,Max_number_of_bin_possible))                 
    if test_contraint(chromo) :             #ntestiw kima golna lfog lcontraint a9ray lcomontair li fl function
        chromo=making_the_suit_ofbins_correct(chromo) #a9ray lcomontair tal function lfog
        population.append(chromo)           #Yajoute lchromosom ida accptinah fl population
        taill_of_population=taill_of_population-1
Referenc=[]
Referenc.append(population) #n7tajouha mb3d fl affichage bah naffichiw lpopulation lowla khlah li khayrnaha
Referenc.append(evaluate_pop(population))

for j in range(100):            #number de giniration lhna n7ato gedah nitaration 7abin
    Evaluate_list=evaluate_pop(population)      #evalue kola chromosom fl population wnhatoha fi list
    
    #The Selection par Roullets 
    Placment_croisment=int((len(dataset["p01"][1]) )/2 )          #The position wayn 7andiro lcrosiment leles child mba3d derto fe nos kil3ada 
    new_pop=[]                      #hna wayn 7ato les child m3a lakher ki naaccptiwhm                   
    List_of_parents=[]                           #list bles parant n7atohm fiha ki nest3mloouhm bah man3awdouch nest3mlouhm
    ss=np.sum(Evaluate_list)            #bah ndiro lprobability ta3hom n7tajo la soum tal evaluation ta kola chromosom fl population
    for i in range(len(population)):
        Evaluate_list[i]=1/(Evaluate_list[i]/ss)          #Give Each Parent his Propabilty {a9al wa7d 3ndo des bin 3ndo  higher chances fe roullet}
    smallest_prob = min(Evaluate_list)                          #adom 3stora li mltht kol n7tajouhm bah neglbo asghar wa7d fles bin 3ando propability ktar 
    Evaluate_list = [p/smallest_prob for p in Evaluate_list]    #char7 : ndirou asghr wahd probaility ta3o =1 mb3d neglbo loukhrin relative lel1 ada apres normaliziw les valeur ta3hom bah ykon jam3 ta3hom egal a 1  
    Evaluate_list = [p/sum(Evaluate_list) for p in Evaluate_list]


    while (len(population)-len(List_of_parents) > 1):              #repeat untile we use all the Fathers to creat new childs...

        parent1=np.random.choice(np.arange(0, len(population)), p=Evaluate_list) # chose the first father{The Best and higher his fittnes the higher chances he got}
        if parent1  in List_of_parents:
            while parent1 in List_of_parents :
                parent1=np.random.choice(np.arange(0, len(population)), p=Evaluate_list)  #make sure we didn't already used this father
        List_of_parents.append(parent1)
        parent2=parent1                                      
        while parent2 ==parent1:
            parent2=np.random.choice(np.arange(0, len(population)), p=Evaluate_list)   #chose the second father{The Best and higher his fittnes the higher chances he got}
        List_of_parents.append(parent2)

        new_born1=np.concatenate((population[parent1][0:Placment_croisment],population[parent2][Placment_croisment:]),axis=0)             #for the first child First Half From First Father Second Half From the second father 
        mutation_point1=random.randint(0, len(dataset["p01"][1])-1)                  #randomly chose the first point for mutation
        mutation_point2=random.randint(0,len(dataset["p01"][1])-1)                 #randomly chose the second point for mutation
        temp=new_born1[mutation_point1]
        new_born1[mutation_point1]=new_born1[mutation_point2]
        new_born1[mutation_point2]=temp                                   #The mutation for the first child

        if  test_contraint(new_born1):           #Test if this child is valide and Respect The Capacity of "the bins "
                new_pop.append(new_born1)
        new_born2=np.concatenate((population[parent2][0:Placment_croisment],population[parent1][Placment_croisment:]),axis=0)             #do The Same for second child with changing the halfs of the parent's
        
        temp=new_born2[mutation_point1]
        new_born2[mutation_point1]=new_born2[mutation_point2]
        new_born2[mutation_point2]=temp
        if  test_contraint(new_born2):
                new_pop.append(new_born2)

    #bora makmlna les croisment w wlmutation tales parent kool khourjetna lista tales childs             
    new_pop=np.asarray(new_pop)                         #adi lista tal child 
    Child_evaluation=evaluate_pop(new_pop)              #nevaluwihm kol
    Evaluate_list=evaluate_pop(population)              #n3awdo nrecupuriw les evaluation tales parent
    if (np.shape(new_pop)[0]>0):                         #ndiro population jdida fiha les parent wles childs 
        All_the_population=np.concatenate((population,new_pop),axis=0)  #adi ay condition 3ajal bah mayou9a3ch erour kon tkon list tales child egal a 0 bah mayesrach errore
    else : All_the_population=population            #adi lkn list tales child fargha macciptina 7ata enfent nkhliw ghir tales parent
    Max_allowed=np.shape(population)[0]                #the max Number allowed for the new population (the same size of the old population)
    List_of_Evaluation=np.concatenate((Evaluate_list,Child_evaluation),axis=0)  #nlemo les evaluate ta3hom fi zoz bah nratbohom 3la 7sab levaluation ta3hom
    all_the_population = [x for (y,x) in sorted(zip(List_of_Evaluation,All_the_population),key=lambda pair: pair[0],reverse=False)]   #sort the best Chromosoms "Fathers and sons"
    all_the_population=np.asarray(all_the_population)    #we change the list to numpay array for simplifying the affichage and the manupulation            
    all_the_population=all_the_population[:Max_allowed]     #nkhaliw ghir lmla7 hasb la taille tal population li khayrnaha lowla 
    population=all_the_population
    


#affichage ta resultat ta3na :(population lowla : levalation ta3ha wlpopulation wlevaluation ta3ha:)

print("the first Popuation :")
print(np.asarray(Referenc[0]))
print("the Evaluation for each chromosom in the population :")
print(np.asarray(Referenc[1]))
print("the last Population (results):")
print(np.asarray(population))
print("the evaluation of the last population:")
print(np.asarray(evaluate_pop(population)))

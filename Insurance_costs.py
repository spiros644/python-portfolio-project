import csv
with open("insurance.csv", newline="") as insurance_file:
    reader = csv.DictReader(insurance_file)
    age = []
    bmi = []
    sex = []
    children = []
    smoker = []
    region = []
    charges = []
    for row in reader:
        age.append(row['age'])
        bmi.append(row['bmi'])
        sex.append(row['sex'])
        children.append(row['children'])
        smoker.append(row['smoker'])
        region.append(row['region'])
        charges.append(row['charges'])

# Function to find the average age of patients on the dataset.

    def average_age(age):
        total = 0
        ages = 0
        for i in age:
            total += 1
            ages = ages+int(i)
        average = ages/total
        return f"The average age of patients is : {average}"
    print(average_age(age))

# Function for to find where are from the most people.

    def most_region():

        dict_reg = {}
        dict_reg["southwest"] = region.count("southwest")
        dict_reg["southeast"] = region.count("southeast")
        dict_reg['northeast'] = region.count("northeast")
        dict_reg['northwest'] = region.count("northwest")
        print(dict_reg)
        maxcount = max(dict_reg, key=dict_reg.get)
        return f"The majority of people are from the {maxcount}"
    print(most_region())

# Function to find the average insurance costs.
    charges = list(map(float, charges))
    def average_costs(charges):
        total = 0
        for value in charges:
            total += value
        average_cost = total / len(charges)
        return f"The average insurance cost for all patients is : {average_cost}"
    print(average_costs(charges))

# Function to estimate insurance cost for smokers patients and non-smoker
    def smoker_insurance(smoker, charges):
        smokers = []
        non_smokers = []
        smoker_costs = list(zip(smoker, charges))
        for i,j in smoker_costs:
            if i == "yes":
                smokers.append(j)
            else:
                non_smokers . append(j)
        return f"The difference between all smokers and non-smokers in charges is : {sum(non_smokers)-sum(smokers)}"

    print(smoker_insurance(smoker, charges))

# Figure out what the average age is for someone who has at least one child.



#Function that calculates the number of males and females in insurance .csv

    def sexes(sex):
        male=0
        female=0
        for i in sex:
            if i=='female':
                female +=1
            elif i =='male':
                male +=1
        return f"The numbers of female patients is {female} and {male} males."
    print(sexes(sex))

#Function to find the unique region the patients are from.
    def regions(region):
        unique=[]
        for i in region:
            if i not in unique:
                unique.append(i)
        return unique

    print(regions(region))

#Function to create a dictionary with all patients information.

    def dict():
        patients_dict={}
        patients_dict["age"]=[ages for ages in age]
        patients_dict["sex"] = [sexes for sexes in sex]
        patients_dict["bmi"] = [bmis for bmis in bmi]
        patients_dict["children"] = [childrens for childrens in children]
        patients_dict["smoker"] = [smokers for smokers in smoker]
        patients_dict["regions"] = [regions for regions in region]
        patients_dict["charges"] = [charge for charge in charges]
        print(patients_dict)
    dict()




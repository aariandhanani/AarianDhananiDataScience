#Aarian Dhanani

age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0



insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
print("This person has an insurance cost of " + str(insurance_cost) + " dollars.")



age += 4
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
print("This person has a new insurance cost of " + str(new_insurance_cost) + " dollars.")
change_in_insurance_cost = new_insurance_cost - insurance_cost;
print("The change in the cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")



age = 28
bmi += 3.1
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost;
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")



bmi = 26.2
sex = 1
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost;
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")



sex = 0
smoker = 1
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost;
print("The change in estimated cost for being a smoker is " + str(change_in_insurance_cost) + " dollars.")



smoker = 0
num_of_children = 10
new_insurance_cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * num_of_children) + (24000 * smoker) - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost;
print("The change in estimated cost for having 10 children instead of 3 is " + str(change_in_insurance_cost) + " dollars.")
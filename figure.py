#getting the inputs
caloriesa = input('How many calories did you burn: ')
activea = input("How many minutes of activity did you do?: ")
stepsa = input('How many hours of stand?: ')
#creating the formulas
calories = int(caloriesa) / 100 * 10
active = int(activea) + 40 
steps = int(stepsa) + 88
#getting the final steps
score = (calories + active + steps) / 3
#printing the results
print('Your score is: ' + str(score))
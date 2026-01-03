def house_hunter():
  # Create a variable called annual_salary. Ask the user to
  # enter their salary and cast it to a float
  anual_salary = float(input("Enter your anual Salary: "))
  # TODO

  # Create a variable called portion_saved. Ask the user to
  # enter the portion of their salary to save and cast it to a float
  montlhy_salary = anual_salary/12
  portion_saved = float(input("Enter your portion of your salary you would like to save: "))
  # TODO

  # Create a variable called total_cost. Ask the user to
  # enter the cost of their dream homeand cast it to a float
  total_cost = float(input("Cost of the House of your dream: "))
  portion_down_payment = total_cost * 0.25 
  # TODO

  # Calulate the portion_down_payment (25% of total_cost)
  #portion_down_payment = total_cost * 0.25 # Leave this line

  # Annual Rate of Return (4%)
  r = 0.04 # Leave this line
  anual_return = anual_salary * r
  # Current Savings ($0)
  current_savings = 0.0 # Leave this line


  count = 0

  # Calculate the number of months
  while current_savings <= portion_down_payment:
    count+=1
    current_savings = current_savings + portion_saved * anual_salary/12
    
    print(f"${current_savings}")
  print(f"Total of {count} months until you buy your dream house")# 

if __name__ =="__main__":
  house_hunter()

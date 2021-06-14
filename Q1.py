import pandas as pd

data = pd.read_csv("data.csv") 

def Q1():
  print("\nQ1")
  print(data.head())
  print(data.tail())

def Q2():
  print("\nQ2")
  data.replace(to_replace=["?","na"],value="NaN")
  data.to_csv("data.csv")

def Q3():
  print("\nQ3")
  print(data.loc[data['company'] == 'volvo'])

def Q4():
  print("\nQ4")
  t = data.company.value_counts()
  print(t)

def Q5():
  print("\nQ5")
  group1 = data.groupby('company')
  max1 = group1.max()
  max2 = max1.reset_index()
  print(max2.filter(['company','price']))

def Q6():
  print("\nQ6")
  temp = data.groupby('company')
  temp1 = temp['company','average-mileage'].mean()
  print("\n")
  print(temp1)

def Q7():
  print("\nQ7")
  Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
  carPriceDf = pd.DataFrame.from_dict(Price)

  Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
  carsHorsepowerDf = pd.DataFrame.from_dict(Horsepower)

  carsDf = pd.merge(carPriceDf, carsHorsepowerDf, on="Company")
  print(carsDf)

Q1()
Q2()
Q3()
Q4()
Q5()
Q6()
Q7()






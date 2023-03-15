name = input("Hello, What's your name?\n")
print("Greetings to " + name+ " \nHope this mmessage finds you well \nHope I get selected for IEEE\nArshaan Iqbal\nRA2111003011319\nan9864@srmist.edu.in\nBelow I have used few NumPy Libraries"+ "!")
import pandas as pd 
import numpy as np

df = pd.read_csv("/Users/arshaaniqbal/Desktop/IEEE Recruitment Project/winequality-white.csv") 
print(df.head())
winequality_white = np.genfromtxt("/Users/arshaaniqbal/Desktop/IEEE Recruitment Project/winequality-white.csv", delimiter=';', skip_header=1)

ph = winequality_white[:,8]
mean_ph = np.nanmean(ph)
std_ph = np.nanstd(ph)
max_ph = np.nanmax(ph)
min_ph = np.nanmin(ph)

print("The average of the pH column is: ", mean_ph)
print("The standard deviation of the pH column is: ", std_ph)
print("The minimum pH in the pH column is:", min_ph)
print("The maximum pH in the pH column is:", max_ph)

alcohol = winequality_white[:,10]
print("The data type of values in the alcohol column is: ", alcohol.dtype)
print("The size of the alcohol column is: ", alcohol.size)
print("The itemsize of the alcohol column is:", alcohol.itemsize)

density = winequality_white[:,7]
array = np.arange(len(density)).reshape(79,62)
print("The shape of the array is: ", array.shape)
print("The array is: ", array)

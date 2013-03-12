#developed to combine text into one giant feature, process text to eliminate unnecessary components, make all lower case
import pandas as pd

#dataset with columns
train = pd.read_csv('/home/play/Example/Kaggle/Adzuna/Data/train3_11_3.csv')
train['Combined'] = ""

valid = pd.read_csv('/home/play/Example/Kaggle/Adzuna/PostMung/Data/valid3_11_3.csv')

count1 = 0
count2 = 0


  for x in train['Title']:
		x1 = x + train['NN'][count]
		x2 = x1 + train['NNP'][count]
		x3 = x2.lower()
		train['Combined'][count] = x3
		count1 += 1
	trainnew = train.drop(['Title', 'NN', 'NNP'], axis=1)
	trainnew.to_csv('home/play/Example/Kaggle/Adzuna/Data/train3_12_3.csv')
	for x in valid['Title']:
		x1 = x + valid['NN'][count]
		x2 = x1 + valid['NNP'][count]
		x3 = x2.lower()
		valid['Combined'][count] = x3
		count2 += 1
	validnew = valid.drop(['Title', 'NN', 'NNP'], axis=1)
	validnew.to_csv('/home/play/Example/Kaggle/Adzuna/PostMung/Data/valid3_12_2.csv')

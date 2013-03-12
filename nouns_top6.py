import pandas as pd

new = pd.read_csv('/Users/williamshelton/Downloads/train3_11_1.csv')
count = 0
new['EngineerNouns'] = "blank"
new['AccountingNouns'] = "blank"
new['HealthcareNouns'] = "blank"
new['GeneralNouns'] = "blank"
new['ITNouns'] = "blank"
new['SalesNouns'] = "blank"
new['AllElse'] = "blank"

jobtypes = ['Engineering Jobs', 'HR & Recruitment Jobs', 'Accounting & Finance Jobs', 'Healthcare & Nursing Jobs', 'Other/General Jobs', 'Hospitality & Catering Jobs', 'IT Jobs',  'Customer Services Jobs', 'Travel Jobs', 'Sales Jobs', 'Manufacturing Jobs', 'Teaching Jobs', 'Creative & Design Jobs', 'Trade & Construction Jobs', 'Property Jobs', 'Admin Jobs', 'Legal Jobs', 'Retail Jobs', 'Consultancy Jobs', 'Energy, Oil & Gas Jobs', 'Logistics & Warehouse Jobs', 'PR', 'Advertising & Marketing Jobs', 'Charity & Voluntary Jobs', 'Scientific & QA Jobs', 'Maintenance Jobs', 'Domestic help & Cleaning Jobs', 'Social work Jobs', 'Graduate Jobs']

for x in new['Category']:
  if x == "Engineering Jobs":
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['EngineerNouns'][count] = newstring2
	elif x == 'Accounting & Finance Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['AccountingNouns'][count] = newstring2
	elif x == 'Healthcare & Nursing Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['HealthcareNouns'][count] = newstring2
	elif x == 'Other/General Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['GeneralNouns'][count] = newstring2
	elif x == 'IT Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['ITNouns'][count] = newstring2
	elif x == 'Sales Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['SalesNouns'][count] = newstring2
	else:
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['AllElse'][count] = newstring2
	count +=1

new.to_csv('/Users/williamshelton/Downloads/train3_11_2.csv')
	

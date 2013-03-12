import pandas as pd

new = pd.read_csv('/Users/williamshelton/Downloads/train3_11_1.csv')
count = 0
new['EngineerNouns'] = "blank"
new['HRNouns'] = "blank"
new['AccountingNouns'] = "blank"
new['HealthcareNouns'] = "blank"
new['GeneralNouns'] = "blank"
new['HospitalityNouns'] = "blank"
new['ITNouns'] = "blank"
new['CustomerNouns'] = "blank"
new['TravelNouns'] = "blank"
new['SalesNouns'] = "blank"
new['ManufacturingNouns'] = "blank"
new['TeachingNouns'] = "blank"
new['CreativeNouns'] = "blank"
new['TradeNouns'] = "blank"
new['PropertyNouns'] = "blank"
new['AdminNouns'] = "blank"
new['LegalNouns'] = "blank"
new['RetailNouns'] = "blank"
new['ConsultancyNouns'] = "blank"
new['EnergyNouns'] = "blank"
new['LogisticsNouns'] = "blank"
new['AdvertisingNouns'] = "blank"
new['CharityNouns'] = "blank"
new['ScientificNouns'] = "blank"
new['MaintenanceNouns'] = "blank"
new['DomesticNouns'] = "blank"
new['SocialNouns'] = "blank"
new['GraduateNouns'] = "blank"
jobtypes = ['Engineering Jobs', 'HR & Recruitment Jobs', 'Accounting & Finance Jobs', 'Healthcare & Nursing Jobs', 'Other/General Jobs', 'Hospitality & Catering Jobs', 'IT Jobs',  'Customer Services Jobs', 'Travel Jobs', 'Sales Jobs', 'Manufacturing Jobs', 'Teaching Jobs', 'Creative & Design Jobs', 'Trade & Construction Jobs', 'Property Jobs', 'Admin Jobs', 'Legal Jobs', 'Retail Jobs', 'Consultancy Jobs', 'Energy, Oil & Gas Jobs', 'Logistics & Warehouse Jobs', 'PR', 'Advertising & Marketing Jobs', 'Charity & Voluntary Jobs', 'Scientific & QA Jobs', 'Maintenance Jobs', 'Domestic help & Cleaning Jobs', 'Social work Jobs', 'Graduate Jobs']

for x in new['Category']:
	if x == "Engineering Jobs":
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['EngineerNouns'][count] = newstring2
	elif x == 'HR & Recruitment Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['HRNouns'][count] = newstring2
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
	elif x == 'Hospitality & Catering Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['HospitalityNouns'][count] = newstring2
	elif x == 'IT Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['ITNouns'][count] = newstring2
	elif x == 'Customer Services Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['CustomerNouns'][count] = newstring2
	elif x == 'Travel Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['TravelNouns'][count] = newstring2
	elif x == 'Sales Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['SalesNouns'][count] = newstring2
	elif x == 'Manufacturing Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['ManufacturingNouns'][count] = newstring2
	elif x == 'Teaching Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['TeachingNouns'][count] = newstring2
	elif x == 'Creative & Design Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['CreativeNouns'][count] = newstring2
	elif x == 'Trade & Construction Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['TradeNouns'][count] = newstring2
	elif x == 'Property Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['PropertyNouns'][count] = newstring2
	elif x == 'Admin Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['AdminNouns'][count] = newstring2
	elif x == 'Legal Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['LegalNouns'][count] = newstring2
	elif x == 'Retail Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['RetailNouns'][count] = newstring2
	elif x == 'Consultancy Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['ConsultancyNouns'][count] = newstring2
	elif x == 'Energy, Oil & Gas Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['EnergyNouns'][count] = newstring2
	elif x == 'Logistics & Warehouse Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['LogisticsNouns'][count] = newstring2
	elif x == 'PR, Advertising & Marketing Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['AdvertisingNouns'][count] = newstring2
	elif x == 'Charity & Voluntary Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['CharityNouns'][count] = newstring2
	elif x == 'Scientific & QA Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['ScientificNouns'][count] = newstring2
	elif x == 'Maintenance Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['MaintenanceNouns'][count] = newstring2
	elif x == 'Domestic help & Cleaning Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['DomesticNouns'][count] = newstring2
	elif x == 'Social work Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['SocialNouns'][count] = newstring2
	elif x == 'Graduate Jobs':
		newstring = ""
		newstring1 = newstring + new['NN'][count]
		newstring2 = newstring1 + new['NNP'][count]
		new['GraduateNouns'][count] = newstring2
	count +=1

new.to_csv('/Users/williamshelton/Downloads/train3_11_2.csv')
	

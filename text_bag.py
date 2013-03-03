import pandas as pd

def main():
  new = pd.read_csv("/Users/williamshelton/Downloads/sample.csv")
	new['principal'] = 0
	new['senior'] = 0
	new['executive'] = 0
	new['assistant'] = 0
	new['analyst'] = 0
	new['manager'] = 0
	new['engineer'] = 0
	new['software'] = 0
	new['developer'] = 0
	new['job'] = 0
	new['nurse'] = 0
	new['consultant'] = 0
	new['support'] = 0
	count = 0
	for i in new.Title:
		if i == "":
			new['Title'][count] = 0
		else:
			t = i.lower()
			v = t.split(" ")
			if "principal" in v:
				new['principal'][count] = 1
			if "senior" in v:
			#u = new.index("principal")
				new['senior'][count] = 1
			if "executive" in v:
			#u = new.index("principal")
				new['executive'][count] = 1
			if "assistant" in v:
			#u = new.index("principal")
				new['assistant'][count] = 1
			if "analyst" in v:
			#u = new.index("principal")
				new['analyst'][count] = 1
			if "manager" in v:
			#u = new.index("principal")
				new['manager'][count] = 1
			if "engineer" in v:
			#u = new.index("principal")
				new['engineer'][count] = 1
			if "software" in v:
			#u = new.index("principal")
				new['software'][count] = 1
			if "developer" in v:
			#u = new.index("principal")
				new['developer'][count] = 1
			if "job" in v:
			#u = new.index("principal")
				new['job'][count] = 1
			if "nurse" in v:
			#u = new.index("principal")
				new['nurse'][count] = 1
			if "consultant" in v:
			#u = new.index("principal")
				new['consultant'][count] = 1
			if "support" in v:
			#u = new.index("principal")
				new['support'][count] = 1
	count+=1		
	new.to_csv("/Users/williamshelton/Downloads/tester1.csv")
	
if __name__=="__main__":
	main()

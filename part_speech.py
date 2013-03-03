from __future__ import division
import nltk, re, pprint
import pandas as pd

def main():
  new = pd.read_csv("tester1.csv")
	new['NN'] = "Hello"
	new['NNP'] = "Hello"
	new['NNS'] = "Hello"
	new['NNPS'] = "Hello"
	new['VB'] = "Hello"
	new['VBD'] = "Hello"
	new['VBG'] = "Hello"
	new['VBP'] = "Hello"
	new['VBP'] = "Hello"
	new['VBZ'] = "Hello"
	new['VBN'] = "Hello"
	new['JJ'] = "Hello"
	new['JJS'] = "Hello"
	new['JJR'] = "Hello"
	new['CC'] = "Hello"
	new['CD'] = "Hello"
	new['TO'] = "Hello"
	new['MD'] = "Hello"
	new['RB'] = "Hello"
	new['RBR'] = "Hello"
	new['RBS'] = "Hello"
	new['FW'] = "Hello"
	count = 0
	for x in new['FullDescription']:
		clean = []
		y = nltk.word_tokenize(x)
		y = [nltk.word_tokenize(a) for a in y]
		y = [nltk.pos_tag(a) for a in y]
		clean.append(y)
		for c in clean:
			nn = " "
			nnp = " "
			nns = " "
			nnps = " "
			vb = " "
			vbd = " "
			vbg = " "
			vbp = " "
			vbz = " "
			vbn = " "
			jj = " "
			jjs = " "
			jjr = " "
			cc = " "
			cd = " "
			to = " "
			md = " "
			rb = " "
			rbr = " "
			rbs = " "
			fw = " "
			for x in c:
				if x[0][1] == 'NN':
					nn = nn + " " + x[0][0]
			for x in c:
				if x[0][1] == 'NNP':
					nnp = nnp + " " + x[0][0]
			for x in c:
				if x[0][1] == 'NNS':
					nns = nns + " " + x[0][0]
			for x in c:
				if x[0][1] == 'NNPS':
					nns = nnps + " " + x[0][0]
			for x in c:
				if x[0][1] == 'VB':
					vb = vb + " " + x[0][0]
			for x in c:
				if x[0][1] == 'VBD':
					vbd = vbd + " " + x[0][0]
			for x in c:
				if x[0][1] == 'VBG':
					vbg = vbg + " " + x[0][0]
			for x in c:
				if x[0][1] == 'VBP':
					vbp = vbp + " " + x[0][0]
			for x in c:
				if x[0][1] == 'VBZ':
					vbz = vbz + " " + x[0][0]
			for x in c:
				if x[0][1] == 'VBN':
					vbn = vbn + " " + x[0][0]
			for x in c:
				if x[0][1] == 'JJ':
					jj = jj + " " + x[0][0]
			for x in c:
				if x[0][1] == 'JJS':
					jjs = jjs + " " + x[0][0]
			for x in c:
				if x[0][1] == 'JJR':
					jjr = jjr + " " + x[0][0]
			for x in c:
				if x[0][1] == 'CC':
					cc = cc + " " + x[0][0]
			for x in c:
				if x[0][1] == 'CD':
					cd = cd + " " + x[0][0]
			for x in c:
				if x[0][1] == 'TO':
					to = to + " " + x[0][0]
			for x in c:
				if x[0][1] == 'MD':
					md = md + " " + x[0][0]
			for x in c:
				if x[0][1] == 'RB':
					rb = rb + " " + x[0][0]
			for x in c:
				if x[0][1] == 'RBR':
					rbr = rbr + " " + x[0][0]
			for x in c:
				if x[0][1] == 'RBS':
					rbs = rbs + " " + x[0][0]
			for x in c:
				if x[0][1] == 'FW':
					fw = fw + " " + x[0][0]
			new['NN'][count] = nn
			new['NNP'][count] = nnp
			new['NNS'][count] = nns
			new['NNPS'][count] = nnps
			new['VB'][count] = vb
			new['VBD'][count] = vbd
			new['VBG'][count] = vbg
			new['VBP'][count] = vbp
			new['VBZ'][count] = vbz
			new['VBN'][count] = vbn
			new['JJ'][count] = jj
			new['JJS'][count] = jjs
			new['JJR'][count] = jjr
			new['CC'][count] = cc
			new['CD'][count] = cd
			new['TO'][count] = to
			new['MD'][count] = md
			new['RB'][count] = rb
			new['RBR'][count] = rbr
			new['RBS'][count] = rbs
			new['FW'][count] = fw
		count+=1
	new.to_csv("clean_wow.csv")

if __name__=="__main__":
	main()




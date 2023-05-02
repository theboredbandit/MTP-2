#creating processed dataset for TapData

from datetime import datetime
import csv

'''
Dataset Columns:

Sample id | Within office hour | Duration from office start | 
Duration from office end | Within office break hour | Duration from office break start | Duration from office break end |
Elapsed time from last reported 0 | Elapsed time from last reported 1 | Did the user report?

'''
# user_id=12
# file1 = open("BTP_Project-main/TapData/user_" + str(user_id)+"/_Tap_Label.txt","r")
# li=file1.readlines()
# print(li[0])
# entry=li[1].split(',')
# print(entry)


heading=['Sample id' ,'Within office hour' ,'Duration from office start' ,
'Duration from office end' , 'Within office break hour' , 'Duration from office break start' , 'Duration from office break end' ,
'Elapsed time from last reported 0' , 'Elapsed time from last reported 1' , 'Did the user report?']

def create_dataset(user_id, office_hour_start, office_hour_end, office_break_start, office_break_end): #all the times are datetime onjects in %H:%M:%S (24-hr) format
	file1 = open("BTP_Project-main/TapData/user_" + str(user_id)+"/_Tap_Label.txt","r")
	li=file1.readlines()

	dataset_valence=[heading]
	dataset_arousal=[heading]

	i=1
	last_valence=dict()
	last_arousal=dict()
	last_valence[0]=last_valence[1]=last_arousal[0]=last_arousal[1]=-1 #later these will be initialised to datetime objects
	time0=datetime.strptime("00:00:00", "%H:%M:%S")
	'''
	-> Use date and not just time to find the elapsed time 
	-> Convert time string into second values for the second column
	'''
	for item in li:
		entry=item.split(',')
		if len(entry)<=2:
			continue
		if entry[2]=='-99':
			continue
		sample_id=i
		i+=1
		prob_time=entry[1][11:-4]
		dt_obj = datetime.strptime(prob_time, "%H:%M:%S")
		within_office_hr="No"
		if dt_obj>office_hour_start and dt_obj<office_hour_end:
			within_office_hr="Yes"
		duration_from_office_start=abs((dt_obj-office_hour_start).total_seconds())
		duration_from_office_end=abs((dt_obj-office_hour_end).total_seconds())
		
		within_break_hr="No"
		if dt_obj>office_break_start and dt_obj<office_break_end:
			within_break_hr="Yes"
		duration_from_break_start=abs((dt_obj-office_break_start).total_seconds())
		duration_from_break_end=abs((dt_obj-office_break_end).total_seconds())

		#elapsed times from last reported emotion
		elapsed_time_valence=dict()
		elapsed_time_arousal=dict()
		elapsed_time_valence[0]=elapsed_time_valence[1]=elapsed_time_arousal[0]=elapsed_time_arousal[1]=-1

		dt_obj2=datetime.strptime(entry[1][2:-4], "%y-%m-%d %H:%M:%S")
		for j in range(2):			
			if last_valence[j]!=-1:
				elapsed_time_valence[j]=(dt_obj2 - last_valence[j]).total_seconds()
			if last_arousal[j]!=-1:
				elapsed_time_arousal[j]=(dt_obj2 - last_arousal[j]).total_seconds()				

		user_reported="No"
		time=abs((time0-dt_obj).total_seconds())
		
		row1_valence=[sample_id,within_office_hr,duration_from_break_start,duration_from_office_end,
						within_break_hr, duration_from_break_start, duration_from_break_end, 
						elapsed_time_valence[0], elapsed_time_valence[1], user_reported]
		
		row1_arousal=[sample_id,within_office_hr,duration_from_break_start,duration_from_office_end,
						within_break_hr, duration_from_break_start, duration_from_break_end, 
						elapsed_time_arousal[0], elapsed_time_arousal[1], user_reported]
		
		#creating second row corresponding to the response time
		sample_id=i
		i+=1
		response_time=entry[3][11:-5]
		#print(response_time)		
		dt_obj = datetime.strptime(response_time, "%H:%M:%S")
		
		within_office_hr="No"
		if dt_obj>office_hour_start and dt_obj<office_hour_end:
			within_office_hr="Yes"
		duration_from_office_start=abs((dt_obj-office_hour_start).total_seconds())
		duration_from_office_end=abs((dt_obj-office_hour_end).total_seconds())
		
		within_break_hr="No"
		if dt_obj>office_break_start and dt_obj<office_break_end:
			within_break_hr="Yes"
		duration_from_break_start=abs((dt_obj-office_break_start).total_seconds())
		duration_from_break_end=abs((dt_obj-office_break_end).total_seconds())

		#elapsed times from last reported emotion
		elapsed_time_valence[0]=elapsed_time_valence[1]=elapsed_time_arousal[0]=elapsed_time_arousal[1]=-1

		#print(entry[3][2:-5])
		dt_obj2=datetime.strptime(entry[3][2:-5], "%y-%m-%d %H:%M:%S")
		for j in range(2):			
			if last_valence[j]!=-1:
				elapsed_time_valence[j]=(dt_obj2 - last_valence[j]).total_seconds()
			if last_arousal[j]!=-1:
				elapsed_time_arousal[j]=(dt_obj2 - last_arousal[j]).total_seconds()			

		if entry[2]=='2':
			last_valence[1]=last_arousal[1]=dt_obj2
		elif entry[2]=='-2':
			last_valence[0]=last_arousal[0]=dt_obj2
		elif entry[2]=='-1':
			last_valence[0]=last_arousal[1]=dt_obj2
		elif entry[2]=='0':
			last_valence[1]=last_arousal[0]=dt_obj2

		#print(entry[2])
		user_reported="Yes"
		time=abs((time0-dt_obj).total_seconds())
		row2_valence=[sample_id,within_office_hr,duration_from_break_start,duration_from_office_end,
						within_break_hr, duration_from_break_start, duration_from_break_end, 
						elapsed_time_valence[0], elapsed_time_valence[1], user_reported]
		
		row2_arousal=[sample_id,within_office_hr,duration_from_break_start,duration_from_office_end,
						within_break_hr, duration_from_break_start, duration_from_break_end, 
						elapsed_time_arousal[0], elapsed_time_arousal[1], user_reported]		
		
		if row1_valence[7]!=-1 and row1_valence[8]!=-1:
			dataset_valence.append(row1_valence)
		
		if row1_arousal[7]!=-1 and row1_arousal[8]!=-1:	
			dataset_arousal.append(row1_arousal)
		
		if row2_valence[7]!=-1 and row2_valence[8]!=-1:		
			dataset_valence.append(row2_valence)
		
		if row2_arousal[7]!=-1 and row2_arousal[8]!=-1:	
			dataset_arousal.append(row2_arousal)

	with open("processed_tap_data/Valence/user_" + str(user_id) + ".csv", "w", newline="") as f:
	    writer = csv.writer(f)
	    writer.writerows(dataset_valence)

	with open("processed_tap_data/Arousal/user_" + str(user_id) + ".csv", "w", newline="") as f:
	    writer = csv.writer(f)
	    writer.writerows(dataset_arousal)



data = list(csv.reader(open("Activity preferences form-2 (Responses) - Form_Responses_1.csv")))

user_time_info={}
for i in range(1,len(data)):
	if data[i][3]=='' or data[i][3]=='0':
		continue
	user_id=int(data[i][3])
	row=[]
	for j in range(7,11):
		row.append(datetime.strptime((data[i][j]), '%I:%M:%S %p'))
	#print(row)
	user_time_info[user_id]=row


#print(user_time_info)

for user_id in user_time_info:
	office_start=user_time_info[user_id][0]
	office_end=user_time_info[user_id][1]
	break_start=user_time_info[user_id][2]
	break_end=user_time_info[user_id][3]
	print(user_id)
	create_dataset(user_id, office_start, office_end, break_start, break_end)




'''
Data preprocessing and model training
-> Reomve the column which has only -1
-> remove rows with missing values (i.e., -1)
-> Check if any type of scaling/standardisation/normalisation is required. --> Apply standardisation
-> Apply logistic regression and decision trees.
'''

'''
Results:
For Processed TapData:

Valence - 
{12: {'accuracy': 0.3825136612021858, 'balanced_accuracy': 0.38294314381270905, 'mcc': -0.23710633975217002, 'roc_auc': 0.3528428093645485, 'f1': 0.4263959390862944, 'precision': 0.39622641509433965, 'recall': 0.46153846153846156}, 
13: {'accuracy': 0.42857142857142855, 'balanced_accuracy': 0.4393939393939394, 'mcc': -0.14012266101608226, 'roc_auc': 0.4075448361162647, 'f1': 0.25806451612903225, 'precision': 0.4, 'recall': 0.19047619047619047}, 
14: {'accuracy': 0.46511627906976744, 'balanced_accuracy': 0.45434782608695656, 'mcc': -0.09555330859059091, 'roc_auc': 0.4804347826086956, 'f1': 0.5490196078431373, 'precision': 0.5, 'recall': 0.6086956521739131}, 
15: {'accuracy': 0.4336734693877551, 'balanced_accuracy': 0.48295454545454547, 'mcc': -0.1381187103333059, 'roc_auc': 0.4442340067340067, 'f1': 0.604982206405694, 'precision': 0.44041450777202074, 'recall': 0.9659090909090909}, 
16: {'accuracy': 0.4618055555555556, 'balanced_accuracy': 0.46136966481794073, 'mcc': -0.07786955844637652, 'roc_auc': 0.4323125150711358, 'f1': 0.42379182156133827, 'precision': 0.4523809523809524, 'recall': 0.3986013986013986}, 
19: {'accuracy': 0.35, 'balanced_accuracy': 0.36857142857142855, 'mcc': -0.26891849420908714, 'roc_auc': 0.3588571428571428, 'f1': 0.31578947368421045, 'precision': 0.4090909090909091, 'recall': 0.2571428571428571}, 
20: {'accuracy': 0.40384615384615385, 'balanced_accuracy': 0.37400318979266345, 'mcc': -0.2456129994385672, 'roc_auc': 0.3365231259968102, 'f1': 0.24390243902439024, 'precision': 0.22727272727272727, 'recall': 0.2631578947368421}, 
23: {'accuracy': 0.46078431372549017, 'balanced_accuracy': 0.4691952252599153, 'mcc': -0.0682375740861273, 'roc_auc': 0.43733153638814015, 'f1': 0.5491803278688524, 'precision': 0.4589041095890411, 'recall': 0.6836734693877551}, 
25: {'accuracy': 0.6029411764705882, 'balanced_accuracy': 0.5932868352223191, 'mcc': 0.1912144661024448, 'roc_auc': 0.5675675675675674, 'f1': 0.5263157894736842, 'precision': 0.5769230769230769, 'recall': 0.4838709677419355}, 
26: {'accuracy': 0.46, 'balanced_accuracy': 0.47766995160360093, 'mcc': -0.058353198564389315, 'roc_auc': 0.45294515910629657, 'f1': 0.5830115830115831, 'precision': 0.45896656534954405, 'recall': 0.798941798941799}, 
29: {'accuracy': 0.44666666666666666, 'balanced_accuracy': 0.4283357771260997, 'mcc': -0.14368441079358107, 'roc_auc': 0.4477639296187683, 'f1': 0.3252032520325203, 'precision': 0.32786885245901637, 'recall': 0.3225806451612903}, 
32: {'accuracy': 0.4857142857142857, 'balanced_accuracy': 0.49673202614379086, 'mcc': -0.010267351727228289, 'roc_auc': 0.6045751633986929, 'f1': 0.625, 'precision': 0.4838709677419355, 'recall': 0.8823529411764706}, 
33: {'accuracy': 0.43548387096774194, 'balanced_accuracy': 0.4349580269408473, 'mcc': -0.13015172024006053, 'roc_auc': 0.4160213444393831, 'f1': 0.4166666666666667, 'precision': 0.42016806722689076, 'recall': 0.4132231404958678}, 
36: {'accuracy': 0.4, 'balanced_accuracy': 0.5, 'mcc': 0.0, 'roc_auc': 0.5, 'f1': 0.5714285714285715, 'precision': 0.4, 'recall': 1.0}, 
37: {'accuracy': 0.43103448275862066, 'balanced_accuracy': 0.4735576923076923, 'mcc': -0.093706146008198, 'roc_auc': 0.46063701923076916, 'f1': 0.5822784810126581, 'precision': 0.4339622641509434, 'recall': 0.8846153846153846}}

Arousal:
{12: {'accuracy': 0.5, 'balanced_accuracy': 0.508695652173913, 'mcc': 0.019114484997483857, 'roc_auc': 0.46478260869565213, 'f1': 0.38461538461538464, 'precision': 0.5357142857142857, 'recall': 0.3}, 
13: {'accuracy': 0.4423076923076923, 'balanced_accuracy': 0.4423076923076923, 'mcc': -0.13829796895557542, 'roc_auc': 0.43877383300460227, 'f1': 0.5628140703517588, 'precision': 0.4628099173553719, 'recall': 0.717948717948718}, 
14: {'accuracy': 0.4672131147540984, 'balanced_accuracy': 0.4956521739130435, 'mcc': -0.06794269948502092, 'roc_auc': 0.44742163801820023, 'f1': 0.6368715083798883, 'precision': 0.4691358024691358, 'recall': 0.991304347826087}, 
15: {'accuracy': 0.46, 'balanced_accuracy': 0.4791478243392624, 'mcc': -0.04981299192627275, 'roc_auc': 0.4880916490804944, 'f1': 0.5645161290322581, 'precision': 0.45161290322580644, 'recall': 0.7526881720430108}, 
16: {'accuracy': 0.4885245901639344, 'balanced_accuracy': 0.49266792809839166, 'mcc': -0.027229944998855574, 'roc_auc': 0.4694246151199794, 'f1': 0.6388888888888888, 'precision': 0.49110320284697506, 'recall': 0.9139072847682119}, 
17: {'accuracy': 0.46078431372549017, 'balanced_accuracy': 0.47304582210242585, 'mcc': -0.0691793081183356, 'roc_auc': 0.44233731228340395, 'f1': 0.5833333333333334, 'precision': 0.463855421686747, 'recall': 0.7857142857142857},
18: {'accuracy': 0.15384615384615385, 'balanced_accuracy': 0.15476190476190477, 'mcc': -0.6904761904761905, 'roc_auc': 0.14285714285714288, 'f1': 0.15384615384615383, 'precision': 0.14285714285714285, 'recall': 0.16666666666666666}, 
19: {'accuracy': 0.4782608695652174, 'balanced_accuracy': 0.4832877864200126, 'mcc': -0.035635496775696204, 'roc_auc': 0.4313643052343914, 'f1': 0.5499999999999999, 'precision': 0.4731182795698925, 'recall': 0.6567164179104478}, 
20: {'accuracy': 0.4957983193277311, 'balanced_accuracy': 0.496045197740113, 'mcc': -0.007923044809025472, 'roc_auc': 0.5005649717514125, 'f1': 0.4827586206896552, 'precision': 0.5, 'recall': 0.4666666666666667}, 
23: {'accuracy': 0.4479166666666667, 'balanced_accuracy': 0.4695986805937328, 'mcc': -0.06545938990854651, 'roc_auc': 0.45585486531061026, 'f1': 0.5137614678899083, 'precision': 0.42105263157894735, 'recall': 0.6588235294117647}, 
25: {'accuracy': 0.5, 'balanced_accuracy': 0.5084033613445378, 'mcc': 0.01692566771665739, 'roc_auc': 0.5560224089635855, 'f1': 0.4864864864864864, 'precision': 0.5625, 'recall': 0.42857142857142855}, 
26: {'accuracy': 0.452970297029703, 'balanced_accuracy': 0.455638931803134, 'mcc': -0.09087704140279214, 'roc_auc': 0.4097452119963707, 'f1': 0.5011286681715577, 'precision': 0.45121951219512196, 'recall': 0.5634517766497462}, 
29: {'accuracy': 0.46285714285714286, 'balanced_accuracy': 0.46339869281045754, 'mcc': -0.07323133818414529, 'roc_auc': 0.4196078431372549, 'f1': 0.46590909090909094, 'precision': 0.45054945054945056, 'recall': 0.4823529411764706}, 
32: {'accuracy': 0.40540540540540543, 'balanced_accuracy': 0.4893939393939394, 'mcc': -0.04605661864718383, 'roc_auc': 0.2787878787878788, 'f1': 0.5599999999999999, 'precision': 0.4, 'recall': 0.9333333333333333}, 
33: {'accuracy': 0.4493927125506073, 'balanced_accuracy': 0.47868906455862975, 'mcc': -0.08179267298472812, 'roc_auc': 0.4621212121212122, 'f1': 0.6046511627906976, 'precision': 0.45414847161572053, 'recall': 0.9043478260869565}, 
36: {'accuracy': 0.20833333333333334, 'balanced_accuracy': 0.2062937062937063, 'mcc': -0.5853694070049635, 'roc_auc': 0.13286713286713284, 'f1': 0.17391304347826086, 'precision': 0.16666666666666666, 'recall': 0.18181818181818182}, 
37: {'accuracy': 0.3418803418803419, 'balanced_accuracy': 0.3447368421052631, 'mcc': -0.31903546155716633, 'roc_auc': 0.3172514619883041, 'f1': 0.40310077519379844, 'precision': 0.3611111111111111, 'recall': 0.45614035087719296}}
'''


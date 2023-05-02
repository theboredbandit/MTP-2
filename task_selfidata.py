import csv
from datetime import datetime
import pickle

'''
remove duplicates while forming the input for selfie
take selfie predicted labels
generate the final dataset <- need to code this from scratch
run it on autoglu... <- code is in colab
'''




unavailable=[21,27, 30]

# ############## creating input for selfie #####################
# for user_id in range(11,34):
#   if user_id in unavailable:
#     continue
#   li=[]
#   user_file = 'CommonFilesData/Arousal/user_'+str(user_id)+'.csv'
#   with open(user_file) as file_obj:
#       reader_obj = csv.reader(file_obj)
#       li=file_obj.readlines()

#   #print(li[1])

#   new_li=[]

#   heading=li[0].split(',')

#   for i in range(3):
#       heading.pop(5)

#   #print(heading)

#   new_li.append(heading)

#   for i in range(len(li)):
#       if i==0:
#           continue
#       pre=li[i-1].split(',')
#       cur=li[i].split(',')
#       if cur[5]==pre[5]:
#           continue
#       row=[]
#       for j in range(5):
#           row.append(cur[j])
#       new_li.append(row)

#   print(len(new_li))

#   # saving new_li as csv
#   with open('selfi_input/Arousal/user_'+str(user_id) + '.csv' , 'w') as f:
#       write = csv.writer(f)
#       write.writerows(new_li)

# li=[]
# with open('processed_tap_data_user12.csv') as file_obj:
#     reader_obj = csv.reader(file_obj)
#     li=file_obj.readlines()

# print(len(li))



############## replacing the manual labels with selfi-predicted labels. ######

prediction_arousal={11: (259, 345, ([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0,
       1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0,
       1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0,
       0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1,
       1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0])), 12: (177, 235, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1])), 13: (112, 149, ([1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 0, 1])), 14: (36, 47, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), 15: (144, 191, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), 16: (91, 121, ([0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1])), 17: (138, 183, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), 18: (157, 209, ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0])), 19: (148, 197, ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0,
       0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0,
       0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1])), 20: (125, 166, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1])), 22: (126, 167, ([0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0,
       0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1,
       1, 1, 1, 1, 0, 1, 1])), 23: (138, 183, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), 24: (24, 31, ([0, 0, 0, 0, 0, 1, 1])), 25: (75, 99, ([1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0,
       0, 1, 0, 0, 0, 0, 0])), 26: (281, 374, ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0])), 28: (75, 99, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 0, 1])), 29: (98, 130, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), 31: (27, 35, ([1, 1, 1, 1, 1, 0, 1, 1, 1])), 32: (34, 45, ([0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1])), 33: (95, 126, ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))}

prediction_valence={11: (487, 649, ([0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1,
       1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0,
       1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
       1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1,
       1, 0, 0, 1, 1, 0, 1, 1, 1])), 12: (177, 235, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1])), 13: (112, 149, ([1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0,
       0, 1, 0])), 14: (36, 47, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), 15: (144, 191, ([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), 16: (91, 121, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), 17: (138, 183, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), 18: (157, 209, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1])), 19: (148, 197, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), 20: (125, 166, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1])), 22: (126, 167, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1])), 23: (138, 183, ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), 24: (24, 31, ([0, 0, 1, 1, 0, 0, 0])), 25: (75, 99, ([0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1])), 26: (281, 374, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1])), 28: (75, 99, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1])), 29: (98, 130, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), 31: (27, 35, ([0, 1, 0, 1, 1, 1, 1, 1, 1])), 32: (34, 45, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), 33: (95, 126, ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]))}


selfi_data=[] #this is the dataset that we'll feed to our model/application

#Columns of selfi_data

columns = ['Sample id', 'Within office hour', 'Duration from office start',
'Duration from office end' , 'Within office break hour' , 'Duration from office break start' , 'Duration from office break end' ,
'Elapsed time from last reported 0' , 'Elapsed time from last reported 1' , 'Did the user report?']

selfi_data.append(columns)

def create_dataset(user_id, office_start_time, office_end_time, office_break_start, office_break_end,start_index, end_index, Y_pred): #all these parameters are datetime objects
    li=[]
    user_file = 'CommonFilesData/Valence/user_'+str(user_id)+'.csv'
    with open(user_file) as file_obj:
	    reader_obj = csv.reader(file_obj)
	    li=file_obj.readlines()    
    num=1
    last={}
    last[0]=-1
    last[1]=-1
    for i in range(len(li)):
        if i==0:
            continue
        pre=li[i-1].split(',')
        cur=li[i].split(',')
        if cur[5]==pre[5]:
            continue
        cur_emo=cur[1]
        if i>start_index and i<end_index:  
            cur_emo=str(Y_pred[i-start_index-1])
        notification_time=cur[5] 
        response_time=cur[7]
        #2021-07-19 18:00:29
        #creating row corresponding to notification_time
        time=datetime.strptime(notification_time[11:-4], '%H:%M:%S')
        if i==3:
            print(time)
        
        within_office_hr='No'
        if time>=office_start_time and time<=office_end_time:
            within_office_hr='Yes'
        
        duration_from_office_start = abs((time-office_start_time).total_seconds())
        duration_from_office_end  = abs((time-office_end_time).total_seconds())
        
        within_office_break='No'
        if time>=office_break_start and time<=office_break_end:
            within_office_break='Yes'        

        duration_from_break_start = abs((time-office_break_start).total_seconds())
        duration_from_break_end  = abs((time-office_break_end).total_seconds())        

        elapsed={}
        elapsed[0]=-1
        elapsed[1]=-1
        for k in range(2):
            if last[k]!=-1:
                elapsed[k]=abs((datetime.strptime(notification_time[2:-4], '%y-%m-%d %H:%M:%S')-last[k]).total_seconds())

        row=[num,within_office_hr, duration_from_office_start, duration_from_office_end, within_office_break, duration_from_break_start,
            duration_from_break_end, elapsed[0], elapsed[1], 'No']
        if row[7]!=-1 and row[8]!=-1:
          selfi_data.append(row)
        num+=1
        if i==3:
            print(row)
        #creating row corresponding to response_time
        print(response_time)
        time=datetime.strptime(response_time[11:-5], '%H:%M:%S')
        if i==3:
            print(time)
        
        within_office_hr='No'
        if time>=office_start_time and time<=office_end_time:
            within_office_hr='Yes'
        
        duration_from_office_start = abs((time-office_start_time).total_seconds())
        duration_from_office_end  = abs((time-office_end_time).total_seconds())
        
        within_office_break='No'
        if time>=office_break_start and time<=office_break_end:
            within_office_break='Yes'        

        duration_from_break_start = abs((time-office_break_start).total_seconds())
        duration_from_break_end  = abs((time-office_break_end).total_seconds())        

        elapsed={}
        elapsed[0]=-1
        elapsed[1]=-1
        for k in range(2):
            if last[k]!=-1:
                elapsed[k]=abs((datetime.strptime(response_time[2:-5], '%y-%m-%d %H:%M:%S')-last[k]).total_seconds())
      
        last[int(cur_emo)]=datetime.strptime(response_time[2:-5], '%y-%m-%d %H:%M:%S')
        row=[num,within_office_hr, duration_from_office_start, duration_from_office_end, within_office_break, duration_from_break_start,
            duration_from_break_end, elapsed[0], elapsed[1], 'Yes']
        if i==3:
            print(row)    
        if row[7]!=-1 and row[8]!=-1:
          selfi_data.append(row)
        num+=1
    with open('processed_selfi_data/Valence/user_'+str(user_id) + '.csv' , 'w') as f:
        write = csv.writer(f)
        write.writerows(selfi_data)

'''
user-12
"Work hours start at | Work hours end at  |	Work breaks start at	|    Work breaks end at
8:00:00 AM	11:00:00 PM	11:00:00 AM	5:00:00 PM

user-15
"Work hours start at | Work hours end at  | Work breaks start at  |    Work breaks end at
11:15:00 AM 3:10:00 PM  2:00:00 PM  2:15:00 PM
'''

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
	if user_id in unavailable:
		continue
	if user_id<12 or user_id>33:
		continue
	print(user_id)
	a,b,c=prediction_valence[user_id]
	create_dataset(user_id, office_start, office_end, break_start, break_end,a,b,c)

'''
Results:
Processed Selfi Data

Valence
{12: {'accuracy': 0.5454961133973479, 'balanced_accuracy': 0.5467624846320474, 'mcc': 0.09889421030141175, 'roc_auc': 0.5762886080607525, 'f1': 0.6077348066298344, 'precision': 0.5314009661835749, 'recall': 0.7096774193548387}, 
13: {'accuracy': 0.5181138585393904, 'balanced_accuracy': 0.5169305555555556, 'mcc': 0.0365156217799075, 'roc_auc': 0.5271269841269841, 'f1': 0.4048295454545454, 'precision': 0.5238970588235294, 'recall': 0.3298611111111111}, 
14: {'accuracy': 0.5124735729386892, 'balanced_accuracy': 0.5131988388512696, 'mcc': 0.026495773752850237, 'roc_auc': 0.5274674768192308, 'f1': 0.5291955900367498, 'precision': 0.5038880248833593, 'recall': 0.5571797076526225}, 
15: {'accuracy': 0.5255102040816326, 'balanced_accuracy': 0.5228227290082961, 'mcc': 0.05371452229959094, 'roc_auc': 0.5345725294178902, 'f1': 0.626005361930295, 'precision': 0.5200445434298441, 'recall': 0.7861952861952862}, 
16: {'accuracy': 0.5304659498207885, 'balanced_accuracy': 0.5297483953517641, 'mcc': 0.06032528727380726, 'roc_auc': 0.5493743969459244, 'f1': 0.485698261357263, 'precision': 0.5312883435582823, 'recall': 0.44731404958677684}, 
17: {'accuracy': 0.5448136958710977, 'balanced_accuracy': 0.5424818039451157, 'mcc': 0.09370920462328146, 'roc_auc': 0.5553022127376441, 'f1': 0.4190231362467866, 'precision': 0.5679442508710801, 'recall': 0.3319755600814664}, 
18: {'accuracy': 0.5166163141993958, 'balanced_accuracy': 0.5179627601314348, 'mcc': 0.07921194203212793, 'roc_auc': 0.5079225994888645, 'f1': 0.6652719665271967, 'precision': 0.5079872204472844, 'recall': 0.9636363636363636}, 
19: {'accuracy': 0.5282663316582915, 'balanced_accuracy': 0.5278437655378155, 'mcc': 0.055842837877408485, 'roc_auc': 0.5231226372655023, 'f1': 0.5478627332931968, 'precision': 0.5315420560747663, 'recall': 0.5652173913043478}, 
20: {'accuracy': 0.5404823428079242, 'balanced_accuracy': 0.5389448653398565, 'mcc': 0.07884929818723638, 'roc_auc': 0.5504170278582625, 'f1': 0.49598488427019366, 'precision': 0.5362614913176711, 'recall': 0.46133567662565905}, 
23: {'accuracy': 0.5260900643316655, 'balanced_accuracy': 0.5240037620887771, 'mcc': 0.049010440235511744, 'roc_auc': 0.5283996810402993, 'f1': 0.4666130329847144, 'precision': 0.5197132616487455, 'recall': 0.4233576642335766}, 
25: {'accuracy': 0.5179738562091504, 'balanced_accuracy': 0.5165230115244535, 'mcc': 0.03459802199433017, 'roc_auc': 0.5251126515024749, 'f1': 0.4308681672025723, 'precision': 0.5185758513931888, 'recall': 0.36853685368536854}, 
26: {'accuracy': 0.5489913544668588, 'balanced_accuracy': 0.5518426191366488, 'mcc': 0.10691494985481689, 'roc_auc': 0.5681000457019403, 'f1': 0.5940337224383916, 'precision': 0.5300925925925926, 'recall': 0.6755162241887905}, 
29: {'accuracy': 0.559074299634592, 'balanced_accuracy': 0.5586856410378143, 'mcc': 0.12013130032526767, 'roc_auc': 0.5658307023998861, 'f1': 0.6021978021978022, 'precision': 0.5502008032128514, 'recall': 0.6650485436893204}, 
32: {'accuracy': 0.5377668308702791, 'balanced_accuracy': 0.5390464835235979, 'mcc': 0.07862660921320984, 'roc_auc': 0.5484931699000841, 'f1': 0.5591229444009397, 'precision': 0.5242290748898678, 'recall': 0.5989932885906041}, 
33: {'accuracy': 0.5645161290322581, 'balanced_accuracy': 0.5669023304529981, 'mcc': 0.13352524601290505, 'roc_auc': 0.5420267085624508, 'f1': 0.5573770491803279, 'precision': 0.5230769230769231, 'recall': 0.5964912280701754}}


Arousal
{12: {'accuracy': 0.5011358473421172, 'balanced_accuracy': 0.5011014798141851, 'mcc': 0.002205764381589197, 'roc_auc': 0.5091536770765042, 'f1': 0.48787313432835816, 'precision': 0.5004784688995215, 'recall': 0.47588717015468607}, 
13: {'accuracy': 0.503968253968254, 'balanced_accuracy': 0.502481501243965, 'mcc': 0.005066716871779173, 'roc_auc': 0.4962391755758561, 'f1': 0.44373808010171645, 'precision': 0.49573863636363635, 'recall': 0.4016110471806674}, 
14: {'accuracy': 0.5232365145228216, 'balanced_accuracy': 0.524231987877118, 'mcc': 0.049087341165881614, 'roc_auc': 0.5428950268632042, 'f1': 0.5558562040974102, 'precision': 0.5146743020758768, 'recall': 0.6042016806722689}, 
15: {'accuracy': 0.5066555740432612, 'balanced_accuracy': 0.5117661719096145, 'mcc': 0.03218093769166703, 'roc_auc': 0.5311558484714223, 'f1': 0.25967540574282144, 'precision': 0.5445026178010471, 'recall': 0.17049180327868851}, 
16: {'accuracy': 0.5342118601115053, 'balanced_accuracy': 0.5343479208116151, 'mcc': 0.06871314439243167, 'roc_auc': 0.5570610396764063, 'f1': 0.5374937091092099, 'precision': 0.5281899109792285, 'recall': 0.5471311475409836}, 
17: {'accuracy': 0.5261599210266535, 'balanced_accuracy': 0.5307989238507428, 'mcc': 0.07385155123034365, 'roc_auc': 0.5432643194135767, 'f1': 0.6261682242990654, 'precision': 0.5114503816793893, 'recall': 0.8072289156626506}, 
18: {'accuracy': 0.4984894259818731, 'balanced_accuracy': 0.499981745162468, 'mcc': -0.00023555430024641325, 'roc_auc': 0.4730558598028478, 'f1': 0.6639676113360324, 'precision': 0.49848024316109424, 'recall': 0.9939393939393939}, 
19: {'accuracy': 0.5351851851851852, 'balanced_accuracy': 0.5357206546043155, 'mcc': 0.07462252734277586, 'roc_auc': 0.5492340239387523, 'f1': 0.593192868719611, 'precision': 0.5258620689655172, 'recall': 0.6802973977695167}, 
20: {'accuracy': 0.5340380549682875, 'balanced_accuracy': 0.5361013386974705, 'mcc': 0.07454159183641246, 'roc_auc': 0.5489349936978066, 'f1': 0.5825757575757576, 'precision': 0.5206499661475965, 'recall': 0.6612209802235598}, 
23: {'accuracy': 0.517531556802244, 'balanced_accuracy': 0.5221191927896449, 'mcc': 0.05844410355173889, 'roc_auc': 0.5367010382297562, 'f1': 0.6344314558979809, 'precision': 0.5063613231552163, 'recall': 0.8492176386913229}, 
25: {'accuracy': 0.5126276195593766, 'balanced_accuracy': 0.5114821256976013, 'mcc': 0.043968149548510735, 'roc_auc': 0.5134646302250804, 'f1': 0.6586375611592021, 'precision': 0.5075406032482599, 'recall': 0.9378349410503751}, 
26: {'accuracy': 0.5163584637268848, 'balanced_accuracy': 0.5176851477134763, 'mcc': 0.0451540608370384, 'roc_auc': 0.5171630918656415, 'f1': 0.6304347826086958, 'precision': 0.5087719298245614, 'recall': 0.8285714285714286}, 
29: {'accuracy': 0.49578820697954273, 'balanced_accuracy': 0.4983750434480362, 'mcc': -0.0036991611612611783, 'roc_auc': 0.5117193836171938, 'f1': 0.3422291993720565, 'precision': 0.5023041474654378, 'recall': 0.25952380952380955}, 
32: {'accuracy': 0.5228915662650603, 'balanced_accuracy': 0.5225558961972006, 'mcc': 0.046973018990887516, 'roc_auc': 0.5203107580824973, 'f1': 0.5816901408450704, 'precision': 0.5188442211055276, 'recall': 0.6618589743589743}, 
33: {'accuracy': 0.5, 'balanced_accuracy': 0.5229117570044514, 'mcc': 0.05533443377767582, 'roc_auc': 0.47656454569258966, 'f1': 0.5974025974025974, 'precision': 0.4742268041237113, 'recall': 0.8070175438596491}}
'''
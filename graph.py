import numpy as np 
import matplotlib.pyplot as plt 
  
X = ['User 1','User 2','User 3','User 4', 'User 5']


Ytap = [60.29,48.57,46.1,46.5, 49.7]
Zselfi = [51.8,53.7,52.6,51.2, 53.7]

'''
Users 25,32, 23, 14, 32
Valence
Ytap = [60.29,48.57,46.1,46.5, 49.7]
Zselfi = [51.8,53.7,52.6,51.2, 53.7]

Users 12, 16, 19, 20, 25
Arousal
Ytap = [50,48.85,47.83,49.6, 50]
Zselfi = [50.1,53.4,53.5,53.4, 51.26]
'''
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, Ytap, 0.4, label = 'Processed TapData')
plt.bar(X_axis + 0.2, Zselfi, 0.4, label = 'Processed SelfiData')
  
plt.xticks(X_axis, X)
plt.xlabel("Users")
plt.ylabel("Accuracy (%)")
plt.title("")
plt.legend()
plt.show()
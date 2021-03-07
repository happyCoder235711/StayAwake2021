import numpy as np  
import matplotlib.pyplot as plt  

def constructGraph(inputArray):
    arrayLength = int(len(inputArray))
    x = np.arange(1,(arrayLength+1))
    #y = np.array([0.12354757,0.13434345,0.189099889,0.213453254354,0.24676767676,0.2876765756,0.40001123232,0.3867575757,0.3579879,0.3234343])
    y = np.array(inputArray)
    #-----Labels-----
    plt.title("Drowsiness over Time")  
    plt.xlabel("Time (each unit is 50 frames)")  
    plt.ylabel("Eye Aspect Ratio (lower ratio means more fatigued)")  
    plt.plot(x, y, color ="green")  
    plt.show()
v="[0.29, 0.34, 0.31, 0.31, 0.36, 0.36, 0.32, 0.34, 0.29, 0.32, 0.33, 0.34, 0.34, 0.28, 0.31, 0.32, 0.32, 0.36, 0.36, 0.38, 0.38, 0.36, 0.34, 0.36, 0.29, 0.28, 0.3, 0.33, 0.31, 0.34, 0.37, 0.34, 0.32, 0.3, 0.35, 0.34, 0.35, 0.33, 0.36, 0.38, 0.33, 0.27, 0.3, 0.31, 0.3, 0.28, 0.36, 0.38, 0.35, 0.31, 0.3, 0.29, 0.33, 0.31, 0.32, 0.33, 0.33, 0.31, 0.31, 0.32, 0.33, 0.32, 0.32, 0.32, 0.28, 0.25, 0.26, 0.28, 0.3, 0.35, 0.29, 0.3, 0.27, 0.26, 0.3, 0.29, 0.31, 0.28, 0.29, 0.32, 0.33, 0.26, 0.21, 0.3, 0.27, 0.29, 0.34, 0.32, 0.33, 0.3, 0.25, 0.3, 0.32, 0.35, 0.31, 0.27, 0.24, 0.22, 0.23, 0.25, 0.26, 0.21, 0.28, 0.31, 0.34, 0.28, 0.31, 0.33, 0.29, 0.25, 0.33, 0.31, 0.29, 0.24, 0.28, 0.24, 0.27, 0.3, 0.3, 0.31, 0.23, 0.28, 0.33, 0.28, 0.26, 0.28, 0.24, 0.29, 0.29, 0.27, 0.29, 0.21, 0.34, 0.29, 0.27, 0.24, 0.25, 0.27, 0.24, 0.26, 0.28, 0.27, 0.31, 0.29, 0.29, 0.27, 0.26, 0.3, 0.25, 0.27, 0.22, 0.27, 0.27, 0.29, 0.23, 0.25, 0.25, 0.27, 0.34, 0.29, 0.28, 0.26, 0.29, 0.24, 0.27, 0.33, 0.32, 0.27, 0.3, 0.35, 0.29, 0.26, 0.28, 0.32, 0.3, 0.3, 0.28, 0.25, 0.25, 0.24, 0.26, 0.35, 0.33, 0.28, 0.3, 0.32, 0.27, 0.24, 0.3, 0.32, 0.33, 0.34, 0.35, 0.35, 0.34, 0.38, 0.38, 0.3, 0.29, 0.3, 0.34, 0.34, 0.29, 0.31, 0.28, 0.29, 0.32, 0.32, 0.35, 0.31, 0.29, 0.31, 0.35, 0.31, 0.36, 0.32, 0.32, 0.34, 0.37, 0.39, 0.4, 0.38, 0.32, 0.38, 0.39, 0.32, 0.31, 0.36, 0.33, 0.34, 0.27, 0.28, 0.3, 0.32, 0.28, 0.29, 0.26, 0.25, 0.27, 0.3, 0.27, 0.31, 0.31, 0.32, 0.33, 0.34, 0.3, 0.32, 0.34, 0.29, 0.28, 0.3, 0.28, 0.29, 0.28, 0.35, 0.28, 0.26, 0.26, 0.29, 0.33, 0.34, 0.36, 0.35, 0.34, 0.34, 0.3, 0.33, 0.34, 0.29, 0.37, 0.31, 0.41, 0.37, 0.35, 0.37, 0.36, 0.36, 0.35, 0.36, 0.32, 0.33, 0.34, 0.32, 0.32, 0.33, 0.35, 0.32, 0.33, 0.32, 0.32, 0.29, 0.34, 0.37, 0.36, 0.36, 0.37, 0.37, 0.35, 0.39, 0.38, 0.34, 0.34, 0.32, 0.35, 0.35, 0.33, 0.34, 0.36, 0.31, 0.32, 0.34, 0.33, 0.32, 0.3, 0.33, 0.38, 0.31, 0.28, 0.28, 0.35, 0.38, 0.35, 0.39, 0.39, 0.39, 0.31, 0.35, 0.35, 0.36, 0.35, 0.36, 0.35, 0.33, 0.35, 0.31, 0.29, 0.34, 0.36, 0.31, 0.3, 0.34, 0.31, 0.31, 0.3, 0.32, 0.29, 0.31, 0.38, 0.33, 0.35, 0.38, 0.29, 0.31, 0.36, 0.32, 0.32, 0.33, 0.32, 0.32, 0.35, 0.33, 0.34, 0.34, 0.31, 0.27, 0.36, 0.38, 0.39, 0.33, 0.33, 0.28, 0.26, 0.25, 0.3, 0.27, 0.25, 0.24, 0.2, 0.25, 0.29, 0.28, 0.3, 0.26, 0.27, 0.29, 0.23, 0.28, 0.27, 0.29, 0.27, 0.28, 0.28, 0.33, 0.3, 0.26, 0.27, 0.3, 0.37, 0.28, 0.28, 0.29, 0.39, 0.38, 0.35, 0.29, 0.27, 0.29, 0.34, 0.31, 0.39, 0.37, 0.32, 0.29, 0.28, 0.35, 0.3, 0.38, 0.35, 0.35, 0.36, 0.38, 0.37, 0.41, 0.39, 0.42, 0.35, 0.35, 0.37, 0.4, 0.39, 0.42, 0.42, 0.46, 0.34, 0.29, 0.31, 0.33, 0.32, 0.35, 0.29, 0.33, 0.33, 0.25, 0.39, 0.35, 0.35, 0.34, 0.31, 0.35, 0.38, 0.32, 0.4, 0.4, 0.39, 0.35, 0.28, 0.29, 0.39, 0.32, 0.33, 0.3, 0.19, 0.19, 0.23, 0.21, 0.35, 0.22, 0.26, 0.23, 0.21, 0.2, 0.21, 0.25, 0.29, 0.35, 0.35, 0.33, 0.3, 0.32, 0.36, 0.28, 0.29, 0.26, 0.28, 0.29, 0.27, 0.29, 0.29, 0.3, 0.3, 0.29, 0.31, 0.28, 0.26, 0.23, 0.21, 0.28, 0.26, 0.36, 0.34, 0.35, 0.4, 0.4, 0.37, 0.35, 0.39, 0.33, 0.25, 0.24, 0.3, 0.27, 0.26, 0.31, 0.28, 0.25, 0.24, 0.27, 0.32, 0.31, 0.31, 0.26, 0.21, 0.28, 0.31, 0.33, 0.32, 0.38, 0.27, 0.32, 0.36, 0.35, 0.3, 0.31, 0.33, 0.21, 0.25, 0.3, 0.32, 0.23, 0.24, 0.24, 0.3, 0.34, 0.35, 0.26, 0.34, 0.37, 0.34, 0.36, 0.34, 0.35, 0.35, 0.32, 0.24, 0.3, 0.33, 0.31, 0.31, 0.29, 0.28, 0.27, 0.3, 0.29, 0.33, 0.32, 0.3, 0.33, 0.3, 0.33, 0.27, 0.22, 0.26, 0.23, 0.26, 0.32, 0.26, 0.28, 0.3, 0.32, 0.31, 0.32, 0.3, 0.3, 0.39, 0.3, 0.26, 0.24, 0.29, 0.37, 0.31, 0.33, 0.32, 0.31, 0.32, 0.32, 0.28, 0.34, 0.27, 0.26, 0.34, 0.37, 0.36, 0.26, 0.24, 0.29, 0.26, 0.3, 0.3, 0.3, 0.36, 0.3, 0.29, 0.32, 0.32, 0.26, 0.28, 0.27, 0.31, 0.32, 0.28, 0.21, 0.33, 0.35, 0.36, 0.31, 0.33, 0.25, 0.24, 0.27, 0.31, 0.31, 0.2, 0.35, 0.36, 0.33, 0.3, 0.32, 0.33, 0.33, 0.39, 0.35, 0.31, 0.3, 0.32, 0.35, 0.3, 0.33, 0.26, 0.38, 0.33, 0.23, 0.25, 0.24, 0.34, 0.32, 0.26, 0.31, 0.25, 0.25, 0.23, 0.27, 0.18, 0.24, 0.32, 0.32, 0.36, 0.27, 0.29, 0.32, 0.24, 0.28, 0.35, 0.34, 0.34, 0.33, 0.35, 0.34, 0.38, 0.35, 0.33, 0.34, 0.27, 0.28, 0.33, 0.39, 0.34, 0.36, 0.35, 0.36, 0.35, 0.36, 0.35, 0.36, 0.35, 0.33, 0.33, 0.33, 0.29, 0.32, 0.33, 0.31, 0.36, 0.29, 0.32, 0.32, 0.31, 0.35, 0.37, 0.32, 0.33, 0.33, 0.3, 0.3, 0.38, 0.33, 0.34, 0.32, 0.35, 0.36, 0.35, 0.29, 0.25, 0.31, 0.34, 0.31, 0.39, 0.32, 0.34, 0.34, 0.37, 0.4, 0.37, 0.34, 0.29, 0.31, 0.4, 0.36, 0.42, 0.36, 0.36, 0.4, 0.31, 0.31, 0.32, 0.29, 0.36, 0.39, 0.36, 0.31, 0.36, 0.34, 0.3, 0.33, 0.32, 0.35, 0.4, 0.32, 0.36, 0.31, 0.28, 0.32, 0.24, 0.29, 0.32, 0.28, 0.31, 0.2, 0.28, 0.3, 0.31, 0.28, 0.29, 0.28, 0.29, 0.31, 0.38, 0.39, 0.36, 0.34, 0.35, 0.33, 0.37, 0.37, 0.39, 0.3, 0.33, 0.32, 0.32, 0.31, 0.31, 0.32, 0.29, 0.34, 0.33, 0.31, 0.23, 0.24, 0.27, 0.34, 0.38, 0.37, 0.33, 0.31, 0.27, 0.24, 0.29, 0.32, 0.27, 0.25, 0.29, 0.28, 0.3, 0.33, 0.39, 0.31, 0.41, 0.36, 0.35, 0.32, 0.29, 0.34, 0.32, 0.3, 0.28, 0.36, 0.36, 0.35, 0.41, 0.39, 0.42, 0.44, 0.35, 0.33, 0.37, 0.32, 0.33, 0.33, 0.35, 0.3, 0.35, 0.41, 0.37, 0.42, 0.36, 0.38, 0.38, 0.34, 0.42, 0.43, 0.41, 0.35, 0.35, 0.37, 0.34, 0.33, 0.29, 0.32, 0.28, 0.33, 0.31, 0.31, 0.31]"

def splitString(orig):
    newStr = orig[1:(len(orig)-1)]
    arr = newStr.split(', ')
    constructGraph(arr)

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

# # Use the application default credentials
# cred = credentials.ApplicationDefault()
# firebase_admin.initialize_app(cred, {
#   'projectId': "dd-data-396fe",
# })

# db = firestore.client()

# users_ref = db.collection(u'dataA')
# docs = users_ref.stream()

# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')
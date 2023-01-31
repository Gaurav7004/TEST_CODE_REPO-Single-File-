"""
******************************************************************************
Isolation Forest is an algorithm for detecting outliers in a dataset. 
It is based on the idea of isolating anomalies, hence the name. 
The algorithm works by constructing a decision tree ensemble, 
where each tree partitions the data into smaller and smaller subsets. 
Outliers are instances that are isolated in the early stages of the
tree-building process, while normal instances are isolated in the later stages. 
The algorithm calculates an anomaly score for each instance based on the 
height of the decision tree, and instances with high anomaly scores are 
considered outliers. The algorithm is effective for detecting anomalies 
in high-dimensional datasets and has a low computational cost compared 
to other outlier detection methods.
******************************************************************************
"""


import os, glob
import codecs
import json

import numpy as np
import pandas as pd

### DJANGO IMPORTS
### **************
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings as djangoSettings
from django.conf.urls.static import static

### file storage on disks
from django.core.files.storage import FileSystemStorage

### evaluate model performance with outliers removed using isolation forest
from sklearn.ensemble import IsolationForest

### INTERNAL IMPORTS
from .functions import handle_uploaded_file
from .forms import UploadForm

### To bypass CSRF (Cross-Site Request Forgery) protection
@csrf_exempt

### function to handle all the requests coming from the frontend i.e. home.html
### ***************************************************************************
def home(request):

    ### declaring the path of uploaded csv as global so that it can be accessed anywhere in the code
    global path_of_uploaded_csv

    '''
    Forms from home.html are returning , in which the browser bundles up the form data, encodes it for
    transmission, sends it to the server, and then receives back its response via the POST method.
    '''
    if request.method == 'POST':

        ### handling uploaded data from the UI
        UploadedData = UploadForm(request.POST, request.FILES)

        ### If uploaded data is valid
        if UploadedData.is_valid():
            
            try :
                ### Reading dataframe which user has uploaded by choosing file and clicking upload button.
                dataframe = pd.read_csv(request.FILES['file'])
            except :
                ### rendering an alert message on front end that data is corrupted or empty.
                return render(request,'home.html', {'message': True})

                ### Removing the dataframe from memory
                del dataframe

            ### Number of rows in uploaded dataframe
            No_of_Rows = dataframe.shape[0]

            ### Assigning dataframe into a variable
            d_frame = request.FILES['file']

            ###
            # import pdb; pdb.set_trace()

            ### File Storage on Disks and it is going into static folder of the django server
            fs = FileSystemStorage()
            fs.save(d_frame.name ,d_frame)

            ### Filtering columns of dataframe having boolean and objects
            df = dataframe.select_dtypes(exclude=["bool_","object_"])

            ### getting all the columns of dataframe into a variable
            list_for_pop = df.columns

            ### path of uploaded csv file
            path_of_uploaded_csv = request.FILES['file']

            ### creating a json object to render it directly as json to home.html
            json_object = {list_for_pop.get_loc(c): c for idx, c in enumerate(list_for_pop)}

            ### flushing the file from the static folder from django server
            path_of_uploaded_csv.flush()

            return render(request, 'home.html', {'DataFrame': dataframe, 'item':list_for_pop, 'path':path_of_uploaded_csv, 'json_response':json_object, 'noOfRows':No_of_Rows})

        elif(request.POST.get):

            ### Dependent variable dropdown
            try:
                dpost_list = request.POST.getlist('dropdown1')
            except :
                ### returning an alert to home.html
                return render(request,'home.html', {'warning1': True})
                del df


            ### Independent variables dropdown
            try:
                ipost_list = request.POST.getlist('dropdown2')
            except :
                ### returning an alert to home.html
                return render(request,'home.html', {'warning2': True})
                del df

            ### If user clicks 2 Standard Deviation or 3 Standard Deviation 
            ### on frontend then it will be assigned in z or w respectively.
            z = request.POST.getlist('2std')
            w = request.POST.getlist('3std')

            #import pdb; pdb.set_trace()

            ###
            df_path = request.POST.get('path')

            try:
                ### Reading the dataframe via path again.
                dataframe = pd.read_csv(df_path)
            except:
                return render(request, 'home.html', {'warning5': True})
                del dataframe

            try :
                ### calling toInitializeOutlierDetection() function and passing
                ### dpost_list, ipost_list, dataframe into it
                var1 = toInitializeOutlierDetection(dpost_list, ipost_list, dataframe)
            except :
                return render(request,'home.html', {'warning3': True})
                del df

            try :
                ### verifying what user has checked 2SD or 3SD
                var3 = Conn_CheckBox1(var1) if ((z == '2 Standard Deviation') == True) else Conn_CheckBox2(var1)
            except :
                return render(request,'home.html', {'warning4': True})
                del df

            ### calling  detectOutliers() function to detect outliers
            ### and update dataset with a new column
            var4 = detectOutliers()

            ### Deviation counts
            SD_Counts = [var4[var4.outlier == 'Yes'].shape[0]]

            ### Creating a new dataframe to store the required results
            Outlier_Summary_Report = pd.DataFrame({"Dependent Variable": [dpost_list],
                                                    "Independent Variables": [ipost_list],
                                                        "Potential Outliers": ['-'],
                                                            "2SD": SD_Counts,
                                                                "3SD": SD_Counts,
                                                                    })

            ### path to static files in the server
            path = "/home/gaurav/Desktop/Deployment Folder/Outlier_Detection_IF/static"

            ### verifying is it 2 Standard Deviation or 3 Standard Deviation 
            ### then it will udate static files according to it and ready to download
            ### *********************************************************************

            ### For 3SD
            if(w == ['3 Standard Deviation']):
                
                ### Static path to outlier static file
                path = r'/home/gauravraj/Outlier_Det/static/3_Standard_Deviation.xlsx'

                ### Writing the caculated outlier to excel sheet
                with pd.ExcelWriter(path) as writer:
                    var4.to_excel(writer, sheet_name='Outliers')
                    Outlier_Summary_Report.to_excel(writer, sheet_name='Outliers_Summary')

                ### Flushing the static files after getting the results
                if(os.path.isfile(df_path)):
                    os.remove(df_path)

                return render(request, 'home.html', {'DataFrame': var4, 'path':path, 'message1':True, 'msg3':True  })

            ### For 2SD
            elif(z == ['2 Standard Deviation']):

                var4.to_excel(r'/home/gauravraj/Outlier_Det/static/2_Standard_Deviation.xlsx', encoding='utf-8')
                
                if(os.path.isfile(df_path)):
                    os.remove(df_path)

                return render(request, 'home.html', {'DataFrame': var4, 'path':path, 'message1':True, 'msg2':True })

    else:
        UploadedData = UploadForm()
        return render(request,"home.html",{'form':UploadedData })


'''
function checks if the request method is a POST request and if so, 
it returns a render function with "home.html". If the request method
is not POST, it returns a render function with "home.html" as well. 
The render function is used to render a template and return an HTTP response.
'''
@csrf_exempt
def selected_data(request):
    if request.method == 'POST':
        #import pdb;pdb.set_trace()
        return render(request,"home.html")
    return render(request,"home.html")


### flushing dataset
### ****************
def Clear(df_path):
    if(os.path.isfile(df_path)):
        os.remove(df_path)


### to calculate the outliers in the dataset
### ****************************************
def toInitializeOutlierDetection(dpost_list, ipost_list, dataframe):
    global df

    ### y1 is target dataframe coming from onSelectTargetCol
    y = pd.DataFrame(dataframe, columns=dpost_list)

    ### selecting final columns selected by the user and passed into X as a dataframe
    X = pd.DataFrame(dataframe, columns=ipost_list)

    ### The dataframe
    df = dataframe

    ### split dataframe into X variable choosing multiple independent columns
    ### it gets converted to matrix
    X = X.values

    ### it gets converted to matrix
    y = y.values

    ### identify outliers in the training dataset
    ### the contamination hyperparameter is fluctuating @ (0.1201 to 0.1209)
    ### Isolation forest algorithm is applied here.
    best_params = {
         'contamination': np.linspace(0.01, 0.5),
         }

    # print(best_params)

    ### The isolation forest classifier
    clf = IsolationForest()

    ### Fitting the model
    clf.fit(X, y)


    ### calculating anomaly score  """ anomaly_score = 2^(-depth / height_of_tree) """
    ### ------------------------------------------------------------------------------
    """ 
    where:
     - depth is the length of the path from the root node to the current node in the decision tree.
     - height_of_tree is the maximum depth of the decision tree.
    """
    df_anomalyScore = clf.decision_function(X)
    df['anomaly_scores'] = pd.DataFrame(df_anomalyScore)

    ### finding STD Deviation
    Std = df['anomaly_scores'].std(axis = 0)

    ### findinng Mean
    Mean = df['anomaly_scores'].mean(axis=0)

    ### Declaring the outlier variable
    df['outlier'] = 0

    ### Appending the std dev and mean into the respective variables
    df['Std'] = df['anomaly_scores'].std(axis = 0)
    df['Mean'] = df['anomaly_scores'].mean(axis=0)

    # return Mean and Standard Deviation
    return df


### Check Box 1 returning 2 Std Deviation
### *************************************
def Conn_CheckBox1(var1):
    global df

    df = var1

    # Applying filter of 2 Std Deviation
    df['outlier'] = np.where((df['anomaly_scores'] < (df['Mean']- (2*df['Std']))), 1, 0)
    df['outlier_1'] = np.where((df['anomaly_scores'] > (df['Mean']+ (2*df['Std']))), 1, 0)
    df.outlier =  df.outlier + df.outlier_1

    return df


### Check Box 2 returning 3 Std Deviation
### *************************************
def Conn_CheckBox2(var1):
    global df

    df = var1

    # Applying filter of 3 Std Deviation
    df['outlier'] = np.where((df['anomaly_scores'] < (df['Mean']- (3*df['Std']))), 1, 0)
    df['outlier_1'] = np.where((df['anomaly_scores'] > (df['Mean']+ (3*df['Std']))), 1, 0)
    df.outlier =  df.outlier + df.outlier_1

    return df


### Outlier Detection Function
### **************************
def detectOutliers():
    global df

    ### dropping Std, Mean, Outlier_1, Anomaly Scores
    del df['Std']
    del df['Mean']
    del df['outlier_1']
    del df['anomaly_scores']

    # Displaying in no. of outliers
    outlier_list = df['outlier'].tolist()

    # Imputing 'yes' with 1 and 'no' with 0
    df['outlier'] = np.where(df['outlier'] == 1, 'Yes', 'No')

    return df


# -*- coding: utf-8 -*-
"""Lab Report based diabetes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sdi4g65JoS2Wsm7lvSUc9JxPx2u1AkS5
"""

from google.colab import drive
drive.mount('/content/drive')

# For ignoring the warnings
import warnings
warnings.filterwarnings('ignore')

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Importing tha data
import pandas as pd
dataset = pd.read_csv('/content/drive/MyDrive/Project Databases/2. (preg)diabetes.csv')
dataset.head()

dataset.isnull().sum() # For null values

x = dataset.iloc[:,:-1]  # Data except last column
y = dataset.iloc[:,-1] # last column in data
x.head()

y.head()

dataset.corr()

import seaborn as sns
sns.heatmap(dataset.corr(),fmt ='.0%',annot = True)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(nrows=4, ncols=2, figsize=(12, 10))
fig.tight_layout(pad=3.0)
ax[0,0].set_title('Pregnancies')
ax[0,0].hist(dataset.Pregnancies[dataset.Outcome==1]);
ax[0,1].set_title('Glucose')
ax[0,1].hist(dataset.Glucose[dataset.Outcome==1]);
ax[1,0].set_title('BloodPressure')
ax[1,0].hist(dataset.BloodPressure[dataset.Outcome==1]);
ax[1,1].set_title('SkinThickness')
ax[1,1].hist(dataset.SkinThickness[dataset.Outcome==1]);
ax[2,0].set_title('Insulin')
ax[2,0].hist(dataset.Insulin[dataset.Outcome==1]);
ax[2,1].set_title('BMI')
ax[2,1].hist(dataset.BMI[dataset.Outcome==1]);
ax[3,0].set_title('DiabetesPedigreeFunction')
ax[3,0].hist(dataset.DiabetesPedigreeFunction	[dataset.Outcome==1]);
ax[3,1].set_title('Age')
ax[3,1].hist(dataset.Age[dataset.Outcome==1])

sns.countplot(data=dataset,x='Outcome')   # Implementing Observational count for calss

## Pairplotting of dataframe
import seaborn as sns
sns.set(style="ticks", color_codes=True)
sns.pairplot(dataset,hue='Outcome',palette='gnuplot');

# For training and testing of model

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.1)

"""**K-Nearest Neighbour**"""

# K nearest neighbor model

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 23)
knn.fit(x_train,y_train)
predict1 = knn.predict(x_test)
predict1

y_test # Testing data of y

# For counting mis-classifies values

count_missclassified1 = (y_test!=predict1).sum()
count_missclassified1

# For finding the accuracy

from sklearn import metrics
accuracy1 = metrics.accuracy_score(y_test,predict1)
accuracy1*100

# Clssification report

c_f1 = metrics.classification_report(y_test,predict1)
print(c_f1)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Obtain predictions from your model
predictions = knn.predict(x_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, predictions)

# Define class labels (if applicable)
class_labels = ['Class 0', 'Class 1', ]  # Replace with your actual class labels

# Plot the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='d', xticklabels=class_labels, yticklabels=class_labels)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.show()

from sklearn.metrics import confusion_matrix

# Obtain predictions from your model
predictions = knn.predict(x_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, predictions)

# Calculate sensitivity (true positive rate)
sensitivity = cm[1, 1] / (cm[1, 0] + cm[1, 1])

# Calculate specificity (true negative rate)
specificity = cm[0, 0] / (cm[0, 0] + cm[0, 1])

# Print sensitivity and specificity
print("Sensitivity:", sensitivity)
print("Specificity:", specificity)

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# Obtain predicted probabilities from your model
probs = knn.predict_proba(x_test)[:,1]
# For binary classification, use: probs = model.predict_proba(x_test)[:, 1]

# Calculate the false positive rate (fpr), true positive rate (tpr), and thresholds
fpr, tpr, thresholds = roc_curve(y_test, probs)
# For binary classification, use: fpr, tpr, thresholds = roc_curve(y_test, probs[:, 1])

# Calculate the Area Under the ROC Curve (AUC)
roc_auc = auc(fpr, tpr)

# Plot the ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', lw=2, label='ROC curve (AUC = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='gray', lw=1, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()

from sklearn.metrics import cohen_kappa_score
predictions = knn.predict(x_test)
kappa = cohen_kappa_score(y_test, predictions)
print("Cohen's kappa value:", kappa)

"""**LOGISTIC REGRESSION**"""

# Analysing with Logistic regression

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(random_state=20,penalty='l2')
lr.fit(x_train,y_train)
predict2 = lr.predict(x_test)
predict2

# Counting mis-classified values for logistic regression

count_missclassified2 = (y_test!=predict2).sum()
count_missclassified2

# For finding the accuracy

accuracy2 = metrics.accuracy_score(y_test,predict2)
accuracy2*100

# Evaluating classification report
c_r2 = metrics.classification_report(y_test,predict2)
print(c_r2)

from sklearn.metrics import confusion_matrix

# Obtain predictions from your model
predictions = lr.predict(x_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, predictions)

# Calculate sensitivity (true positive rate)
sensitivity = cm[1, 1] / (cm[1, 0] + cm[1, 1])

# Calculate specificity (true negative rate)
specificity = cm[0, 0] / (cm[0, 0] + cm[0, 1])

# Print sensitivity and specificity
print("Sensitivity:", sensitivity)
print("Specificity:", specificity)

# Testing with the values

n = [[1,85,66,29,0,26.6,0.351,31]]
pred2 = lr.predict(n)
pred2

from sklearn.metrics import cohen_kappa_score
predictions = lr.predict(x_test)
kappa = cohen_kappa_score(y_test, predictions)
print("Cohen's kappa value:", kappa)

"""**RANDOM FOREST ALGORITHM**"""

#Random Forest Algorithm

from sklearn import ensemble
rf = ensemble.RandomForestClassifier(n_estimators = 7,criterion = 'entropy',max_features = 5,random_state=20) #random forest model
rf.fit(x_train,y_train)
predict3 = rf.predict(x_test) #prediction
predict3

# Counting mis-classified values for logistic regression

count_missclassified3 = (y_test!=predict3).sum()
count_missclassified3

accuracy3 = metrics.accuracy_score(y_test,predict3)
accuracy3*100

# Evaluating classification report
c_r3 = metrics.classification_report(y_test,predict3)
print(c_r3)

from sklearn.metrics import confusion_matrix

# Obtain predictions from your model
predictions = rf.predict(x_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, predictions)

# Calculate sensitivity (true positive rate)
sensitivity = cm[1, 1] / (cm[1, 0] + cm[1, 1])

# Calculate specificity (true negative rate)
specificity = cm[0, 0] / (cm[0, 0] + cm[0, 1])

# Print sensitivity and specificity
print("Sensitivity:", sensitivity)
print("Specificity:", specificity)

from sklearn.metrics import cohen_kappa_score
predictions = rf.predict(x_test)
kappa = cohen_kappa_score(y_test, predictions)
print("Cohen's kappa value:", kappa)

# Testing with the values

n = [[1,85,66,29,0,26.6,0.351,31]]
pred3 = rf.predict(n)
pred3

"""**SUPPORT VECTOR MACHINE(SVM)**"""

# support vector machine SVM
from sklearn import svm
#svc-> classificational algorithm

model = svm.SVC(probability=True)
model.fit(x_train,y_train)
predict4=model.predict(x_test)
predict4

# Counting mis-classified values for support vector machine SVM

count_missclassified4 = (y_test != predict4).sum()
count_missclassified4

#accuracy for support vector machine SVM
accuracy4=metrics.accuracy_score(y_test,predict4)
accuracy4*100

# Clssification report support vector machine SVM

c_r4 = metrics.classification_report(y_test,predict4)
print(c_r4)

from sklearn.metrics import confusion_matrix

# Obtain predictions from your SVM model
predictions = model.predict(x_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, predictions)

# Calculate sensitivity (true positive rate)
sensitivity = cm[1, 1] / (cm[1, 0] + cm[1, 1])

# Calculate specificity (true negative rate)
specificity = cm[0, 0] / (cm[0, 0] + cm[0, 1])

# Print sensitivity and specificity
print("Sensitivity:", sensitivity)
print("Specificity:", specificity)

from sklearn.metrics import cohen_kappa_score
predictions = model.predict(x_test)
kappa = cohen_kappa_score(y_test, predictions)
print("Cohen's kappa value:", kappa)

# Testing with the values

n = [[1,85,66,29,0,26.6,0.351,31]]
pred4 = model.predict(n)
pred4

"""**DECISION TREE MODEL**"""

# Using Decision Tree model

from sklearn import tree
dtree = tree.DecisionTreeClassifier(criterion = 'entropy',max_depth=1,min_samples_split=7)
dtree.fit(x_train,y_train)
predict5 = dtree.predict(x_test)
predict5

# Counting mis-classified values for Decision Tree Algorithm

count_missclassified5 = (y_test != predict5).sum()
count_missclassified5

# Finding the accuracy

accuracy5 = metrics.accuracy_score(y_test,predict5)
accuracy5*100

# Clssification report

c_r5 = metrics.classification_report(y_test,predict5)
print(c_r5)

from sklearn.metrics import confusion_matrix

# Obtain predictions from your SVM model
predictions = dtree.predict(x_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, predictions)

# Calculate sensitivity (true positive rate)
sensitivity = cm[1, 1] / (cm[1, 0] + cm[1, 1])

# Calculate specificity (true negative rate)
specificity = cm[0, 0] / (cm[0, 0] + cm[0, 1])

# Print sensitivity and specificity
print("Sensitivity:", sensitivity)
print("Specificity:", specificity)

from sklearn.metrics import cohen_kappa_score
predictions = dtree.predict(x_test)
kappa = cohen_kappa_score(y_test, predictions)
print("Cohen's kappa value:", kappa)

# Testing with the values

n = [[1,85,66,29,0,26.6,0.351,31]]
pred5 = dtree.predict(n)
pred5

"""**XG BOOST**"""

#Using XG Boost
import xgboost as xgb
model2 = xgb.XGBClassifier(n_estimators=16, learning_rate=0.01, max_depth=3)
model2.fit(x_train, y_train)
predict6 = model2.predict(x_test)
predict6

#No. Of Missclassified
count_missclassified6 = (y_test != predict6).sum()
count_missclassified6

#calculating accuracy score
accuracy6 = metrics.accuracy_score(y_test,predict6)
accuracy6*100

# Clssification report

c_r6 = metrics.classification_report(y_test,predict6)
print(c_r6)

from sklearn.metrics import confusion_matrix

# Obtain predictions from your SVM model
predictions = model2.predict(x_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, predictions)

# Calculate sensitivity (true positive rate)
sensitivity = cm[1, 1] / (cm[1, 0] + cm[1, 1])

# Calculate specificity (true negative rate)
specificity = cm[0, 0] / (cm[0, 0] + cm[0, 1])

# Print sensitivity and specificity
print("Sensitivity:", sensitivity)
print("Specificity:", specificity)

from sklearn.metrics import cohen_kappa_score
predictions = model2.predict(x_test)
kappa = cohen_kappa_score(y_test, predictions)
print("Cohen's kappa value:", kappa)

# Testing with the values

n = [[1,85,66,29,0,26.6,0.351,31]]
pred6 = model2.predict(n)
pred6

"""**GAUSSIAN NAIVE BAYES ALGORITHM**"""

#Using Gaussian Naïve Bayes Classifier
from sklearn.naive_bayes import GaussianNB
model3 = GaussianNB()
model3.fit(x_train, y_train)
predict7 = model3.predict(x_test)
print(predict7)

# Counting mis-classified values for Gaussian Naïve Bayes Classifier

count_missclassified7 = (y_test != predict7).sum()
count_missclassified7

#calculating accuracy score
accuracy7 = metrics.accuracy_score(y_test,predict7)
accuracy7*100

# Clssification report

c_r7 = metrics.classification_report(y_test,predict7)
print(c_r7)

from sklearn.metrics import confusion_matrix

# Obtain predictions from your SVM model
predictions = model3.predict(x_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, predictions)

# Calculate sensitivity (true positive rate)
sensitivity = cm[1, 1] / (cm[1, 0] + cm[1, 1])

# Calculate specificity (true negative rate)
specificity = cm[0, 0] / (cm[0, 0] + cm[0, 1])

# Print sensitivity and specificity
print("Sensitivity:", sensitivity)
print("Specificity:", specificity)

from sklearn.metrics import cohen_kappa_score
predictions = model3.predict(x_test)
kappa = cohen_kappa_score(y_test, predictions)
print("Cohen's kappa value:", kappa)

# Testing with the values

n = [[1,85,66,29,0,26.6,0.351,31]]
pred7 = model3.predict(n)
pred7

"""**ADA BOOST**"""

#using ada boost
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
model4 = AdaBoostClassifier(n_estimators=10, learning_rate=0.01, random_state=0)
model4.fit(x_train, y_train)
predict8 = model4.predict(x_test)
print(predict8)

# Counting mis-classified values for ADA Boost

count_missclassified8 = (y_test != predict8).sum()
count_missclassified8

#calculating accuracy score
accuracy8 = metrics.accuracy_score(y_test,predict8)
accuracy8*100

# Clssification report

c_r8 = metrics.classification_report(y_test,predict8)
print(c_r8)

from sklearn.metrics import confusion_matrix

# Obtain predictions from your SVM model
predictions = model4.predict(x_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, predictions)

# Calculate sensitivity (true positive rate)
sensitivity = cm[1, 1] / (cm[1, 0] + cm[1, 1])

# Calculate specificity (true negative rate)
specificity = cm[0, 0] / (cm[0, 0] + cm[0, 1])

# Print sensitivity and specificity
print("Sensitivity:", sensitivity)
print("Specificity:", specificity)

from sklearn.metrics import cohen_kappa_score
predictions = model4.predict(x_test)
kappa = cohen_kappa_score(y_test, predictions)
print("Cohen's kappa value:", kappa)

# Testing with the values

n = [[1,85,66,29,0,26.6,0.351,31]]
pred8 = model4.predict(n)
pred8

"""**GRADIENT BOOSTED MODEL**"""

#Gradient Boosted Model
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
model5 = GradientBoostingClassifier(n_estimators=10, learning_rate=0.01, random_state=0)
model5.fit(x_train, y_train)
predict9 = model5.predict(x_test)
print(predict9)

# Counting mis-classified values for Gradient Boosted Model

count_missclassified8 = (y_test != predict9).sum()
count_missclassified8

#calculating accuracy score
accuracy9 = metrics.accuracy_score(y_test,predict9)
accuracy9*100

# Clssification report

c_r9 = metrics.classification_report(y_test,predict9)
print(c_r9)

from sklearn.metrics import confusion_matrix

# Obtain predictions from your SVM model
predictions = model5.predict(x_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, predictions)

# Calculate sensitivity (true positive rate)
sensitivity = cm[1, 1] / (cm[1, 0] + cm[1, 1])

# Calculate specificity (true negative rate)
specificity = cm[0, 0] / (cm[0, 0] + cm[0, 1])

# Print sensitivity and specificity
print("Sensitivity:", sensitivity)
print("Specificity:", specificity)

from sklearn.metrics import cohen_kappa_score
predictions = model5.predict(x_test)
kappa = cohen_kappa_score(y_test, predictions)
print("Cohen's kappa value:", kappa)

# Testing with the values

n = [[1,85,66,29,0,26.6,0.351,31]]
pred9 = model5.predict(n)
pred9

"""1D CNN

"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

"""**COMPARISION**"""

import pandas as pd
model_compare = pd.DataFrame({"KNN":accuracy1*100,
"Logistic Regression":accuracy2*100,
"Random Forest Classifier":accuracy3*100,
"Support Vector Machine":accuracy4*100,
"Decision Tree Algorithm":accuracy5*100,
"XG Boost":accuracy6*100,
"Gaussian Naive Bayes":accuracy7*100,
"ADA Boost Model":accuracy8*100,
"Gradient Boosted Model":accuracy9*100},
index=["accuracy"])
model_compare.T.plot.bar(figsize=(15,10));

# Hypertuning
from sklearn.model_selection import GridSearchCV
import numpy as np
lr_params = [{'C': np.logspace(-4,4,30), "solver":["liblinear"]}]
clf = GridSearchCV(lr,lr_params,cv = 5,verbose=True) #grid search cv model creation
clf.fit(x_train,y_train)
score=clf.score(x_test,y_test)
print(score*100)

y_prediction=clf.predict(x_test)
y_prediction

sns.set(font_scale=2)
import seaborn as sns
from sklearn.metrics import confusion_matrix
sns.heatmap(confusion_matrix(y_test,y_prediction), annot=True,cbar=False, fmt='g')
plt.xlabel("True label")
plt.ylabel("Predicted label");

# from sklearn.metrics import accuracy_score
print(metrics.accuracy_score(y_test,y_prediction))

print(metrics.classification_report(y_test, y_prediction))

from sklearn.metrics import RocCurveDisplay
RocCurveDisplay.from_estimator(clf,x_test,y_test)

import pickle
# Save trained model to file
pickle.dump(clf, open("Diabetes.pkl", "wb"))
loaded_model = pickle.load(open("Diabetes.pkl", "rb"))
loaded_model.predict(x_test)
loaded_model.score(x_test,y_test)
#######OUTPUT########
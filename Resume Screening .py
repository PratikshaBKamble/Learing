#!/usr/bin/env python
# coding: utf-8

# # Machine Learning Project on Resume Screening with Python.
# ### Companies often receive thousands of resumes for each job posting and employ dedicated screening officers  to screen qualified candidates. In this article, I will introduce you to a machine learning project on Resume Screening with Python programming language.

# ### What is Resume Screening?
# #### Hiring the right talent is a challenge for all businesses. This challenge is magnified by the high volume of applicants if the business is labour-intensive, growing, and facing high attrition rates.
# #### An example of such a business is that IT departments are short of growing markets. In a typical service organization, professionals with a variety of technical skills and business domain expertise are hired and assigned to projects to resolve customer issues. This task of selecting the best talent among many others is known as Resume Screening.
# #### Typically, large companies do not have enough time to open each CV, so they use machine learning algorithms for the Resume Screening task.

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.naive_bayes import MultinomialNB
from sklearn.multiclass import OneVsRestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
from pandas.plotting import scatter_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics 

resumeDataset = pd.read_csv('UpdatedResumeDataSet.csv')
resumeDataset['cleaned_resume']=''
resumeDataset.head()


# # Now let’s have a quick look at the categories of resumes present in the dataset:

# In[6]:


print ("Displaying the distinct categories of resume -")
print(resumeDataset['Category'].unique())


# # Now let’s have a look at the distinct categories of resume and the number of records belonging to each category:

# In[8]:


print ("Displaying the distinct categories of resume and the number of records belonging to each category -")
print(resumeDataset['Category'].value_counts())


# # Now let’s visualize the number of categories in the dataset:

# In[15]:


import seaborn as sns
plt.figure(figsize=(20,20))
plt.xticks(rotation=90)
sns.countplot(y="Category",data=resumeDataset)


# # Now let’s visualize the distribution of categories:

# In[22]:


from matplotlib.gridspec import GridSpec
targetCounts = resumeDataset['Category'].value_counts()
targetLabels = resumeDataset['Category'].unique()
# make square figures and axes
plt.figure(1,figsize=(25,25))
the_grid = GridSpec(2,2)

cmap=plt.get_cmap('coolwarm')
colors=[cmap(i) for i in np.linspace(0,1,3)]
plt.subplot(the_grid[0,1],aspect=1,title="CATEGORY DISTRIBUTION")

source_pie = plt.pie(targetCounts,labels=targetLabels,autopct='%1.1f%%',shadow=True,colors=colors)
plt.show()


# # Now I will create a helper function to remove the URLs, hashtags, mentions, special letters, and punctuations:

# In[25]:


import re
def cleanResume(resumeText):
    resumeText = re.sub('http\S+\s*', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#\S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('@\S+', '  ', resumeText)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeText)  # remove punctuations
    resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeText) 
    resumeText = re.sub('\s+', ' ', resumeText)  # remove extra whitespace
    return resumeText
    
resumeDataset['cleaned_resume'] = resumeDataset.Resume.apply(lambda x: cleanResume(x))


# In[29]:


import sys
print(sys.executable)


# In[33]:


import nltk
from nltk.corpus import stopwords
import string
from wordcloud import WordCloud

oneSetOfStopWords = set(stopwords.words('english')+['``',"''"])
totalWords =[]
Sentences = resumeDataset['Resume'].values
cleanedSentences = ""
for i in range(0,160):
    cleanedText = cleanResume(Sentences[i])
    cleanedSentences += cleanedText
    requiredWords = nltk.word_tokenize(cleanedText)
    for word in requiredWords:
        if word not in oneSetOfStopWords and word not in string.punctuation:
            totalWords.append(word)
    
wordfreqdist = nltk.FreqDist(totalWords)
mostcommon = wordfreqdist.most_common(50)
print(mostcommon)

wc = WordCloud().generate(cleanedSentences)
plt.figure(figsize=(15,15))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()


# # Now I will convert these words into categorical values:

# In[36]:


from sklearn.preprocessing import LabelEncoder

var_mod = ['Category']
le = LabelEncoder()
for i in var_mod:
    resumeDataset[i] = le.fit_transform(resumeDataset[i])


# # Training Machine Learning Model for Resume Screening
# #### Now the next step in the process is to train a model for the task of Resume Screening. Here I will use the one vs the rest classifier; KNeighborsClassifier. For this task, I will first split the data into training and test sets:

# In[38]:


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack

requiredText = resumeDataset['cleaned_resume'].values
requiredTarget = resumeDataset['Category'].values

word_vectorizer = TfidfVectorizer(
    sublinear_tf=True,
    stop_words='english',
    max_features=1500)
word_vectorizer.fit(requiredText)
WordFeatures = word_vectorizer.transform(requiredText)

print ("Feature completed .....")

X_train,X_test,y_train,y_test = train_test_split(WordFeatures,requiredTarget,random_state=0, test_size=0.2)
print(X_train.shape)
print(X_test.shape)


# # Now let’s train the model and print the classification report:

# In[39]:


clf = OneVsRestClassifier(KNeighborsClassifier())
clf.fit(X_train, y_train)
prediction = clf.predict(X_test)
print('Accuracy of KNeighbors Classifier on training set: {:.2f}'.format(clf.score(X_train, y_train)))
print('Accuracy of KNeighbors Classifier on test set: {:.2f}'.format(clf.score(X_test, y_test)))

print("\n Classification report for classifier %s:\n%s\n" % (clf, metrics.classification_report(y_test, prediction)))


# In[ ]:





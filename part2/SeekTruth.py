#!/usr/bin/env python
# coding: utf-8

# In[3]:


# SeekTruth.py : Classify text objects into two categories
#
# PLEASE PUT YOUR NAMES AND USER IDs HERE
#
# Based on skeleton code by D. Crandall, October 2021
#

import sys
import re

def load_file(filename):
    objects=[]
    labels=[]
    with open(filename, "r") as f:
        for line in f:
            parsed = line.strip().split(' ',1)
            labels.append(parsed[0] if len(parsed)>0 else "")
            objects.append(parsed[1] if len(parsed)>1 else "")

    return {"objects": objects, "labels": labels, "classes": list(set(labels))}

# classifier : Train and apply a bayes net classifier
#
# This function should take a train_data dictionary that has three entries:
#        train_data["objects"] is a list of strings corresponding to reviews
#        train_data["labels"] is a list of strings corresponding to ground truth labels for each review
#        train_data["classes"] is the list of possible class names (always two)
#
# and a test_data dictionary that has objects and classes entries in the same format as above. It
# should return a list of the same length as test_data["objects"], where the i-th element of the result
# list is the estimated classlabel for test_data["objects"][i]
#
# Do not change the return type or parameters of this function!

#
    #helper functions
def clean_function(data):
    tranformed_data=[]
    stopwords=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 
            'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]  

    for line in data:
        line=line.lower()
        line=line.replace('\W_', '')
        line=line.replace('[^A-Za-z0-9!.?'']+', '')
        line=re.sub(r'[^a-z0-9A-Z_]',' ',line)
        line=re.sub(r'[0-9]+','',line)
        line=line.strip()
        no_stop_words=[word for word in re.split(r'\W+',line) if word not in stopwords]
        new_line=" ".join(no_stop_words)
        tranformed_data.append(new_line)
    return tranformed_data

def classifier(train_data, test_data):
    




    # This is just dummy code -- put yours here!

    #Calculating prior probabilities inititally we have 0.5 , 0.5 for each class
    T_count=0
    D_count=0
    for i in train_data['labels']:
        if i=='truthful':
            T_count+=1
        elif i=='deceptive':
            D_count+=1
            
    Prior_prob_Truthful = T_count/len(train_data['labels'])
    Prior_prob_Deceptive = D_count/len(train_data['labels'])



    Truthful_train_data=[]
    Deceptive_train_data=[]
    for i in range(len(train_data['objects'])):
        if (train_data['labels'][i]=='truthful'):
            Truthful_train_data.append(train_data['objects'][i])
            
        else:
            Deceptive_train_data.append(train_data['objects'][i])
            
    #creating a bag of words for each label
    bag_of_words_truthful = []
    bag_of_words_deceptive = []
    for sentence in clean_function(clean_function(Truthful_train_data)):
        sentence_as_list = sentence.split()
        for word in sentence_as_list:
            bag_of_words_truthful.append(word)  
            
    for sentence in clean_function(clean_function(Deceptive_train_data)):
        sentence_as_list = sentence.split()
        for word in sentence_as_list:
            bag_of_words_deceptive.append(word) 
            
    #removing duplicates
    bag_of_words_truthful=set(bag_of_words_truthful)
    bag_of_words_deceptive=set(bag_of_words_deceptive)


    # print('Truthful bag of words' , len(bag_of_words_truthful))
    # print('deceptive bag of words' , len(bag_of_words_deceptive))


    #Here we are creating likelihoods of words(features) from the training set and measuring whats the probability of 
    #the word being a truthful review or a deceptive review
    #if we select a word x whats the probability that this word is in a truth review and whats the probability this word 
    #is in a deceptive review

    likelihood_of_words_truth = {}
    likelihood_of_words_decept = {}

    cleaned_Truthful_train_data=clean_function(Truthful_train_data)
    cleaned_Deceptive_train_data=clean_function(Deceptive_train_data)

    no_of_truth_emails = len(Truthful_train_data)
    no_of_deceptive_emails = len(Deceptive_train_data)


    for w in bag_of_words_truthful:
        count= 0 
        for sentence in cleaned_Truthful_train_data:
            if w in sentence:
                count+=1
            prob_of_truth = (count+1)/(no_of_truth_emails)
            likelihood_of_words_truth[w] = prob_of_truth
            
            
    for w in bag_of_words_deceptive:
        count_decept= 0 
        for sentence_Decept in cleaned_Deceptive_train_data:
            if w in sentence_Decept:
                count_decept+=1
            prob_of_decept = (count_decept+1)/(no_of_deceptive_emails)
            likelihood_of_words_decept[w] = prob_of_decept
        
        
    #We can see the probabilities of each word being deceptive , truthful

    # likelihood_of_words_truth
    # for i in likelihood_of_words_decept.keys():
    #     if i in likelihood_of_words_truth.keys():
    #         print(i," :decept ",likelihood_of_words_decept[i] ,"truth ", likelihood_of_words_truth[i])


    clean_ip=clean_function(test_data['objects'])
    clean_ip


    op_list=[]
    for sentence in clean_ip:
        words=list(str(sentence).split())
        #print(words)
        for word in words:
            if word not in (bag_of_words_truthful and bag_of_words_deceptive):
                words.remove(word)
                
        prob_input_is_deceptive=1
        prob_input_is_truth=1
        for i in words:
            if ((likelihood_of_words_decept.get(i) is not None) and (likelihood_of_words_truth.get(i) is not None)):
                prob_input_is_deceptive*=likelihood_of_words_decept.get(i)/(likelihood_of_words_decept.get(i)+likelihood_of_words_truth.get(i))
                prob_input_is_truth*=likelihood_of_words_truth.get(i)/(likelihood_of_words_decept.get(i)+likelihood_of_words_truth.get(i))


        if(prob_input_is_truth>prob_input_is_deceptive):
            op_list.append('truthful')

        else:
            op_list.append('deceptive')


    # print(op_list.count('deceptive'))
    # print(op_list.count('truthful'))


    return op_list

    #return [test_data["classes"][0]] * len(test_data["objects"])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Usage: classify.py train_file.txt test_file.txt")

    (_, train_file, test_file) = sys.argv
    # Load in the training and test datasets. The file format is simple: one object
    # per line, the first word one the line is the label.

    #train_data= load_file('/Users/anuragsangem/Desktop/deceptive.train.txt')
    #test_data = load_file('/Users/anuragsangem/Desktop/deceptive.test.txt')
    train_data = load_file(train_file)
    test_data = load_file(test_file)
    if(sorted(train_data["classes"]) != sorted(test_data["classes"]) or len(test_data["classes"]) != 2):
        raise Exception("Number of classes should be 2, and must be the same in test and training data")

    # make a copy of the test data without the correct labels, so the classifier can't cheat!
    test_data_sanitized = {"objects": test_data["objects"], "classes": test_data["classes"]}

    results= classifier(train_data, test_data_sanitized)

    # calculate accuracy
    correct_ct = sum([ (results[i] == test_data["labels"][i]) for i in range(0, len(test_data["labels"])) ])
    print("Classification accuracy = %5.2f%%" % (100.0 * correct_ct / len(test_data["labels"])))


# In[ ]:





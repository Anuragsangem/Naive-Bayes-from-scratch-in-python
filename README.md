# ansangem-vkashir-hripb-a2

REPORT AND WORKFLOW- A2

## PART1:

### Workflow:


#### Search Abstraction:
1) Successor states: There are at most 4 possible legal ways for pichu to traverse across any given state diagonally. Simillarly for pikachu, it can travel 15 different ways including the opponent pieces it has to jump over. Lastly, raichu is the best one! Raichu can alone have more successor states combined that of pichu and pikachu - travelling diagonally and no limits on the empty spaces between jumped pieces gives it a lot of states to cover.
2) Initial state: Given the value of N, we understand that the matrix starts with white pieces on row 2 and row 3 with half of N number of pikachus and pichus respectively, and black pieces for pichu and pikachu on row n-2 and n-1 respectively (considering that rows range is [1,N] ).
3) Cost function: We have designed the given problem using min-max algorithm and later optimized it by alpha-beta pruning approach in order to reduce time taken by our implemented algorithm. We have used variables such as rewards and cost that calculates and awards for the pieces on the board present given a specific number of points for that individual piece. Later, subtracting the scores from the opponent player's pieces score to get the whole score for that particular given successor state.

#### Challenges faced:
1) 

#### Notable Observations:
1) The given min-max algorithm takes a lot of time to calculate costs, since it manually calculates for all at a single time. So, using alpha-beta prining indeed saved us a lot of time.
2) Sometimes, there maybe test cases where the winning move might be just with 1 move, but due to a lot of successor states and a lot of computations, there maybe a possibility that it might not choose the fastest path, but this algorithm will surely guarantee you another path that maybe long but surely be the highest recommended move for the player to win.
3) Points based approach is the technique we used to calculate certain scores to score each successor state and use max heap for calculating the better score.

#### Further Improvements which can be done: 
Baiting! - I just found out that some moves maybe possible that can sacrifice smaller pieces at first to gain a huge advantage in the end game, as we see a lot of plays in chess that proves this point. A simple example would be to bait the smaller white pichu to black pikachu to allow the black pikachu to move ahead and devour white pichu, but later we can sort of tweak the algorithm such that we have either a white pikachu or white raichu waiting for that black pikachu to step on that index to make a move and jump over it gaining extra points for a small price to pay at the beginning.

## PART2:

### Workflow:

#### Data Preprocessing:
1) Downloaded the data set and checked for any missing values or any not so relevant information given in the text files, I found all the data to be relevant and there are no missing values.

2)In a text processing ML problem statement the words in the text themselves are the features of the model, hence I wrote a ‘clean_function’ function which loops an input list and 
a) Removes the words which doesn’t have any physical meaning but are just present in the sentence due to English grammar (like ourselves', 'you', "you're", "you've", "you'll", "you'd” etc. ) 
b) convert the sentence to lowercase(as we don’t want to create separate features for the same words of lower and upper case)
c)Replaced all the numbers, symbols like [!.?'' etc.,] Replaced with blanks
d)Cleared any additional spaces (if) are present before and after a sentence or a word.
I used regex to loop through the sentence and clear out characters, symbols which seemed not so relevant for our algorithm

#### Idea:
The core idea we wanted to implement to solve this classification problem using naive bayes algorithm is: 
1)We want to calculate the conditional probability of every word in each sentence in the train set with respect to if the word is present in sentences classified as deceptive/truthful
I.e., let’s say there is a word “wonderful” , using bag of words model we create 2 separate bag of words for all the words belongs to Deceptive and truthful in the training set , and we calculate the probability of the word ‘wonderful’ present in ‘deceptive bag of words’ and the probability the word ‘wonderful is present in ‘truthful bag of words’’ .
We do that by dividing the frequency of a word in the entire training set where label is ‘deceptive’ and where label is ‘truthful’
(count_of_occurance_of word/len(truth_reviews_in _train_data) and 
(count_of_occurance_of word/len(deceptive_reviews_in _train_data)
2)After calculating this value we append it’s value to a dictionary which has the keys as the bag of words (we create 2 dictionaries with keys as words in bag_of_truth_words and bag_of_deceptive_words.
3)These 2 dictionaries namely likelihood_of_words_decept,likelihood_of_words_truthful
are the main part of our solution as calculating these probability values is nothing but ‘training’ of our model.

#### Classifying the test data (predictions):
1)Now that we have out likelihood values of every relevant word in both classes, we use this to classify the test set data which the model has not seen so far.
2)We perform the same transformations we performed to clean the train data (Note: no information from the test data will be leaked to the algorithm in this process, this is just a preprocessing step) We clean the stop words , unnecessary symbols , grammatical words etc. 
3)Now we take this cleaned list of test_data and we split every review into words and check the probability of the word is in our likelihood_of_words_decept ,likelihood_of_words_truthful dictionaries.
4)We multiply the probabilities of each word in the review with the probabilities found for the word in both the dictionaries, finally we compare both these values and whichever is greater we classify the review as it belongs to that particular class.(as Naive bayes assumption is all the features are independent to each other , in a text processing problem statement the features are just the words)

#### Challenges faced:
1)While checking for the probabilities of the test_set words in the dictionaries we obtained from the training data likelihood_of_words_decept ,likelihood_of_words_truthful ,if we encounter a word in the test_set which is not present in the either of the dictionaries then this would give it a probability 0 and this would return a final value of 0 irrespective of other words present in the sentence , to fix this I have put a condition where if a word is not found in either of dictionaries , I simply skip including the word in my final probability calculation (in other words we just multiply by 1 if the word in test_set is not found in the likelihood dictionaries) - This fixed my issue 

2)In calculating ‘prob_of_truth’ or ‘prob_of_decept’ to append in our dictionaries on the training data, instead of just calculating (count)/(no_of_truth_reviews) or (count)/(no_of_decept_reviews) , we used a smoothing technique by adding 1 in the numerator to prevent a probability from being a ‘0’,
We used (count+1)/(no_of_truth_reviews) and (count+1)/(no_of_decept_reviews) to calculate the probabilities.
Another famous technique to fix this issue is ‘Laplace smoothing technique’ which also is a hyper parameter used in sklearn naive bayes algorithm (alpha), but we didnt use it in our code as smoothing just by adding 1 in the numerator performed pretty well on the test dataset.

#### Notable Observations:
1)The prior probabilities of each class turned out to be 0.5 each 
2)The bag of words after cleaning, removing the stop words from each review individually in each class from the train dataset, we got 
Truthful bag of words- 5568 words
deceptive bag of words- 5058 words
3)We calculated the conditional probabilities of each of these words belonging to either classes
4)On testing on our test_data we were able to get an accuracy of 86.25%



#### Further Improvements which can be done: 
As we designed the algorithm using no help from sklearn , nltk libraries , we were unable to perform techniques like stemming , lemmatization which we believe could significantly improve the performance of our model


References : 
1)https://www.youtube.com/watch?v=O2L2Uv9pdDA&ab_channel=StatQuestwithJoshStarmer
2)https://www.youtube.com/watch?v=HZGCoVF3YvM&t=313s&ab_channel=3Blue1Brown (This video changed our entire perspective on Naive Bayes!)
3)https://towardsdatascience.com/na%C3%AFve-bayes-spam-filter-from-scratch-12970ad3dae7
4)https://towardsdatascience.com/laplace-smoothing-in-na%C3%AFve-bayes-algorithm-9c237a8bdece




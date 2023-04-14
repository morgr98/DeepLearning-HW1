r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
**Your answer:**

1. false, we train our model on the training set and there can be a case the train and test sets has distribution differences so the test error is diferent from the train error = in-sample error.

2. false, for example if we are in classification problem with 2 classe {1,-1} if we split the data that the train will be all the samples with lable 1 we will get a tilted model that give 1 to all the samples when its not the case.

3. true, the cross validation is part of the learning rate so if we used the test set than the model is relaying on the test set, so the test set is no longer valid for testing.

4. false, after the cross validation we train the model on all the data with optimal hyperparameter and then we use the test set to get the proxy generalization error.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part1_q2 = r"""
**Your answer:**

No, our friend approch is not justified,
we can't use the test set to tune hyperparameters, for that we have the validation set. when we using the test set to choose the optimal $\lambda$ the test set is no longer valid as an proxy for the generalization error.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 1$

"""

# ==============
# Part 2 answers

part2_q1 = r"""
**Your answer:**
 
not necessarily, when k is to big (for example when k = m (num of samples)) the model predict each point to labled as the most common lable from all the samples, and its will let to poor accuracy. we can use cross-validation to get the best k.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part2_q2 = r"""
**Your answer:**
1. in order to estimate the generalization error we need to run the model on samples that the model hasn't see before, if we will find the parameters values based on the all training samples the optimal k will be 1 and we will get 100% accuracy because each dot is the closes neighbor of herself and that is not the case on unseen data. 

2. by choosing the best model based on the test accuracy we useing the test set as part of our training so the model is now tilted to fit the test set and we can not use the set test as an andipended set in order to astimate the generalization error. 

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
**Your answer:**
The goal of using  $\Delta$ is to help us to determine the margin size between the classes while using soft svm.
If we change the value of  $\Delta$ , we will need to change our *$W$* weights matrix in order to get the same
predictions depend on the boundaries that we get, therefore the value of $\Delta$ is arbitrary.


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q2 = r"""
**Your answer:**
1.The linear model gets from us a data and then try to learn the best representations of the classes by training on the data.
After training the data, the model will have a weight matrix that can classify test samples in order to predict the most similar class of the test samples.
As we can see in the example above, if in the data test there are some digits that look similar to another digits (like 1 or 7) so the model can mistake by classify one digit to not to the class that its belong.

2.
The difference between this model to the KNN- model is that when the model make the predictions on the data test,
the result in soft svm depends on all the data compared to in KNN that the result depends on only the k- cloests samples.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q3 = r"""
**Your answer:**
We think that the learning rate that we chose is good.
First, we can see that the loss-graph that we get is decreased almost monotonically and rapidly.
Second, we can assume that if the value of the learning rate was too high so we would get a graph with divergent behavior while jumping over the minimum without converging to it.
And if the value of the learning rate was too low, we would get a graph that has slowly progressing to the minimum, and should have a much bigger number of epoch in order to converge.

We think that probably the model is slightly overfitted.
As we can see in the graphs above, the loss function of the traning is smaller than of the validation, and the accuracy of the traning is bigger than the validation.
Also in the accuracy graph of the traning we can see that the accuracy still increase while the accuracy of the validation remains unchanged.
The gap between the traning and the validation is not so bad but maybe with another data test we can get much huge gap that can point on overfitting.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

# ==============
# Part 4 answers

part4_q1 = r"""
**Your answer:**

the optimal pattern is that all the dots are on the 'y=0' line because that means the model y_pred is equal to y for all the dots.
we can see from the plots that most of the dots are close to 0 means the model prediction was good, but some dots have a big error - after the CV the number of dots with
big error is decreas and the dots are closer to 0 as axpected.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q2 = r"""
**Your answer:**
1. It is still a linear model because the linerity of the model comes from that the liniar multipy of W in X and adding more columns in X doesn't effect the linear multipy.

2. Yes we can, the a simple example is on 2-D with dots in distance 1 and 2 from center (0,0), dots with distance 1 gets the lable 1 and dots with distance 2 get the lable -1. 
   without more feature the model can't separate the dots but if we will add the fature $x_1^2 + x_2^2$ the model could split the data with the line y = 3 for example.
   
3. if we are adding a non-linear features to our data, we will get that the decision boundary still be a hyperplane, but because the new features are non-linear, we can assume by looking them as more features in higher dimension.
So, we will get a new hyperplane which will separate our data in this higher space.
As a result, the new decision boundary probably will not be linear and because of that will not be a hyperplane in the orginial space.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q3 = r"""
**Your answer:**
1. np.linspace return evenly space numbers while np.logspace numbers on a log scale witch means on different scale level so using CV with np.logspace we get a bigger variaty of $\lambda$ values. If we wanted to get that variaty using np.linspace we would have to run the model many more times that means much more time, and time is money.

2. the $\lambda$ range has 20 different values, the degree range has 3 and k_fold is set to 3.
   so its total of 180 fits.    

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

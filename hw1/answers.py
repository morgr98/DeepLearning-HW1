r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""
**Your answer:**

1. false, we train our modle on the training set and there can be a case the train and test sets has distribution difference so the test error is not the in-sample error.

2. false, for example if we are in classification problem with 2 classe {1,-1} if we split the data that the test will be all the samples with lable 1 we will get a tilted modle that give 1 to all the samples when its not the case.

3. true, the cross validation is part of the lerning rate so if we used the test set than the modle is relaying on the test set so the test set is no longer valid for testing.

4. ??? 
false, the folds are part of the training set so the error can be tilted.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part1_q2 = r"""
**Your answer:**

Yes, the friend approch is justified,
becasue after adding regularization as much complex the w vector will be the bigger the error will be so the modle will get less complex function that fit the data so we will decrease the overfitting. by trying differents values of lambda he will make sure the modle won't underfit.

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
 
not necessarily, when k is to big (for example when k = m (num of samples) the modle predict each point to labled as the most common lable from all the samples, and its will let to poor accuracy. we can use cross-validation to get the best k usaully around 5.

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part2_q2 = r"""
**Your answer:**
1. in order to get an estimate the generalization error we need to run the modle on samples that the modle hasn't see before, if we will        find the parameters values based on the all samples we will get overfitting.
2. by choosing the best modle based on the test accuracy we useing the test set as part of our training modle so the modle is now tilted to    fit the test set and we can not use the set test as aundipended set in order to astimate the generalization error. 

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


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q3 = r"""
**Your answer:**


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

the optimal pattern is that all the dots are on the 'y=0' line because that means the model y_pred is equal to y got all the dots.
we can see from the pots that most of the dots are close to 0 means the model prediction was good, but some dots have a big error - after the CV the number of 
big error is decreas and the dots and closer to 0 as axpected.

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
   without more feature the model can't separate the dots but if we will add the fature x_1^2 + x_2^2 the model could split the data with th line y = 3 for example.
3. ??????????

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q3 = r"""
**Your answer:**
1. np.linspace return evenly space numbers while np.logspace numbers on a log scale witch means on different scale level so using CV with np.logspace we get a bigger variaty of lambda 
   values. If we wanted to get that variaty using np.linspace we would have to run the model many more times wich means longer time.
2. the lambda range has 20 different values, the degree range has 3 and k_fold is set to 3.
   so its total of 3*3*20 = 180 fits.    

Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

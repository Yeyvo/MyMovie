# For Python 2 / 3 compatability

# Toy dataset.
# Format: each row is an example.
# The last column is the label.
# The first two columns are features.
# Feel free to play with it by adding more features & examples.
# Interesting note: I've written this so the 2nd and 5th examples
# have the same features, but different labels - so we can see how the
# tree handles this case.

from __future__ import print_function
from subprocess import CREATE_NEW_CONSOLE
from numpy import math
import pandas as pd
import pickle
import os

recomendationTreeFilePath = 'decisionTree.data'



def unique_vals(rows, col):
    """Find the unique values for a column in a dataset."""
    return set([row[col] for row in rows])

def class_counts(rows):
    """Counts the number of each type of example in a dataset."""
    counts = {}  # a dictionary of label -> count.
    for row in rows:
        # in our dataset format, the label is always the last column
        label = row[0]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts

def is_numeric(value):
    """Test if a value is numeric."""
    return isinstance(value, int) or isinstance(value, float)

class Question:
    """A Question is used to partition a dataset.

    This class just records a 'column number' (e.g., 0 for Color) and a
    'column value' (e.g., Green). The 'match' method is used to compare
    the feature value in an example to the feature value stored in the
    question. See the demo below.
    """

    def __init__(self, column, value, header):
        self.column = column
        self.value = value
        self.header = header

    def match(self, example):
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.column]
        # print("####",val,"####")
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        # This is just a helper method to print
        # the question in a readable format.
        condition = "is"
        if is_numeric(self.value):
            condition = "More or equal"
        return "%s ?" % (
            enhancedQuestionHeader(self.header[self.column], condition, str(self.value)))

def partition(rows, question):
    """Partitions a dataset.

    For each row in the dataset, check if it matches the question. If
    so, add it to 'true rows', otherwise, add it to 'false rows'.
    """
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows

def gini(rows):
    """Calculate the Gini Impurity for a list of rows.

    There are a few different ways to do this, I thought this one was
    the most concise. See:
    https://en.wikipedia.org/wiki/Decision_tree_learning#Gini_impurity
    """
    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl**2
    return impurity

def info_gain(left, right, current_uncertainty):
    """Information Gain.

    The uncertainty of the starting node, minus the weighted impurity of
    two child nodes.
    """
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)

def find_best_split(rows, header):
    """Find the best question to ask by iterating over every feature / value
    and calculating the information gain."""
    best_gain = 0  # keep track of the best information gain
    best_question = None  # keep train of the feature / value that produced it
    current_uncertainty = gini(rows)
    n_features = len(rows[0]) - 1  # number of columns

    for col in range(1,n_features):  # for each feature != id

        values = set([row[col] for row in rows])  # unique values in the column

        for val in values:  # for each value
            question = Question(col, val, header)

            # try splitting the dataset
            true_rows, false_rows = partition(rows, question)

            # Skip this split if it doesn't divide the
            # dataset.
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            # Calculate the information gain from this split
            gain = info_gain(true_rows, false_rows, current_uncertainty)

            # You actually can use '>' instead of '>=' here
            # but I wanted the tree to look a certain way for our
            # toy dataset.
            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question

class Leaf:
    """A Leaf node classifies data.

    This holds a dictionary of class (e.g., "Apple") -> number of times
    it appears in the rows from the training data that reach this leaf.
    """

    def __init__(self, rows):
        for key, value in class_counts(rows).items():
            self.predictions = key
class Decision_Node:
    """A Decision Node asks a question.

    This holds a reference to the question, and to the two child nodes.
    """

    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch
def build_tree(rows, header):
    """Builds the tree.

    Rules of recursion: 1) Believe that it works. 2) Start by checking
    for the base case (no further information gain). 3) Prepare for
    giant stack traces.
    """

    # Try partitioing the dataset on each of the unique attribute,
    # calculate the information gain,
    # and return the question that produces the highest gain.
    gain, question = find_best_split(rows, header)

    # Base case: no further info gain
    # Since we can ask no further questions,
    # we'll return a leaf.
    if gain == 0:
        return Leaf(rows)

    # If we reach here, we have found a useful feature / value
    # to partition on.
    true_rows, false_rows = partition(rows, question)
    
    # Recursively build the true branch.
    true_branch = build_tree(true_rows, header)
    # Recursively build the false branch.
    false_branch = build_tree(false_rows, header)
    
    

    # Return a Question node.
    # This records the best feature / value to ask at this point,
    # as well as the branches to follow
    # dependingo on the answer.
    return Decision_Node(question, true_branch, false_branch)


def print_tree(node, spacing=""):
    """World's most elegant tree printing function."""

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        print (spacing + "We recommend you : ", node.predictions)
        return 

    # Print the question at this node
    print (spacing + str(node.question))
    
    # Call this function recursively on the true branch
    print (spacing + '--> True:')
    print_tree(node.true_branch, spacing + "  ")
    
    # Call this function recursively on the false branch 
    print (spacing + '--> False:')
    print_tree(node.false_branch, spacing + "  ")
    

def createTreeDict(node):
    L = {}
    #print(L[0], end = '')
    if isinstance(node, Leaf) :
        L["recommendation"]=  node.predictions
        L["true_branch"]={}
        L["false_branch"]={}
        # print(L)
        return L
    else:
        L["Question"]=node.question.__repr__() 
        L["true_branch"]=createTreeDict(node.true_branch)
        L["false_branch"]=createTreeDict(node.false_branch)
        # print(L)
        return L
    


def classify(row, node):
    """See the 'rules of recursion' above."""

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        return node.predictions

    # Decide whether to follow the true-branch or the false-branch.
    # Compare the feature / value stored in the node,
    # to the example we're considering.
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)

def print_leaf(counts):
    """A nicer way to print the predictions at a leaf."""
    total = sum(counts.values()) * 1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] = str(int(counts[lbl] / total * 100)) + "%"
    return probs

def enhancedQuestionHeader(headerName, cond, value):
    if(headerName == 'rating'):
        return "do you think that the movie should be rated " + value
    elif(headerName == 'genre'):
        return "do you think that it should be an " + value + " movie"
    elif(headerName == 'year'):
        return "do you think that it should have been produced after or in " + (value)
    elif(headerName == 'director'):
        return "do you think that the movie director should be " + value
    elif(headerName == 'star'):
        return "do you think that "+value + " has starred in the movie "
    elif(headerName == 'company'):
        return "do you think that the production company should be " + value
    elif(headerName == 'runtime'):
        return "do you think that the movie runtime should be more than " + round(value) + " minutes"
    return 'ERROR ('+headerName+') ' + value

    



# Evaluate
"""
testing_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 4, 'Apple'],
    ['Red', 2, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]
for row in testing_data:
    print ("Actual: %s. Predicted: %s" %
           (row[-1], print_leaf(classify(row, my_tree))))
"""

def getModel():
    if ( not os.path.exists(recomendationTreeFilePath)) :
        df = pd.read_csv('RecommendationDataset/new-movies.csv',delimiter=',')  
        #training_data = [[row[col] for col in df.columns] for row in df.to_dict('records')]
        # Column labels.
        # These are used only to print the tree.


        training_data = [list(row) for row in df.values]
        # print(training_data)
        header = list(df.columns)
        my_tree = build_tree(training_data, header)
        dict = createTreeDict(my_tree)

        decisionTreeFile = open(recomendationTreeFilePath,"wb")
        pickle.dump(dict,decisionTreeFile)
        return dict
    else :
        # df = pd.read_csv('RecommendationDataset/new-movies.csv',delimiter=',')
        # header = list(df.columns)        
        decisionTreeFile = open(recomendationTreeFilePath, 'rb')
        Tree = pickle.load(decisionTreeFile)
        decisionTreeFile.close()
        return Tree

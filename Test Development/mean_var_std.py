# Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, 
# max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
# The input of the function should be a list containing 9 digits. 
# The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, 
# max, min, and sum along both axes and for the flattened matrix.

import numpy as np

example_matrix = [0,1,2,3,4,5,6,7,8]

#creates new dictionary with {}, or by doing dict()
results = {
    'mean': [],
    'variance': [],
    'standard deviation': [],
    'max' : [],
    'min' : [],
    'sum' : []
}

def calculate(nums):

    try:
        if (len(nums) == 9):
            ##print("Great!")

            reshaped = np.reshape(nums,(3,3))
            mean1 = reshaped.mean(axis = 0, dtype = float)
            mean2 = reshaped.mean(axis = 1, dtype = float)
            meanresults = [mean1.tolist(),mean2.tolist(),reshaped.mean().tolist()]
            results.update({'mean': meanresults})

            #variance
            results.update({'variance' : [np.var(reshaped,axis = 0).tolist(),np.var(reshaped,axis = 1).tolist(),np.var(reshaped).tolist()]})
            #standard deviation
            results.update({'standard deviation' : [np.std(reshaped,axis = 0).tolist(),np.std(reshaped,axis = 1).tolist(),np.std(reshaped).tolist()]})
            #max
            results.update({'max' : [np.max(reshaped,axis = 0).tolist(),np.max(reshaped,axis = 1).tolist(),np.max(reshaped).tolist()]})
            #min
            results.update({'min' : [np.min(reshaped,axis = 0).tolist(),np.min(reshaped,axis = 1).tolist(),np.min(reshaped).tolist()]})
            #sum
            results.update({'sum' : [np.sum(reshaped,axis = 0).tolist(),np.sum(reshaped,axis = 1).tolist(),np.sum(reshaped).tolist()]})
            print(results)
        else:

            print("List must contain nine numbers.")
    except Exception as error:
        print("Something went wrong, whoops!")
        print(error)


##calculate(example_matrix)






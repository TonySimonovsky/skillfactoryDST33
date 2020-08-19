import numpy as np


def binary_search(number, min_number=1, max_number=100):
    '''Using binary search algorythm to guess the number'''

    attempt = 0
    predict = int(max_number/2) # setting first prediction as the middle between the maximum possible number
    prediction_borders = [min_number,max_number] # set the borders between which we make predictions

    # each time we make an attempt to guess we narrowing search window for the next attempt
    while number != predict:
        if number > predict:
            prediction_borders[0] = predict
            predict = prediction_borders[0] + int((prediction_borders[1]-prediction_borders[0])/2)
            # catering for the case where the number equals initial top border of the window
            if prediction_borders[1]-prediction_borders[0] == 1:
                predict = prediction_borders[1]
        elif number < predict:
            prediction_borders[1] = predict
            predict = prediction_borders[0] + int((prediction_borders[1]-prediction_borders[0])/2)
        
        attempt += 1
        
    return(attempt)


def algorythm_test(algorythm, test_cycles=1000, min_number=1, max_number=100):
    '''Testing the algorythm `test_cycles` times.'''
    
    attempts_required = []
    np.random.seed(1) # setting RANDOM SEED for experiment to be reproducible
    random_array = np.random.randint(min_number, max_number+1, size=(test_cycles))

    for number in random_array:
        attempts_required.append(algorythm(number))

    attempts_avg = int(np.mean(attempts_required))
    print(f"Your algorythm guesses the number on average within {attempts_avg} attempts.")

    return(attempts_avg)


algorythm_test(binary_search)

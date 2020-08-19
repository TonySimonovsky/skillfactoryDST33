import numpy as np

def binary_search(number, min_number=1, max_number=100):
    '''Using binary search algorythm to guess the number'''
    attempt = 0
    # setting first prediction as the middle between the maximum possible number
    predict = int(max_number/2)
    # set the borders between which we make predictions
    prediction_borders = [min_number,max_number]

    # in the cycle each attempt we make - we are basically narrowing search window
    while number != predict:
        if number > predict:
            prediction_borders[0] = predict
            predict = prediction_borders[0] + int((prediction_borders[1]-prediction_borders[0])/2)#prediction_borders[0] + int((prediction_borders[1]-predict)/2)
            if prediction_borders[1]-prediction_borders[0] == 1:
                predict = prediction_borders[1]
        elif number < predict:
            prediction_borders[1] = predict
            predict = prediction_borders[0] + int((prediction_borders[1]-prediction_borders[0])/2)
        attempt+=1
        
    return(attempt)
        
        
def algorythm_test(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(binary_search(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

algorythm_test(binary_search)

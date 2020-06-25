def prediction_model(pclass, sex, age, sibsp, parch, fare, embarked_q, embarked_s):
    '''
    INPUTS
    passenger class (pclass), sex, age, siblings onboard(sibsp), parents onboard(parch), ticker fare (fare),
    embarked port (embarked_q = 1 -> Queenstown; embarked_s = 1 -> Southhampton; else -> Cherbourg)

    OUTPUTS
    prediction { 1 -> survided, 0 -> not survived}

    '''
    import pickle
    x = [[pclass, sex, age, sibsp, parch, fare, embarked_q, embarked_s]]
    lr_model = pickle.load(open('titanic_model.sav', 'rb'))
    predictions = lr_model.predict(x)

    return predictions
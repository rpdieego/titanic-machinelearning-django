from django.shortcuts import render
from . import fake_model
from . import ml_predict

def home(request):
    return render(request, 'index.html')

def results(request):

    # get data from form
    user_input_age = int(request.GET['age'])
    user_input_sex = int(request.GET['sex'])
    user_input_pclass = int(request.GET['pclass'])
    user_input_sibsp = int(request.GET['sibsp'])
    user_input_parch = int(request.GET['parch'])
    user_input_fare = float(request.GET['fare'])
    user_input_embarked = request.GET['embarked']

    user_input_embarked_q = 0
    user_input_embarked_s = 0

    if user_input_embarked == 'Q':
        user_input_embarked_q = 1
    elif user_input_embarked == 'S':
        user_input_embarked_s = 1


    # input data into model
    prediction = fake_model.fake_predict(user_input_age)

    ml_prediction = ml_predict.prediction_model(user_input_pclass,
                                                user_input_sex,
                                                user_input_age,
                                                user_input_sibsp,
                                                user_input_parch,
                                                user_input_fare,
                                                user_input_embarked_q,
                                                user_input_embarked_s)

    # Label it into a string
    if ml_prediction == 1:
        ml_prediction_string = 'Survived'
    elif ml_prediction == 1:
        ml_prediction_string = 'Have not Survived'
    else:
        ml_prediction_string = 'Error'


    return render(request, 'result.html', {'user_age':user_input_age,
                                           'prediction':prediction,
                                           'ml_prediction':ml_prediction_string})

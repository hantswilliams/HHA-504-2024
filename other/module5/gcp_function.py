import functions_framework

@functions_framework.http
def hello_http(request):

    request_json = request.get_json(silent=True)
    request_args = request.args

    ## this is for looking into the BODY of the http request 
    if request_json and 'systolic' in request_json and 'diastolic' in request_json:
        systolic = request_json['systolic']
        diastolic = request_json['diastolic']
    
    ## this is for looking to the parameters of the http request 
    elif request_args and 'systolic' in request_args and 'diastolic' in request_args:
        systolic = request_args['systolic']
        diastolic = request_args['diastolic']
    
    else:
        return 'Please provide systolic and diastolic values in the request arguments or JSON body.'

    try:
        systolic = float(systolic)
        diastolic = float(diastolic)
    except ValueError:
        return 'Systolic and diastolic values must be valid numbers.'

    # Define the ranges for systolic blood pressure
    if systolic < 90:
        systolic_status = 'below the normal range'
    elif 90 <= systolic <= 120:
        systolic_status = 'within the normal range'
    else:
        systolic_status = 'above the normal range'

    return f'Systolic: {systolic} mmHg is {systolic_status}. Diastolic: {diastolic} mmHg.'


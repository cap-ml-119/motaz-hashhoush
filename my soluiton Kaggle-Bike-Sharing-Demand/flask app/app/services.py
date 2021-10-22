
__required = [
    "hour",
    "humidity",
    "month",
    "temp",
    "weather",
    "windspeed",
    "workingday"
]


def check_required_features(data: dict):
    """function to check that all the features required for prediction are present

    Args:
        data (dict): [features user sended]

    Raises:
        Exception: [if some feature not found]
    """
    features = data.keys()

    for feature in features:
        if feature not in __required:
            raise Exception(
                f'some feature not found. feature required is {__required}')


def get_data_of_features(data: dict):
    """function to extract value from request

    Args:
        data (dict): [json request contain the features and values]

    Returns:
        [list]: [contain values only without the features]
    """

    values = []
    for feature, value in data.items():
        values.append(value)
        print(value)

    return values

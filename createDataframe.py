import pandas as pd
import json
from pandas import json_normalize


def convert_json_to_dict(filename):
    #Converting Json to Python dictionary
    with open(filename, 'r') as JSON:
        json_dict = json.load(JSON)
    return json_dict


def convert_dict_to_df(filename):
    # Converting Python Dict to Pandas Dataframe
    return pd.json_normalize(convert_json_to_dict(filename))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
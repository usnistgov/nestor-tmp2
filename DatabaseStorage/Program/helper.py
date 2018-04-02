import yaml
from datetime import datetime

# def openYAMLFile(yaml_path, dict=None):
#     """
#     open a Yaml file based on the given path
#     :return: a dictionary
#     """
#     try:
#         with open(yaml_path, 'r') as yamlfile:
#             config = yaml.load(yamlfile)
#             print("yaml file open")
#         return config
#     except FileNotFoundError:
#         with open(yaml_path, 'w') as yamlfile:
#             yaml.dump(dict, yamlfile)
#             print("yaml file created")
#         return dict

def openYAMLFile(yaml_path):
    """
    open a Yaml file based on the given path
    :return: a dictionary
    """
    with open(yaml_path, 'r') as yamlfile:
        config = yaml.load(yamlfile)
        print("yaml file open")
    return config


def isoStringToDate(date):
    """
    convert a ISO8601 String date format to a DateTime format

    :param date: a ISO date in String format
    :return: a DateTime date
    """
    try:
        return datetime(year=int(date[:4]), month=int(date[5:7]), day=int(date[8:10]), hour=int(date[11:13]), minute=int(date[14:16]))
    except AttributeError and ValueError:
        pass

    try:
        return datetime(year=int(date[:4]), month=int(date[5:7]), day=int(date[8:10]), hour=int(date[11:13]))
    except AttributeError and ValueError:
        pass

    try:
        return datetime(year=int(date[:4]), month=int(date[5:7]), day=int(date[8:10]))
    except AttributeError and ValueError:
        pass

    return None


def timeBetweenIsoStringDates(date1, date2):
    """
    return the time spen between date1 and date2

    :param date1: ISO string format of the early date
    :param date2: ISO string format of the last date
    :return: timedelta of the difference
    """
    if date1 is None or date1 is "" or date2 is None or date2 is "":
        return None
    if date1 > date2:
        return None
    return isoStringToDate(date2) - isoStringToDate(date1)

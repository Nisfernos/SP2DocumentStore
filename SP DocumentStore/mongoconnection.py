import pymongo


def localmongoconnection(connectionstring = "mongodb://localhost:27017/"):
    """This function will make a connection with a local mongoDB server.
    Input: connection string (optional)
    Output: pymongo.mongo_client.MongoClient"""
    client = pymongo.MongoClient(f"{connectionstring}")
    return client


def mongodatarequest(client, database, collection):
    """This function will return a dataset from a specific database collection.
    Input: client, databasename(s), collectionname(s)
    Returns: Data"""
    db = client[f"{database}"]
    col = db[f"{collection}"]
    data = col.find()
    return data


def firstentry(data, identry, nameentry, mini=1000000000):
    """This function will return the value of the variable nameentry, with the smallest identry.
    Input: Dataset(iterative object with dictionaries), identry(s), nameentry(s), start of minimum value(optional)
    Returns: string"""
    for dictionary in data:
        if int(dictionary[identry]) < int(mini):
            mini = dictionary[identry]
            firstentryinjson = dictionary[nameentry]
    return firstentryinjson


def firstentrywithletter(data, entryname, letter, mini="zz"):
    """Returns the first entry in a json file that starts with a given letter.
    Input: Dataset(iterative object with dictionaries), entryname(s), letter(s, l=1), startvalue minimum (optional)
    Returns: string"""
    for dictionary in data:
        if dictionary[entryname][0].lower() == letter:
            if dictionary[entryname].lower() < mini.lower():
                mini = dictionary[entryname]
                returnentry = dictionary[entryname]
    return returnentry


def averageindoublejson(data, entryname1, entryname2):
    """This will return the average of an integer in a nested json file
    :param data: iterative object with dictionaries
    :param entryname1: string of shallow key
    :param entryname2: string of deep key
    :return: float
    """
    total = 0
    elements = 0
    for product in data:
        total += product[entryname1][entryname2]
        elements += 1
    return total/elements



from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    id = ""
    name = "0"
    age = -1
    occupation = "0"

    if 'id' in request.args:
        id = request.args['id']
    if 'name' in request.args:
        name = request.args['name']
    if 'age' in request.args:
        age = int(request.args['age'])
    if 'occupation' in request.args:
        occupation = request.args['occupation']

    if (id == "") and (name == "0") and (age == -1) and (occupation == "0"):
        return USERS

    search_results = []

    for people in USERS:
        if people['id'] == id:
            search_results.append(people)
        elif people['name'].find(name) > -1:
            search_results.append(people)
        elif people['age'] == age or people['age'] == age+1 or people['age'] == age-1:
            search_results.append(people)
        elif people['occupation'].find(occupation) > -1:
            search_results.append(people)

    return search_results

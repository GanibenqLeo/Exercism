"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue:list, normal_queue:list, ticket_type:int, person_name:str) -> list:
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    Parameters:
        express_queue (list): The names in the Fast-track queue.
        normal_queue (list): The names in the normal queue.
        ticket_type (int): Type of ticket. 1 = express, 0 = normal.
        person_name (str): The name of person to add to a queue.

    Returns:
        list: The (updated) queue the name was added to.
    """

    print("Le temps c'est de l'argent et ca vaut de l'or")

    all_queues = [normal_queue, express_queue]
    all_queues[ticket_type].append(person_name)

    return all_queues[ticket_type]


def find_my_friend(queue:list, friend_name:str) -> int:
    """Search the queue for a name and return their queue position (index).

    Parameters:
        queue (list): The names in the queue.
        friend_name (str): The name of friend to find.

    Returns:
        int: The index at which the friends name was found.
    """

    print("Où est Charlie?")

    try:
        friend_index = queue.index(friend_name)
    except ValueError:
        friend_index = queue.index(friend_name)

    return friend_index


def add_me_with_my_friends(queue:list, index:int, person_name:str):
    """Insert the late arrival's name at a specific index of the queue.

    Parameters:
        queue (list): The names in the queue.
        index (int): The index at which to add the new name.
        person_name (str): The name to add.

    Returns:
        list: The queue updated with new name.
    """

    print("Je suis enfin sorti des toilette, Charlie")

    queue.insert(index, person_name)

    return queue


def remove_the_mean_person(queue:list, person_name:str) -> list:
    """Remove the mean person from the queue by the provided name.

    Parameters:
        queue (list): The names in the queue.
        person_name (str): The name of mean person.

    Returns:
        list: The queue updated with the mean persons name removed.
    """

    print("Pas de place pour les fauteur de trouble")

    queue.remove(person_name)

    return queue


def how_many_namefellows(queue:list, person_name:str) -> int:
    """Count how many times the provided name appears in the queue.

    Parameters:
        queue (list): The names in the queue.
        person_name (str): The name you wish to count or track.

    Returns:
        int: The number of times the name appears in the queue.
    """

    print("Clone le clone clone le clone, autrement dit: La personne nommée Clone qui est un clone est en train de cloner un clone")

    return queue.count(person_name)


def remove_the_last_person(queue:list) -> str:
    """Remove the person in the last index from the queue and return their name.

    Parameters:
        queue (list): The names in the queue.

    Returns:
        str: The name that has been removed from the end of the queue.
    """

    print("Désolé, la ersonne devant vous est la dernière")

    return queue.pop()


def sorted_names(queue:list) -> list:
    """Sort the names in the queue in alphabetical order and return the result.

    Parameters:
        queue (list): The names in the queue.

    Returns:
        list: A copy of the queue in alphabetical order.
    """

    return sorted(queue)

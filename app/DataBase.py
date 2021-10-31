from datetime import datetime
import uuid

# list the tasks be stored
__data_base = []


def add_todo(content: str, status: int) -> bool:
    """This function adds a task to the database
       and creates a unique ID for this task

    Args:
        content (str): [content of task]
        status (int): [status of task: 0 ->PENDING, 1->DONE, 2->CANCELED]

    Returns:
        bool: [The function return true if added successfully]
        bool: [return False if there is an error in status]
    """

    current_status = ""

    if status < 0 or status > 2:
        return False

    if status == 0:
        current_status = "PENDING"
    elif status == 1:
        current_status = "DONE"
    else:
        current_status = "CANCELED"

    __data_base.append({
        "content": content,
        "status": current_status,
        "time_created": datetime.now().date().today(),
        "todo_id": uuid.uuid4().int
    })

    return True


def delete_todo(id: int) -> bool:
    """This function removes a task from the database

    Args:
        id (int): [uuid of todo that we want to remove it from the list]

    Returns:
        bool: [return True if added successfully other False]
    """

    for i in __data_base:
        if i['todo_id'] == id:
            __data_base.remove(i)
            return True

    return False


def update_todo(content: str, status: int, id: int) -> tuple:
    """this function update by specific id

    Args:
        content (str): [content of task that we want to update it]
        status (int): [status of task that we want to update it]
        id (int): [uuid of task that we want to update it from the data base]

    Returns:
        tuple: [return (true, 0) if updatetd successfully]
        tuple: [return (False, 1) if if there is an error in status range]
        tuple: [return (False, 2) if id not found]
    """

    current_status = ""

    if status < 0 or status > 2:
        return False, 1

    if status == 0:
        current_status = "PENDING"
    elif status == 1:
        current_status = "DONE"
    else:
        current_status = "CANCELED"

    for i in __data_base:
        if i['todo_id'] == id:
            i['content'] = content
            i['status'] = current_status
            return True, 0

    return False, 2


def get_todos() -> list:
    """return all tasks

    Returns:
        list: [Contains tasks and each task is a dictionary object]
    """
    return __data_base

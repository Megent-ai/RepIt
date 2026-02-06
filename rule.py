"""
User role detection module.

Determines whether a Telegram user is an Admin, Teacher, Student,
or Unknown based on their Telegram ID.
"""

admins = {
    "2116090154"
}

teachers = {
    "2116090154"
}

students = {
    "7684908170"
}


def who(user_id: str) -> str:
    """
    Identify the role of a user.

    Args:
        user_id (str): Telegram user ID

    Returns:
        str: User role (Admin, Teacher, Student, or Unknown)
    """
    if user_id in admins:
        return "__Admin__"
    elif user_id in teachers:
        return "__Teacher__"
    elif user_id in students:
        return "__Student__"
    else:
        return "__Unknown__"

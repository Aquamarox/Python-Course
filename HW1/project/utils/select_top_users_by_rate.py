from typing import List
from models.user import User


def select_top_users_by_rate(users: List[User], top_size: int) -> List[User]:
    if top_size <= 0:
        return []
    
    sorted_users = sorted(users, key=lambda x: x.rate, reverse=True)
    return sorted_users[:top_size]

import uuid
from typing import Union


class User:
    def __init__(self, name: str):
        self.id = uuid.uuid4()
        self.name = name
        self.comments_count = 0
        self.rate = 0
        self.is_banned = False

    def edit_name(self, new_name: str) -> None:
        self.name = new_name

    def increment_rate(self) -> None:
        if not self.is_banned:
            self.rate += 1

    def ban_user(self) -> None:
        self.is_banned = True

    def unban_user(self) -> None:
        self.is_banned = False

    def __repr__(self) -> str:
        status = "banned" if self.is_banned else "active"
        return (f"User(id={self.id}, "
                f"name='{self.name}', "
                f"rate={self.rate}, "
                f"comments={self.comments_count}, "
                f"status='{status}')")

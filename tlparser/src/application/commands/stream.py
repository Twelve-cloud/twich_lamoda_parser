"""
stream.py: File, containing twich stream commands.
"""


from dataclasses import dataclass
from application.commands.base import Command


@dataclass(frozen=True)
class ParseTwichStream(Command):
    user_login: str


@dataclass(frozen=True)
class DeleteTwichStream(Command):
    user_login: str

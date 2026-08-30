from enum import Enum
# Enums
class Category(Enum):
    MERN = "MERN NESTJS Fullstack"
    PYTHON= "AI python Fullstack"

# Database

students={
    3 : {"id": 3, "name": "Justin", "age": 26, "category": Category.MERN},
    12 : {"id": 3, "name": "David", "age": 28, "category":Category.MERN},
    14 : {"id": 3, "name": "Max", "age": None, "category":Category.PYTHON},
    23 : {"id": 3, "name": "Justin", "age": 22, "category":Category.PYTHON},
}
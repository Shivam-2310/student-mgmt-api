from bson import ObjectId
from .database import get_database
from .models import StudentCreate, StudentUpdate


class StudentCRUD:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db['students']

    def create_students(self, student: StudentCreate):
        student_dict = student.dict()
        result = self.collection.insert_one(student_dict)
        return str(result.inserted_id)

    def list_students(self, country: str = None, age: int = None):
        query = {}
        if country:
            query['address.country'] = country
        if age is not None:
            query['age'] = {'$gte': age}

        students = list(self.collection.find(query))
        return [
            {"name": student['name'], "age": student['age']}
            for student in students
        ]

    def get_student(self, student_id: str):
        student = self.collection.find_one({"_id": ObjectId(student_id)})
        if not student:
            return None

        student['id'] = str(student['_id'])
        del student['_id']
        return student

    def update_student(self, student_id: str, student_update: StudentUpdate):
        update_data = {k: v for k, v in student_update.dict().items() if v is not None}

        result = self.collection.update_one(
            {"_id": ObjectId(student_id)},
            {"$set": update_data}
        )

        return result.modified_count > 0

    def delete_student(self, student_id: str):
        result = self.collection.delete_one({"_id": ObjectId(student_id)})
        return result.deleted_count > 0

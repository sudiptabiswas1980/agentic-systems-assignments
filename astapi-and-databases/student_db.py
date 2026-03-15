import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, CheckConstraint, insert, select, update, delete

# 1. Create database connection (SQLite creates a local file named school.db)
DATABASE_URL = "sqlite:///school.db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# 2. Define the students table
students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('age', Integer, CheckConstraint('age >= 18')),
    Column('city', String(100), nullable=True)
)

def run_operations():
    # Using 'connect' for Core operations
    with engine.connect() as connection:
        # Create students table
        metadata.create_all(engine)
        print("--- Table created successfully ---")

        # 3. Insert 3 student records
        # Note: SQLite requires a list of dicts for multiple inserts in Core
        ins_query = insert(students)
        student_data = [
            {"name": "Rahul", "age": 21, "city": "Mumbai"},
            {"name": "Anjali", "age": 19, "city": "Delhi"},
            {"name": "Vikram", "age": 22, "city": "Bangalore"}
        ]
        connection.execute(ins_query, student_data)
        connection.commit() # Important for persisting changes
        print("Inserted 3 records.")

        # 4. Fetch all students
        print("\n--- Current Students ---")
        fetch_query = select(students)
        results = connection.execute(fetch_query).fetchall()
        for row in results:
            print(row)

        # 5. Update city of student whose name = "Rahul"
        upd_query = update(students).where(students.c.name == "Rahul").values(city="Pune")
        connection.execute(upd_query)
        connection.commit()
        print("\nUpdated Rahul's city to Pune.")

        # 6. Delete student whose age < 20
        del_query = delete(students).where(students.c.age < 20)
        connection.execute(del_query)
        connection.commit()
        print("Deleted students aged under 20 (Anjali).")

        # Final verification
        print("\n--- Final Student Records ---")
        final_results = connection.execute(select(students)).fetchall()
        for row in final_results:
            print(row)

if __name__ == "__main__":
    run_operations()
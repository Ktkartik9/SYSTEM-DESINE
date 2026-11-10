# Python OOP – Relationships Between Classes

## 1. Aggregation

### What is Aggregation?

- Aggregation is a type of relationship between two classes.
- It represents a **Has-A relationship**.
- One class contains a reference to another class.
- Both objects can exist independently.
- If the parent object is deleted, the child object still exists.

### Example: Student and Department

- A Department has multiple Students.
- Students can exist without a Department.
- Deleting the Department does not delete the Students.

### Important Points

- Represents a weak Has-A relationship.
- Both objects have independent lifecycles.
- One object can use another object's functionality.

---

## 2. Association

### What is Association?

- Association represents a relationship between two independent classes.
- One object uses another object to perform a task.
- Both objects can exist independently.
- It does not represent ownership.

### Example: Teacher and Student

- A Teacher teaches a Student.
- A Student can exist without a Teacher.
- A Teacher can exist without a Student.
- Both objects have their own independent lifecycles.

### Important Points

- Represents a relationship between objects.
- Both objects are independent.
- One object interacts with another object.
- It can be one-to-one, one-to-many, or many-to-many.

---

## 3. Composition

### What is Composition?

- Composition is a strong type of Has-A relationship.
- One class owns another class.
- The contained object is created inside the owner class.
- The contained object's lifecycle is closely connected to the owner's lifecycle.

### Example: Car and Engine

- A Car has an Engine.
- The Engine is created inside the Car constructor.
- The Engine belongs to the Car in this example.
- When the Car object is deleted and no other references exist, its Engine can also be garbage-collected.

### Important Points

- Represents a strong Has-A relationship.
- Shows ownership between objects.
- Objects have closely connected lifecycles.
- Commonly used when one object is a necessary part of another.

---

## 4. Dependency

### What is Dependency?

- Dependency represents a relationship where one class temporarily uses another class.
- One object depends on another object to perform a particular operation.
- It does not own the other object.
- Both objects can exist independently.

### Example: Printer and Document

- A Printer prints a Document.
- The Document is passed as an argument to the `print_document()` method.
- The Printer does not create or own the Document.
- The Document can exist without the Printer.

### Important Points

- Represents a Uses-A relationship.
- Objects are independent.
- One class uses another class temporarily.
- Dependency is commonly implemented using method parameters.

---

## Difference Between All Relationships

| Relationship | Meaning | Example |
|---|---|---|
| Association | Interaction | Teacher – Student |
| Aggregation | Weak Has-A | Department – Student |
| Composition | Strong Has-A | Car – Engine |
| Dependency | Uses-A | Printer – Document |

## Quick Revision

- **Association:** One object interacts with another object.
- **Aggregation:** One object contains another object, but both can exist independently.
- **Composition:** One object owns another object, with closely connected lifecycles.
- **Dependency:** One object temporarily uses another object.

## Conclusion

These four relationships are important concepts in Object-Oriented Programming (OOP) and Low-Level Design (LLD).

They help us understand how different classes interact with each other and how objects are connected in real-world applications.
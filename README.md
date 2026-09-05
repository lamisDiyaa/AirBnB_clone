# AirBnB Clone - The Console

## Description of the Project
The **AirBnB Clone** project starts with building a command-line interpreter (console) to manage persistent objects across the system. This initial phase lays the backend groundwork for data serialization and manipulation without a graphical user interface.

Persistent objects handled by this engine include:
* `BaseModel`
* `User`
* `State`
* `City`
* `Amenity`
* `Place`
* `Review`

All instances are automatically serialized and deserialized into a JSON file storage system (`file.json`).

---

## Description of the Command Interpreter
The command interpreter is a custom shell application built using Python's `cmd` module. It allows developers and administrators to manage storage objects interactively or via scripts.

### Capabilities:
* **Create** new objects.
* **Retrieve** an object from a file using class name and `id`.
* **Perform operations** on objects (count, compute stats).
* **Update** attributes of existing objects.
* **Destroy** objects permanently from storage.

---

## How to Start It

1. Make sure `console.py` has executable permissions:
   ```bash
   chmod +x console.py

# msaccessdb

A pure Python module to create a new (empty) Access database. 
Potentially of interest to `pyodbc` users who:

- switched from `pypyodbc` and miss having the `pypyodbc.win_create_mdb` method (see Note 2, below), 

- need to create a new Access database so they can dump information into it, or

- want to create a temporary database to help work around issues regarding performance, prevent "bloat" in the 
main database, or avoid the dreaded *"Operation must use an updateable query."* error message.
  
**Usage:**

    import msaccessdb
    msaccessdb.create(r'C:\path\to\new.accdb')
    
**Notes:**

1. No effort is made to prevent overwriting an existing file.

2. This module simply creates the file. It doesn't automatically connect to it using `pyodbc` (or anything else).


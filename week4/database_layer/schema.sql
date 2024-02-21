CREATE TABLE Role (
      id INTEGER PRIMARY KEY,
      role_name TEXT
);
CREATE TABLE User (
      id INTEGER PRIMARY KEY,
      first_name TEXT,
      last_name TEXT,
      email TEXT,
      role INTEGER,
      FOREIGN KEY (role) REFERENCES Role(id)
);
CREATE TABLE Subject (
     id INTEGER PRIMARY KEY,
     title TEXT,
     subject_leader INTEGER,
     FOREIGN KEY (subject_leader) REFERENCES User(id)
);
CREATE TABLE Course (
   id INTEGER PRIMARY KEY,
   award TEXT,
   title TEXT,
   course_leader INTEGER,
   subject_id INTEGER,
   FOREIGN KEY (course_leader) REFERENCES User(id),
   FOREIGN KEY (subject_id) REFERENCES Subject(id)
);
CREATE TABLE Module (
    id INTEGER PRIMARY KEY,
    code TEXT,
    title TEXT,
    level INTEGER,
    module_leader INTEGER,
    course_id INTEGER,
    FOREIGN KEY (module_leader) REFERENCES User(id),
    FOREIGN KEY (course_id) REFERENCES Course(id)
);
CREATE TABLE ModuleTutor (
      id INTEGER PRIMARY KEY,
      user_id INTEGER,
      module_id INTEGER,
      FOREIGN KEY (user_id) REFERENCES User(id),
      FOREIGN KEY (module_id) REFERENCES Module(id)
);


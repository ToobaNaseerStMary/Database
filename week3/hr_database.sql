CREATE TABLE "department" (
  "department_id" INTEGER PRIMARY KEY,
  "department_name" TEXT,
  "manager_id" INTEGER,
  "location_id" INTEGER
);

CREATE TABLE "employee" (
  "employee_id" INTEGER PRIMARY KEY,
  "first_name" TEXT,
  "last_name" TEXT,
  "email" TEXT UNIQUE,
  "phone_number" TEXT,
  "hire_date" DATE,
  "job_title_id" INTEGER,
  "salary" REAL,
  "department_id" INTEGER
);

CREATE TABLE "job_title" (
  "job_title_id" INTEGER PRIMARY KEY,
  "title_name" TEXT,
  "description" TEXT,
  "base_salary" REAL
);

CREATE TABLE "employee_task" (
  "employee_id" INTEGER,
  "task_id" INTEGER,
  PRIMARY KEY ("employee_id", "task_id")
);

CREATE TABLE "location" (
  "location_id" INTEGER PRIMARY KEY,
  "city" TEXT,
  "state" TEXT,
  "country" TEXT
);

CREATE TABLE "task" (
  "task_id" INTEGER PRIMARY KEY,
  "task_name" TEXT,
  "description" TEXT
);

ALTER TABLE "employee" ADD FOREIGN KEY ("job_title_id") REFERENCES "job_title" ("job_title_id");

ALTER TABLE "employee" ADD FOREIGN KEY ("department_id") REFERENCES "department" ("department_id");

ALTER TABLE "department" ADD FOREIGN KEY ("manager_id") REFERENCES "employee" ("employee_id");

ALTER TABLE "department" ADD FOREIGN KEY ("location_id") REFERENCES "location" ("location_id");

ALTER TABLE "employee_task" ADD FOREIGN KEY ("employee_id") REFERENCES "employee" ("employee_id");

ALTER TABLE "employee_task" ADD FOREIGN KEY ("task_id") REFERENCES "task" ("task_id");

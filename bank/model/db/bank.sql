CREATE table if not EXISTS bank(
    id integer PRIMARY KEY AUTOINCREMENT,
    title text,
    branch text,
    description text,
    balance integer,
    employee number integer
);
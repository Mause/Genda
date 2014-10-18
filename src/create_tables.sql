CREATE TABLE IF NOT EXISTS users (
    uid integer primary key autoincrement,
    username text,
    password text
);

CREATE TABLE IF NOT EXISTS genders (
    gid integer primary key autoincrement,
    name text
);

CREATE TABLE IF NOT EXISTS pronoun (
    pid integer primary key autoincrement,
    gid integer,

    object_word text, -- them
    subject_word, -- they
    self_word text, -- themself
    owner_word text -- their

    foreign key (gid) references genders(gid)
);

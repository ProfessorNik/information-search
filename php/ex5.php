<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Создание таблицы notebook</title>
</head>
<body>
<?php
include "connect.inc";
global $conn;
$result = pg_query($conn, "
INSERT INTO notebook (name, city, address, birthday, mail)
VALUES ('John Smith', 'New York', '123 Main St', '1990-05-15', 'john@example.com'),
    ('Alex Johnson', 'London', '456 Elm St', '1993-07-12', 'alex@example.com'),
    ('Sarah Brown', 'Paris', '789 Oak St', '1991-02-28', 'sarah@example.com');") or die("Ошибка при вставке записей");

print "Все ок!";
include "disconnect.inc";
?>
</body>
</html>
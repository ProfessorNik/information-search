<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Создать notebook</title>
</head>
<body>
<?php
include "connect.inc";
global $conn;
pg_query($conn, "DROP TABLE IF EXISTS notebook");
$result = pg_query($conn, "
CREATE TABLE notebook (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  city VARCHAR(50),
  address VARCHAR(50),
  birthday DATE,
  mail VARCHAR(20) NOT NULL 
);") or die("Нельзя создать таблицу notebook");

print "Все ок!";
include "disconnect.inc";
?>
</body>
</html>
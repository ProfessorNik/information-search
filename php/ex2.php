<!doctype html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Добавить запись в notebook</title>
</head>
<style>
    label {
        display: block;
        margin-bottom: 5px;
    }
</style>
<body>
<?php
include "connect.inc";
global $conn;

$name = $_POST['name'] ?? null;
$city = $_POST['city'] ?? null;
$address = $_POST['address'] ?? null;
$birthday = $_POST['birthday'] ?? null;
$mail = $_POST['mail'] ?? null;

if ($name != null) {
    pg_query($conn, "
INSERT INTO notebook (name, city, address, birthday, mail) 
VALUES ('$name', '$city', '$address', '$birthday', '$mail')
");
}

include "disconnect.inc";
?>

<form method="POST">
    <label>Введите фамилию и имя[*]: <input name="name" required></label>
    <label>Введите город: <input name="city"></label>
    <label>Введите адрес: <input name="address"></label>
    <label>Введите дату рождения в формате ДД-ММ-ГГГГ: <input name="birthday"></label>
    <label>Введите фамилию и имя[*]: <input name="mail" required></label>
    <button type="submit">Записать</button>
    <p>Поля помеченные [*] являются обязательными!</p>
</form>
</body>
</html>
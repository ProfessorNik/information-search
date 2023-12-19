<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
<?php
$lang = $_GET['lang'] ?? null;


$langName = match ($lang) {
    'ru' => 'русский',
    'en' => 'английский',
    'fr' => 'французский',
    'de' => 'немецкий',
    default => 'неизвестный язык'
};

print $langName
?>
</body>
</html>
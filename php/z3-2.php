<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
<?php
$coloredText = fn($color, $text) => "<p style='color: $color'>$text</p>";
function Ru($color)
{
    global $coloredText;
    return $coloredText($color, "Здравствуйте!");
}
function En($color)
{
    global $coloredText;
    return $coloredText($color, "Hello!");
}

function Fr($color)
{
    global $coloredText;
    return $coloredText($color, "Bonjour!");
}

function De($color)
{
    global $coloredText;
    return $coloredText($color, "Guten Tag!");
}

$lang = $_GET['lang'] ?? null;
$color = $_GET['color'] ?? 'black';

if ($lang) {
    print $lang($color);
} else {
    print "Неизвестный язык";
}
?>

</body>
</html>
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
<?php
$params = (isset($_POST)) ? $_POST : $_GET;
$align = $params['align'] ?? null;
$valign = $params['valign'] ?? null;

print "<table style='border: 1px solid'><tr><td style='border: 1px solid; width: 100px; height: 100px; text-align: $align; vertical-align: $valign[0]'>Текст</td></tr></table>"
?>
</body>
<a href="z4-1a.html">Назад</a>
</html>
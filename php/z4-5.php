<?php

if (isset ($_POST["site"]) && $_POST["site"] != '') {
    $site = $_POST["site"];
    header("Location: https://$site");
    exit;
}

else { // начало блока else
?>

<html> <head>
    <title> Листинг 10-9. Посылка заголовка с помощью
        функции header() </title> </head> <body>

<?php
print "<form action='{$_SERVER['PHP_SELF']}' method='post'>";

$list_sites = [
    "www.yandex.ru",
    "www.rambler.ru",
    "www.yahoo.com",
    "www.altavista.com",
    "www.google.com"
];

$map_to_option = fn($value) => "<option value='$value'>$value</option>";
$map_to_options = fn($array) => implode("", array_map($map_to_option, $array));
$select = fn($name, $undefOptionName, $options) => "<select name='$name'><option value = ''>$undefOptionName</option> $options</select>";

print $select("site", "Поисковые системы:", $map_to_options($list_sites))
?>
<input type="submit" value="Перейти">
</form>

<?php
} // конец блока else
?>
</body> </html>


<?php
$page = $_GET['page'];

if ($page == 'health') {?>

    <li><a href="contributor.php?page=health&contributor=young-carers">Young Carers</a></li>
    <li><a href="contributor.php?page=health&contributor=cansa">CANSA</a></li>
    <li><a href="contributor.php?page=health&contributor=mandela-trust">Nelson Mandela Trust</a></li>
    <li><a href="#">Health Organisation</a></li>
    <li><a href="#">Health Organisation</a></li> 

<?php } elseif ($page == 'education') { ?>

    <li><a href="contributor.php?page=education&contributor=grassroots">Grassroots</a></li>
    <li><a href="contributor.php?page=education&contributor=fundza">FunDza</a></li>
    <li><a href="contributor.php?page=education&contributor=innovation-edge">Innovation Edge</a></li>
    <li><a href="contributor.php?page=education&contributor=asset">ASSET</a></li>
    <li><a href="contributor.php?page=education&contributor=little-hands-trust">Little Hands Trust</a></li>

<?php } elseif ($page == 'social-protection') { ?>

    <li><a href="contributor.php?page=social-protection&contributor=gem">GEM</a></li>
    <li><a href="contributor.php?page=social-protection&contributor=cindi">CINDI</a></li>
    <li><a href="#">Social Protection Organisation</a></li>
    <li><a href="#">Social Protection Organisation</a></li>
    <li><a href="#">Social Protection Organisation</a></li>

<?php } ?> 
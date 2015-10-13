<?php include 'header.php'; ?>
<?php $page = $_GET['page']; ?>
<body class="<?php echo $page; ?>">
    <div class="container sector-page">
        <!-- HEADER -->
        <header class="row sector-header">
            <div class="row site-links">
                <div class="col-md-12">
                    <?php include 'site-links.php'; ?>
                </div>
            </div>
            <div class="col-md-3">
                <div class="row">
                    <a href="index.php"><img class="logo" src="inc/img/NDP.png"/></a>
                </div>
            </div>

            <div class="col-md-9">
                <div class="row">
                    <div class="col-md-12">
                        <img class="sector-bubble" src="inc/img/sectors/<?php echo $page; ?>.png"/>
                        <h1><?php echo str_replace('-', ' ', $page); ?></h1>
                    </div>
                </div>
            </div>
        </header>
        <!-- END HEADER -->
        <div class="row">
            <div class="col-md-8">
                <div class="row">
                    <div class="col-md-6">
                        <hr class="sep hidden-sm hidden-xs"/>
                        <div class="vision">
                            <h2>VISION</h2>
                            <?php include 'content/sector-vision.php'; ?>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <hr class="sep hidden-sm hidden-xs"/>
                        <hr class="hidden-md hidden-lg" />
                        <div class="goals">
                            <h2>GOALS</h2>
                            <ul>
                                <?php include 'content/sector-goals.php'; ?>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="row">
                    <div class="col-md-12">
                        <div class="contributors">
                            <hr class="sep hidden-sm hidden-xs"/>
                            <hr class="hidden-md hidden-lg" />
                            <h2>CONTRIBUTORS</h2>
                            <div class="info">Click on a link to find out more</div>
                            <ul>
                                <?php include 'content/sector-contributors.php'; ?>
                                <li><a href="#">Another Organisation</a></li>
                                <li><a href="#">Another Organisation</a></li>
                                <li><a href="#">Another Organisation</a></li>
                                <li><a href="#">Another Organisation</a></li>
                                <li><a href="#">Another Organisation</a></li>
                                <li><a href="#">Another Organisation</a></li>
                                <li><a href="#">Another Organisation</a></li>
                                <li><a href="#">Another Organisation</a></li>
                                <li><a href="#">Another Organisation</a></li>
                                <li><a href="#">Another Organisation</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-12 get-involved">
                        <hr/>
                        <?php include 'get-involved.php'; ?>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-12">
                        <hr/>
                        <?php include 'sector-links.php'; ?>
                    </div>
                </div>
            </div>

        </div>
    </div>
</div>
<?php include 'footer.php'; ?>

<?php include 'header.php'; ?>
<?php $page = $_GET['page']; ?>
<?php $contributor = $_GET['contributor']; ?>

<body class="<?php echo $page; ?>">
    <div class="container contributor-page">
        <!-- HEADER -->
        <header class="row contributor-header">
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
                        <a href="sector.php?page=<?php echo $page; ?>">
                            <img class="sector-bubble" src="inc/img/sectors/<?php echo $page; ?>.png"/>
                        </a>
                        <h1><?php echo str_replace('-', ' ', $contributor); ?></h1>
                    </div>
                </div>
            </div>
        </header>
        <!-- END HEADER -->
        <div class="row">
            <div class="col-md-8">
                <div class="row">
                    <div class="col-md-6">
                        <div class="contributor-logo">
                            <a href=""><img src="organisations/<?php echo $contributor; ?>.jpg"/></a>
                        </div>
                        <?php include 'content/contributor-about.php'; ?>
                    </div>
                    <div class="col-md-6">
                        <hr class="hidden-md hidden-lg" />
                        <div class="projects">
                            <h2>PROJECTS</h2>
                            <?php include 'content/contributor-projects.php'; ?>
                        </div>
                        <hr/>
                        <div class="goals">     
                            <h2>NDP GOALS</h2>  
                            <ul>
                                <?php include 'content/contributor-goals.php'; ?>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="row">
                    <div class="col-md-12 contact">
                        <hr class="hidden-md hidden-lg" />
                        <h2>CONTACT</h2>
                        <?php include 'content/contributor-contact.php'; ?>
                    </div>
                </div>
                <div class="row links">
                    <div class="col-md-12 contact">
                        <hr/>
                        <h2>LINKS</h2>
                        <?php include 'content/contributor-links.php'; ?>
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
    <?php include 'footer.php'; ?>
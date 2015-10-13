<?php include 'header.php'; ?>
<body class="home">
    <div class="container">
        <!-- HEADER -->
        <header class="home-header">

            <div class="row site-links">
                <div class="col-md-12">
                    <?php include 'site-links.php'; ?>
                </div>
            </div>    
            <div class="row">
                <div class="col-md-12">
                    <div class="NDP-logo">
                        <a href=""><img src="inc/img/NDP-2030.png"/></a>
                    </div>
                    <div class="logo">
                        <a href=""><img src="inc/img/NDP.png"/></a>
                    </div>
                    <div class="NDP-blurb">demystifying the plan and<br/>tracking progress made</div>
                </div>
            </div>

        </header>
        <!-- END HEADER -->
        <div class="row">
            <div class="col-md-3 intro-blurb">
                <p>An ambitious vision to reduce inequality and poverty by 2030. Let's understand our progress</p> 
                <div class="home-info">Click on an icon to find out more about objectives and activities</div>   
                <div class="PDF-link"><span>+</span><a href="http://www.gov.za/documents/national-development-plan-2030-our-future-make-it-work">READ MORE DOWNLOAD THE NATIONAL DEVELOPMENT PLAN: A PDF</a></div>
                <div class="logos hidden-sm hidden-xs">
                    <div class="dgru">
                        <a href="http://www.dgru.uct.ac.za/" target="_blank">
                            <img src="inc/img/dgru.png"/>
                        </a>
                    </div>
                    <div class="code-for-sa">
                        <a href="http://www.code4sa.org" target="_blank">
                            <img src="inc/img/code-for-sa.png"/>
                        </a>
                    </div>
                </div>
            </div>
            <div class="col-md-9 sectors">

                <div class="sector-bubble">
                    <a href="sector.php?page=health"><img src="inc/img/sectors/health.png"/></a>
                    <h2><a href="sector-health.php">Health</a></h2>
                    <div class="blurb" style="display: none">
                        <a href="sector-health.php">
                            <h3>HEALTH</h3>
                            <p>Reduce the disease burden to manageable levels.</p>
                            <p>Promote healthy behaviours and lifestyles.</p>
                            <div class="contributor-number">15</div>
                        </a>
                    </div>
                </div>
                <div class="sector-bubble disabled">
                    <a href=""><img src="inc/img/sectors/international.png"/></a>
                    <h2><a href="">International</a></h2>
                </div>
                <div class="sector-bubble disabled">
                    <a href=""><img src="inc/img/sectors/government.png"/></a>
                    <h2><a href="">Government</a></h2>
                </div>
                <div class="sector-bubble disabled">
                    <a href=""><img src="inc/img/sectors/rural-economy.png"/></a>
                    <h2><a href="">Rural<br/>Economy</a></h2>
                </div>
                <div class="sector-bubble">
                    <a href="sector.php?page=education"><img src="inc/img/sectors/education.png"/></a>
                    <h2><a href="sector-education.php">Education</a></h2>
                    <div class="blurb" style="display: none">
                        <a href="sector-education.php">
                            <h3>EDUCATION</h3>
                            <p>Take urgent action throughout the education system.</p>
                            <p>Build national capability for quality early childhood development, basic education and further and higher education.</p>
                            <div class="contributor-number">110</div>
                        </a>
                    </div>
                </div>
                <div class="sector-bubble disabled">
                    <a href=""><img src="inc/img/sectors/communities.png"/></a>
                    <h2><a href="">Communities</a></h2>
                </div>
                <div class="sector-bubble">
                    <a href="sector.php?page=social-protection"><img src="inc/img/sectors/social-protection.png"/></a>
                    <h2><a href="sector-social-protection.php">Social<br/>Protection</a></h2>
                    <div class="blurb" style="display: none">
                        <a href="sector-social-protection.php">
                            <h3>SOCIAL PROTECTION</h3>
                            <p>Address poverty induced hunger, malnutrition and micronutrient deficiencies.</p>
                            <p>Create an inclusive social protection system that addresses all areas of vulnerability and is responsive to the needs of those who are most at risk.</p>
                            <div class="contributor-number">12</div>
                        </a>
                    </div>
                </div>
                <div class="sector-bubble disabled">
                    <a href=""><img src="inc/img/sectors/social-cohesion.png"/></a>
                    <h2><a href="">Social<br/>Cohesion</a></h2>
                </div>
                <div class="sector-bubble disabled">
                    <a href=""><img src="inc/img/sectors/environment.png"/></a>
                    <h2><a href="">Environment</a></h2>
                </div>
                <div class="sector-bubble disabled">
                    <a href=""><img src="inc/img/sectors/economy-employment.png"/></a>
                    <h2><a href="">Economy &amp;<br/>Employment</a></h2>
                </div>
                <div class="sector-bubble disabled">
                    <a href=""><img src="inc/img/sectors/infrastructure.png"/></a>
                    <h2><a href="">Infrastructure</a></h2>
                </div>
                <div class="sector-bubble disabled">
                    <a href=""><img src="inc/img/sectors/corruption.png"/></a>
                    <h2><a href="">Corruption</a></h2>
                </div>
                <div class="sector-bubble disabled">
                    <a href=""><img src="inc/img/sectors/human-settlements.png"/></a>
                    <h2><a href="">Human<br/>Settlements</a></h2>
                </div>
            </div>
        </div>
        <div class="logos row hidden-md hidden-lg">
            <div class="dgru">
                <a href="http://www.dgru.uct.ac.za/" target="_blank">
                    <img src="inc/img/dgru.png"/>
                </a>
            </div>
            <div class="code-for-sa">
                <a href="http://www.code4sa.org" target="_blank">
                    <img src="inc/img/code-for-sa.png"/>
                </a>
            </div>
        </div>
    </div>
    <?php include 'footer.php'; ?>
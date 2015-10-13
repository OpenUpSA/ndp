<?php include 'header.php'; ?>
<?php $page = $_GET['page']; ?>
<body class="about">
    <div class="container about-page">
        <!-- HEADER -->
        <div class="row about-header">
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
                        <h1>ABOUT THIS SITE</h1>
                    </div>
                </div>
            </div>
        </div>
        <!-- END HEADER -->
        <div class="row">
            <div class="col-md-8">
                <div class="row">
                    <div class="col-md-5" id="swap1">
                        <hr class="sep hidden-sm hidden-xs"/>
                        <div class="code-for-sa">
                            <a href="http://www.code4sa.org" target="_blank">
                                <img src="inc/img/code-for-sa.png"/>
                            </a>
                        </div>
                        <div class="dgru">
                            <a href="http://www.dgru.uct.ac.za/" target="_blank">
                                <img src="inc/img/dgru.png"/>
                            </a>
                        </div>
                        
                    </div>
                    <div class="col-md-7 about-text" id="swap2">
                        <hr class="sep hidden-sm hidden-xs"/>
                        <hr class="hidden-md hidden-lg" />
                        <p>In 2012, the National Planning Committee authored an ambitious vision document. It details actions to be taken and goals to be met to reduce inequality and poverty in South Africa by 2030.</p>
                        <p>This site aims to make the plan accessible to citizens, and highlight progress made towards the NPD objectives. Public and private sectors, and citizens, are called to work together to achieve the common goals. The site allows you to explore the NDP and view organisations and projects working towards its objectives. The tracking and measuring of progress towards the end goals is crucial to achieve the vision.</p>
                        <p>This project is currently a feasibility study and focuses on health, education and social protection.</p>

                        <h2>CODE4SA</h2>
                        <p>ASSET through its Saturday Programme, called the Learner Development Programme (LDP), offers supplementary tuition in key subjects to grades 11 and 12 learners from selected township schools, with very close liaison with school principals and subject teachers, throughout the year and during school holidays when Winter and Spring Schools take place. The LDP objectives include: improving conceptual understanding and learner performance; improving language proficiency across the curriculum and helping learners explore appropriate career choices.</p>

                        <h2>DGRU</h2>
                        <p>Our vision is of a socially just Africa, where equality and constitutional democracy are upheld by progressive and accountable legal systems, enforced by independent and transformative judiciaries, anchored by a strong rule of law. Our mission is to advance social justice and constitutional democracy in Africa by:</p>
                        <ul>
                            <li>Conducting applied and comparative research;</li>
                            <li>Supporting the development of an independent, accountable and progressive judiciary;</li>
                        </ul>        
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="row">
                    <div class="col-md-12">
                        <hr class="hidden-md hidden-lg" />
                        <h2>CONTACT</h2>
                        <p><a href="mailto:info@asset.org.za">info@asset.org.za</a></p>
                        <p>and or telephone number</p> 
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-12">
                        <hr/>
                        <h2>LINKS</h2>
                        <a href="http://www.asset.org.za">http://www.asset.org.za</a>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-12 get-involved">
                        <hr class="sep hidden-sm hidden-xs"/>
                        <hr class="hidden-md hidden-lg" />
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

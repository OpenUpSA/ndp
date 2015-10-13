# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from django.db import migrations
from django.template.defaultfilters import slugify

sectors = [
    (
        'Economy and Employment',
        """To eliminate poverty and reduce inequality, South Africa has to raise levels of employment and, through productivity growth, the earnings of working people.
South Africa needs faster growth and more inclusive growth. Key elements of this strategy include raising exports, improving skills development, lowering the costs of living for the poor, investing in a competitive infrastructure, reducing the regulatory burden on small businesses, facilitating private investment and improving the performance of the labour market to reduce tension and ease access to young, unskilled work seekers.
Only through effective partnerships across society can a virtuous cycle of rising confidence, rising investment, higher employment, rising productivity and incomes be generated.
South Africa requires both a capable and developmental state, able to act to redress historical inequities and a vibrant and thriving private sector able to investment, employ people and penetrate global markets.""",
        """The unemployment rate should fall from 24.9 percent in June 2012 to 14 percent by 2020 and to 6 percent by 2030. This requires an additional 11 million jobs. Total employment should rise from 13 million to 24 million.
The proportion of adults working should increase from 41 percent to 61 percent.
The proportion of adults in rural areas working should rise from 29 percent to 40 percent.
The labour force participation rate should rise from 54 percent to 65 percent.
Gross Domestic Product (GDP) should increase by 2.7 times in real terms, requiring average annual GDP growth of 5.4 percent over the period. GDP per capita should increase from about from about R50 000 per person in 2010 to R110 000 per person in 2030 in constant prices.
The proportion of national income earned by the bottom 40 percent should rise from about
6 percent today to 10 percent in 2030.
Broaden ownership of assets to historically disadvantaged groups.
¤ Exports (as measured in volume terms) should grow by 6 percent a year to 2030 with non-traditional exports growing by
10 percent a year.
¤ Increase national savings from 16 percent
of GDP to 25 percent.
¤ The level of gross fixed capital formation
should rise from 17 percent to 30 percent, with public sector fixed investment rising to 10 percent of GDP by 2030.
¤ Public employment programmes should reach 1 million by 2015 and 2 million people by 2030."""),

    (
        'Infrastructure',
        """South Africa needs to maintain and expand its electricity, water, transport and telecommunications infrastructure in order to support economic growth and social development goals. Given the government's limited finances, private funding will need to be sourced for some of these investments.
The role and effectiveness of sector regulators needs to be reviewed. In addition to issuing licences and setting tariffs, regulators need to place more emphasis on stimulating market competition and promoting affordable access to quality services. This will require capacity-building in regulatory institutions.
Policy planning and decision-making often requires trade-offs between competing national goals. For instance, the need to diversify South Africa's energy mix to include more renewable energy sources, which tend to be variable in terms of production, should be balanced against the need to provide a reliable, more affordable electricity supply.""",
        """The proportion of people with access to the electricity grid should rise to at least 90 percent by 2030, with non-grid options available for the rest.
The country would need an additional 29 000MW of electricity by 2030. About 10 900MW of existing capacity is to be retired, implying new build of more than 40 000MW.
At least 20 000MW of this capacity should come from renewable sources.
Ensure that all people have access to clean, potable water and that there is enough water for agriculture and industry, recognising the trade-offs in the use of water.
Reduce water demand in urban areas to 15 percent below the business-as-usual scenario by 2030.
The proportion of people who use public transport for regular commutes will expand significantly. By 2030, public transport will be user- friendly, less environmentally damaging, cheaper and integrated or seamless.
Durban port capacity should increase from 3 million containers a year to 20 million by 2040.
Competitively priced and widely available broadband."""),

    (
        'Environment',
        """South Africa has a rich endowment of natural resources and mineral deposits, which, if responsibly used, can fund the transition to a low-carbon future and a more diverse and inclusive economy. 
Developmental challenges must be 
addressed in a manner that ensures ￼environmental sustainability and builds resilience to the effects of climate change, particularly in poorer communities.
Investment in skills, technology and 
￼institutional capacity is critical to support the development of a more sustainable society and the transition to a low-carbon economy. Focused, institutionalised capacity building and management structures are needed.
Carbon-pricing mechanisms that target specific mitigation opportunities need to be implemented.
Consumer awareness initiatives and sufficient recycling infrastructure should result in South Africa becoming a zero- waste society.
The development of environmentally sustainable green products and services, including renewable energy technologies, will contribute to the creation of jobs in niche markets where South Africa has or can develop a competitive advantage.""",
        """A set of indicators for natural resources, accompanied by publication of annual reports on the health of identified resources to inform policy.
A target for the amount of land and oceans under protection (presently about 7.9 million hectares of land, 848kms of coastline and
4 172 square kilometres of ocean are protected).
Achieve the peak, plateau and decline trajectory for greenhouse gas emissions, with the peak being reached around 2025.
By 2030, an economy-wide carbon price should be entrenched.
Zero emission building standards by 2030.
Absolute reductions in the total volume of
waste disposed to landfill each year.
At least 20 000MW of renewable energy should be contracted by 2030.
Improved disaster preparedness for extreme climate events.
Increased investment in new agricultural technologies, research and the development of adaptation strategies for the protection of rural livelihoods and expansion of commercial agriculture."""),

    (
        'Rural Economy',
        """Rural communities require greater social, economic and political opportunities to overcome poverty.
To achieve this, agricultural development should introduce a land-reform and job- creation/livelihood strategy that ensures rural communities have jobs.
Ensure quality access to basic services, health care, education and food security.
Plans for rural towns should be tailor-made according to the varying opportunities in each area. Intergovernmental relations should be addressed to improve rural governance.""",
        """An additional 643 000 direct jobs and 326 000 indirect jobs in the agriculture, agro- processing and related sectors by 2030.
Maintain a positive trade balance for primary and processed agricultural products."""),

    (
        'International Development',
        """In global terms, South Africa’s foreign policy must be shaped by the interplay between diplomatic, political, security, environmental, economic and regional co-operative dynamics that define early 21st century international relations. In particular, our foreign policy-making should remain cognisant of global shifts in hard, soft and smart or mental power from West to East; the stratification of regional groupings in the world; the proliferation of threats to human and state security; to internal and external sovereignty, and to natural resources.
On the basis of our identity as an African country, South Africa’s foreign policy should be driven by a clear and critical understanding of our national, regional and continental priorities in a multi- polar world where the geo-strategic politics of the continent is, once again, becoming increasingly central to global political economic competition for natural resources and market share. As such, we need to have a clear strategy of South Africa’s place in the region, on the continent and in the world over the next 20 – 30 years, and the political space the country will occupy.
On the continent, South Africa should improve ￼collaboration and co-operation, through deeper integration and increased trade with its regional trade partners in Africa, and the global south, in general, particular emphasis should be placed on the role that South Africa can play in mediating the role and influence of the BRICS group and African countries. The impending Tripartite Free Trade Area is a significant step towards improved African integration and should be a priority in South Africa’s foreign policies. In the sub-region, policy-makers must identify regional synergies with South Africa’s immediate SADC neighbours in investment, production and in specific market sectors such as energy and agro-processing.
￼￼￼The NPC submits that the Department of International Relations and Cooperation should focus on organisational transformation to make the department more efficient and effective in its operations abroad, internally and domestically. The NPC recommends that the department’s research capabilities be strengthened, and that it works in collaboration with South Africa’s research, business and academic institutions and with epistemic communities to develop the country’s foreign policies.
South Africa’s business community must be drawn more closely into our foreign policy making. It is an incontestable reality of late capitalist international relations that it may be states that secure international trade or financial relations, but it is, ultimately, private companies that do business across borders. This reality places a high burden of expectations on South African companies to act ethically and responsibly in the region, on the continent and in the world.""",
        """Intra-regional trade in Southern Africa should increase from 7 percent of trade to 25 percent of trade by 2030.
South Africa's trade with regional neighbours should increase from 15 percent of our trade to 30 percent."""),

    (
        'Human Settlements',
        """Respond systematically, to entrenched spatial patterns across all geographic scales that exacerbate social inequality and economic inefficiency.
In addressing these patterns we must take account of the unique needs and potentials of different rural and urban areas in the context of emerging development corridors in the southern African subregion.
The state will review its housing policies to better realise constitutional housing rights, ensure that the delivery of housing is to be used to restructure towns and cities and strengthen the livelihood prospects of households.
Active citizenship in the field of spatial development will be supported and incentivised through a range of interventions including properly funded, citizen-led neighbourhood vision and planning processes and the introduction of social compacts from neighbourhood to city level.
Planning in South Africa will be guided by a set of normative principles to create spaces that are liveable, equitable, sustainable, resilient and efficient, and support economic opportunities and social cohesion.
South Africa will develop a national spatial framework and resolve the current deficiencies with the local system of integrated development planning and progressively develop the governance and administrative capability to undertake planning at all scales.""",
        """Strong and efficient spatial planning system, well integrated across the spheres of government.
Upgrade all informal settlements on suitable, well located land by 2030.
More people living closer to their places of work.
Better quality public transport.
More jobs in or close to dense, urban
townships."""),

    (
        'Education',
        """The South African education system needs urgent action. Building national capabilities requires quality early childhood development, basic education, further and higher education.
Early childhood development should be broadly defined, taking into account all the development needs of a child, and provided to all children.
The priorities in basic education are human capacity, school management, district support, infrastructure and results-oriented mutual accountability between schools and communities.
Further Education and Training colleges, public adult learning centres, sector education and training authorities, professional colleges and Community Education and Training Centres are important elements of the post-school system that provide diverse learning opportunities.
Further education should expand moderately, and as quality improves/expands rapidly, higher education should incorporate a range of different institutions that work together to serve different priorities, including effective regulatory and advisory institutions.
Distance education, aided by advanced information communication technology, will play a greater role in expanding learning opportunities for different groups of learners and promote lifelong learning and continuous professional development. Private providers will continue to be important partners in the delivery of education and training at all levels.
Research and innovation by universities, science councils, departments, NGOs and the private sector has a key role to play in improving South Africa’s global competitiveness. Coordination between the different role-payers is important.""",
        """Make early childhood development a top priority among the measures to improve the quality of education and long-term prospects of future generations. Dedicated resources should be channelled towards ensuring that all children are well cared for from an early age and receive appropriate emotional, cognitive and physical development stimulation.
All children should have at least 2 years of pre-school education.
About 90 percent of learners in grades 3, 6 and 9 must achieve 50 percent or more in the annual national assessments in literacy, maths and science.
Between 80 – 90 percent of learners should complete 12 years of schooling and or vocational education with at least 80 percent successfully passing the exit exams
Eradicate infrastructure backlogs and ensure that all schools meet the minimum standards by 2016.
Expand the college system with a focus on improving quality. Better quality will build confidence in the college sector and attract more learners. The recommended participation rate of 25 percent would accommodate about 1.25 million enrolments.
Provide 1 million learning opportunities through Community Education and Training Centres
Improve the throughput rate to 80 percent by 2030.
Produce 30 000 artisans per year.
Increase enrolment at universities by at least 70 percent by 2030 so that enrolments increase to about 1.62 million from 950 000 in 2010.
Increase the number of students eligible to study towards maths and science based degrees to 450 000 by 2030.
Increase the percentage of PhD qualified staff in the higher education sector from the current 34 percent to over 75 percent by 2030.
Produce more than 100 doctoral graduates per million per year by 2030. That implies an increase from 1420 in 2010 to well over 5 000 a year.
Expand science, technology and innovation outputs by increasing research and development spending by government and through encouraging industry to do so."""),

    (
        'Health',
        """Greater intersectoral and inter-ministerial collaboration is central to the Commission’s proposals to promote health in South Africa.
Health is not just a medical issue. The social determinants of health need to be addressed, including promoting healthy behaviours and lifestyles.
A major goal is to reduce the disease burden to manageable levels.
Human capacity is key. Managers, doctors, nurses and community health workers need to be appropriately trained and managed, produced in adequate numbers, and deployed where they are most needed.
The national health system as a whole needs to be strengthened by improving governance and eliminating infrastructure backlogs.
A national health insurance system needs to be implemented in phases, complemented by a reduction in the relative cost of private medical care and supported by better human capacity and systems in the public health sector.""",
        """Increase average male and female life expectancy at birth to 70 years.
Progressively improve TB prevention and cure.
Reduce maternal, infant and child mortality.
Significantly reduce prevalence of non-communicable chronic diseases.
Reduce injury, accidents and violence by 50 percent from 2010 levels.
Deploy primary healthcare teams provide care to families and communities.
Everyone must have access to an equal standard of care, regardless of their income.
Fill posts with skilled, committed and competent individuals."""),

    (
        'Social Protection',
        """A social floor is defined and a multi-pronged strategy recommended to ensure that no household lives below this floor. Problems such as poverty induced hunger, malnutrition and micronutrient deficiencies will be addressed.
Create an inclusive social protection system that addresses all areas of vulnerability and is responsive to the needs, realities, conditions and livelihoods of those who are most at risk.
Provide support that builds and utilises the capabilities of individuals, households, communities and NGOs to promote self reliant sustainable development.
Encourage a culture of individual saving for risks associated with loss of income due to unemployment, old age and illness by providing appropriate frameworks and incentives.
Enhance services and programmes for labour market activation for the unemployed and create opportunities in public employment.""",
        """Ensure progressively and through multiple avenues that no one lives below a defined minimum social floor.
All children should enjoy services and benefits aimed at facilitating access to nutrition, health care, education, social care and safety.
Address problems such as hunger, malnutrition and micronutrient deficiencies that affect physical growth and cognitive development, especially among children.
Address the skills deficit in the social welfare sector.
Provide income support to the unemployed through various active labour market initiatives such as public works programmes, training and skills development, and other labour market related incentives.
All working individuals should make adequate provision for retirement through mandated savings. The state should provide measures to make pensions safe and sustainable.
Social protection systems must respond to the growth of temporary and part-time contracts, and the increasing importance of self-employment and establish mechanisms to cover the risks associated with such.
Create an effective social welfare system that delivers better results for vulnerable groups, with the state playing a larger role compared to now.
Civil society should complement government initiatives."""),

    (
        'Communities',
        """The criminal justice system is to have a single set of objectives, priorities and performance- measurement targets. Further implementation of the seven-point plan will receive greater interdepartmental coordination.
Demilitarise the police. The police should be selected and trained to be professional and impartial, responsive to community needs, competent and inspire confidence.
An integrated approach to safety and security will require coordinated activity across a variety of departments, the private sector and community bodies, the latter to include revitalised community-safety centres.
All vulnerable groups including women, children and rural communities should enjoy equal protection and their fear of crime should be eradicated through effective, coordinated responses of the police, business, community and civil society.""",
        """In 2030 people living in South Africa feel safe and have no fear of crime. They feel safe at home, at school and at work, and they enjoy an active community life free of fear. Women can walk freely in the street and the children can play safely outside. The police service is a well-resourced professional institution staffed by highly skilled officers who value their works, serve the community, safeguard lives and property without discrimination, protect the peaceful against violence, and respect the rights of all to equality and justice."""),

    (
        'Government',
        """South Africa needs to build a state that is capable of playing a developmental and transformative role.
The public service needs to be immersed in the development agenda but insulated from undue political interference.
Staff at all levels must have the authority, experience and support they need to do their jobs. This will require a more long-term approach to skills development.
Improving relations between national, provincial and local government requires a proactive approach to resolving coordination problems.
The governance structures for state-owned enterprises (SOEs) should be simplified to ensure clear lines of accountability and stable leadership.""",
        """A state that is capable of playing a developmental and transformative role.
A public service immersed in the development agenda but insulated from undue political interference.
Staff at all levels have the authority, experience, competence and support they need to do their jobs.
Relations between national, provincial and local government are improved through a more proactive approach to managing the intergovernmental system.
Clear governance structures and stable leadership enable state-owned enterprises (SOEs) to achieve their developmental potential."""),

    (
        'Corruption',
        """Corruption undermines good governance, which includes sound institutions and the effective operation of government in South Africa. The country needs an anti-corruption system that makes public servants accountable, protects whistle-blowers and closely monitors procurement.
These efforts to eradicate corruption need to include the private sector and individuals by increasing public awareness and improving access to information.
A strategy is needed to strengthen the independence of the judiciary, through improving the quality of judges and scaling up judicial training.""",
        """A corruption-free society, a high adherence to ethics throughout society and a government that is accountable to its people."""),

    (
        'Social Cohesion',
        """To make it easier for South Africans to interact with each other across racial and class divides, the country needs to improve public spaces and public services.
It is important for all South Africans to be active citizens and exercise leadership throughout society.
A social contract could help propel South Africa onto a higher developmental trajectory as well as build a more cohesive and equitable society.
Unity in diversity will be fostered by a shared commitment to constitutional values. The values entrenched in the Constitution and its Preamble and further expanded upon in the Bill of Responsibilities are part of children's education and should also be promoted amongst adult South Africans.
South Africa needs to build a more equitable society where opportunity is not defined by race, gender, class or religion. This would mean building people's capabilities through access to quality education, health care and basic services, as well as enabling access to employment, and transforming ownership patterns of the economy. Redress measures that seek to correct imbalances of the past should be strengthened.""",
        """Our vision is a society where opportunity is not determined by race or birthright; where citizens accept that they have both rights and responsibilities. Most critically, we seek a united, prosperous, non-racial, non-sexist and democratic South Africa."""),
]


def add_sectors(apps, schema_editor):
    Sector = apps.get_model("ndp", "Sector")

    for name, vision, goals in sectors:
        vision = re.sub(r'\n+', '\n\n', vision)
        sector = Sector(name=name, vision=vision, goals=goals, slug=slugify(name))
        sector.save()


def drop_sectors(apps, schema_editor):
    Sector = apps.get_model("ndp", "Sector")

    for name, vision, goals in sectors:
        sector = Sector.objects.filter(name=name).first()
        if sector:
            sector.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('ndp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_sectors, drop_sectors),
    ]

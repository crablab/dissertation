# Abstract 

<!-- 1. A section motivating the project and giving the original project aims.
This section must include a description of how you think that the work involved in your
project will help in your future career. -->

# Introduction 

## Motivation 

# Research 

<!-- 6. A theory section. This might include a literature survey, sections on specific theory,
or even an interesting discussion on what you have achieved in a more global context. -->

## Background Theory 

## Clicker: reverse engineering 

## Browser Fingerprinting 

## Bluetooth 

## Signing and authentication

# Design and Software Engineering

<!-- 7. Sections describing the software engineering method that you used. If your project is
based on a software product then this may even be most of your report. -->

## Initial Design

The proposed proof of concept replacement for both the paper registers will make use of modern web technologies to deliver a secure and trustworthy registration system that students can use on their mobile devices. This report lays out the design of the core components of the system and is intended to provide a full specification for the system being built with justification for the various design choices.  

## Components 

### Webservices 

The proposed application is primarily a webservice which is made up of two components: a backend server for processing and storing data, and a set of frontend webpages which will allow users to interact and manage the application. 

There is a choice between whether to use backend driven views or one of many JavaScript web frameworks (such as Vue, React etc.); which provide a more interactive and arguably seamless experience. These frameworks use static HTML pages served by a CDN (Content Delivery Network) which then utilise APIs provided on the backend to populate the pages on demand and deliver a richer user experience. This method of API centric design also reduces coupling of the user views with the underlying classes and models on the backend. However, these frameworks can be complex to use, require more careful design and provision of a rich API, and do create their own issues; for instance the use of JavaScript can be a drain on the viewing devices' system resources. For this basic proof of concept only a basic website is required with limited user user experience and design, and thus decoupling the frontend and the backend is not considered worthwhile. 

Instead, the backend will fill pre-designed HTML templates and serve them to the browser in a more traditional way. This does increase server load but as mentioned, increases coupling and reduces overall system complexity. 

As originally specified, the backend will be based on a Python application. Python is a high level interpreted programming language which is well supported in web development (with various web frameworks) and with many well maintained libraries (for instance, the ECDSA library). The version used will be the current Python 3 (2.7 was recently deprecated) and which has binaries for most modern operating systems (Linux, Windows MacOS). Python web services can be developed locally (eg. on the developers machine) and can also be deployed to production servers. For this project it is not intended to deploy the application to a server; although the web frameworks discussed later do support WSGI (Web Server Gateway Interface - a convention in how web servers communicate with the actual web application) so with a full CI/CD pipeline, automated deployments are possible. 

In order to efficiently develop a web application with both a basic API and serving webpages a web framework will be used. A short analysis of two options is provided: 

#### Flask

Flask is a lightweight web application framework which supports the WSGI and can thus be easily deployed with most common web servers (Nginx, Apache) (@pallets_welcome_2010). Whilst Flask does provide support for Jinga (a Python templating engine) and thus can easily support the rendering of HTML views on the backend. Being a more lightweight and "lower level" framework, Flask provides a significant latitude to the developer allowing quick and easy development; however potentially allowing the cultivation of poor software engineering practices. It is therefore important to understand the full set of features provided by Flask, it's design patterns and the Pythonic approach - this is all covered in the documentation (@pallets_welcome_2010). 

#### Django 

Django is a higher level more feature rich web framework. By default it provides tools such as a database abstraction layer, form validation, authentication controls etc. These provide a lower barrier to entry and are well maintained within the ecosystem, reducing the boilerplate required to get started and enforcing best practice and security by default. However, the prescriptive nature of the framework requires you to design your webservice in a specific way and use specific Django features. As mentioned, this can pay off in the long run by providing better maintainability, support and more predictable code (through use of a standard set of libraries) but does restrict development to the "Django way". 

--- 

For this proof of concept I will use Flask. This will provide a very simple base on which to integrate my classes and although it will require writing additional boilerplate (eg. for a login system), as this is a proof of concept scope creep can be avoided through a clear design from the outset. 

#### Webservice UML 

![UML diagram. This does not include classes generated or required by Flask - only application classes. ](assets/uml.png)

#### Webservice Pages 

The following pages will be provided at the following URLs as an HTML user interface, as discussed above. 

**/login**

Form with entry for email and password to login. 

**/signup** 

Exists purely for the PoC, to allow an easy method to add new users. Will allow setting of all parameters including privilege level 

**/dashboard** 

Will display different data depending on privilege level. 
- Students will see their current overall attendance percentage, upcoming lectures and missed lectures 
- Lecturers will see their classes and attendance percentages for each class, their upcoming lectures and attendance percentage for recently held lectures 
- Administrators will see students with high levels of poor attendance 

**/register/{class_id}** 

Only accessible to students, starts the challenge-response flow and redirected to from their dashboard. 

The frontend JavaScript is discussed in more detail later on, however as an overview an asynchronous request will be made to the backend to start the process and obtain the backend cryptogram. The cryptogram will then be signed and returned by the Bluetooth device and the result submitted by POST redirection to an endpoint for validation. 

**/provision/{class_id}** 

Only accessible to lecturers, this will generate the certificate bundle needed by the Bluetooth device for operation in that lecture. 

**/create/class** 

Only accessible to administrators, this allows the creation of classes for a specific time, against a course code. 

**/assign/student/{user_id}** 

Only accessible to administrators, this allows a student to be assigned to a course code. 

**/assign/lecturer/{user_id}** 

Only accessible to administrators, this allows a lecturer to be assigned to a course. 

#### API

A basic API will be provided to facilitate the frontend asynchronous requests. It may be useful to provide some other endpoints, but these are not in scope for now. 

**/api/authenticate** 

- Method: POST 
- Parameters: Client ID, Secret 
- Returns: Access Token, Expiry 

**/api/registration/start**

- Method: POST
- Parameters: Client ID, Access Token, User, Course, Browser Fingerprint 
- Returns: Challenge ID, Challenge

--- 

For form submissions, session cookies will be checked upon submission to the endpoint at prefix **/api/forms/**. 

#### Design Patterns

The modular unit tested design of the webservice codebase lends itself well to the use of standard design patterns. The choice of pattern for a number of components is discussed below, identifying the tradeoffs between different types of design. 

One important distinction to make here is that although the webserver is constantly "spinning", that is waiting for a new connection, each request would be handled in a separate thread (with a WSGI configuration). Thus each connection is stateless and some design patterns, such as the observer pattern, do not fit well into the specific application here. An example of the observer in this context might be when interfacing with an external system and waiting for a response or webhook to service the original request, but this use case is not relevant to this codebase. 

**ORM/Database Class** 

The database class will provide a wrapper over the underlying ORM modules to add custom functionality as well as a more consistent user interface. Whilst on the surface this might look like an adaptor design patter, it will more closely follow that of a singleton. There should only ever be one database connection per session (otherwise you end up with crippling scaling issues as I discovered in the Second Year Team Project) and therefore there should only ever be a single instance of the database connection which will be shared between classes globally. The connection is effectively stateless (concurrent requests are threaded in the background) and will only ever be instantiated once, at the beginning of the session, and destructed at the very end. 

It is important to note that the underlying ORM (SQLAlchemy - as discussed below) is a bridge - allowing multiple underlying database technologies to be used (eg. MySQL) with a choice of database connectors (eg. PyMySQL). 

**`fingerprints`/`cohesion`** 

The `cohesion` class is composed of the `fingerprints` class, which is ultimately composed of the `browsers` class. Both `cohesion` and `fingerprints` instantiate a large number of classes in the background to provide functionality - the `fingerprints` can generate a graph of fingerprint connections between users which instantiates a number of `browsers` instances. The `cohesion` class carries out some (basic) risk scoring on a user and therefore relies on the generating multiple `fingerprints` classes to calculate linked risk scores between users. 

The obvious choice here might be a factory, since both classes orchestrate the creation of multiple classes behind the scenes. However, since the creation of objects is essentially in a tree structure and designed so that the eventual output is a manipulation of the entire tree structure, the composition design pattern is a better fit. Primarily this pattern helps to handle distinction between leafs and nodes in the tree, which will be an important consideration here. 

**`crypto`**

The crypto class provides a wrapper to a more complex and extensive class. The wrapper provides a consistent set of interfaces that encapsulate several calls to the underlying class, as well as reducing the complexity of the interface. This is a classic use of the adapter pattern. 

## Frontend (JavaScript)

The frontend will be based on the proof of concept programs developed previously. Two major pieces of functionality are planned: 
- Browser Fingerprinting 
- Bluetooth device functionality 

The browser fingerprint will be calculated using the ClientJS library as it provides a more stable result (based on limited testing). 

The Bluetooth device functionality will be developed using the experiments in the Web Bluetooth API and the device ID will (for now) be hardcoded in the frontend to the specific development device in use. 

## Device 

The Bluetooth device will be based on the Python ECDSA wrapper proof of concept, as the backend alongside the basic serial connection to the Bluetooth chip. It will read and verify the certificate bundle, import it and sign any data sent to the Bluetooth chip before returning it. 

For MVP purposes, the Bluetooth device will sign and return any data sent to it - this may be improved to perform some kind of validation, time permitting. 

## Database

The application data will be stored in a relational database - this type of database lends itself well to the structured nature of the application with indexed columns. 

The database engine I shall use is MySQL given my familiarity with the technology, the relative ubiquity and good library support. MySQL does not scale or lend itself to replication well but this is not required for the MVP. The schema could be easily migrated with readily available tools to another engine, such as Postgres. MySQL version 8 is the most recent stable release and whilst there are no plans to use any of the 

I have elected to use an ORM (Object Relationship Mapping) tool - SQLAlchemy - with PyMySQL as the database connector. 

### Entity Relationship Diagram 

This is not provided right now, since it essentially maps bijectivly to the UML class diagram by design. 

## Building the webservice 

The first step in building the webservice was to configure the Python environment and set up the database. For final delivery of the code, I have decided to Dockerise the entire webservice to aid running of the code in the future and ensure a watermarked version of packages and dependencies are stored, so breaking changes introduced later do not render the software unable to run. 

I first created a very naive Flask webservice which could load a page from an individual "service". I then added a database integration with a single (again naive) unit test as a proof of concept - this allowed testing of the DBMS and local connection. Creating the first version of the schema required modelling various constraints on the database to avoid consistency and normalization issues later on. For example, some tables exist purely to map IDs to IDs to remain in 3NF - this approach is discussed later on. 

Having a working database, I looked into using my ORM connection to run queries on the database. Initially I had planned to extend my existing class but I discovered there is actually a Flask plugin for SQLAlchemy and it's use is encouraged as part of usage with Flask Blueprints. @todd_birchard_organizing_2018

### Flask Blueprints

The naive way to build a Flask application is to have an `app.py` which serves as a kind of edge proxy - you import all of your services into this single file and bind instantiations to a URL handler. This becomes unmaintainable very quickly, can create circular import issues and makes it hard to reason about how you should deal with object classes lower down the call stack. 

Flask Blueprints allow us to separate out groups of pages that go together into Pythonic modules - these share templates and associated business logic. Underlying classes and objects remain shared throughout the application as appropriate. The routing for a Blueprint works in a similar way to the naive approach, except we handle more of subsequent request handling in the module with the associated business logic. It also allows us to use the factory design pattern with the `create_app` functionality built into Flask, which will then orchestrate the creation of the required modules to serve the request - for free! This gets rid of a lot of boilerplate that would otherwise exist to route requests. 

We also are able to simplify unit and integration testing with this approach by passing different parameters to the `create_app` call to set up different objects. This avoids the situation where we unit test underlying classes, but not business logic in the modules where it is intertwined with display logic. In this case, we'll continue using pytest but use the Flask plugin to simplify the testing by providing Flask specific functionality. 

In this application we will split the application out into several modules:

- `Login` to handle the login and session creation 
- `Student` for all student pages and business logic 
- `Lecturer` for all lecturer pages and logic
- `Administrator` for the back office processing pages and logic
- `API` for the basic API we'll be providing 

# Professional Issues

Privacy and freedom of expression is becoming an increasingly debated issue, especially online and in the digital world. As computing power and storage capacity have increased over the last few decades, it has become feasible for companies to collect large amounts of data at an individual level for analysis and data mining. Whilst often the data is claimed to be anonymised, studies such as @rocher_estimating_2019 have shown that it is possible to use modern machine learning techniques on large datasets to identify individuals. 

This project advocates not only requiring students to prove their presence in an auditable way but the bulk collection of browser data to prevent fraud and deception. Taking the former as a given, is it proportionate to collect a uniquely identifiable hash of the student's browser each time they mark their attendance?

One important consideration is data protection, specifically the requirements of the General Data Protection Regulation or GDPR. As this data can uniquely identify a browser, it is possible it could be used in conjunction with other information (for example, lectures attended) to identify an individual. It is therefore classed as Personally Identifiable Information. 

In order to process the data we must have a lawful reason to do so - in this case we claim legitimate interest applies. We must therefore meet the following test: 

> Identify a legitimate interest;
> Show that the processing is necessary to achieve it; and
> Balance it against the individual’s interests, rights and freedoms.
> @noauthor_legitimate_2019


Our legitimate interest is in the prevention of fraud but we still need to show that our processing of the PII is necessary, proportionate and balances the individual freedoms of the person. 

The @noauthor_legitimate_2019 continues: 

> Does this processing actually help to further that interest?
> Is it a reasonable way to go about it?
> Is there another less intrusive way to achieve the same result?

The processing of the PII does further the interest as we use it to measure connections between students and to identify suspicious patterns of behavior (eg. a single device signing in multiple students). We consider this to be a reasonable method of measuring this data points and that this is the least intrusive method - we do not store the raw data for example, just the irreversible fingerprint hash. 

The ICO test around individual freedoms look mainly at the sensitivity of the data, disclosure of the processing and appropriate safeguards to minimize harm. The data is fairly sensitive - appropriate controls should be in place to limit and record access and it should be removed as soon as the legitimate interest ends. 

Even though we can demonstrate that the data collection in this scenario is proportionate, there are a number of other uses for browser fingerprints, particular in advertising, which operate in a decidedly more grey area. This type of tracking is not uncontroversial and from 2012 to 2014, Verizon (a US network carrier) injected unique identifiers into network traffic without their customers being aware of such 'supercookies' being attached to their data. [@brodkin_verizons_2016] [@noauthor_verizon_nodate] It transpired that not only were Verizon using these supercookies themselves, but third parties had discovered their existence and were using them to track individual devices for purposes such as advertising. The FCC's investigation determined that Verizon should have sought explicit opt-in consent from customers for the direct sharing of what the FCC referred to as UIDH (unique identifier headers) and given the option for customers to opt out of their use by Verizon internally. A specific case cited related to a third party advertiser using supercookies to continue tracking customers after they had explicitly removed normal cookies from their devices. 

As previously discussed the GDPR applies within the UK and contains specific provision for what it calls "Special category Data". This is "personal data which the GDPR says is more sensitive, and so needs more protection." [@gov.uk_guide_nodate] and includes "biometric" data which traditionally has been used to refer to specific human characteristics (such as retina data) however could arguably be applied to specific characteristics of a device a user owns; in the same way that an IP address is considered Personally Identifiable Information.[@noauthor_eur-lex_nodate]

In an increasingly digital world where the resources exist to store large volumes of data for an indeterminate period and carry out increasingly accurate machine learning and modelling, the practice of trying to uniquely identify a user across the internet by their browser fingerprint is concerning. Not only does this allow private corporations another alarming way to build up data profiles of citizens, without their knowledge, but nation state actors can also use this highly targeted and specific data to track down individuals and groups. Law enforcement have long argued this kind of unique identifier allows them to catch criminals - but at what level of accuracy and at what cost to individual liberties and freedoms? It is easy to dismiss these concerns as "fanatical" or "out of touch with reality" whilst we live in a society where freedom of speech is championed and the rights of an individual protected. As the Metropolitan Police Service in London begin their rollout of facial recognition technology, it is clear this issue will continue to be debated in various forms for a while to come. @police_uk_2018 @kaltheuner_facial_2020

<!-- 2. A short section on professional issues (See Section 6) that raised concern during the
year, particularly with respect to doing your project or the material contained in your
project. -->

<!-- Ethical behaviour is concerned with what is good or bad, with moral duty and obligation and
as such deals with opinions and beliefs.
Professionalism in computing is concerned with the societal impact of computer technology
and the creation and understanding of policies for the ethical use of such technologies.
Professional bodies such as the British Computer Society (BCS) and the Association for
Computing Machinery (ACM) help ensure professionalism and ethical behaviour by providing
standards and a code of individual conduct: guaranteeing certain levels of competence, integrity
and a commitment to the interests of all end-users and other stakeholders.

"I am amazed when I meet computer professionals in business and industry or even
computer science teachers in colleges and universities who fail to recognise that their
profession has social and ethical consequences" Terrell Ward Bynum (2003 )

After completing a Royal Holloway Computer Science degree we expect that you will be
ready to be ethical computing professionals. To this end we include material on professional
issues in our undergraduate modules.
The individual project is no exception. By completing an individual project, as well as
the theory and practise essential to your chosen topic, you will have acquired skills in time
management, prioritisation and both oral and written presentation.
Certainly you will have encountered some professional issues: correct citation, licensing,
accessibility etc., -->

# Assessment 

## Outcomes

## Issues encountered

## Self-evaluation 

<!-- 3. Some sort of self-evaluation in the assessment section: How did the project go? Where
next? What did you do right/wrong? What have you learnt about doing a project? -->

# Software Deliverables 

<!-- 4. A description of how to run any software that you have submitted, including any
environmental requirements (Java version number, IOS version etc.,) 
User manual in appendix
-->


8. Lastly there are some added extras you might want to include. Perhaps parts of a program
listing. Perhaps some sample output or experimental results. Often you will include
a user manual (though complete installation and operating instructions are mandatory).
These extra documents may be put into an appropriate appendix so as not to count towards
the word limit.

# Acknowledgements 

Thanks to @tom_pollard_template_2016 for the front cover template which I have adapted and "corentin" for the Gantt chart example in \LaTeX [@noauthor_pgfgantt_nodate].

\pagebreak 
\onecolumn 

# Bibiography 

<!-- 5. A bibliography of works referred to in the text, or that have been read in order to
understand the project. -->

---

<div id="refs"></div>

\pagebreak 

# Appendix 

<!--
• Long or complicated test output (referred to in the report).
• Examples showing the use of the project.
• Detailed instructions for executing submitted programs.
• Copies of papers and other reference material used for the project.
It is usual to include such material in the appendix to the final report. -->

### Glossary

**Bluetooth device:** In the context this refers exclusively to the Raspberry Pi module that lecturers provision and bring to the lecture for students to authenticate against. 

**Cryptogram:** A challenge that has been signed. This can refer to either the challenge signed by the backend, _or_ the challenge signed by the backend and the Bluetooth device. 

**Class:** A single lecture with an immutable start time. This has a course code (to which an arbitrary number of classes can be created). Students and lecturers are allocated against a course arbitrarily. There is no concept of academic or calendar year. 

**Fingerprint:** The browser fingerprint calculated by the frontend JavaScript. 

**Certificate bundle:** The keys and other data generated by the backend for the Bluetooth device to sign data provided by student devices. 

**MVP:** For the purposes of the project, a Minimum Viable Product will be produced. This is enough to prove the concept and related technologies, but is cut down and not production ready. 
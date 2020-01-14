# Outline 

The proposed proof of concept replacement for both the paper registers will make use of modern web technologies to deliver a secure and trustworthy registration system that students can use on their mobile devices. This report lays out the design of the core components of the system and is intended to provide a full specification for the system being built with justification for the various design choices.  

# Components 

## Webservices 

The proposed application is primarily a webservice which is made up of two components: a backend server for processing and storing data, and a set of frontend webpages which will allow users to interact and manage the application. 

There is a choice between whether to use backend driven views or one of many JavaScript web frameworks (such as Vue, React etc.); which provide a more interactive and arguably seamless experience. These frameworks use static HTML pages served by a CDN (Content Delivery Network) which then utilise APIs provided on the backend to populate the pages on demand and deliver a richer user experience. This method of API centric design also reduces coupling of the user views with the underlying classes and models on the backend. However, these frameworks can be complex to use, require more careful design and provision of a rich API, and do create their own issues; for instance the use of JavaScript can be a drain on the viewing devices' system resources. For this basic proof of concept only a basic website is required with limited user user experience and design, and thus decoupling the frontend and the backend is not considered worthwhile. 

Instead, the backend will fill pre-designed HTML templates and serve them to the browser in a more traditional way. This does increase server load but as mentioned, increases coupling and reduces overall system complexity. 

As originally specified, the backend will be based on a Python application. Python is a high level interpreted programming language which is well supported in web development (with various web frameworks) and with many well maintained libraries (for instance, the ECDSA library). The version used will be the current Python 3 (2.7 was recently deprecated) and which has binaries for most modern operating systems (Linux, Windows MacOS). Python web services can be developed locally (eg. on the developers machine) and can also be deployed to production servers. For this project it is not intended to deploy the application to a server; although the web frameworks discussed later do support WSGI (Web Server Gateway Interface - a convention in how web servers communicate with the actual web application) so with a full CI/CD pipeline, automated deployments are possible. 

In order to efficiently develop a web application with both a basic API and serving webpages a web framework will be used. A short analysis of two options is provided: 

### Flask

Flask is a lightweight web application framework which supports the WSGI and can thus be easily deployed with most common web servers (Nginx, Apache) (@pallets_welcome_2010). Whilst Flask does provide support for Jinga (a Python templating engine) and thus can easily support the rendering of HTML views on the backend. Being a more lightweight and "lower level" framework, Flask provides a significant latitude to the developer allowing quick and easy development; however potentially allowing the cultivation of poor software engineering practices. It is therefore important to understand the full set of features provided by Flask, it's design patterns and the Pythonic approach - this is all covered in the documentation (@pallets_welcome_2010). 

### Django 

Django is a higher level more feature rich web framework. By default it provides tools such as a database abstraction layer, form validation, authentication controls etc. These provide a lower barrier to entry and are well maintained within the ecosystem, reducing the boilerplate required to get started and enforcing best practice and security by default. However, the prescriptive nature of the framework requires you to design your webservice in a specific way and use specific Django features. As mentioned, this can pay off in the long run by providing better maintainability, support and more predictable code (through use of a standard set of libraries) but does restrict development to the "Django way". 

--- 

For this proof of concept I will use Flask. This will provide a very simple base on which to integrate my classes and although it will require writing additional boilerplate (eg. for a login system), as this is a proof of concept scope creep can be avoided through a clear design from the outset. 

## Webservice UML 

This does not include classes generated or required by Flask - only application classes. 

## Device 


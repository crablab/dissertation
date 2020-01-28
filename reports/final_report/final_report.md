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
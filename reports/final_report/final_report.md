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

Ideas:
- Ethics around attendance monitoring as a whole 
- Ethics around asking people to carry phones and requiring them to do so 
- The moral and ethical concerns around browser fingerprinting and how it is commonly used
    - More general concern around digital and web privacy 

---

Privacy and freedom of expression is becoming an increasingly debated issue, especially online and in the digital world. As computing power and storage capacity have increased over the last few decades, it has become feasible for companies to collect large amounts of data at an individual level for analysis and data mining. Whilst often the data is claimed to be anonymised, studies such as @https://www.nature.com/articles/s41467-019-10933-3 have shown that it is possible to use modern machine learning techniques on large datasets to identify individuals. 

This project advocates not only requiring students to prove their presence in an auditable way but the bulk collection of browser data to prevent fraud and deception. Taking the former as a given, is it proportionate to collect a uniquely identifiable hash of the student's browser each time they mark their attendance?

One important consideration is data protection, specifically the requirements of the General Data Protection Regulation or GDPR. As this data can uniquely identify a browser, it is possible it could be used in conjunction with other information (for example, lectures attended) to identify an individual. It is therefore classed as Personally Identifiable Information. 

In order to process the data we must have a lawful reason to do so - in this case we claim legitimate interest applies. We must therefore meet the following test: 

> Identify a legitimate interest;
> Show that the processing is necessary to achieve it; and
> Balance it against the individual’s interests, rights and freedoms.

https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/lawful-basis-for-processing/legitimate-interests/

Our legitimate interest is in the prevention of fraud but we still need to show that our processing of the PII is necessary, proportionate and balances the individual freedoms of the person. 

The https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/lawful-basis-for-processing/legitimate-interests/ continues: 

> Does this processing actually help to further that interest?
> Is it a reasonable way to go about it?
> Is there another less intrusive way to achieve the same result?

The processing of the PII does further the interest as we use it to measure connections between students and to identify suspicious patterns of behavior (eg. a single device signing in multiple students). We consider this to be a reasonable method of measuring this data points and that this is the least intrusive method - we do not store the raw data for example, just the irreversible fingerprint hash. 

The ICO test around individual freedoms look mainly at the sensitivity of the data, disclosure of the processing and appropriate safeguards to minimize harm. The data is fairly sensitive - appropriate controls should be in place to limit and record access and it should be removed as soon as the legitimate interest ends. 

Even though we can demonstrate that the data collection in this scenario is proportionate, there are a number of other uses for browser fingerprints which operate in a decidedly more grey area. 

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
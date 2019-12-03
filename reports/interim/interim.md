# Abstract

Royal Holloway keeps track of attendance in lectures both to ensure that students are regularly attending and also to satisfy legal requirements regarding the visas of overseas students [@home_office_uk_government_tier4_2019]. It is essential that this data is gathered and analysed efficiently and accurately.

In the past attendance has been tracked using signatures on registers. More recently, due to the lack of scalability of this former approach, a system of clickers has been employed [@royal_holloway_department_of_computer_science_department_2018]. This latter system has proved to be non-optimal and insecure. 

The aim of this research is to investigate existing attendance monitoring solutions and existing academic research into the problem to determine a more optimal solution for Royal Holloway. An MVP (Minimum Viable Product) will be built to test assumptions and demonstrate the core ideas of the proposed solution. The system will need to be user friendly and satisfy Royal Holloway's requirements whilst also not becoming burdensome on lecturers, students and administrative staff. 

## Motivation 

The primary motivation is to offer a more secure and convenient system for students. The author is well acquainted with both the paper based and clicker systems in use, and the associated merits and pitfalls. An improvement in the process not only allows less detractions from the lecture content but, as @universities_uk_student_2019 writes: "Attendance monitoring can also be perceived as unfair and harm international student experience." - a more low key and low effort system reduces the potential for discrimination as a result of the perception of international students imposing rules on domestic students, as a result of their presence. 

@universities_uk_student_2019 continues, "The current system imposes a significant administrative burden on both institutions and the Home Office..." with a survey conducted by Universities UK concluding the the total cost of compliance with Tier 4 rules being £40 million to the UK Higher Education sector [@universities_uk_student_2019]. A separate study by @ey_challenges_2019 for the Russell Group noted "Attendance monitoring is particularly time consuming across such a large university with many different modes of study. Collating the data, analysing it and escalating cases for investigation/explanation has created an industry of work for very little tangible benefit given that HEI students are very low risk of visa abuse.". 

It is therefore clear that a more streamlined, automated and secure system is a clear benefit to both the University and Higher Education sector alike, as well as to students. 

## First Term Progress

Work in the first time hasn't gone entirely as planned, however some interesting discoveries were made in the reports and I have made significant progress on my understanding of the overall Bluetooth standards and clarified how my proposed implementation will work in practice. 

The hardware elements of the project have taken longer than expected, in both the clicker research and Bluetooth implementation. This has mainly been due to communication issues between the BLE/Nordic devices and the various microcontrollers. The delays here have been disappointing, especially in the BLE case where a simple move to a different version of the device fixed the issues. The work to get the devices to communicate has allowed considerable research into troubleshooting techniques for UART and I learned a lot about flow control, which I hadn't come across before. 

The clicker project remains unfinished at the moment. I intend to try and eliminate the encoding issues with the Arduino by connecting directly to the NRF chip from a Raspberry Pi. This will also require working on a basic library for the NRF chip, based on the code already in use on the clicker basestation, by @mooney_nickmooney/turning-clicker_2019. I hope to achieve this over Christmas to complete that report.

The BLE work has been delayed by the issues with the clicker, and then extensive issues with the BLE device itself as described in the report. However, once working there has been good progress and work will now continue on developing a working Web Bluetooth PoC for integration with the overall system. 

Work on the cryptography report was pushed back, although the PoC program was completed and is ready to be implemented. As the signing mechanism isn't the most crucial part of the project (as long as it works and uses an established and peer reviewed algorithm) the report here was likely to contain less information that the aforementioned research. 

Overall design work on the system continues on track as the user stories and functional requirements have been defined. The full design with appropriate schemas, UML and mock user interfaces is to be developed for the draft report. 

An additional report on browser fingerprinting was added as this was discovered to be a bigger part of the project than originally envisioned. This did take up additional time however was extremely useful research and yielded an interesting PoC program. 

In summary, although there have been significant challenges in several areas, the identification of these risks early on allowed mitigation within the project by rescheduling other workstreams and running parts in parallel to allow for greater flexibility whilst troubleshooting. Background research has gone well and provided additional context when troubleshooting issues and also when designing the overall system, to ensure constraints are observed. 

## Continued Risks

There are continued risks in the project, and additional risks have been identified. 

### Clicker emulator encoding
- **Impact:** Medium

This risk currently exists and is being mitigated. It is not a crucial part of the project and although it serves as a useful demonstration and makes for an interesting report, lack of a fully working system is not critical to success of the project. The plan is to attempt a different approach, however this will be timeboxed to ensure excessive time is not wasted. 

### Web Bluetooth API 
- **Impact:** High

The Web Bluetooth API is less mature and less well supported than originally hoped. On the one hand, this does make a more interesting and relevant project (as there are few applications that use the API) however support is limited both in browsers and in documentation. Currently, although the API works on a specific Chromium set-up there are driver issues on Linux. Workarounds are being investigated and anecdotal research suggests that Google Chrome on Windows 10 may provide a more stable development environment. This has not yet been tested on any smartphones - this is an area to investigate.

Should the API fail to work with any software combination, it will be necessary to seek another solution. The implementation would be possible using standard HTTP client/server architecture on a dedicated wireless network; however this is not ideal for various reasons. There may also be other communication mediums commonly supported on smartphones, for example NFC, that could be investigated should the need arise. 

The current plan is to continue working towards a Web Bluetooth implementation, but should this not prove possible more mature technologies are available and there is valuable research in looking at the current usability of Web Bluetooth. 

## Literature Survey 

?? not sure what to write

## Reports

Reports are included in the following order, at the end of this document: 

- Clicker Report
- Browser Fingerprinting Report
- Communication Report
- Outline System Design 

# Acknowledgements 

Thanks to @tom_pollard_template_2016 for the front cover template which I have adapted, @marco_torchiano_how_2015 for the Pandoc table preamble and @cohen_third_2013 for the Final Year Project guide and suggested layouts. 

\pagebreak 
\onecolumn 

# Bibiography 

Due to the nature of this project, available references on the subject are limited and will be confined to more general information security concepts as well as attendance monitoring. In this report the available references are provided by those who have investigated these devices beforehand. 

---

<div id="refs"></div>
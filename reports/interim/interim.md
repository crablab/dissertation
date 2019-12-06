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

## Project Diary 

### October 21, 2019

Monday:

- Have spent the day debugging issues with serial communication
- Have written a small Python script to try sending data which isn’t working
- Discovered that I’m not actually broadcasting the hardcoded messages I thought I was (or at least they aren’t valid). I’m trying to determine why this is…

### October 28, 2019

- Finished writing up report on clicker emulation for now
- Additionally, gave up on getting the final pieces of clicker emulation to work for the moment: I will come back to it over a period of time once I’ve had a chance to consult the internet and Nuno some more, to work out what is going wrong!
- Begun researching communication methods for my proposed solution and preemptively ordered a HM-10 Bluetooth 4 module for further investigation

### November 4, 2019

- Wrote some more about clicker communication
- Got a Raspberry Pi working over Serial with Ethernet passthrough
- Determined that it’s not possible to connect to a Pi over Serial and utilize UART on the GPIO. Although the Broadcom chip support this, it is not connected in a way that allows both these Serial connections at once unless you use the Compute Module (the professional version of the Pi)
- Going to look into other options here as I want to avoid using an Arduino as I would like the networking capabilities of the Pi and the additional processing capacity. It also allows me to work with more standard cryptography libraries.

### November 4, 2019	 

- Switched from a Pi Zero to a Pi 2 and now connecting via SSH with ethernet passthrough
- UART is now working, testing to try and get communications working with the HM-10

### November 5, 2019

- I have a serial connection open, but I am not receiving data back. The board does have UART flow control pins and although I have tried the hacks (hold the enable pin low), I am still not getting any data back. Enabling hardware flow control on the Pi is possible, but involved. I have been testing with minicom and all of the Google solutions are still not enabling it.

### November 13, 2019

Yesterday:

- Worked on more issues with the UART. I think I have found a solution but it seems it requires setting a config parameter on the board itself, so I have had to purchase some additional equipment to do this.

Today:

- Researched and wrote a PoC for fingerprinting web browsers and devices
- Researched PKI and RSA vs ECDSA algorithms. Wrote a quick Adaptor class with tests to play around with a library for this. To be extended.

Current blocker is getting the Bluetooth working. Once that is done it should be fairly easy to send data end to end (he says…) 

### November 14, 2019	  

- CeDAS workshop on report writing with very useful context and helpful information about how to structure the report. Have begun laying out interim report.
- Meeting with supervisor. Discussed progress and where to concentrate work from now on. Discussed how reports are not final and feedback is really useful on work that isn’t quite complete. Structure of interim report clarified.
- Started writing up investigations into browser fingerprinting. I shall probably provide an extra POC program here for illustrative purposes.

### November 18, 2019

- Discovered an article that suggested this might well be a logic level issue on the RX pin (3.3v vs 5v) and that there are two different baud rates depending on software.
- Took notes on BLE specification stuff for a report on communication options
- Discussed project in general with Dave – the various reports and the structure the project should take, plus the specific Bluetooth issues. Dave has suggested that as per another article there could be an issue with AT commands missing a line feed/carriage return, causing the null byte issue I’m seeing

### November 20, 2019

Yesterday:

- Chatted with supervisor about clicker report. Feedback about general tone and structure of report.
- Discussed general project outline and progress to date
- Feedback on current report proposals. Agreed to add an additional report on general project ideas and outline, as without it the context of the project is somewhat confusing for an outsider.
- Communication report to be written, cryptography report to be delayed in light on the additional outline report and browser fingerprinting work.

Today:

- Implemented changes suggested in clicker report: https://github.com/RHUL-CS-Projects/FullUnit_1920_HughWells/pull/5
- Working on outline report

### November 28, 2019

Earlier this week:

- Finished writing up the Outline report covering the basic system design and user stories
- Meeting with Supervisor to discuss this report, feedback and changes
- Significant research and compilation of notes on BLE specifications

Yesterday:

- Progress on Communications report theory. MIFARE attack covered and Bluetooth section complete up to part way through security features

Today:

- Finally managed to get HM-10 devices working properly. This has been delayed by waiting for hardware to arrive in dribs and drabs. An HM-10 from a different supplier and manufacturer arrived and, with no changed settings, has “magically” started working.
- I can now send data from a phone, through the HM-10 to a serial console and back again. My script to test AT commands works and various notifications are logged to the serial port when device changes take place (eg. disconnection). This is huge progress and I shall now be able to write a driver for the HM-10.
- Started work on a Web Bluetooth implementation. Have discovered that browser support is *shocking*. I currently am running experimental versions of Chromium (with flags enabled) and bluez (flags enabled) and am still encountering errors. I shall need to look further into this but it may prove unfortunatly rather fatal if I cannot find some combination of hardware that has reasonable support. Will discuss with supervisor.

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

## Directory Listing

The repository has the following structure:

- proof_of_concept_programs
    - clicker_basestation
    - clicker_emulator
    - crytographic_signing
    - device_fingerprinting
    - hm-10-investigations
- reports
    - clicker_report
    - communication_report
    - fingerprinting_report
    - interim 
    - outline_report
    - plan
    - proposal 

Reports are written in "Frankenstein" Markdown and \LaTeX. They are compiled using Pandoc via the Bash generation script in each directory. Compilation is non-trivial without all of the packages installed and thus it is recommended to refer to the end of this document for the outputs. Source is provided for reference. 

Each proof of concept program directory contains source code and where not covered in a report, a README for installation and execution. 

## Running Programs 

It should be noted that most programs submitted require hardware which I am happy to provide to those assessing the programs should they require it.  

## Reports

Reports are included in the following order, at the end of this document: 

- Project Plan (included for context)
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
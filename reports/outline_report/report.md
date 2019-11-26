---
title: "A proposed technical solution to attendance monitoring at Royal Holloway"
author: "Hugh Wells - 864564"
date: "20th November 2019"
papersize: a4
geometry: margin=3cm
---

# Abstract 

The current systems at Royal Holloway to monitor student attendance at lectures and other mandatory events have been discussed at length previously. This report aims to propose a new solution using modern technology which is more secure, trustworthy and less of an administrative burden. Functional requirements will be discussed and the overall solution including technical choices explained. Additional reports investigating technical details and justifying those in more detail will be available. 

# Problem Statement 

Royal Holloway keeps track of attendance in lectures both to ensure that students are regularly attending and also to satisfy legal requirements regarding the visas of overseas students [@home_office_uk_government_tier4_2019]. It is essential that this data is gathered and analysed efficiently and accurately.

In the past attendance has been tracked using signatures on registers. More recently, due to the lack of scalability of this former approach, a system of clickers has been employed [@royal_holloway_department_of_computer_science_department_2018]. This latter system has proved to be non-optimal and insecure. 

In the context of a lecture there are several key problems faced:

- **Circulation of a register**: In classes that range from 50 to 200 students it is infeasible to expect a paper register to have made a complete circuit of the room by the end of a class. Adding another register doesn't always solve this, as the paths of the two registers will often intersect and students are less interested in the optimal pathing of the register than the lecture content. There is often a "scrum" at the end of a lecture between those who did not sign to register their attendance and leave in time for their next class. 
- **Data processing**: When discussing paper registers, it is obvious that significant administrative effort is required to process the written records and translate them to a digital medium for easy statistical analysis. This becomes more complex when there are multiple registers for a class, or when changes to the document in question are made. For instance, sometimes students have not been included on the sheet due to an oversight and they will then append their name to the end of the document to register their attendance in a non-standard fashion. Whilst with the digital clickers there is no need more manual transcription, the data from the Turning Point software is in a propitiatory format and requires conversion to a CSV and then further processing to be handled by the custom software used in the department for attendance monitoring. 
- **Forgery**: Both the clicker and paper register systems are vulnerable to attack. The paper register can simply be signed by another person on behalf of an absentee. The way to prevent this is to carry out signature checking against a sample on record and random ID checks at lectures where forgery is suspected. The signature comparison is labour intensive and only catches bad forgeries. The attack on the clicker system has been described in more detail in another report. 
- **Intrusiveness**: The paper register is relatively intrusive in a lecture, however more so to the students than to the lecturer. The clicker system, anecdotally, tends to cause more issues as the set up process is non-trivial, cutting into lecture time and lecturer patience, and data collection can be somewhat unreliable too. There is no real feedback for a student that their attendance has indeed been counted in the same way as there is on a paper register. The clicker system also requires you to remember a device that must be in your possession to verify your identity - a device is easy to forget, a signature less so. 

# User Stories 

A number of user stories have been written to illustrate the user journey and clarify the key focus of a solution. These are included in Appendix 1. 

# General Description

The proposed solution is to have a Bluetooth Lite device that a lecturer will configure with an online gateway prior to the lecture, and will be plugged in to a power source for the duration of the lecture in the lecture theatre. No networking or connection to a PC will be required for this device. 
Students will log in to a website and request to register for the lecture. The website will, using the Bluetooth API, connect to the Bluetooth device in the lecture and will request that the device signs a blob of data provided by the server. This will provide proof that the student was in, at least the vicinity, of the lecture. 

## Issues with the solution

- There is nothing to stop someone signing in and then simply walking out; or indeed standing just inside the range of Bluetooth Light but outside the lecture theatre. This is not a risk mitigated by either the register or the clickers. It could be possible to have the student device poll for signatures throughout the lecture, however this would potentially have technical constraints around student device battery life, the capacity of the Bluetooth signing device and running background processes in a web browser. Ultimately, Bluetooth Light is not designed for these kind of constant connections so Bluetooth Classic (which is more difficult to implement) would be a more appropriate communication medium.  
- It is conceivable that students might attempt a relay attack by generating their data blob remotely and then passing it to another student to transmit it for signing, before they submit the signed data back to the server without ever having been near the lecture. There are two ways this could be solved:
    - Firstly, including the student Bluetooth MAC address in the blob signed by the server and validating it with the source MAC address of the transmission on the Bluetooth device would allow you to ensure the device that sent the message also generated the message. This then requires the Bluetooth device to carry a certificate used by the server to validate the message it has sent - this isn't a bad idea regardless, although having the Bluetooth device blindly sign messages regardless isn't a huge security concern as a brute force attack is infeasible. Technically, Bluetooth devices are supposed to have a fixed and unique MAC address which will not change - plus a configurable MAC that does. However, device manufacturers have begun to randomize even the supposedly fixed MAC addresses for privacy reasons, so these may not be a reliable identifier. [@kalantar_analyzing_2018]
    - Secondly, implementing timing based controls to detect the round trip time of a message to ensure it does not exceed a certain value. This is the method used in EMV payment cards (In the specification known as Relay Resistance Protocol) and is vulnerable to attack should a rogue card reader not carry out the timing checks correctly. Our security model here is different, as we make the assumption that both the server and the Bluetooth device are not compromised and as any modification of the data would be detected (as the signatures would no longer match) it would not be possible for the student device to alter the timestamp to carry out such an attack. [@chothia_making_nodate] This is the solution that will be implemented, subject to time constraints. 

# Functional Requirements 

1. Student

    a) A website for students to access to manage their attendance 
    b) An average percentage attendance score for students for their currently ongoing classes 
    d) An individual percentage attendance score for students for a given class 
    e) Data exports of attendance by class
    f) Capability to initiate registration process for a class to mark a student as having attended 

        1. Website to initiate wireless connection with device in lecture theatre 
        2. Website to send data to be signed by wireless device, and receive response 
        3. Website to record correctly signed responses as attendance 
    g) Ability to make absence request for a given time period 
        1. Ability to view absence requests and their status
        2. Ability to withdraw an absence request 
2. Lecturer

    a) Lecturers to be able to view their classes on a website
    b) Lecturers to be able to see overall percentage attendance for their class 
    c) Lecturers to be able to see breakdown of percentage attendance by student per class 
    d) Lecturers to be able to see breakdown attendance records by student per class 
    e) Lecturers to be able to provision wireless device for an upcoming class 
        1. This involves providing a configuration file and certificate to the device 
3. Administrator

    a) Administrators to be able to view classes by department on a website 
    b) Administrators to be able to view same breakdown of data as lecturers 
    c) Administrators to be able to view student overall attendance across all classes 
    d) Administrators to be able to view students whose attendance falls below required minimum 
    e) Administrators to be able to view students whose days of absence is above a required threshold 
    f) Administrators to be able to manage absence requests 
        1. Ability to review outstanding requests
        2. Ability to approve or deny requests 
        3. Ability to view previous requests per class or per student 
    g) Administrators to be able to view browser fingerprinting data 
        1. Ability to see when a fingerprint is used across multiple students
        2. Ability to see fingerprint consistency per student 
    h) Arbitrary data export for all previous views

# Constraints 

## Design constraints 

1.1) The website will be hosted on a Python Flask application backed by a MySQL database 
1.2) The frontend will be based on the Bootstrap framework 
1.3) The wireless device will be a Bluetooth Low Energy device compatible with the Bluetooth 4.1 specification
    1.3.1) This is currently planned to be a HM-10; further details are available in other reports 
    1.3.2) The processing capability will be provided by a Raspberry Pi
    1.3.2) The provisioning of the device will be carried out by copying a file to the SD card of the device 

# UML Sequence Diagram

Included in Appendix 2

<!--
## Data-Flow Diagram

Included in Appendix 3. 
-->

# Acknowledgements 

Thanks to @tom_pollard_template_2016 for the front cover template which I have adapted, @marco_torchiano_how_2015 for the Pandoc table preamble and @cohen_third_2013 for the Final Year Project guide and suggested layouts. The Data-Flow Diagram was based on a StackOverflow example: @noauthor_tikz_nodate.

\pagebreak 
\onecolumn 

# Bibiography 

<!--
Due to the nature of this project, available references on the subject are limited and will be confined to more general information security concepts as well as attendance monitoring. In this report the available references are provided by those who have investigated these devices beforehand. 
-->

<div id="refs"></div>

# Appendix 

\pagebreak  

## Appendix 1

### User Stories 

#### Student 

1) "As a student I want to register my attendance so I can prove I was at a lecture"
2) "As a student I want to register my attendance without distraction from the lecture content"
3) "As a student I want to be able to know my attendance has been counted"
4) "As a student I want to be able to see my attendance history" 
4) "As a student I want to register with the minimum of additional hassle"
5) "As a student I don't want to have to remember extra items to register" 

#### Lecturer 

1) "As a lecturer I want to not have to think about lecture registration"
2) "As a lecturer I want to have the minimum of distractions and the minimum of fuss, in registration"
3) "As a lecturer I don't want to be involved in the registration process" 

#### Administrator

1) "As an administrator I want to have all the registration data in a machine readable format"
2) "As an administrator I want to be able to easily identify students who have not reached minimum attendance levels"
3) "As an administrator I want to easily identify cases of fraud or forgery" 
4) "As an administrator I want to generate reports on attendance and export raw data" 

#### Home Office

1) "As the Home Office I want to be assured that Tier 4 visa students are meeting attendance requirements" 
2) "As the Home Office I want to audit the Universities process to ensure it is compliant" 
3) "As the Home Office I want the system to be trustworthy and not open to abuse" 

## Appendix 2

### UML Sequence Diagram

\begin{figure}

  \centering
  \begin{sequencediagram}

    \newinst[1]{A}{Server}{}
    \newinst[2]{B}{Student Device}{}
    \newinst[3]{C}{Bluetooth Device}{}
    \begin{call}{B}{Request Webpage}{A}{}
    \end{call}

    \postlevel
    
    \begin{call}{B}{Browser Fingerprint}{A}{Ack}
        \postlevel
        \postlevel
        \begin{call}{A}{\shortstack{S(fingerprint,\\ nonce,\\ timestamp)}}{B}{\shortstack{S(S(fingerprint,\\ nonce,\\ timestamp))}}
            \begin{call}{B}{\shortstack{S(fingerprint,\\ nonce,\\ timestamp)}}{C}{\shortstack{S(S(fingerprint,\\ nonce,\\ timestamp))}}
            \postlevel
            \postlevel
            \end{call}
        \postlevel
        \end{call}
    \postlevel
    \end{call}

  \end{sequencediagram}
\end{figure}

<!--
## Appendix 3

\begin{tikzpicture}[
  font=\rmfamily\footnotesize,
  every matrix/.style={ampersand replacement=\&,column sep=2cm,row sep=.6cm},
  source/.style={draw,thick,rounded corners,fill=yellow!20,inner sep=.3cm},
  process/.style={draw,thick,circle,fill=blue!20},
  sink/.style={source,fill=green!20},
  datastore/.style={draw,very thick,shape=datastore,inner sep=.3cm},
  dots/.style={gray,scale=2},
  to/.style={->,>=stealth',shorten >=1pt,semithick,font=\rmfamily\scriptsize},
  every node/.style={align=center}]

  % Position the nodes using a matrix layout
  \matrix{
    \node[source] (a) {Server}; \& \& \\
    \& \& \node[source] (b) {Student Device};\\
    \node[source] (c) {Bluetooth Device}; \\     
  };

  % Draw the arrows between the nodes and label them.
  \draw[to] (a) -- node[midway,above] {1) Webpage} (b);
  \draw[to] (b) -- node[midway,above] {2) Browser Fingerprint} (a);
  \draw[to] (a) -- node[midway,above] {3) S(fingerprint, nonce, timestamp)} (b);
  \draw[to] (b) -- node[midway,above] {4) S(fingerprint, nonce, timestamp)} (c);
  \draw[to] (c) -- node[midway,above] {5) S(S(fingerprint, nonce, timestamp))} (b);
  \draw[to] (b) -- node[midway,above] {6) S(S(fingerprint, nonce, timestamp))} (a);

  % Draw the dotted surrounding lines and add the labels as separate nodes
  % This is necessary because the anchor of the fitted node is always center

  \node[draw,dotted,fit=(a) (b),inner sep=4ex,] (AB) {};
  \node[above=-3ex of AB] (ABt) {Internet};
  \node[draw,dotted,fit=(b) (c),inner sep=4ex,] (BC) {};
  \node[above=-3ex of BC] (BCt) {Bluetooth};
\end{tikzpicture}
-->
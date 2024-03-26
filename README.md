# Lottery App Security Enhancement Project

## Introduction
This repository documents the transformation of a vulnerable web application into a fortified platform with sophisticated security measures. The project aimed to deter potential attackers and mitigate security risks associated with the lottery app.

***Note: Due to the security oriented nature of this project, the web interface is not very polished and sometimes difficult to use***

## Overview
The lottery app allows users to submit draws of 6 numbers, either chosen randomly by the website or manually inputted. The admin selects a winning draw, and matches result in user wins. Three user types exist: regular users with accounts, admins for administration, and anonymous users who can register or log in.

## Security Analysis
The initial app lacked essential security features, enabling unrestricted access to all pages and storing sensitive data without encryption. Vulnerabilities included lack of input validation, absence of error handling, and insufficient access controls. Additionally, critical features such as two-factor authentication and secure data storage were missing.

## Security Enhancements
To address vulnerabilities, a series of security enhancements were implemented:

- **Input Validation**: Implemented robust input validation for passwords, emails, and phone numbers to prevent data manipulation and unauthorized access.
- **Error Handling**: Enhanced error handling mechanisms to provide informative feedback and prevent system crashes.
- **Cryptography**: Employed cryptographic techniques to encrypt passwords and lottery draws stored in the database, ensuring data confidentiality.
- **Two-Factor Authentication (2FA)**: Implemented 2FA for enhanced user authentication, mitigating the risk of unauthorized access.
- **Access Management**: Established role-based access controls to restrict page access based on user roles, enhancing system integrity.
- **Logging Feature**: Implemented logging functionality to monitor user activity and detect suspicious behavior, aiding in threat detection. Logs can be found in the .log file
- **Security Headers**: Added security headers to mitigate common web vulnerabilities and ensure secure communication.

## Evaluation
Despite challenges, the project successfully enhanced the security posture of the lottery app. Future enhancements could include implementing Google's reCAPTCHA and improving key management practices for added security.


---
*This project was conducted as part of coursework. For more details, refer to the provided lab report (Lottery App - Lab Report).*

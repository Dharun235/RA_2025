# Work Documentation

## **Important Links**
1. [Excel sheet for task tracking and time management](https://docs.google.com/spreadsheets/d/1C0Kd1SOetn8jI25BcTjdE50et2n8ZGj_UXqiCZhcxL4/edit?usp=sharing)  
2. [Pepper Robot Documentation](http://doc.aldebaran.com/2-4/home_pepper.html)  
3. [Choregraphe Software (GUI for programming Pepper)](https://www.aldebaran.com/en/support/nao-6/downloads-softwares)  
4. [Tips for using Pepper](https://docs.google.com/document/d/1MynBVZmqCWqIwQ_w5aU5E7giC-ntxYUUJDfNpHRQ4MI/edit?usp=sharing)  
5. [Last year's scripts and instructions for Pepper](https://drive.google.com/drive/folders/1O8ZfYgEOGoVL9HCtFLH7XAZz9CRnFjlt?usp=sharing)  

---

## **02/12/2024**  
- Setup an [Excel sheet](#important-links) for tracking work hours and joined Slack for communication.  
- Reviewed documentation on Pepper robot's basic setup.  
- Encountered issues connecting to Pepper's IP address with delays.  
    - Resolved temporarily by unplugging and reconnecting devices. Issue reoccurred.  
- Planned to explore Pepper's SDK functionalities and work on door-opening mechanisms during the next session.  

---

## **03/12/2024**  
- Studied conflict resolution between humans and robots using a simple interaction scenario (e.g., robot movement along a conflict line).  
- Tested basic functionality:
    - Implemented and tested code for Pepper to speak and move a meter using Choregraphe.  
- Created a GitHub repository for documenting all tasks and activities.  
- Installed Choregraphe software.  
- Set up a Python virtual environment:  
    1. Navigate to the desired folder using `cd`.  
    2. Create the virtual environment:  
       ```bash
       virtualenv -p C:\path\to\python27\python.exe my_env
       ```  
    3. Activate the environment:  
       ```bash
       my_env\Scripts\activate
       ```  
    4. Deactivate the environment when finished:  
       ```bash
       deactivate
       ```  

---

## **06/12/2024**  
- Worked from 9:00 AM to 12:00 PM.  
- Received additional examples and resources for using Pepper from Ilaria. Relevant GitHub repositories:  
    - [Pepper Applications by Vicken-Ghoubiguian](https://github.com/Vicken-Ghoubiguian/pepperApplications): Contains various applications installed on Pepper for trade fairs, open days, etc.  
    - [PepperChat by ilabsweden](https://github.com/ilabsweden/pepperchat): A dialog system for Pepper and Nao based on ChatGPT.  
    - [Pepper Tic-Tac-Toe by Maverick Joy](https://github.com/maverickjoy/pepper-tic-tac-toe): Real-time Tic-Tac-Toe game between a human and Pepper.  
    - [Pepper Teleoperation by nevalsar](https://github.com/nevalsar/pepper-teleop): A simple Python-based teleoperation script for Pepper.  
- Set up the required dependencies and environments for working with Pepper:  
    - Created environment variables for different Python versions:  
        - `python2732`: Python 2.7 (32-bit)  
        - `python2764`: Python 2.7 (64-bit)  
        - `python`: Python 3.x (default environment)  
    - Used **Visual Studio Code** as the terminal for running scripts. Commands starting with `python` must be preceded by `.\`.  
    - Initialized **Python 2.7 (32-bit)** as the default environment for the PepperChat project.  
- Confirmed that no additional virtual environments are needed for PepperChat as it works without issues in the default environment setup.  

--- 

## **10/12/2024**  
- Worked from 9:00 AM to 12:00 PM.  
- Pepper showed different IP addresses starting with 10 but later after 30-40 minutes showed the correct IP address and got connected to the PC
- Access to chatGPT requires payment so couldn't do the pepperchat implementation  
- Next day try for displaying the text on the tablet and test the teleoperation, chatGPT integration and various applications listed in Pepper Applications
  
--- 

## **13/12/2024**  
- Worked from 9:00 AM to 12:00 PM.  
- Pepper showed different IP address and as it connects to some IP address starting with 10, I suspect it is connecting to NOMAD or any other chalmers wifi
- Registered a case with Aldebran regarding this issue - https://corporate-internal-prod.aldebaran.com/en/support/case
- Thinking about factory reset the robot - https://support.unitedrobotics.group/en/support/solutions/articles/80000962214-pepper-how-to-factory-reset-the-tablet-only
  
--- 

## **19/12/2024**  
- Worked from 9:00 AM to 17:00 PM.  
- Pepper robot - AP990396A14Y9A200044 and version 1.8 and the same for tablet and Got reply from aldebran to mail to United robotics group - https://support.unitedrobotics.group/en/support/solutions/80000327218
- Mailed to IT support for finding out the wifi corresponding to the IP address - 10.132.0.186
- Connected the ethernet cable to the head and then robot connected to the IP address - 192.168.0.101 and the wifi as suspected is connected to NOMAD and now changed
- Tablet is turned on, connected to wifi and the settings tab is open by following this - https://github.com/arlemi/setup-wifi-pepper. So head and tablet to be checked whether they are on same wifi.
- Connect to tablet using ssh and you can make it do various tasks like displaying text, photo or website on tablet.
- Trying to do the teleoperation using the ubuntu 20.04 in virtual box
--- 

## **20/12/2024**  
- Worked from 9:00 AM to 16:00 PM.
- Using virtual box for ubuntu environments
- pynput cannot be installed on many platforms like ubuntu 20, 16, and windows 11 too so tried with keyboard library but problem persisted.
- evdev package was installed with command pip install evdev or with pip install evdev==<version> and it works randomly for different environments
- pepper tablet is fine and works perfectly
- Android app creation requires qiSDK which is compatible only for some platforms like ubuntu 16.04 or windows 10
- Eduroam is not connecting properly with pepper tablet so have to stick with robotkuggen or robotkuggen5G
- Tried with these tutorials for teleoperations but didn't work out well - https://github.com/nevalsar/pepper-teleop/tree/main and https://github.com/lucregrassi/robot-teleoperation-interface so had to look for other ways of using them, which requires python sdk to be downloaded, which again depends on which enviroment you use and what sdk you are trying to use as there are few types like naoqi, qiSDK and also choregraphe can be used where there is python block inside programming in box libraries which you can use to program the robot.

--- 


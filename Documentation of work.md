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

## **30/1/2025**  
- Worked from 9:00 AM to 17:00 PM.
- The website - https://www.aldebaran.com/fr/support/nao-6/downloads-softwares is not present.
- The scp command didn't work out well as the location of html file or any other file in pc to be moved to tablet was not able to be discovered. So, I had to use gmail to send and download. But even then, through the command terminal in ssh, I was not able to find the downloads folder.
- Downloaded the NAOQI older version in the ubuntu 14 and successfully ran some simpler scripts like pepper robot saying "hello I am pepper" in python through python sdk using command terminal in ssh.
- Tried to install the requirements of tic tac toe game https://github.com/maverickjoy/pepper-tic-tac-toe?tab=readme-ov-file but couldnt install properly and the reason was not found.
- Tasks for next week - app for "yes or no", recognize a line through camera and stop moving, game like implementation in pepper for exhibitions.
- Use ./filename.run for executing the setup file and also be in root to install and change the permissions.
- Executed some programs in the pepper applications example - https://github.com/Vicken-Ghoubiguian/pepperApplications but the tablet didn't work properly as intended.

--- 
## **6/2/2025**  
- Worked from 9:00 AM to 17:00 PM.
- Clicking the tablet search app will take you to the initial stage of tablet. So, you need to power off.
- Tried to send using bluetooth, scp, mail, usb and everything worked except scp, but couldnt find the file's location. 
- Used flask based web app for "ARE you happy" and ran from pc and not in pepper, just entering the IP address is enough to see in browser. Same concept is to be used for user studies setup preparation.  
- Tried to install cv2, numpy, pillow but it doesn't get installed using pip and also the website is not available for download for pip2.7. Need to figure this out. Currently, black line detection program using pillow, numpy is done.
--- 

## **11/2/2025**  
- Worked from 12 to 17:00.
- Issue of installing cv2, numpy or any other is solved by using sudo apt python-<package>.
- "ARE YOU HAPPY" is enhanced.  
- Object detection is available, but line detection is not. Custom code is not working for some reason, which uses numpy, cv2. Cannot install gstreamer or any new package in python.
- Next is to work on line detect code
--- 

## **13/2/2025**  
- Worked from 9 to 17:00.
- Line detection removed.
- Figured out all control to be done from windows using cmd by connecting to pepper using ssh nao@IP, storing the files in pepper robot, thus directly using its packages and no installation required.
- No android app development and control only using python libraries and display using web interface in tablet.
- Antonia script for user studies is used.
- The only problem with pepper is not knowing how to use its camera properly for own purposes like line detection, even though libraries are available in pepper, we dont know how to connect to camera.
- ChatGPT interface is on the plan.
- Teleoperation script to move and rotate the robot is done in python and can be controlled with wasd keys.
- Are you happy script is updated.
--- 

## **18/2/2025**  
- Worked from 13 to 17:00.
- Read about misty robot and couldnt download app because of which no IP address -> No program development.
- Misty robot documentation - https://docs.mistyrobotics.com/.
- From Thursday, pilot studies to be conducted for Antonia's user studies.
--- 

## **20/2/2025**  
- Worked from 9 to 17:00.
- No pilot studies
- Coding is completed for user studies.
- Display of webpage or image is yet to be done.
- This documentation of code for pepper robot is found - http://doc.aldebaran.com/2-5/naoqi/core/altabletservice.html
- Next week Thursday pilot studies to be done for 2 people.
--- 

## **20/2/2025**  
- Worked from 10 to 17:00.
- No pilot studies
- Coding is completed for sonar movement with const vel and front sonar.
- Choregraph cannot be used for retrieving values from sonar. Webot, pybullet can be used with ROS or TCP along with choregraph for simulation.
--- 

## **27/2/2025**  
- Worked from 9 to 17:00.
- 2 pilot studies
- Studied about LLMs for pepper robot implementation
--- 

## **4/3/2025**  
- Worked from 9 to 17:00.
- 1 pilot studies, took notes of meeting following the questions:
  Record physical and verbal reactions
1.Smiling vs. neutral vs. discomfort (frowning, backing away).
2.Do they look at Pepper naturally, or avoid eye contact?
3. Do users acknowledge the explanation?
4. Do they react positively or negatively to the explanation?
5.Do users seem confused or uncomfortable when Pepper moves without explanation?
6. Do they verbalize concerns (e.g., "I didn’t expect that" or "Why did it do that?")?
Note engagement level
1. Are users more focused or distracted when Pepper is close?
2.Do users spend more time hesitating when Pepper is near?
3. Do users seem engaged or hesitant?
4. Do they look at Pepper naturally, or avoid eye contact?
- Studied about LLMs for pepper robot implementation and used Dialogpt for conversations. Recording the audio is possible in pepper but converting to text from wav isn't. So, have to find a way to programmatically transfer the files and then convert to text, then give to gpt for processing, then transfer the text to pepper, then use tts to speak.
--- 

## **6/3/2025**  
- Worked from 9 to 17:00.
- 0 pilot studies
- Excel sheet for experiment timings created
- Pepper chatgpt integration was much more difficult as pepper robot dont support or my pc doesnt allow to connect to pepper through HTTP, socket, TCP, FTP for to and forth transfer of audio files and text for STT, gpt reasoning and TTS.
- Tried to use the direct path of python2 in my pc instead of variables which worked.
- Created the portfolio and successfully displayed many correct information but there are some problems with display of special characters.
- Try to store the file in pc through HTTP after recording using pepper's audio channel. Code- audio_recorder.startMicrophonesRecording(audio_file, "wav", 16000, [0, 0, 1, 0])  and audio_recorder.stopMicrophonesRecording()
--- 

## **11/3/2025**  
- Worked from 9 to 17:00.
- 2 user studies
- Google sheets for experiment notes created
- Corrected the filtering of paper type in website
- Used audio from microphone of pc instead of pepper as it is not possible to stream the audio from pepper's microphone to pc for processing, and used Dialogpt for conversation.
--- 

## **13/3/2025**  
- Worked from 9 to 17:00.
- 2 user studies
- Tested all the example codes provided before for exhibition. ALTabletService is not working properly, other than that everything works fine.
--- 

## **18/3/2025**  
- Worked from 9 to 17:00.
- 3 user studies
- Tested all the example codes provided before for exhibition. ALTabletService is not working properly, other than that everything works fine.
- Website is improved.
--- 

## **21/3/2025**  
- Worked from 9 to 17:00.
- 2 user studies
- Tested all the example codes provided before for exhibition through choregraphe. ALTabletService is not working properly, other than that everything works fine.
- Website is improved.
- 2 methods to run behaviour files (.xar) - choregraphe and qilaunch behavior_file.xar in pepper.
- Problems to solve: [Factory reset](https://support.old.unitedrobotics.group/en/support/solutions/articles/80001010870-factory-reset-pepper-2-5-) and update the robot after Antonia's experiment to solve AlTabletService, all the projects that doesn't have component of tablet is working through choregraphe in ubuntu 14, chatgpt requires api key, teleoperation script done, tablet service is present but is curopted so need to do factory reset and update which requires email and password and can be doen after Ilaria has arrived, collect data from Mohammad to update the website and hosting details which can be done after he arrives.
--- 

## **25/3/2025**  
- Worked from 9 to 12:00.
- 1 user study
- Website is improved.
- Mailed to Aldebran support for ALTabletService not working.
--- 

## **26/3/2025**  
- Worked from 9 to 17:00.
- Website is improved with new pages. 
- Replied to Aldebran support with serial number - AP990396A14Y9A200044.
- Learnt and implemented some programs in Misty robot.
- Connect ethernet to misty -> check for ip address in 192.168.0.1 with admin as username and password -> find the ip address of robot using mac adress mentioned under DHCP client list and also in robot bottom -> Enter in the website to control and program
- [Documentation for python sdk of misty robot](https://github.com/MistyCommunity/Python-SDK)
- New task -  Language interpretor with misty
--- 



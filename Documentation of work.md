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
- [Documentation for python sdk of misty robot](https://github.com/MistyCommunity/Python-SDK) and [Misty robot lessons](https://lessons.mistyrobotics.com/python/python-lessons)
- New task -  Language interpretor with misty
--- 

## **28/3/2025**  
- Worked from 9 to 12:00.
- Learnt and implemented some programs in Misty robot, but capturing audio is not working properly.
- 1 experiemnt 
--- 

## **01/04/2025**  
- Worked from 9 to 12:00.
- 2 user studies
--- 

## **02/04/2025**  
- Worked from 9 to 17:00.
- Created the start version for HRI Trust study setup with website working, but buttons dont properly function in tablet.  
--- 

## **03/04/2025**  
- Worked from 9 to 12:00.
- 1 user study
--- 

# **08/04/2025**  
- Worked from 9 to 12:00.
- Troubleshooting tablet. Found that physical connection is proper as when typed lsub it shows google inc., pinging the tablet ip - 192.168.0.100 after ssh works, qicli list doesn't provide AlTabletService, cannot run into sudo as user nao is not given permission to restart naoqi, tabletservice is not found as before, tried to restart the robot physically using button pressing but didnt work, checked into logs in var folder where there are some stuff related to tablet-browser but not related to our issue, there is no problem with version and the only problem is whether altabletservice is not installed or naoqi is cracked or installed properly which can be solved only by aldebran support.
--- 

# **09/04/2025**  
- Worked from 9 to 15:00.
- Found from students that autonomous life is not disabled by them and this version doesn't have android studio.
- Troubleshooting tablet and website hosting process.
- 
---

# **15/04/2025**  
- Worked from 9 to 12 and 14-16.
- 4 Experiments completed and Antonia's experiments are done
- Website optimization for Ilaria experiment using JS and flask. Finish this task within this month.
- Mohammad website is hosted properly. Next steps is to correct the format and complete it within this week or next week.
---

# **15/04/2025**  
- Worked from 9 to 12.
- Website optimization for Ilaria experiment using JS and flask. Have to create pages for individual tasks.
- Mohammad website is to be updated with new information. Website host - ssh.strato.de and username -  570617047.swh.strato-hosting.eu and port - 22
---

# **23/04/2025**  
- Worked from 9 to 15.
- Website optimization for Ilaria experiment using JS and flask and now creating pages for individual tasks.
- Mohammad website is currently on updation with new information. 
---
# **24/04/2025**  
- Worked from 9 to 12.
- Website for Ilaria experiment is not completed becuase of some coding errors in js. 3 New tasks are given and have updated 1 and 3. 
- Mohammad website is updated with new information. 
---
# **28/04/2025**  
- Worked from 9 to 12.
- Website for Ilaria experiment is updated and progress bar is to be corrected. 2nd task is started, preferably uses flask, python sdk instead of ros, subprocess, basic webpage using html. 
- Mohammad website is updated with new publications but havent done the bibtex link for 2 publications. 
---
# **02/05/2025**  
- Worked from 9 to 15.
- Basic architecture for communication with gemini, pepper and user is done via pc microphone.
- Robot behaviour for different states of the game is almost over adn currently testing and improving the behaviour. Next is to embed them with the game.  
---

# **07/05/2025**  
- Worked from 9 to 15.
- Created the functions for pepper movement and gpt interface and embedded with the game.
- Have to fine tune the functions and proper timing of gpt interface
---

# **09/05/2025**  
- Worked from 9 to 12.
- Used multiprocessing for handling the gpt and game process parallel
- The following tasks are to be done next. 
1. in the game architecture, I would like you to add the option for a delay (this could be a random number between 3 and 6 seconds) before the robot does anything in response to a human's action. So basically, every time the human asks a question, the robot would wait before answering, every time the human makes an action in the game, the robot waits before starting a movement or performing another action. This could be one of our two conditions. Once this is ready, we will video record some trials and do the online experiment to figure out what people think is AI vs hard-coded
2. in the game architecture, have placeholders ready for adding gesture commands that the robot will perform every time an action is triggered. For example, every time the robot speaks to the human, it makes a corresponding gesture, every time the robot returns money, it also makes a corresponding gesture. What the gesture exactly is is still tbd (I'll send you a list later), but for now, just have placeholders ready
3. we would like the robot to say something at every turn of the game, even if the human doesn't initiate dialogue. For this, we could take inspiration from a list of sentences we used in previous experiments, using few shot prompting. Please read the documentation that I sent you earlier, and I will send some examples of these sentences later
10:09
4. after these things are set up, we will record videos and run the online experiment. I have everything already in place for the experiment, just missing the videos. Do you think that end of May could be a realistic timeline for having finished with parts 1-3?
10:10
5. While we run the online experiment, please continue working on the listening agent. By that time I will also have received the room microphone that I want to use.
- The main thing to clarify is to have for the entire experiment is to have AI / non AI and Trust and Non trust. 
---
# **14/05/2025**  
- Worked from 9 to 16.
- Did all the tasks mentioned except the microphone.
- Have to test everything and fine tune the prompts for each function.
- Have to get the robot movmements from Ilaria soon this month.
---

# **16/05/2025**  
- Worked from 9 to 12.
-  Regarding the gestures of the robot, here are some gestures that are already pre-built in choregraphe:
1) self and others: fastpointatuser (points to the human), openarminfront (used to invite to participate in a conversation, or pointing at an object);
2) affirmation: wide open both hands (to widely invite to participate in a conversation)
3) question: slowly offer both hands (it's meant to be used when waiting for an answer from the human); question lean front (robot leans towards the human)
3) moods (both negative and positive).
if you use the motion timeline, you can create new movements (you can have each joint move at the same time, by having two overlapping timelines)
- Have to use these with python, one way is to do behaviour code and another is to copy the script. Both dont work as for former, the files are trasnfered but the xar files are not identified as behavior meanwhile for later, no access to script for the required behaviors.
---

# **22/05/2025**  
- Worked from 9 to 10 and from 13 to 17.
- Created the custom movement functions as the behaviors werent working. Need to fine tune it.
- ALways robot to be in Autonomous Life mode.
- Need to create the few shot prompts for each stage of the game.
- Need to do a small experiment to notice the delay of the actions tomorrow for the AI vs non AI.
- The problem of the gemini ai replying in style - role: assistant, content: xxx to be eradicated.
---

# **23/05/2025**  
- Worked from 9 to 12.
- Integrated the movements to game, but doenst execute properly.
- AI vs Non AI differentiation with timer doenst seem good. So remove timer, and make as AI - fully autonomous experiment and NON AI as instruction given experiment, both has pepper communication, but the later has only specific instruction to talk.
- Used pgadmin for database to navigate conversations to one file for easy fetch and retrieve but advised to use SQLITE with python as it is much simpler to do.
- So next task is to split the AI vs NON AI system entirely, make the AI system experiment fully autonomous. Add the emergency responses. Make the game and conversation go in parallel.
- Experiments will take place on June mid and august mid. So need to complete within June first week. 
---

# **27/05/2025**  
- Worked from 15 to 17.
- Fixed to the csv and text file for data logging, seperate for game data and seperate for conversations. If it works properly, then remain, otherwise have to look into database usage.
- Need to find a way to integrate conversation and game seamlessly, the current problem I face is making the conversation always running irrespective of game, and change the prompt according to each state of the game.
- Tomorrow show an example of the game running fully.
---

# **28/05/2025**  
- Worked from 9 - 12, 13-14, 15-17.
- Successfully integrated the conversations with the stages of game through threading using semaphore concept to prevent overlapping of conversations.
- Fine tuned the prompts for each stage using few shot prompting.
- Only problem faced now is the sad behavior which gets into loop.
---

# **02/06/2025**  
- Worked from 9 - 11.
- Added the debugging code and reset code for each task using semaphore concept to handle only one task at a time.
- Same problem of behavior into loop occurs even when removed the particular code.
---
# **04/06/2025**  
- Worked from 9 - 11.
- Looping behavior stopped.
- Screen lock can be done by running command - "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --kiosk "http://192.168.0.101:5000" --edge-kiosk-type=fullscreen in command prompt after running the python app.py
- Overall game without GPT works well. Your laptop is to be used for experiment, no tablet.
- Integrating communication has some parts - interruption of mic and pepper voice is corrected, at every stage conversation is initiated by gemini, and the following is to be done for the gpt_conversation function. Code is to be changed in test1.py and then     use app.py for final remarks.
  A continuous, always-listening loop:
      1) Pepper speaks the stage prompt once at the very beginning.
      2) Then Pepper listens indefinitely:
         • If no speech for 10 seconds → Pepper “re-sparks” with a gentle nudge.
         • If user speaks:
             – Check intent: if “stop,” say goodbye and exit.
             – Otherwise, generate a response and speak it.
         • Loop back to listening again.
      3) The only way out of the loop is either:
         • stop_event.set() is called, or
         • the user’s intent is classified as “stop.”
- Next week full game display.
---
    

# **09/06/2025**  
- Worked from 9 - 13.
- Added a delay according to the number of characters to make sure the mic doesnt overlap with the pepper's speech.
- The correct logic for the game with and without gpt is implemented and the prompts for each type of speech is tuned.
- Have to tune the prompts for initial prompt at each stage and the response to be much shorter and reduce the delay between the pepper's speech and the mic listening to make it look more real.
- Need to find way to make the entire game more faster.
- Ensure the number of rounds is 10.
---

# **10/06/2025**  
- Worked from 13 - 17.
- Solved problems before.
- Had to make the reaction for results come in thinking page.
- Had to make the delay after invest page to reduce when using gpt.
- Had to make the unified gpt instead of creating and deleting threads.
---

# **18/06/2025**  
- Worked from 9 - 14.
- Solved the problem of kiosk and loading page using electron, making the setup easier.
- Old code without autonomous life is used even though it has delay as the problem of loading is solved.
- GPT and README file has to be optimized.
---

# **19/06/2025**  
- Worked from 13 - 17.
- Stored the web-app-loader in google drive for downloading.
- Need to have a parameter based game to input the game type of AI/ Non AI and Trustworthy/ Untrustworthy for the whole game at the start.
- Optimize the GPT for the whole game such that it talks only when the user havent responded for a long time for conversation as there are already default dialogues delivered by the robot.
---


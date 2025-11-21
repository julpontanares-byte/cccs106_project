# Lab 2 Report: Git Version Control and Flet GUI Development

**Student Name:** Pontanares, Juliet S.\
**Student ID:** 231002289\
**Section:** BSCS - 3A\
**Date:** 09/03/2025

## Git Configuration

### Repository Setup
- **GitHub Repository:** https://github.com/julpontanares-byte 
- **Local Repository:** ✅ Initialized and connected
- **Commit History:** 1 commit related to the Week 1 lab activity, documenting initial setup and completion of required tasks with a clear.

### Git Skills Demonstrated
- ✅ Repository initialization and configuration
- ✅ Adding, committing, and pushing changes
- ✅ Branch creation and merging
- ✅ Remote repository management

## Flet GUI Applications

### 1. hello_flet.py
- **Status:** ✅ Completed
- **Features:** Interactive greeting, student info display, dialog boxes
- **UI Components:** Text, TextField, Buttons, Dialog, Containers
- **Notes:** Encountered an unexpected error due to disabled settings in the terminal while running the application. Resolved the issue by enabling the required settings in the command prompt (cmd). Also, was unable to display the app info as intended.

### 2. personal_info_gui.py
- **Status:** ✅ Completed
- **Features:** Form inputs, dropdowns, radio buttons, profile generation
- **UI Components:** TextField, Dropdown, RadioGroup, Containers, Scrolling
- **Error Handling:** Input validation and user feedback
- **Notes:** The personal_info_gui.py application is simple yet highly flexible, allowing easy customization of form fields and user interactions. Its modular design makes it straightforward to add new input types or validation rules as needed.

## Technical Skills Developed

### Git Version Control
- Understanding of repository concepts
- Basic Git workflow (add, commit, push)
- Branch management and merging
- Remote repository collaboration

### Flet GUI Development
- Flet 0.28.3 syntax and components
- Page configuration and layout management
- Event handling and user interaction
- Modern UI design principles

## Challenges and Solutions

### Challenges and Solutions

During the lab, I encountered several difficulties:

- **Git Setup Issues:** Initially, I had trouble connecting the local repository to GitHub due to incorrect remote URL configuration. I resolved this by double-checking the remote settings and using `git remote set-url origin <correct-url>` to fix the connection.
- **Terminal Settings for Flet:** While running the Flet applications, an error occurred because certain terminal settings were disabled. I enabled the necessary settings in the command prompt, which allowed the applications to run smoothly.
- **Input Validation in GUI:** Although I did not add new features to `personal_info_gui.py`, I ensured that basic input validation was in place by checking for empty fields and providing user feedback through dialog boxes.

Overall, these challenges improved my troubleshooting skills and deepened my understanding of both Git and Flet.

## Learning Outcomes

Through this lab, I learned how to use Git for version control by following step-by-step instructions, which helped me understand the workflow of adding, committing, and pushing changes. I also gained experience in handling unexpected errors during setup and application development, which taught me to troubleshoot issues and remain patient throughout the process. Additionally, I improved my skills in GUI development using Flet and recognized the importance of persistence and careful attention to detail when working collaboratively and solving technical problems.

## Screenshots

![Git Reporsitory](lab2_screenshots/GIT.png)
### Git Repository
- [ ] GitHub repository with commit history
- [ ] Local git log showing commits


### GUI Applications
![hello_world.py Output](lab2_screenshots/Hello_flet.png)
- [ ] hello_flet.py running with all features

![personal_info_gui.py Output](lab2_screenshots/Personal_info_gui.png)
- [ ] personal_info_gui.py with filled form and generated profile

## Future Enhancements

- **Enhanced Input Validation:** Implement more robust validation for form fields, including regex checks for email and phone numbers.
- **User Authentication:** Add login and registration features to secure personal information.
- **Data Persistence:** Integrate local or cloud-based storage to save user profiles and application data.
- **Responsive Design:** Improve UI responsiveness for different screen sizes and devices.
- **Export Functionality:** Allow users to export their profile information to PDF or CSV formats.
- **Theme Customization:** Provide options for users to switch between light and dark modes.
- **Accessibility Improvements:** Ensure the applications are usable with screen readers and keyboard navigation.
- **Error Logging:** Add logging for application errors to aid in debugging and maintenance.
- **Multi-language Support:** Enable localization for different languages to reach a broader audience.
- **Integration with External APIs:** Connect the applications to external services for extended functionality, such as profile picture uploads or data validation.
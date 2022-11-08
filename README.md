# Project descripttion : 

1. This project was worked on as course requirement for ENPM662-Fall22, at UMD,College Park in collaboration with Aditi Bhoir https://github.com/Abhoir1
2. This project included solidworks modelling, and ros deployment of a basic 4 wheeled robot
3. Every package has a readme with further description and usage instructions

# Initial Setup (if using docker):

1. Install vs-code editor on your ubuntu 20.04 host OS : https://linuxize.com/post/how-to-install-visual-studio-code-on-ubuntu-20-04/
2. Install docker on your ubuntu 20.04 host OS : https://docs.docker.com/engine/install/ubuntu/
3. Please remember to follow all the steps in docker installation, and verifying it's successful installation @ https://docs.docker.com/engine/install/ubuntu/#next-steps > https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user (Step 1 2 3 4)
4. Install following extensions on your VSCode: 
    1. Docker : https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker
    2. Remote-Containers :  https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
5. Clone this repository using:
    > ``` git clone https://github.com/vedran97/project1_enpm662.git ```
6. From the current working directory, cd to project1_enpm662 repo which u just cloned
7. Open a terminal in project1_enpm662 and type 
    > ``` code . ```
8. A VSCode popup should arise which says "Open folder in Container" where you choose Yes OR press F1,search for "Open Folder in Container" and execute the command
9. Now wait for the build process to finish, once it's completed, you have a fully functional ROS1 workspace with example packages
11. When the container is built for the first time, a error will popup saying "Failed to enable ROS Extension" , just choose the reload window option
10. Set up ROS dependencies using the following section

# Setting up ROS-Dependencies :

1. Once the repo is opened in a container, you have to install ROS1-dependencies. To do this, follow these steps:
    0. Inside the container, use a bash terminal will open at the following command's path if not, run it
    1. cd /workspaces/project1_enpm662
    2. rosdep update
    3. sudo apt-get update
    4. rosdep install --from-paths src --ignore-src -r -y

# Building Packages:

1. cd /workspaces/project1_enpm662
2. catkin_make







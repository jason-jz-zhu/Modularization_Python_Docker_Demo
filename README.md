# Table of Contents
2. [Tech Stack](README.md#tech-stack)
1. [Executate Code](README.md#executate-code)
1. [Testing](README.md#testing)
1. [Questions?](README.md#questions?)



# Tech Stack

I am using following platform and data strutures:

* [Python 3.7.9] - Main programing language
* [Docker] - Container



# Executate Code

1. Move to the root of project.
2. Install Docker Image:
    ```
    docker image build -t demo:latest .
    ```
3. Run the Docker Container
    ```
    docker run -d --name demo_app demo:latest
    ```
4. Run Python Command
    ```
    demo 
    ```


# Testing



You can run the test with the following command from within the root folder:

    pytest 

# Questions?
Email me at jason.jz.zhu@gmail.com

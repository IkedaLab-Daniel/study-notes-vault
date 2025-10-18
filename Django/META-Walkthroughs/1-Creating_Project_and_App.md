# 1 - Craeting Django Project and App

## Learning Instructions
Ensure you are in the directory where you want to create your project.

This lab mainly deals with the command line inside the VS Code console present. If not open, go to Terminal on your Menu bar at the top of your screen and select 'New Terminal'. Add the commands below inside the command line.

Follow the instructions below and make sure you check the output at every step:

### Step 1
Verify that you are in /home/coder/project directory.

Terminal:

```bash
pwd
```

If you are not in the above directory, navigate to the same using:

```bash
cd .. # Navigate to the parent directory
```

## Step 2
Make sure you have Django installed. 

```bash
python3 -m django --version
```

If django is not installed, use pip to install the same

```bash
pip3 install django
```

## Step 3
Run a command to Start/setup a project such as myproject.  

```bash
django-admin startproject myproject
```

The project should ideally be set up at this point.

## Step 4
Step inside the project directory that you have created.

```bash
cd myproject
```
## Step 5
Create an app called myapp.

```bash
 python3 manage.py startapp myapp
```
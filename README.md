# Project Title

Simple Online Card Payment App

# Table of Contents

- [Project Title](#project-title)
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
  - [Pre-requisites](#pre-requisites)
  - [Getting Started](#getting-started)
    - [Frontend](#frontend)
      - [`cd frontend`](#cd-frontend)
      - [`npm install`](#npm-install)
      - [`npm start`](#npm-start)
    - [Backend](#backend)
      - [`cd backend`](#cd-backend)
      - [`pip install -r requirements.txt`](#pip-install--r-requirementstxt)
      - [`uvicorn main:app`](#uvicorn-mainapp)
- [Usage](#usage)
  - [Frontend](#frontend-1)
  - [Backend](#backend-1)

# Introduction

This project is a solution to level up take home assignment for June 2023 cohort

# Features
1. Validates that PAN (card number) is between 16 and 19 digits long
2. Validates that CVV (security code) of the credit card must be exactly 3 digits long
   - Unless it’s an American Express card, in which case the CVV must be exactly 4 digits long
   - American Express are cards whose PAN (card numbers) starts with either “34” or “37”
  
3. Validates that expiry date of the credit card (year and month) must be AFTER present time
4. Validates that PAN (card number) follows Luhn’s algorithm

# Installation
## Pre-requisites

You must have the following installed on your system before you begin

- [NodeJS](https://nodejs.org/)
- [Python](https://www.python.org/)

## Getting Started

Start by cloning the repository to do this click on the green Code button just above the file browser
![WhatsApp Image 2023-05-14 at 9 18 42 PM](https://github.com/danthecm/card-payment/assets/52335952/e155fb0e-ebd3-47b2-97fc-9e83edef10c2)



The project root directory contains frontend and backend folders
below are the configurations to setup both

### Frontend

1. Change directory into the frontend folder

#### `cd frontend`

2. run the following command to install all dependencies

#### `npm install`

3. run the app in development mode

#### `npm start`

### Backend

After following the steps listed above for running the frontend open a new terminal in the root folder and do the following to run the backend

1. change directory into the backend folder

#### `cd backend`

2. Install all the packages

#### `pip install -r requirements.txt`

3. Start the backend server

#### `uvicorn main:app`


# Usage
If you followed the instructions above meticulously you should have the frontend and backend running on the following url:

## Frontend

Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

## Backend

visit [http://localhost:8000/docs](http://localhost:8000/docs) to view the backend documentation on your browser

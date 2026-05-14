Build a static website explaining how this project was converted from a Monolithic Architecture to a Microservices Architecture which was deployed on AZURE through git actions using ubuntu runner for Frontend and storing images on kodmicroservices. the images were later converted and stored a an actifact for later use in the job build after as successfull ssh with a public ip and other secret variables stored in github secrets. Apigateway and backend are github selfhosted runners where codes were checked out and build locally and were later pushed backed to the kodmicroservices ACR. Explain the use of namecheap, cloud flare for hosting and WAF blocking incoming trafic from a COUNTRY "Nigeria". Explain the process of ssl with lets encript that was used in the Nginx application stored in the frontemd side. T alk about all the porrts that were expose on the backend and how frontend only communicat with apigateway and apigateway only communicate with the backend service only. explain the deboging process of how we had cd into each containers to check the problems and the issue why the application is not comming up and how this issue was solved. talk about how each backend conainers had to run depending on each database connected to it. backend images literally waite for posgress database to start and get connected. Use each images and videos above explain the process. talk about the game application. here is the Readme file for monolitic before it was converted: 

# ft_transcendence

Final project of the Ecole 42 Common Core curriculum. An advanced version of the classic Pong game, built using a microservices architecture with AI opponents, remote multiplayer capabilities, and robust user authentication. Frontend developed with Pure JS as a Single Page Application. Backend developed with Django Rest Framework.

<img width="714" height="407" alt="AZURE ACHI-DIG" src="https://github.com/user-attachments/assets/62d721e8-d50e-48a2-8101-e5fa6be61ad4" />


Project Subject: https://cdn.intra.42.fr/pdf/pdf/117706/en.subject.pdf

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Architecture](#architecture)

## Introduction
This project aims to create an enhanced version of the Pong game with a focus on scalability, security, and advanced gameplay features. By leveraging microservices architecture and modern web technologies, we've built a robust platform that goes beyond the traditional Pong experience.

## Features
- **Microservices Architecture**: Backend designed as microservices for improved scalability and maintainability. Each service has its own database.
- **User Management**: Standard user management system with authentication across tournaments.
- **Remote Authentication**: Implement secure remote authentication for users.
- **Two-Factor Authentication (2FA)**: Enhanced security with 2FA and JWT (JSON Web Tokens).
- **AI Opponent**: Challenge yourself against an intelligent AI player.
- **Remote Multiplayer**: Play against other players remotely.
- **Server-Side Pong**: Core game logic implemented on the server for fair play.
- **RESTful API**: Full-featured API for game interactions and data management.
- **Frontend Framework**: Modern, responsive user interface built with a frontend framework/toolkit.
- **Database Integration**: Robust data management using a backend database.

## Installation
To set up this project, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yigithankarabulut/ft_transcendence.git
   cd ft_transcendence
   ```

2. **Edit .env file**\
  Edit .env file for both frontend and backend with necessary configurations

4. **Run with Docker Compose**
   ```sh
   docker-compose up --build
   ```

## Architecture
Our microservices architecture includes the following components:

1. **API Gateway**\
  Entry point for client requests, routing to appropriate services
2. **Authentication Service**\
  Provides authentication for requests to internal services. ApiGateway sends requests to the auth service as a middleware for all requests except Excluded Routes
3. **User Management Service**\
  Manages user management and authentication
4. **Friend Service**\
  Handles users' friendships.
5. **Bucket Service**\
  Service that stores and serves files such as Media, Photo, etc.
6. **Game Playing Service**\
  Service that processes the game on the server side. It has a Websocket consumer and connects to wss.
7. **Game Service**\
  Manages game logic and state
8. **Mail Service**\
  A consumer that consumes RabbitMQ. Asnyc handles cases such as 2FA code, Email verification, Forgot Password.
9. **Status Service**\
  Handles online/offline status of users.

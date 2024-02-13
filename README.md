# Unauthorized PC Usage Alert System

This repository contains a system that alerts the user whenever another person uses the computer without authorization.

## Method Used

The system utilizes a client-server architecture to monitor computer usage and send alerts to the owner. Here's an overview of the method used:

1. **Client Application**: A lightweight client application is installed on the user's computer. This application continuously monitors user activity, such as keyboard input or mouse movement.

2. **Server Application**: A server application is set up to listen for requests from client applications. This server can be hosted on a remote server or run locally on the user's computer.

3. **Communication Protocol**: The client application periodically sends status updates to the server, indicating that the computer is in use. If the server does not receive these updates within a specified time frame, it assumes that the computer is being used by an unauthorized person.

4. **Alert Mechanism**: When the server detects unauthorized usage, it triggers an alert mechanism. This could involve sending an email or SMS notification to the owner of the computer, notifying them of the unauthorized access.

## How It Works

1. **Initialization**: The client application is installed on the user's computer, and the server application is set up either locally or on a remote server.

2. **Client-Server Communication**: The client application establishes a connection with the server and sends periodic status updates.

3. **Monitoring User Activity**: The client application continuously monitors user activity, such as keyboard input and mouse movement, to determine if the computer is in use.

4. **Alert Triggering**: If the server does not receive status updates from the client within the expected time frame, it triggers the alert mechanism.

5. **Alert Delivery**: The alert mechanism notifies the owner of the computer about the unauthorized usage, allowing them to take appropriate action.

## Getting Started

To set up the unauthorized PC usage alert system, follow these steps:

1. Clone or download this repository to your local machine.
2. Set up the server application by running the provided server code on a remote server or your local machine.
3. Install the client application on the user's computer(s) that you want to monitor.
4. Configure the client application to connect to the server and specify the desired time frame for status updates.
5. Run the client application on the user's computer(s) to start monitoring for unauthorized usage.

## Contributing

Contributions to this project are welcome! If you have any ideas for improvements or new features, feel free to fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the terms of the license.

# Low-Level Group Messaging Application

## Introduction

This project implements a low-level group messaging application using ZeroMQ. The application consists of a central message server, multiple groups, and users interacting with each other in real-time. Users can join or leave groups, send and receive messages within those groups.

## Architecture Overview

The architecture includes:

- **Message Server**: Maintains a list of groups and handles requests from group servers and users.
  
- **Groups**: Manage user memberships, store and handle messages sent by users, and interact with users.

- **Users**: Interact with the message server and groups, joining or leaving groups, and sending or receiving messages.

## Types of Nodes

### Message Server

- **Group List Maintenance**: Maintains a list of groups with their IP addresses.
  
- **User Interaction**: Handles user requests to join or leave groups and updates group membership accordingly.

### Groups

- **User Management**: Maintains a list of users in the group and handles join/leave requests.
  
- **Message Handling**: Stores and retrieves messages sent by users in the group.
  
- **Message Storage**: Persists messages in memory to ensure availability even if users join or leave.

### Users

- **Group Interaction**: Users can join or leave multiple groups simultaneously.
  
- **Message Operations**: Users can send messages within groups, fetch messages, and leave groups.

## Detailed Explanation

### Message Server ↔ Group

1) **MessageServer Registration**: A group server registers itself with the message server. The message server acknowledges the registration.

2) **User ↔ Message Server Interaction**: Users request the message server for the list of live groups. The message server responds with the list of groups and their IP addresses.

### User ↔ Group

1) **Join Group**: Users can request to join a group by sending their UUID. The group accepts the user and responds with success.

2) **Leave Group**: Users can request to leave a group, and the group removes the user from its membership.

3) **Get Messages**: Users can request all messages from a group after a specified timestamp or all messages if no timestamp is specified.

4) **Send Message**: Users can send messages to a group, and the group stores the message with a timestamp.

## Code Files

- **user.py**: Implements the User class, allowing users to interact with the message server and groups.

- **group.py**: Defines the GroupServer class, managing user requests, user memberships, and message handling.

- **message_server.py**: Implements the MessageServer class, handling group registration, managing the list of groups, and responding to user requests.

## Usage

1. Run `message_server.py`.
2. Run multiple instances of `group.py` for different groups.
3. Run `user.py` for each user, interacting with the message server and groups.

## Assumptions
1. Since the assignment does not explicitly state to include the date along with time, thereby I have just used time for filtering conversations.
2. Since the assignment does not explicitly state which timezone's time to include when filtering messages, thereby I am using UTC time.

## Dependencies

- ZeroMQ: Ensure you have ZeroMQ installed on your system.


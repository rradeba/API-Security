Reset this lesson?
BE Module 13 Lesson 3: Assignment | API Security
Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!

Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!

Enhancing Security with JWT Tokens in Factory Management System
Objective: The objective of this assignment is to implement JWT token-based authentication and authorization in the factory management system to ensure secure access to resources and endpoints.

Problem Statement: You are tasked with enhancing the security of the factory management system by implementing JWT token-based authentication and authorization. This involves generating JWT tokens for user authentication and adding role-based access control to endpoints to restrict access based on user roles.

Task 1: Define User Model

Create a User model to represent users of the factory management system.
Define the following attributes for the User model:
id: Integer, primary key for identifying users.
username: String, unique username for authentication.
password: String, hashed password for secure authentication.
role: String, representing the role of the user (e.g., 'admin' or 'user').
Implement the necessary methods and relationships in the User model for interaction with the database.
Task 2: Implement JWT Token Generation

Add the pyjwt library to the requirements.txt file to enable JWT token generation and validation.
Create a utils folder and generate the util.py file to create tokens and validate tokens as required.
Define a secret key to be used for signing the JWT tokens.
Implement a function named encode_token(user_id) in util.py to generate JWT tokens with an expiration time and user ID as the payload.
Ensure that the secret key is kept secure and not exposed publicly.
Test the token generation function to ensure that tokens are generated correctly.
Task 3: Authentication Logic

Create a login function to authenticate users using the User model.
Utilize the encode_token function from the util.py module to generate the JWT token with the user ID as the payload.
Return the JWT token along with a success message upon successful authentication.
Create the controller to handle the JWT token returned from the authentication service.
Task 4: Implement Role-based Access Control

Add @role_required decorator to all save functions in the controllers to validate admin and user roles before creating any data.
Modify the authentication logic to validate user roles before allowing access to sensitive endpoints.
Expected Outcomes:

Upon completing this assignment, students should achieve the following outcomes:

Definition of a User model to represent users of the factory management system.
Implementation of JWT token-based authentication and authorization to enhance the security of the factory management system.
Successful generation of JWT tokens with expiration time and user ID as the payload.
Integration of JWT token generation and validation into the authentication logic to provide secure access to endpoints.
Implementation of role-based access control to restrict access based on user roles (admin and user) for sensitive operations and endpoints.
A more secure factory management system with JWT token-based authentication and role-based access control, ensuring the protection of sensitive data and resources.

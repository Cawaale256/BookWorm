# BookWorm Library Management System

## Overview

BookWorm is a web application designed to manage the operations of a library. It allows users to manage books, members, borrowing and returning of books, and track due dates and fines. The system is built using Django, a high-level Python web framework.

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
## User Experience UX
### User Stories :
US01:As a user, I want to sign up, sign in, and sign out for an account so that I can access the library system

Acceptance Criteria:

- User is redirected to the login page after signing up.
- User receives a confirmation message upon successful registration.
- User is authenticated and redirected to their profile page upon successful login.
- User sees an error message if the login credentials are incorrect.
- User can click a "Sign Out" button.

US02: As a librarian, I want to add new books to the library so that members can borrow them.

Acceptance Criteria:
- Librarian can enter book details (title, author, ISBN, description, availability).
- Book is added to the library's inventory.
- Librarian receives a confirmation message upon successful addition.

US03: As librarian, I want to edit the details of existing books so that the information is accurate and up-to-date.

Acceptance Criteria:
- Librarian can update book details (title, author, ISBN, description, availability).
- Changes are saved and reflected in the library's inventory.
- Librarian receives a confirmation message upon successful update.

US04:As a librarian, I want to delete books from the library so that outdated or damaged books are removed from the system

Acceptance Criteria:
- Librarian can delete a book from the library's inventory.
- Book is removed from the system.
- Librarian receives a confirmation message upon successful deletion.

US05: As a librarian, I want to view a list of all books in the library so that I can manage the library's inventory.

Acceptance Criteria:
- Librarian can see a list of all books with details (title, author, ISBN, availability).
- Librarian can search for books by title or author.

US06: As a member, I want to search for books by title or author so that I can find the books I am interested in.

Acceptance Criteria:
Member can enter a search query (title or author).
Member sees a list of books matching the search criteria.

US07: As a member, I want to view the details of a book so that I can decide if I want to borrow it.

Acceptance Criteria:
- Member can click on a book to view its details (title, author, ISBN, description, availability).

US08: As a librarian, I want to add new members to the library so that they can borrow books.

Acceptance Criteria:
- Librarian can enter member details (name, email).
- Member is added to the library's membership list.
- Librarian receives a confirmation message upon successful addition.

US09:As a librarian, I want to edit the details of existing members so that the information is accurate and up-to-date

Acceptance Criteria:
- Librarian can update member details (name, email).
- Changes are saved and reflected in the membership list.
- Librarian receives a confirmation message upon successful update.

US10: As a librarian, I want to view a list of all members so that I can manage the library's membership

Acceptance Criteria:
- Librarian can see a list of all members with details (name, email, borrowed books).
- Librarian can search for members by name or email.

US11:As a member, I want to view my profile so that I can see my personal information and borrowed books

Acceptance Criteria:
- Member can view their profile with details (name, email, borrowed books).
- Member can see the due dates of their borrowed books.

US12:As a member, I want to borrow a book so that I can read it

cceptance Criteria:
- Member can click a "Borrow" button on a book's detail page.
- Book is marked as borrowed and assigned to the member.
- Member receives a confirmation message upon successful borrowing

US13: As a member, I want to return a borrowed book so that I can borrow more books

Acceptance Criteria:
- Member can click a "Return" button on their profile page.
- Book is marked as returned and removed from the member's borrowed list.
- Member receives a confirmation message upon successful return.

US14:As a member, I want to extend the due date of my borrowed books so that I can have more time to read them.

Acceptance Criteria:
- Member can click an "Extend Due Date" button on their profile page.
- Member can select a new due date.
- Due date is updated and reflected in the member's borrowed list.
- Member receives a confirmation message upon successful extension

US15: As a librarian, I want to track which books are borrowed and by whom so that I can manage the library's inventory.

Acceptance Criteria:
- Librarian can view a list of borrowed books with details (title, member name, due date).
- Librarian can search for borrowed books by title or member name.

US16: As a member, I want to view the due dates of my borrowed books so that I can return them on time

cceptance Criteria:
- Member can see the due dates of their borrowed books on their profile page

US17:As a member, I want to return my borrowed books by myself so that I can manage my borrowed books easily

Acceptance Criteria:
- Member can click a "Return" button on their profile page.
- Book is marked as returned and removed from the member's borrowed list.
- Member receives a confirmation message upon successful return.



## Features
![New Wireframe 1](https://github.com/user-attachments/assets/8753ee23-ec29-4cf7-b722-bf52619deaab)

Desktop Wireframes iPad View Wireframes Mobile View Wireframes Entity-Relationship diagrams and summarisation for DBMS Entity-Relationships Schematic Graphic of the Entity-Relationships Diagram

## ER Diagram Breakdown
### Entities: Entity-Relationship Diagram (ERD) Entities User:
Entities and Relationships
User

Attributes: user_id, username, email, password, is_superuser, etc.
Description: Represents a user of the library system. Users can borrow books.
Book

Attributes: book_id, title, author, isbn, copies, borrowed_copies, borrower, borrow_date, due_date
Description: Represents a book in the library. Each book has a title, author, ISBN, number of copies, and borrowing details.
Member

Attributes: member_id, first_name, last_name, email, join_date
Description: Represents a member of the library. Each member has a first name, last name, email, and join date.
Relationships
User - Book

Relationship: One-to-Many
Description: A user can borrow multiple books, but each book can be borrowed by only one user at a time.
Member - User

Relationship: One-to-One (Implicit through the User model)
Description: Each member is associated with a user account.
ERD Diagram
Below is a textual representation of the ERD for the Bookworm Library application:
![image](https://github.com/user-attachments/assets/54a8f9d4-6a52-4407-81f5-8acea52a83b4)

### Explanation
User: Represents the users of the library system. Each user has a unique user_id, username, email, password, and a boolean is_superuser to indicate if the user is an admin.

Book: Represents the books in the library. Each book has a unique book_id, title, author, isbn, copies, borrowed_copies, borrower, borrow_date, and due_date.

Member: Represents the members of the library. Each member has a unique member_id, first_name, last_name, email, and join_date.
### Relationships
User - Book: A user can borrow multiple books, but each book can be borrowed by only one user at a time.
Member - User: Each member is associated with a user account (implicitly through the User model).

## Testing
### Testing User Stories:

#### TC01: Verify user sign-up, sign-in, and sign-out functionality.
- **US01**: As a user, I want to sign up, sign in, and sign out for an account so that I can access the library system.
- Expected Outcome: The user can successfully sign up, sign in, and sign out, with appropriate messages displayed.
- Actual Outcome: The user can successfully sign up, sign in, and sign out, with appropriate messages displayed.
- - **Pass/Fail**: Pass

#### TC02: Verify that a librarian can add new books to the library.
**US02**: As a librarian, I want to add new books to the library so that members can borrow them.
- Expected Outcome: The librarian can successfully add new books to the library, and a confirmation message is displayed.
- Actual Outcome: The librarian can successfully add new books to the library, and a confirmation message is displayed.
- - **Pass/Fail**: Pass
  
#### TC03: Verify that a librarian can edit the details of existing books.
- **User Story**: US03: As a librarian, I want to edit the details of existing books so that the information is accurate and up-to-date.
- **Expected Outcome**: The librarian can successfully edit book details, and a confirmation message is displayed.
- **Actual Outcome**:  The librarian can successfully edit book details, and a confirmation message is displayed.
- - **Pass/Fail**: Pass

#### TC04: Verify that a librarian can delete books from the library.
- **User Story**: US04: As a librarian, I want to delete books from the library so that outdated or damaged books are removed from the system.
- **Expected Outcome**: The librarian can successfully delete books from the library, and a confirmation message is displayed.
- **Actual Outcome**: The librarian can successfully delete books from the library, and a confirmation message is displayed.
- **Pass/Fail**: Pass


#### TC05: Verify that a librarian can view a list of all books in the library.
- **User Story**: US05: As a librarian, I want to view a list of all books in the library so that I can manage the library's inventory.
- **Expected Outcome**: The librarian can view a list of all books and search for books by title or author.
- **Actual Outcome**: All books can be viewed on the homepage or through the book navigation bar
- **Pass/Fail**: Pass


#### TC06: Verify that a member can search for books by title or author.
- **User Story**: US06: As a member, I want to search for books by title or author so that I can find the books I am interested in.
- **Expected Outcome**: The member can search for books by title or author and see a list of matching books.
- **Actual Outcome**: All books can be viewed on the homepage or through the book navigation bar
- **Pass/Fail**: Pass

#### TC07: Verify that a member can view the details of a book.
- **User Story**: US07: As a member, I want to view the details of a book so that I can decide if I want to borrow it.
- Expected Outcome: The member can view the details of a book.
- - **Actual Outcome**: All books can be viewed on the homepage or through the book navigation bar
- **Pass/Fail**: Pass
  
#### TC08: Verify that a librarian can add new members to the library.
- **User Story**: US08: As a librarian, I want to add new members to the library so that they can borrow books.
- **Expected Outcome**: The librarian can successfully add new members to the library, and a confirmation message is displayed.
- **Actual Outcome**: New member can sign up and recieves confirmation message
- **Pass/Fail**: Pass

#### TC09: Verify that a librarian can edit the details of existing members.
- **User Story**: US09: As a librarian, I want to edit the details of existing members so that the information is accurate and up-to-date.
- **Expected Outcome**: The librarian can successfully edit member details, and a confirmation message is displayed.
- **Actual Outcome**: The librarian can't  edit member details
- **Pass/Fail**: F

#### TC10: Verify that a librarian can view a list of all members.
- **User Story**: US10: As a librarian, I want to view a list of all members so that I can manage the library's membership.
- **Actual Outcome**: There is bug to view the members
- **Pass/Fail**: Fail
- 
#### TC11: Verify that a member can view their profile.
- **User Story**: US11: As a member, I want to view my profile so that I can see my personal information and borrowed books.
- **Expected Outcome**: The member can view their profile and see the due dates of their borrowed books.
- **Actual Outcome**: The member can view their profile and see the due dates of their borrowed books.
- **Pass/Fail**: Pass

#### TC12: Verify that a member can borrow a book.
- **User Story**: US12: As a member, I want to borrow a book so that I can read it.
- **Expected Outcome**: The member can successfully borrow a book, and a confirmation message is displayed.
- **Actual Outcome**: The member can successfully borrow a book, and a confirmation message is displayed.
- **Pass/Fail**: Pass

#### TC13: Verify that a member can return a borrowed book.
- **User Story**: US13: As a member, I want to return a borrowed book so that I can borrow more books.
- **Expected Outcome**: The member can successfully return a borrowed book, and a confirmation message is displayed.
- **Actual Outcome**: The member can successfully return a borrowed book, and a confirmation message is displayed.
- **Pass/Fail**: Pass
  
#### TC14: Verify that a member can extend the due date of their borrowed books.
- **User Story**: US14: As a member, I want to extend the due date of my borrowed books so that I can have more time to read them.
- **Expected Outcome**: The member can successfully extend the due date of their borrowed books, and a confirmation message is displayed.
- **Actual Outcome**:  The member can successfully extend the due date of their borrowed books, and a confirmation message is displayed.
- **Pass/Fail**: Pass
- 
#### TC15: Verify that a librarian can track which books are borrowed and by whom.
- **User Story**: US15: As a librarian, I want to track which books are borrowed and by whom so that I can manage the library's inventory.
- **Expected Outcome**: The librarian can track borrowed books and search for them by title or member name.
- **Actual Outcome**: The librarian can view available book on his dashboard
- **Pass/Fail**: Pass

#### TC16: Verify that a member can view the due dates of their borrowed books.
- **User Story**: US16: As a member, I want to view the due dates of my borrowed books so that I can return them on time.
- **Expected Outcome**: The member can view the due dates of their borrowed books.
- **Actual Outcome**:  The member can view the due dates of their borrowed books.
- **Pass/Fail**:Pass
- 
#### TC17: Verify that a member can return their borrowed books by themselves.
- **User Story**: US17: As a member, I want to return my borrowed books by myself so that I can manage my borrowed books easily.
- **Expected Outcome**: The member can successfully return their borrowed books, and a confirmation message is displayed.
- **Actual Outcome**:  The member can successfully return their borrowed books, and a confirmation message is displayed.
- **Pass/Fail**: Pass

### Future Enhancements
By addressing these issues, the application will meet all the user stories and provide a better user experience for both librarians and members:
- **Fix TC09**: Investigate and resolve the issue preventing the librarian from editing member details.
- **Fix TC10**: Investigate and resolve the bug preventing the librarian from viewing the list of members.

## Validator Testing
- CSS Validator
  ![image](https://github.com/user-attachments/assets/ec9a4989-8df4-494b-8c25-48c1568d774b)

- Python Validator
  ![image](https://github.com/user-attachments/assets/ae58aa5d-7798-4027-9d93-2c21f0b21ac5)

  


Deployment

Final Deployment steps
The live link to the application can be found here
https://bookworm-library-162a2f259259.herokuapp.com/


## Technologies Used

- Django
- Postgres
- HTML/CSS
- Javascript  

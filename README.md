# Online Course Management System

## Overview
The Online Course Management System uses SQLite as its database to handle all course-related information. It helps manage students, instructors, courses, course materials, and enrollments. The system allows users to add, update, view, search for, and delete records, and users can also export data to CSV files.

## Features 
- **Database Management**: Automatically creates the necessary tables for students, instructors, courses, course materials, and enrollments.
- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on all entities.
- **Search Functionality**: Search records across various tables based on specified criteria.
- **Data Export**: Export all course-related data into a CSV format for easy access and sharing.
- **User-Friendly Interface**: Command-line interface for easy navigation and operation.

## Database Schema
![Schema](/images/schema.png)

## Usage

Once the system is running, you will see a main menu with the following options:

1. **Add**: Add new students, instructors, courses, course materials, or enrollments.
2. **Update**: Update existing records for students, instructors, courses, course materials, or grades.
3. **View or Search**: View enrollment history, course materials, or search records based on specified criteria.
4. **Delete**: Delete course materials or enrollment records.
5. **Export to CSV File**: Export all data from the database to a CSV file.
6. **Exit**: Terminate the application.

## Command-Line Interface

The system uses a command-line interface for interaction. Here’s how you can navigate through the options:

- **Choose an option** by entering the corresponding number (1-6) and pressing Enter.
- Follow the prompts for additional input when adding or updating records.
- Use the appropriate commands to perform the desired operations.

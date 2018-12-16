# Changelog
All notable changes in TA Scheduling App will be documented in this file.

## Sprint 3
### Added
- Added CSS styling to website
- Implemented permissions so not everyone is allowed to edit/view
- Login and Signup implementation with forms
- Permissions groups for Django (Custom Migration)
  - Groups: TA, Instructor, Administrator, Supervisor, Default
- Created Home page 
- Created html templates and class based views for each of the following features
  - Courses
    - add course
    - edit course
    - view courses
  - Sections
    - add course
    - edit course
    - view courses
  - Users 
    - add user
    - edit user
    - view user
    - assign user to section
  - Registration
    - login
    - signup


### Changed
- views.py rewritten to use class based views
- All the managers modified to return dictionaries


## Sprint 2
### Added
- Command line web ui
- Created Django models for Course, Section and User


### Changed
- Converted command parser(Sprint 1) into views.py for Django
- Storage Manager saves to Django database instead of Json
- Classes modified to use Django database
  - CourseManager
  - StorageManager
  - SectionManager
  - UserManager

### Removed
- Json storage functionality


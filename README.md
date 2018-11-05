# TA-App
Software Engineering Fall 2018 Project

### Command Line Usage

    $ <Command> <Action> <Fields/Args>
    
    Commands:
      Course  
      Section  
      User  
    
    Actions:
      add 
      delete
      edit
      view
     
    Fields:
      dept
      cnum
      section
      ins
      
### Examples

    Department(dept) and course number(cnum) are required field to add a course
      
    $ Course add dept=CS cnum=351
    $ Course add dept=CS cnum=351 section=802 ins=None
    $ Course add dept=CS cnum=351 section=802 ins=Rock
    $ Course add code=CS-351-802 inst=Rock
    

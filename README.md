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
      snum
      ins
      
### Examples

    Department(dept) and course number(cnum) are required field to add a course
      
    $ Course add dept=CS cnum=351
    $ Course add dept=CS cnum=351 snum=802
    $ Course add dept=CS cnum=351 snum=802 ins=Rock
    $ Course add code=CS-351-802 ins=Rock
    
    $ User add user=Foo 
    $ User add user=Foo password=abc123 
    $ User add user=Foo password=abc123 role=TA


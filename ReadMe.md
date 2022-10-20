# Project Description
This project will continue on from task 02
of applied python. (Bob and Alice)
It will also add some additional stuff
which means that you may need to update
some UML diagrams to fit accordingly to
the new program

# UML Diagrams
This section will contain the UML diagrams

## Class Diagram
```mermaid
classDiagram
    PenPal "1" --|> "1" Person
    Postie "1" --|> "1" Person
    LetterBox "1" --* "1" PenPal
    Letter "1" -- "1" LetterBox
    Letter "1" -- "1" Postie
    Letter "1" -- "1" Person
    Letter -- Encryptor
    Letter "1" -- "1" PostOffice
    
    
    class Person{
        +string name
        +Letter letter
        +deliver_letter()
    }
    
    class PenPal{
        +LetterBox LetterBox
        +create_letter()
        +get_letter_from_letterbox()
        +encrypt()
        +decrypt()
        +read_letter()
    }
    
    
    class Postie{
        +receive_letter()
    }
    
    class LetterBox{
        +Letter letter
        +bool flag_raised
    }
    
    class Letter{
        +PenPal sender
        +PenPal receiver
        +bool is_read
        +string message
    }
    
    class Encryptor{
        +encrypt()
        +decrypt()
    }
    
    class PostOffice{
        +Letter letter
        +notify_postie()
    }
```
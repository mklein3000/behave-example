Feature: Test Calculator Functionality

Scenario:Addition
 Given Calculator app is run
 When I input "2" to calculator
 And I input plus "3" to calculator
 Then I get result "5"

Scenario:Addition Negative
 Given Calculator app is run
 When I input "-2" to calculator
 And I input plus "3" to calculator
 Then I get result "1"

Scenario Outline: Multiplication         
 Given Calculator app is run       
 When I input "<factor a>" to calculator   
 And multiplicate with "<factor b>"      
 Then I get result "<result>"        
 
 Examples: positive integers      
 | factor a         | factor b     | result    |   
 | 1                | 1            | 1         |           
 | 2                | 3            | 5         |   
 | 3                | 2            | 6         |  
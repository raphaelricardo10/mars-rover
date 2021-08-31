#Mars Rover
This was a challenge proposed by a interviewer in a big IT consulting company.


I was asked to implement a Mars Rover deployment system. The user should input the size of a grid where the rover would move and each rover's initial position (x,y) followed by its instruction set. The instructions accepted are: 'M', 'L' and 'R'. The 'M' instructions tells the robot to move one point in front of it. The 'R' and 'L' instructions are a rotation respectively to right and left, without changing its position.


This software is composed by two libraries and one driver program. The libraries are made using using good programming practices, allowing better software maintainability, scalability and readability. With this construction, these libraries can be easily integrated with any driver program.


The Plateau class contains the attributes and methods related to the grid where the rover is moving. A object is anything that can be inserted in a plateau, so its class contains all the common attributes of each one. The rover is a inherited class from object, containing its specific attributes and methods. This modelling allows to create new objects in future and deploy them in any two-dimensional grid.
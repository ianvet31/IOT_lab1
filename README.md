# Self-driving PiCar
An intro IoT project that turns a Raspberry Pi 4B into an autonomous toy car. The main navigation loop involves three main steps: a scanning step that swivels a servo-mounted ultrasonic sensor and generates a 2D mapping of surrounding obstacles, a routing step that runs the A* pathfinding algorithm on the 2D mapping, and an execution step that translates the path to DC motor instructions. 
![image](https://github.com/ianvet31/IOT_lab1/assets/61299105/dd910fa4-7d71-421d-8107-16b19164552f)

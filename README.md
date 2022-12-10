Main.py is the main code. 

The constructor for the Cube object takes an array of strings indicating the position of each cubie. The easiest way to create a Cube is to use the solved array that is located in Main.py. After creating the cube, you can rotate the faces. Rotations' notations use the first letter of the face (performs a 90 degree turn), the first letter then 2 (performs a 180 degree turn), and the first letter and P (performs a -90 degree turn). For example, calling the cube's F() function will rotate the front face by 90 degrees. Calling the cube's print_cube() function will print the faces. To get the state of the cube, use its get_state() function, which will return the state. 

The search functions are BFS(state), LocalSideways(state), LocalParent(state), and IDAstar(state), which take the state of the cube (the array of strings) as inputs and perform the search on it.

In Main.py, you can also find the states on which we ran the searches. The results are in the Evaluation section of the report.
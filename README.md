# Joseph Gallegos Miniproject: NYC MTA Graphing


To get the files to run the program, either `git clone` the repository in the terminal or download it as a zip to your computer.

To run the simulation/prompt, do `python3 main.py` in the terminal or you might have to do `python main.py` depending on the system you're running it on.


> No additional modules need to be installed, only Python is required to run the program.

## File Rundown


__getData.py:__ This is the file ingesting the MTA data and putting it into graph form that can be used in the search algorithm.

__main.py:__ This is the main file that runs the simulation/prompt, it also has the code for the search algorithm.

__MTA_Subway_Stations.csv:__ This helps initialize the stops with their lines and what stops have transfers to other lines.

__stops.txt:__ This is the data that helps us order the stops so that the path is in the correct stop order.

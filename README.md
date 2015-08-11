1. Setup
	1) Download and Install Python 2.7.10 for Windows from link,
	  https://www.python.org/downloads/
	2) Add Python 2.7 path into Windows System Path
		- Let¡¯s assume that Python 2.7 has been installed at ¡°C:\Python27¡±
		- Control Panel -> System and Security -> System -> Advanced system settings ->
		  Advanced tab -> Environment Variables
	3) Following screen capture is showing the result after setting the Python2.7 path
	4) Install unirest python library using ¡°pip install unirest¡± in command prompt
2. How to execute tests
	1) Download Test_Utimate_Weather.zip from the location in 4.1 
	2) Unzip the file and Let¡¯s assume that ¡°Test_Utimate_Weather_Forcasts.py¡±, ¡°cities.json¡±
		are saved in ¡°D:\Workspace¡±
	3) Open the command prompt and change the directory into ¡°D:\Workspace¡± by using ¡°cd
		d:\Workspace¡±
	4) Execute ¡°python Test_Utimate_Weather_Forcasts.py¡± in command prompt
3. Outputs
	1) Debug.log file will be created and saved in same directory with source code.
	2) Python ¡°logging¡± library was used to record the output from test.
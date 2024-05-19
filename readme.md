# Face Attendence tracker

### Instruction to Run code:

##### [downlaod images and files from this link](https://usercontent.one/wp/www.computervision.zone/wp-content/uploads/2022/12/Files.zip?media=1632743877)

<h3>install all required libraries(sequences is important)

1. pip
2. cmake
3. dlib
4. face_recognition
5. cvzone
6. numpy
7. panda
8. openCV2-python

<h3> make local environment

1. python -m venv myenv
2. myenv\Scripts\activate
3. pip install `<package-name>` (install above packages)

<li>Install CMake and dlib:

Download and install CMake from here.
Make sure to add CMake to your system PATH during installation.
Install Visual Studio Build Tools:

Download and install the Visual Studio Build Tools from here.
During the installation, make sure to select the "Desktop development with C++" workload.
Download the dlib .whl File:

Go to a website like Unofficial Windows Binaries for Python Extension Packages.
Download the appropriate .whl file for your Python version and system architecture (e.g., dlib-19.22.99-cp311-cp311-win_amd64.whl for Python 3.11 on a 64-bit Windows system).
Open the Terminal in PyCharm:

Open your PyCharm IDE and load your project.
Ensure your virtual environment (.venv) is activated.
Open the terminal within PyCharm (View > Tool Windows > Terminal).
Change Directory to the Location of the .whl File:

If you saved the .whl file in your .venv/Lib/site-packages folder, navigate to that directory in the terminal:
sh
Copy code
cd path\to\your\project\.venv\Lib\site-packages
Install the .whl File Using pip:

Run the following command to install the dlib package from the .whl file:
sh
Copy code
pip install dlib-19.22.99-cp311-cp311-win_amd64.whl
Make sure to replace the filename with the actual name of the .whl file you downloaded.

<h2>Create a .env File:

Create a file named .env in the root directory of your project.
Add Environment Variables to the .env File:

Add your database URL and storage bucket information to the .env file. The file should look something like this:

```
DATABASE_URL= -----
STORAGE_BUCKET= -----

```

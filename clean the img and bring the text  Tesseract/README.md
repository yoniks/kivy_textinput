Installing Tessersct for Mac m1 OS X 


https://github.com/tesseract-ocr/
https://tesseract-ocr.github.io/tessdoc/Installation.html
https://docs.brew.sh/

Example for Hebrew Language:
   cd finder of main.py 
1) install envar python3 -m env venv
   source env/bin/activate 
   sudo "pwd"/venv/bin/python3 -m pip install --upgrade pip

   deactivate (exit activate)    


2) brew install tesseract
   brew info tesseract
   And install Dependencies 

3) install the package of tesseract:
  git clone https://github.com/tesseract-ocr/tesseract.git
  cd tesseract
  sudo ./autogen.sh
 sudo ./configure
  make
  sudo make install
     
4) change the paths in main.py and Name finder 

5) 
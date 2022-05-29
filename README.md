# ANPR

Number Plate recognition, also called License Plate realization or recognition using image processing methods is a potential research area in smart cities and the Internet of Things. An exponential increase in the number of vehicles necessitates the use of automated systems to maintain vehicle information for various purposes.
In the proposed algorithm an efficient method for recognition of Indian vehicle number plates has been devised. We are able to deal with noisy, low illuminated, cross angled, non-standard font number plates. This work employs several image processing techniques such as, morphological transformation, Gaussian smoothing, Gaussian thresholding and Sobel edge detection method in the pre-processing stage, afterwhich number plate segmentation, contours are applied by border following and contours are filtered based on character dimensions and spatial localization. Finally we apply Optical Character Recognition (OCR) to recognize the extracted characters.

Steps :
1. Import the repository from github 
2. Create a virtual environment and install the libraries opencv , numpy , imutils , easyocr , sys. 
3. Also you have to install django in the same environment , this is used to connect frontend and backend. 
4. In app folder go to final_anpr.py and type the image name from the images in media.
5.Open the command prompt and run the command "python manage.py runserver" and then go to the link
6. In the link go to "work" and press the button "execute the external python script"

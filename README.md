# License-Plate-Recognition-Based-Smart-Parking-System
* Main.py calls LicensePlateRecognition.py to extract possible number plates from the image.
* LicensePlateRecognition calls DetectPlates.py which returns dimensions and all the necessary data to detect characters in that plate and store it in class made in PossiblePlate.py.
* This data is then fed to DetectChars.py which determines all the possible characters in that plate stores it in PossibleChars.py and returns it to LicensePlateRecognition.py.

# Hyperparamters tuning:
* The hyperparameters to be tuned according to our needs are: 
1. MIN_PIXEL_WIDTH = 2
2. MIN_PIXEL_HEIGHT = 8

3. MIN_ASPECT_RATIO = 0.25
4. MAX_ASPECT_RATIO = 1.0

5. MIN_PIXEL_AREA = 80

6. MIN_DIAG_SIZE_MULTIPLE_AWAY = 0.3
7. MAX_DIAG_SIZE_MULTIPLE_AWAY = 5.0

8. MAX_CHANGE_IN_AREA = 0.5

9. MAX_CHANGE_IN_WIDTH = 0.8
10. MAX_CHANGE_IN_HEIGHT = 0.2

11. MAX_ANGLE_BETWEEN_CHARS = 12.0

12. MIN_NUMBER_OF_MATCHING_CHARS = 3

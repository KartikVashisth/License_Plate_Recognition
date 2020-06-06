import string, subprocess, time, sys, os
from subprocess import call
import LicensePlateRecognition as Lic

print("System Working")

def matchLicPlate():
    Lic.LicRecognition()
    with open('numberplate.txt','r') as file:
        numberplate = file.read()
    numberlist = ['HR268R9044', 'PB09AC3627', 'KA03MG2825', 'MH08AG7110', 'DL4CAF4943', 'TS08ER1643', 'KA02MJ4606', 'DL8CN8726', 'HR26BF0990', 'HR26BC8009', 'MH12DE1433']
    if numberplate in numberlist:
        time.sleep(1)
        print("Number Plate matched :", end = " ")
        print(numberplate)

    else:
        print('Number plate not matched!')

def capture_image():
    call(["raspistill -n -t 2000 -o /home/pi/scripts/camera/LicenseImage.jpg -w 2592 -h 1944"], shell=True)
    print("Image Shot")
    p = subprocess.Popen(["runlevel"], stdout=subprocess.PIPE)
    out, err=p.communicate()
    if out[2] == '0':
        print('Halt detected')
        exit(0)
    if out [2] == '6':
        print('Shutdown detected')
        exit(0)
    print("Detecting License Plate")
    matchLicPlate()
    print('----------------------------------------------')


matchLicPlate()


exit(0)

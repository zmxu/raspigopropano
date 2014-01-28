raspigopropano
==============

A python script to take panoramic pictures with a GoPro HERO camera, raspberry pi (wifi or not), and servo.

What it does
-------------

First, it rotates the servo 45 degrees 6 times, between rotation, in wifi option (raspi with wifi adapter) it triggers the camera to take a picture, but in no wifi option (raspi with no wifi adapter) all is syncronized perfectly so the servo rotates and the gopro takes a picture with the autoexec.ash, that takes 6 pics with 3 seconds interval and then turn off.

When the spinning finishes, only in wifi option, it download the 6 pics, and start stiching the panorama, then saves the panorama as an image.

Photosynth / Pano upload
------------------------

If you plan to upload the panorama to photosynth, check the following:
* Copy the six gopro pics from the sd to your computer.
* go to www.photosynth.net/preview  you need a photosynth account (free)
* Click upload 
* Select panorama option
* Select the six gopro pics you copied before
* Wait...

Photosynth Preview stiches the gopro pics perfectly, note that photosynth does not accept the pano stiched by the raspi. The pano stiched by the raspi is only for websites, or your custom viewer like KRPano.

Enjoy! :octocat: :octocat: :octocat:

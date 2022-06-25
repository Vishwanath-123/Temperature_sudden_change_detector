What is this device?

This is a device that detects a sudden change in temperatures using a Z-score analysis of the latest (FRAME_SIZE) number of inputs.
Description: In making this device and code I have used the Bolt wifi module and Bolt python library to collect input every 10 seconds and I have used python to make a Z-score analysis of the input temperature using the latest (FRAME_SIZE) number of inputs which are stored in a list named 'history_data'. and if the input temperature crosses the threshold set by the Z-score i.e. the immediate last input + Z-score then I have set it to send a mail to my account by using an application called 'mailgun'.

Hardware connections for the temperature detector with the bolt wifi module:
1) Get your bolt wifi module connected to the cloud properly.
2) You should secure 3 male to female wires and an LM35 sensor(this is the main part that senses the temperature).
3) connect VCC pin of the sensor to 5v pin of bolt module, Output pin of LM35 to A0 pin of Bolt module, Gnd pin of LM35 to Gnd off Bolt module using the 3    female to male wires (for flexibility).
4) Now Power up the module and the hardware connections are done.

Note: Save the files in a local server in Linux by running the command "ssh (device name)@(IP address of the device)". And create the file using "sudo nano (file name)".

Calculating Z-Score: 
When we get an input temperature from the sensor we will have the previous 10 inputs (if not then the program should return "System needs more inputs to calculate the Z-score." as the output.) now we will follow the below steps in order.
 
1) Calculate the mean of the previous 10 inputs.
2) Calculate the Variance which is the square root of the average of squares of the difference between the data and mean.
3) Now multiply the variance with a multiplication factor (which decides the length of the Z-range).
4) The final number is the Z-score of the last 10 - inputs.
5) Now we have got the Z-score value we have to add this value to the last input and it will be the threshold for the new input.


How to create an account in mailgun:
1) Go to the site www.mailgun.com and click the "start sending" button on the top right.
2) Now fill up your details (you canagree to not to give your credit card or debit card or account details).
3) Then verify the account through a link that will be sent to your mail inbox through which you have signed in.
4) Give your mobile number and after that give the Verification code you get on your mobile through SMS.
5) Now on the left of the screen, you can see a sending option with a downward arrow beside it click on it.
6) Then click on overview the below API click select and click python.
7) (Important point - not mentioned in the bolt course) to the right of the page, you can see "Authorised recipients".
8) Add your email to that recipient and click save recipients. That's it account created.


Now before running the code make necessary changes to the "email_conf.py" file by filling in the appropriate keys and I'd.
1) MAILGUN_API_KEY: The Private API key you can see on the mailgun website after selecting python.
2) SANDBOX_URL: The URL you can find on the website of the format "sandbox........mailgun.org".
3) RECIPIENT_EMAIL: the mail to which you want the alert mail to be received.
4) API_KEY: API key of your bolt account (you can see this on the [Bolt account](https://cloud.boltiot.com/api)).
5) DEVICE_ID: Id of your bolt device (format will be BOLTXXXXX). # Temperature_sudden_change_detector.

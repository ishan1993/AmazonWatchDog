# Amazon WatchDog



###Introduction
Application uses Twilio’s Python API to send an SMS notification to user when the price of the product that they configured the script to track drops to a desired amount.When the user will install the app using the install.sh file, it will run a deamon in the background which will track the prices at an hourly frequency.User will be able to create his watch_list of products that he wants to track using the add_product script. Using this script the user will add the URL, the desired lower bound on thr price of the products and his user_id, which in turn will get stored in a JSON format.
The JSON would be a 2-dimensional dictionary of the following format:
{User_Id : { URL : desired_cost}}
The background process will open a TCP socket to establish a connection with the Amazon Server. It will then iterate through the watch_list and will fetch the HTML page using the product URL. We will then parse the HTML page to retrieve the most recent price of the product and will compare it with the lower bound set by the user. If the price is less than or equal to the desired price , then the app will notify the user via an email or an SMS.   

###How to Install the app
1) Clone the repo
2) Execute install.sh script for setup 


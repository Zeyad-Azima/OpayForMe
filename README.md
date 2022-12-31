# OpayForMe
<h3> It's for educational purposes. You are not allowed to use it against anybody and i'm not responsible for your behaviour.</h3>
CVE-2021-43150 Exploit for `opay` android app webview

# install
```
pip3 install flask
```
# Run

- Modify the `IP` in the last line inside `main.py`:
```
if __name__ == '__main__':
    app.run(host="Your_IP")
```

```
python3 main.py
```

# Endpoints
- `/login`: This endpoint handles the login process. It accepts both GET and POST requests. If the request method is POST, it gets the username and password from the form, checks if the credentials are valid, and saves the user information in the session if the credentials are correct. If the request method is GET, it simply renders the login page.  
- `/signup`: This endpoint handles the signup process. It also accepts both GET and POST requests. If the request method is POST, it gets the username, password, and full name from the form, checks if the username is already taken, and saves the new user to the users.json file if the username is available. If the request method is GET, it simply renders the signup page.
- `/dashboard`: This endpoint renders the dashboard page. It checks if the user is logged in, and redirects to the login page if the user is not logged in. If the user is logged in, it gets a list of the files in the victims folder and renders the dashboard.html template, passing the user's full name and the list of files to the template.      
- `/load-file`: This endpoint handles the process of loading a file and displaying its content in the dashboard page. It accepts only POST requests, and it gets the filename from the POST request. It opens the file and reads its contents, and then renders the results.html template, passing the file content and the filename to the template.      
- `/logout`: This endpoint clears the session and redirects the user to the login page.      
- `/`: This is the index page of the application. It logs the user's IP address and request headers to a file in the victims folder, and renders the index.html template.

# Screentshots
- Index:
![image](https://user-images.githubusercontent.com/62406753/210156621-7ee547b4-66da-44b8-a7c9-58b2728296cd.png)

- Signup:
![image](https://user-images.githubusercontent.com/62406753/210156630-08b5fdcc-7fa7-46e4-92f2-7fec8f38bf21.png)

- Login:
![image](https://user-images.githubusercontent.com/62406753/210156638-df3cff3e-ece8-4725-a8e6-913624000eea.png)

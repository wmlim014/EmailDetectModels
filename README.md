# Custom Email Classification
![](./FlaskApp/PageDemo.gif)

# Load app.py
```
cd FlaskApp
```
```
myenv\Scripts\activate
```
```
python app.py
```

# [Basic Setup in Terminal](https://blog.bolajiayodeji.com/how-to-deploy-a-machine-learning-model-to-the-web)
1. Install or upgrade pip
    ```
    python.exe -m pip install --upgrade --user pip
    ```
2. Python installation
    - Verified python versions
        ```
        python --version
        ```
    - Install python
        ```
        pip install python
        ```
3. Python environment setup
    - Go to folder stored webpage
        ```
        cd FlaskApp
        ```
    - Create a python environment
        ```
        python -m venv myenv
        ```
    - Access created environment
        ```
        myenv\Scripts\activate
        ```
    - Install package needed *(add more if needed)*
        ```
        pip install flask joblib scikit-learn
        ```
    - Check package list and version
        ```
        pip list
        ```
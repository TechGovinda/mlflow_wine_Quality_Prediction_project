# this file is no use its  only for the learn about tracking_uri

import mlflow

print(
    "printing tracking URI scheme below in file format but mlflow unable to track file so we have to convert file into http or https"
)
print(mlflow.get_tracking_uri())
print("\n")

mlflow.set_tracking_uri("http://127.0.0.1:5000")
print("printing new tracking URI scheme below")
print(mlflow.get_tracking_uri())
print("\n")

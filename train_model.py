ValueError: The feature names should match those that were passed during fit. Feature names unseen at fit time: - AccountAgeGroup - ContentType - DeviceRegistered - Gender - GenrePreference - ... Feature names seen at fit time, yet now missing: - AccountAgeGroup_Mid - AccountAgeGroup_Old - ContentType_Movies - ContentType_TV Shows - DeviceRegistered_Mobile - ...
Traceback:
File "C:\Users\pavithra sekar\AppData\Local\Programs\Python\Python312\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 88, in exec_func_with_error_handling
    result = func()
             ^^^^^^
File "C:\Users\pavithra sekar\AppData\Local\Programs\Python\Python312\Lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 579, in code_to_exec
    exec(code, module.__dict__)
File "C:\Users\pavithra sekar\app.py", line 81, in <module>
    input_imputed = imputer.transform(input_data)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\pavithra sekar\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\utils\_set_output.py", line 316, in wrapped
    data_to_wrap = f(self, X, *args, **kwargs)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\pavithra sekar\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\impute\_base.py", line 570, in transform
    X = self._validate_input(X, in_fit=False)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\pavithra sekar\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\impute\_base.py", line 350, in _validate_input
    raise ve
File "C:\Users\pavithra sekar\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\impute\_base.py", line 332, in _validate_input
    X = self._validate_data(
        ^^^^^^^^^^^^^^^^^^^^
File "C:\Users\pavithra sekar\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\base.py", line 608, in _validate_data
    self._check_feature_names(X, reset=reset)
File "C:\Users\pavithra sekar\AppData\Local\Programs\Python\Python312\Lib\site-packages\sklearn\base.py", line 535, in _check_feature_names
    raise ValueError(message)
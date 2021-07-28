# OPERA Prediction API
## Author
Scott Kolmar

## Description
This API makes OPERA predictions on provided smiles strings. Predictions can be made for the following endpoints: BCF, logBCF, BP, logP, MP, VP, logVP, WS, AOH, BioDeg, RB, ReadyBiodeg, HL, logHL, KM, logKM, KOA, Koc, logKoc, and RT. Currently, the API runs
OPERAv2.7.

Documentation for the OPERA software, developed by Kamel Mansouri, can be found here:
[OPERA-documentation](https://github.com/kmansouri/OPERA)

## Deployment
The API is run via the Python package Flask from inside of a Docker container. Everything needed to build the Docker image, start the Docker container, and run the flask app is contained here.

To build the Docker image, start the docker container, and run the flask app, apply the following commands:
``` python run_docker.py```

## API Reference

The API can be accessed at the following base URL: (http://127.0.0.1:5000/)


### Endpoints

Each of the endpoints listed in the description can be accessed for predictions. For example:

#### GET '/logBCF?smiles={smiles_string}'
- Predicts logBCF for the supplied smiles string
- Returns: A JSON object with the prediction key, which has the value of the prediction, and a success key, which returns True if the calculation succeeded, and False if an error occurred
- Example: ```curl http://127.0.0.1:5000/logBCF?smiles=CCC```

```
{
    "prediction": "0.71",
    "success": true
}
```

### Error Handling
Errors are returned in the following json format:
```
{
    'success': False,
    'error': 404,
    'message': 'Resource Not Found'
}
```
The API returns 2 types of errors:
- 404: not found
- 422: unprocessable
- 500: internal server error



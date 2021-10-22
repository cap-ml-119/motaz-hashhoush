# Kaggle-Bike-Sharing-Demand
## you have tow endpint

### single_prediction
+ Endpoint : `api/v1/single/prediction`
+ Request body: {
    "hour",
    "humidity",
    "month",
    "temp",
    "weather",
    "windspeed",
    "workingday"

}
+ every data type in request should be number
+ Responses: {
  - 200 status.
  - predict value.
}
### batch_preduction
+ Endpoint : `POST /api/v1/batch/preduction`
+ Request form schema: the csv file contain sample
+ Responses: file contain predictions
  
 

def calculate(pred,real,X_test):
  from sklearn.metrics import mean_absolute_error,mean_squared_error,root_mean_squared_error,r2_score
  print(10*'*')
  print("MSE:",mean_squared_error(real,pred))
  print("MAE:",mean_absolute_error(real,pred))
  print("RMSE:",root_mean_squared_error(real,pred))
  print("R2 Score:",r2_score(real,pred))
  score=r2_score(real,pred)
  adjust=1-((1-score)*(len(real)-1) / (len(real)-X_test.shape[1]-1))
  print("Adjusted R2 Score:",adjust)
  print(10*'*')
  

class Model():
    def fit(self, data):
        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        # Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')     
class IncrementModel(Model):
    def predict(self, data):
        prediction=0
        for item in data:
            # Logica per la predizione
            prediction=item+prediction 
        prediction = prediction/len(data)
        return prediction   

print('prediction')
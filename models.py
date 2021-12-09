class Model():
    def fit(self, data):
        # Fit non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        # Predict non implementanto nella classe base
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    def predict(self, data):
        incremento=0
        item1=0
        for item in data:
            if(item != data[0]):
                incremento=(item-item1)+incremento
            item1=item
        prediction = ((incremento/(len(data)-1)) + item)
        return prediction

Modello=IncrementModel()
data=[50,52,60]
previsione=Modello.predict(data)
print("La previsione è: {}".format(previsione))


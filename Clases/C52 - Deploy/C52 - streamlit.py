import streamlit as st
from sklearn.base import BaseEstimator, TransformerMixin
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
from sklearn.preprocessing import OneHotEncoder


titanic = sns.load_dataset('titanic')

st.write(titanic)


selected_columns = []
for column in titanic.columns:
    selected_columns.append(st.checkbox(column))
selected_columns = [column for column, selected in zip(titanic.columns, selected_columns) if selected]

class Columns_selector(BaseEstimator, TransformerMixin):
    
    def __init__(self,columns):
        if len(columns) == 0:
            self.selected = False
        else:
            self.selected = True
        self.columns = columns
    
    def fit(self,X,y=None):
        return self
    
    def transform(self, X, y=None):
        if self.selected:
            return X[self.columns]      
        else:
            return X

columns_selector = Columns_selector(selected_columns)
titanic_filtrado = columns_selector.fit_transform(titanic)
st.write(titanic_filtrado)


st.write("Veamos que pasa con los Nans:")
fig = plt.figure(figsize=(10, 4))
sns.heatmap(titanic_filtrado.isna(), cbar=False)
st.pyplot(fig)

st.text(f"Las dimensiones actuales del dataset es: {titanic_filtrado.shape}")
st.write("Vamos a hacer una limpieza rapida tirando todos los registros con nans.")

titanic_filtrado = titanic_filtrado.dropna()

st.text(f"Las dimensiones despues de la limpieza del dataset es: {titanic_filtrado.shape}")
st.write(titanic_filtrado)

st.write("Selecciones la columna target")
target = st.selectbox('Target', titanic_filtrado.columns)
st.write(f"El target seleccionado es: {target}")

encoder = OneHotEncoder(handle_unknown='ignore', sparce_output=False)
encoder.fit(titanic_filtrado)
dummies = encoder.transform(titanic_filtrado)
st.write(dummies)











with open('dummies_order.pkl', 'rb') as f_dummy:
    dummies_encoder = pickle.load(f_dummy)

st.write(dummies_encoder)

# Cargamos el modelos desde nuestra carpeta local en el servidor usando Pickle
with open('./math_model.pkl', 'rb') as f_math:
    modelo_matematicas = pickle.load(f_math)

st.write(modelo_matematicas.coef_)

st.write(f'El modelo predice un valor de {modelo_matematicas.predict([[0,1,1,1,0,0,1,0,1,0,1,1,0,1,0,1,1]])[0]}')


values = []
for name in dummies_encoder:
    values.append(st.checkbox(name))

#st.write(values)

"El valor del modelo para el caso seleccionado es: "
st.write(modelo_matematicas.predict([values])[0])
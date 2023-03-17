import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pickle


st.title("Hola Mundo")
st.write("Mi primer pagina.")

titanic = sns.load_dataset('titanic')

st.write(titanic)

selected_columns = []
for column in titanic.columns:
    selected_columns.append(st.checkbox(column))
selected_columns = [column for column, selected in zip(titanic.columns, selected_columns) if selected]

titanic_filtrado = titanic[selected_columns]
st.write(titanic_filtrado)

st.write("Veamos que pasa con los Nans:")
fig = plt.figure(figsize=(10, 4))
sns.heatmap(titanic_filtrado.isna(), cbar=False)
st.pyplot(fig)


st.title("Pasamos a otro tema")





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
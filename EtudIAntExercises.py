import easygui
import google.generativeai as genai
import PIL.Image
import streamlit as st

genai.configure(api_key="AIzaSyCprFH7QKpCAGBv9meQPy2se-PFli9_QJo")
model = genai.GenerativeModel(model_name="gemini-1.5-flash-002")

st.title('EtudIAnt')

def select_image():
    file_path=easygui.fileopenbox(title="Selectionne une image",filetypes=["*.png;*.jpeg;*.jpg;*.bmp;"])
    return file_path

image_path = select_image()
image = PIL.Image.open(image_path)

def analyze_image():
    prompt = "Resoud ce devoir le plus precisement, repond en francais également"
    response = model.generate_content([prompt, image])
    result=response.text
    st.success(f"Réponse de l'IA : {result}"+"\n"+"N'hésitez pas à nous faire vos retours sur votre experience !")
    st.header("As tu des questions ?")
    question = st.text_area("Ta question")
    return question

def main():  
    if image_path:
        print(f"Image selectionnée:{image_path}")
        print("Préparation de la réponse")
        st.image(image, caption="Image téléchargée", use_column_width=True)
        st.write("Analyse de l'image en cours...")
        return analyze_image()      
    else :
        print("Aucune image selectionnée")

if __name__== "__main__":
    main()





    







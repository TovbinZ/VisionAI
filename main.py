import gradio as gr
from PIL import Image
import shutil
from vision import Single
from vision import Multiple




def Main(image,Question,QuestionType,Tokens, IsConsice):

	source = "image1.png"
	destination = "image2.png"
	shutil.copyfile(source, destination)

	source2 = image
	destination2 = "image1.png"
	shutil.copyfile(source2,destination2)


	if QuestionType == "Single":
		result = Single(Question,IsConsice,Tokens)
	else:
		result = Multiple(Question,IsConsice,Tokens)

	return result



inputs = [gr.Image(source="webcam",type='filepath'),gr.Text(),gr.Radio(['Single','Multiple'],value='Single'), gr.Slider(150,350), gr.Radio([True,False],value=False)]


App = gr.Interface(fn=Main, inputs=inputs, outputs="text")



App.launch()



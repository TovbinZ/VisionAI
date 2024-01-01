from openai import OpenAI
import base64



client = OpenAI()
OpenAI.api_key = "API KEY"



def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')



def Multiple(Question, IsConsice, Tokens):



    image_path1 = "/Users/zevtovbin/Desktop/GradioVision/image1.png"
    image_path2 = "/Users/zevtovbin/Desktop/GradioVision/image2.png"


    base64_image1= encode_image(image_path1)
    base64_image2= encode_image(image_path2)




    if IsConsice:
        consice = "Answer in a short and consice maner."
    else:
        consice = ""


    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": f"data:image/png;base64,{base64_image2}",
                    },
                    {
                        "type": "image_url",
                        "image_url": f"data:image/png;base64,{base64_image1}",
                    },
                    {
                        "type": "text",
                        "text": f"{Question} {consice}",
                    },
                ],
            }
        ],
        max_tokens=Tokens,
    )


    return (response.choices[0].message.content)


def Single(Question, IsConsice, Tokens):



    image_path1 = "/Users/zevtovbin/Desktop/GradioVision/image1.png"
    image_path2 = "/Users/zevtovbin/Desktop/GradioVision/image2.png"


    base64_image1= encode_image(image_path1)
    base64_image2= encode_image(image_path2)




    if IsConsice:
        consice = "Answer in a short and consice maner."
    else:
        consice = ""


    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": f"data:image/png;base64,{base64_image1}",
                    },
                    {
                        "type": "text",
                        "text": f"{Question} {consice}",
                    },
                ],
            }
        ],
        max_tokens=Tokens,
    )

    return (response.choices[0].message.content)












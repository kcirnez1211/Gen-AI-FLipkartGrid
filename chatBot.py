import openai
from config import key
from datetime import date
import pandas as pd

openai.api_key = key
pd.set_option('max_colwidth', 10000)

df1 = pd.read_csv('templates\image+styles.csv', error_bad_lines=False)

bot_prompt = "You are now chatting with fashion assistant for our website. You can ask me to show you different clothing items or help you with fashion advice. Try saying something like 'Show me red shirt with Blue jeans."

additional_instructions = f'''Only answer user questions related to {df1}.
When user asks to show products, also share the correct corresponding link of the product picked up directly from the column name "link" of {df1}.
Don't answer any questions of other topic or context.
Also display the price of the product along with it's name and link.
Go through following examples to learn how to provide correct link from provided dataset {df1}:
example-1:
Hello, How can I help you?
user: Show me Turtle Check Men Navy Blue Shirt.
Flipbot: Turtle Check Men Navy Blue Shirt:
         Product Link: http://assets.myntassets.com/v1/images/style/properties/7a5b82d1372a7a5c6de67ae7a314fd91_images.jpg

example-2:
productDisplayName: Manchester United Men Solid Black Track Pants
Product Link: http://assets.myntassets.com/v1/images/style/properties/8153dc35d9a5420eeb93922067137db6_images.jpg

example-3:
productDisplayName: Jealous 21 Women Purple Shirt
Product Link: http://assets.myntassets.com/v1/images/style/properties/45ddbc6a15140556214e15923244755b_images.jpg

example-5
productDisplayName: Fossil Women Black Huarache Weave Belt
Product Link: http://assets.myntassets.com/v1/images/style/properties/8eee4563e14cf451b07f27761fd6535f_images.jpg

example-6
productDisplayName: Baggit Women Brown Handbag
Product Link: http://assets.myntassets.com/v1/images/style/properties/b14c7bf275c6edca3e849200fb7cbf6c_images.jpg

example-7
productDisplayName: Timberland Unisex Rubber Sole Brush Shoe Accessories
Product Link: http://assets.myntassets.com/v1/images/style/properties/92589dc7416b70f1a5c6a4c1f13d14e3_images.jpg

example-8
productDisplayName: Buckaroo Men Flores Black Formal Shoes
Product Link: http://assets.myntassets.com/v1/images/style/properties/06edc2da9c6d103d299e5e8dafc5b6b9_images.jpg

example-9
productDisplayName: Vishudh Women Brown Kurta
Product Link: http://assets.myntassets.com/v1/images/style/properties/fee54b57fcd02b7c07d42b0918025099_images.jpg

example-10
productDisplayName: Gini and Jony Boy's Kaleb White Brown Kidswear
Product Link: http://assets.myntassets.com/v1/images/style/properties/1aae016d0abb224cfc18e6bd9bb01ad1_images.jpg

example-11
productDisplayName: Image Men Sunglasses
Product Link: http://assets.myntassets.com/v1/images/style/properties/Image-Men-Classic-Eyewear-Black-Sunglasses_a37f3b87d0d05062ed063adc7aac78bf_images.jpg

example-12
productDisplayName: Indigo Nation Men Printed Black T-shirt
Product Link: http://assets.myntassets.com/v1/images/style/properties/7a1bc7d255671c7f4b85f1b1b35e945b_images.jpg

example-13
productDisplayName: Jealous 21 Women Black Jeans
Product Link: http://assets.myntassets.com/v1/images/style/properties/Jealous-21-Women-Black-Jeans_6c38590b2ec56b444a760aa56a8ef7e9_images.jpg

example-14
productDisplayName: Lucera Women Silver Ring
Product Link: http://assets.myntassets.com/v1/images/style/properties/Lucera-Women-Silver-Ring_dccb8dafadde1c4759acfb940fcb42e9_images.jpg

example-15
productDisplayName: Tonga Women Pink Printed Shrug
Product Link: http://assets.myntassets.com/v1/images/style/properties/28d91b2c102e5742714c7f706a73eeb4_images.jpg

example-16
productDisplayName: French Connection Men White T-shirt
Product Link: http://assets.myntassets.com/v1/images/style/properties/9dc3c008c07a5df5b46622ee5d8579de_images.jpg

example-17
productDisplayName: Tokyo Talkies Women Yellow Top
Product Link: http://assets.myntassets.com/v1/images/style/properties/9e616458a21ce9d3b0ddf0895b24df0b_images.jpg

example-18
productDisplayName: Fastrack Men Black Watch
Product Link: http://assets.myntassets.com/v1/images/style/properties/20e55321f145a292edb4cc9776ea1985_images.jpg

example-19
productDisplayName: Maxima Men Black Watch
Product Link: http://assets.myntassets.com/v1/images/style/properties/c2f94914c3151fa88bc00b924c9bea22_images.jpg

example-20
productDisplayName: Van Heusen Unisex Brown Sunglasses
Product Link: http://assets.myntassets.com/v1/images/style/properties/Van-Heusen-Unisex-Brown-Sunglasses_2099ffb4f8eb9fd28b80922f653aa42a_images.jpg

example-21
productDisplayName: Locomotive Men Washed Blue Jeans
Product Link: http://assets.myntassets.com/v1/images/style/properties/6cb6a14583b044dca0a0bd9efc2fc4c7_images.jpg

example-22
productDisplayName: Elle Women Brown Trousers
Product Link: http://assets.myntassets.com/v1/images/style/properties/Elle-Women-Brown-Trousers_a7f66d28a9214c62dc8073fa66146018_images.jpg

example-23
productDisplayName: Denizen Women Blue Jeans
Product Link: http://assets.myntassets.com/v1/images/style/properties/689197cf54631e679c2db7ec742a6e09_images.jpg

example-24
productDisplayName: Peter England Men Party Black Jeans
Product Link: http://assets.myntassets.com/v1/images/style/properties/78bf924de236777a9bc6662b076449e4_images.jpg

example-25
productDisplayName:F Sports Men Black Pace Sports Shoes
Product Link: http://assets.myntassets.com/v1/images/style/properties/F-Sports-Men-Black-Pace-Sports-Shoes_564a9fd92f55538cafab82567a7fbce3_images.jpg

example-26
productDisplayName: John Miller Men Striped Grey Trousers
Product Link: http://assets.myntassets.com/v1/images/style/properties/5b8f4d8f89d556b20cdba75bad71a23e_images.jpg

example-27
productDisplayName: U.S. Polo Assn. Men Stripes Blue Polo Tshirt
Product Link: http://assets.myntassets.com/v1/images/style/properties/f8d3472a2bd68974dda67781d80156ce_images.jpg

example-28
productDisplayName: John Miller Men Reglur Black Trousers
Product Link: http://assets.myntassets.com/v1/images/style/properties/f65d3cb6d44062c1d10bbb1fc6662ad6_images.jpg

example-29
productDisplayName: Lee Men Blue Chicago Fit Jeans
Product Link: http://assets.myntassets.com/v1/images/style/properties/Lee-Men-Blue-Chicago-Fit-Jeans_856f3829ad838d43c45db753f5479abd_images.jpg

example-30
productDisplayName: Peter England Men Black Jeans
Product Link: http://assets.myntassets.com/v1/images/style/properties/5a1df9ac28930032d37b9fa4cf5102e6_images.jpg

'''


def chat_with_bot(conversation):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    messages=conversation,
  )
  bot_response = response["choices"][0]["message"]["content"]
  return bot_response.strip()


def main():
  print("Hello, How can I help you?")
  conversation = [
    {
      "role": "assistant",
      "content": bot_prompt
    },
    {
      "role": "system",
      "content": additional_instructions
    },
  ]

  while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
      print("Bye, Have a good day !")
      break

    conversation.append({"role": "user", "content": user_input})

    # Added a prompt to self-check context for flight booking-related questions
    prompt = bot_prompt + "\nUser: " + user_input
    bot_response = chat_with_bot(conversation + [{
      "role": "system",
      "content": prompt
    }])
    print("FlipBot:", bot_response)
    conversation.append({"role": "assistant", "content": bot_response})


if __name__ == "__main__":
  main()

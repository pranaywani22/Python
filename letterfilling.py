'''
Author:- Pranay Ajitkuamr Wani
'''
letter='''
        Dear <|Name|>,
        We are very happy to say that You are selected!. you can join from next month.
 Date=<|Date|>.
        
        Signature,
        HR.
'''
a=input("Enter your name")
b=input("Enter todays date in dd/mm/yyyy format")
letter=letter.replace("<|Name|>",a)
letter=letter.replace("<|Date|>",b)
print(letter)
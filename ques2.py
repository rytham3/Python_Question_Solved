name = "Rytham"
date = "13th July 2025"


letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 

new_letter = letter.replace("<|Name|>",name).replace("<|Date|>",date)
print(new_letter)
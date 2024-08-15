import pytermgui as ptg
letters=['!','\"','#','$','%','&','\'','(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~']
def to_94(num):
  array =[]
  result = ""
  if num == 0:
    result = '!'
  while num !=0:
    array.insert(0,num%94)
    num= num // 94
  for i in array:
    result+=letters[i]
  return result

def to_10_from_94(stringnum):
  result = 0
  array=list(stringnum)
  array.reverse()
  for i in range(len(array)):
    array[i]=letters.index(array[i])
  for i in range(len(array)):
    result+=array[i]*pow(94,i)
  return result






def to_94_from_string():
  def submit(window):
        for widget in window:
          if isinstance(widget, ptg.InputField):
            inputy = widget.value
            widget.update_selection(0,correct_zero_length=True)
            break
        stringy = []
        endresult = ""
        for char in inputy:
            stringy.append(ord(char))
        endresult = ""
        for i in stringy:
            endresult+=str(to_94(i))+" "
    
        for widget in window:
          if isinstance(widget, ptg.Label):
            widget.value = "Output: " + str(endresult)
            break
  with ptg.WindowManager() as manager:
    layout = ptg.Layout()
    layout.add_slot("body")
    manager.layout=layout
    window = (
      ptg.Window(
        "",
        ptg.InputField("",prompt='Enter a string to convert: '),
        "",
        ["Submit", lambda *_: submit(window)],
        "",
        ptg.Label("")
      )
    .set_title("Base 94r Convertor")
    .center()
    )
    manager.add(window)
    
def to_string_from_94(inputy):
  x = inputy
  print("implement later")  
def to_94_from_number(inputy):
    try:
      val = int(eval(inputy))
      return to_94(val)
    except:
      print("not an int or expression that results in an int.")
def to_number_from_94(inputy):
  try:
    val= inputy
    print(int(to_10_from_94(val)))
  except:
    print("Given string is not an integer in base 10.")




    



CONFIG = """
config:
    InputField:
        styles:
            prompt: dim italic
            cursor: '@72'
            cursor_move: true
    Label:
        styles:
            value: dim bold

    Window:
        styles:
            border: '60'
            corner: '60'

    Container:
        styles:
            border: '96'
            corner: '96'
"""

with ptg.YamlLoader() as loader:
    loader.load(CONFIG)


with ptg.WindowManager() as manager:
  layout = ptg.Layout()
  layout.add_slot("body")
  manager.layout=layout
  window = (
    ptg.Window(
      "",
      ptg.Button(label='To Base 94r from String',onclick = lambda *_: to_94_from_string()),
      "",
      ptg.Button(label='To String from Base 94r',onclick = lambda *_: to_string_from_94()),
      "",
      ptg.Button(label='To Base 94r from Number',onclick = lambda *_: to_94_from_number()),
      "",
      ptg.Button(label='To Number from Base 94r',onclick = lambda *_: to_number_from_94()),

    )
    .set_title("Base 94r Convertor")
    .center()
  )
  manager.add(window)



# option = input("[0] To 94 from string \n[1] To String from 94\n[2] To 94 from number\n[3] To Number from 94\nInput \'0\',\'1\',\'2\', or \'3\'.\n")

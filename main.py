import pytermgui as ptg
import datetime
import os
import sys
def main():
  letters=['!','\"','#','$','%','&','\'','(',')','*','+',',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~']
  def to_94(num):
      array =[]
      result = ""
      if num == 0:
          result = '!'
      while num != 0:
        array.insert(0,num%94)
        num= num // 94
      for i in array:
          result+=letters[i]
      return result

  def to_10_from_94_num(stringnum):
    result = 0
    array=list(stringnum)
    array.reverse()
    for i in range(len(array)):
      array[i]=letters.index(array[i])
    for i in range(len(array)):
      result+=array[i]*pow(94,i)
    return result


  def to_10_from_94_string(stringnum):
    array = stringnum.split(" ")
    result = ""
    for i in array:
      result+=chr(to_10_from_94_num(i))
    return result
  def writefile(window):
    f = open("output.txt","a") 
    for widget in window:
        if isinstance(widget, ptg.InputField):
            input = widget.value
            break
    for widget in window:
        if isinstance(widget, ptg.Label):
            output = widget.value
            f.write(str(datetime.datetime.now()) + "  Input: " + input + " " + str(output) + "\n")
            widget.value = f"Written to file: {os.path.abspath("output.txt")}"
            break
    f.close()





  def to_94_from_string():
    def submit(window):
      for widget in window:
        if isinstance(widget, ptg.InputField):
          inputy = widget.value
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
          ["Write Output to File (output.txt)", lambda *_: writefile(window)],
          "",
          ["Back", lambda *_: main()],
          ptg.Label("")
        )
        .set_title("Base 94r Convertor")
        .center()
      )
      manager.add(window)

  def to_string_from_94():
    def submit(window):
      for widget in window:
          if isinstance(widget,ptg.InputField):
              val = widget.value
              break
      for widget in window:
          if isinstance(widget,ptg.Label):
            widget.value = f"Output: {to_10_from_94_string(val)}"
            break
    with ptg.WindowManager() as manager:
      layout = ptg.Layout()
      layout.add_slot("Body")
      manager.layout = layout
      window = (
        ptg.Window(
              "",
              ptg.InputField("",prompt='Enter a base94r string to convert: '),
              "",
              ["Submit", lambda *_: submit(window)],
              "",
              ["Write Output to File (output.txt)", lambda *_: writefile(window)],
              "",
              ["Back", lambda *_: main()],
              ptg.Label("") 
          )
          .set_title("Base94r Convertor")
          .center()
      ) 
      manager.add(window)

  def to_94_from_number():
      def submit(window):
        for widget in window:
            if isinstance(widget,ptg.InputField):
              
              try:
                  val = int(eval(widget.value))
                  break
              except:
                  widget.value = "NOT AN INT!"
                  break
        for widget in window:
          if isinstance(widget,ptg.Label):
              widget.value = f"Output: {to_94(val)}"
              break


      with ptg.WindowManager() as manager:
        layout = ptg.Layout()
        layout.add_slot("body")
        manager.layout = layout
        window = (
          ptg.Window(
              "",
              ptg.InputField("",prompt='Enter a number to convert: '),
              "",
              ["Submit", lambda *_: submit(window)],
              "",
              ["Write Output to File (output.txt)", lambda *_: writefile(window)],
              "",
              ["Back", lambda *_: main()],
              ptg.Label("")
          )
          .set_title("Base94r Convertor")
          .center()
        )
        manager.add(window)
  def to_number_from_94():
    def submit(window):
      for widget in window:
          if isinstance(widget,ptg.InputField):
                val = widget.value
                break
      for widget in window:
          if isinstance(widget,ptg.Label):
            widget.value = f"Output: {to_10_from_94_num(val)}"
            break
    with ptg.WindowManager() as manager:
      layout = ptg.Layout()
      layout.add_slot("Body")
      manager.layout = layout
      window = (
          ptg.Window(
              "",
              ptg.InputField("",prompt='Enter a base94r number to convert: '),
              "",
              ["Submit", lambda *_: submit(window)],
              "",
              ["Write Output to File (output.txt)", lambda *_: writefile(window)],
              "",
              ["Back", lambda *_: main()],
              ptg.Label("") 
          )
          .set_title("Base94r Convertor")
          .center()
      )
      manager.add(window)




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
        ptg.Button(label='Convert String to Base 94r',onclick = lambda *_: to_94_from_string()),
        "",
        ptg.Button(label='Convert Base 94r to String',onclick = lambda *_: to_string_from_94()),
        "",
        ptg.Button(label='Convert Number to Base 94r',onclick = lambda *_: to_94_from_number()),
        "",
        ptg.Button(label='Convert Base 94r to Number',onclick = lambda *_: to_number_from_94()),

      )
      .set_title("Base 94r Convertor")
      .center()
    )
    manager.add(window)

main()

# option = input("[0] To 94 from string \n[1] To String from 94\n[2] To 94 from number\n[3] To Number from 94\nInput \'0\',\'1\',\'2\', or \'3\'.\n")

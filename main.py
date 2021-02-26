# -*- coding:utf -8 -*-

import socket

def fanc1():
  color_a = "[+] "
  print("~"*50)
  host = input(color_a + "Host --> ")
  port = int(input(color_a + "Port --> "))
  print("~"*50)

  scan = socket.socket()

  color_b = "[×] "
  color_c = "[✓] "

  try:
      scan.connect((host, port))
  except :
      print(color_b + "Port -- ", port, " -- [CLOSED]")
      start()
  else:
      print(color_c + "Port -- ", port, " -- [OPEN]")
      print("FINISHED")
      print("="*55)
      start()


def fanc2():
    color_a = "[+] "
    color_b = "[×] "
    color_c = "[✓] "
    host = input(color_a + "Host --> ")
    print("pleas wait it can takes sevral seconds")
    port = [20, 21, 22, 23, \
    42, 43, 53, 67, 69, 80, \
    8080, 9090, 8000]
    for i in port:
      try:
        scan = socket.socket()
        scan.settimeout(0.2)
        scan.connect((host, i))
      except :
        pass
        #print(color_b + "Port -- ", i, " -- [CLOSED]\n")
      else:
        print(color_c + "Port -- ", i, " -- [OPEN]\n")
    print("finished...")
    print("="*55)
    start()

def start():
  print("~"*55)
  print("|"," "*51,"|")
  print("|\t /\\/ __ /\\/\\AP BY KEYJ ")
  print("|\t[1] --- сканировать отделный порт")
  print("|\t[2] --- сканировать список возможных портов")
  print("|"," "*51,"|")
  print("~"*55)
  print("\n")
  text_a = input("[type of scan]--> ")

  if text_a == "1":
      fanc1()
  elif text_a == "2":
      fanc2()
  else:
      print("Параметр введен не правильно!")
      start()

start()

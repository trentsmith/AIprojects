# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:36:02 2021

@author: Trent Smith
"""

import sqlite3

def create_table():
  c.execute('CREATE TABLE IF NOT EXISTS Talk(Keywords TEXT, Response TEXT, User TEXT)')

def listToString(s):  
    # initialize an empty string 
    str1 = " " 
    # return string   
    return (str1.join(s)) 

def insert_value_into_table(user,keywords,response):
  c.execute('INSERT INTO Talk(Keywords,Response,User)VALUES(?,?,?)',(keywords,response,user))
  str1= " "
  keywords = str1.join(keywords)
  print(keywords)
  conn.commit()

def select_from_table(user,keywords):
        sql_select_query = """select * from Talk where user = ? and keywords = ?"""
        c.execute(sql_select_query, (user,keywords))
        records = c.fetchall()
        print("Printing ID ", user)
        for row in records:
            print("keywords = " , sorted(row[0]))
            print("response = ", sorted(row[1]))
            response=row[1]
            # print("user = ", row[2])
        #c.close()
        #c.execute('Select * from Talk where user = '+user)
#create_table()
#insert_value_into_table("admin","show test response","This is a test response")
#print(select_from_table("admin"))
class node:
  def __init__(self,value=None):
    self.value = value
    self.word = []
    self.wordnode =[]
    
class binary_search_tree:
  def __init__(self):
    self.root=None

  def insert(self,value):
    if self.root==None:
      self.root=node(value)
    else:
      self._insert(value,self.root)  

  def _insert(self,value,cur_node,words):
    flag = False
    keywords = []
    while len(words)!=0:
        print(words)
        for i in words:
            if i in cur_node.word:
                cur_node= self.wordnode[cur_node.word.index(i)]
                words.remove(i)
                keywords.append(i)
                if len(words)==0:
                       break
            elif flag:
                cur_node.word.append(i)
                cur_node.wordnode.append(node(value))
                words.remove(i)
                keywords.append(i)
                keywordsstr = str(keywords)
                keywordsstr = listToString(keywords)
                print("the keywordsstr is "+ keywordsstr)
                if len(words)==0:
                  #insert_value_into_table()             
                  break
            if i == words[len(words)-1]:
                flag = True
                break

         
  def find(self,value):
    if self.root!=None:
        return self._find(value,self.root)

  def _find(self,words,cur_node):
    flag = False
    final = ""
    while len(words) != 0:
        for i in words:
            if i in cur_node.word:
                words.remove(i)
                cur_node= cur_node.wordnode[cur_node.word.index(i)]
                flag=False
                final = cur_node.value
        if flag:
            break
        flag=True
    return final

print("hello how are you")
#response = raw_input()
#print(response)
a = binary_search_tree()
a.insert("Hello")
a._insert("How are you??!!",a.root,["Hello"])
#a._insert("I am sorry to hear that",a.root,["bad","Hello"])
a._find(["good","Hello"],a.root)
print(a.root.wordnode[0].value)
#a._insert(7,a.root)
#print(a.root.right_child.value)

# List of string 
print(a.root.value)

while True:
  print("input please")
  x =input()
  x=x.split(" ")
  answer = a._find(x,a.root)
  print("answer is "+answer)
  if answer == None or answer =="":
    print("unfamiliar what to say what should I say?")
    y = input()
    a._insert(y,a.root,x)
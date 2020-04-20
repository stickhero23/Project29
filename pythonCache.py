# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:35:56 2020

@author: Anonymous
"""

class ContentItem:
    def __init__(self,content_id:int, size:int, header:str, content:str):
        self.content_id = content_id
        self.size = size
        self.header = header
        self.content = content
    

#end class
        
class Cache:
    def __init__(self):
        self.level = None
        
    
    def hashFunc(contentHeader:str):
        #sum ascii values of each header size
        #returns between 0 and 2 inclusive
        
        
        pass
    
    def insert(content:ContentItem, evictionPolicy:str):
        #adds a contentItem to the proper linkedlist
        #returns string inserted+contentItem representation
        pass
    
    
    def retrieveContent(contnent: ContentItem):
        #gets the content Item fro mthe hash table
        #returns contentItem if content is in the hashtable, str otherwise
        pass
    
    def updateContent(content: ContentItem):
        #updates the content item in the hashtable
        #returns updated+contentitem representation if content is in the hashtable
        pass
    



class CacheList:
    def __init__(self):
        self.next :CacheList = None
        self.maxsize :int = 200
        
    def put(self,content, evictionPolicy):
        # adds nodes at the begining of the list. If necessary , uses mru/lru
        #..to remove items before adding
        newlist = CacheList()
        newlist.put(content, evictionPolicy)
        newlist.next = self.next
        self.next = newlist
    
    def update(self,cid:int, content: ContentItem):
        #updates the content in the list, if content is found and updated, node
        #is moved at the begining of the list
        #returns contentItem if it is cid in the list
        
        item : Cachelist() = self.next
        while item.next is not None:
            if item.id == cid:
                #update
                item = content
            else:
                item = item.next
        
    
    def mruEvict():
        #removed the first item of the list
        #return snone
        pass
    
    def lruEvict():
        #removes the last item from the list
        #return none
        pass
    
    def clear():
        #removes all items from the list
        #returns none
        pass
    
    
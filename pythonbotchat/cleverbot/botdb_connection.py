'''
Created on Jan 29, 2015

@author: grajpurohit
'''

import sqlite3

class botdbConnection(object):
    '''
    Get connection to botchatdb
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    
    def getbotdbConnection(self):
        '''
        getting conncetion to botchatdb
        '''
        botdbconnect = sqlite3.connect('botchatdb.db')
        conobject = botdbconnect.cursor()
        return conobject
    
    def dbTablecreation(self,dbconnectionobject):
        
        dbconnectionobject.executescript("""
        CREATE TABLE botquestion(  
             botquesid INTEGER PRIMARY KEY ASC,  
             botques  TEXT,
             botquesweight INTEGER  
             );
        INSERT INTO botquestion VALUES(1,'how are you?',0);
        INSERT INTO botquestion VALUES(2,'are you good thinker?',0);
        INSERT INTO botquestion VALUES(3,'i like know more about you',0);
        INSERT INTO botquestion VALUES(4,'hi',0);
        CREATE TABLE botresponse(  
             botresid INTEGER PRIMARY KEY,  
             botres  TEXT,
             botquesweight INTEGER,
             forbotquesid INTEGER,
             FOREIGN KEY(forbotquesid) DEFAULT 0 REFERENCES botquestion(botquesid) ON DELETE SET DEFAULT  
             );
        INSERT INTO botresponse VALUES(1,'hi',1,4);
        """)
        
    
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
             botresid INTEGER PRIMARY KEY ASC,  
             botres  TEXT,
             botresweight INTEGER,  
             );
        INSERT INTO botresponse VALUES(1,'hi',1);
        INSERT INTO botresponse VALUES(1,'yes',2);
        CREATE TABLE botquesres(
            quesresid INTGER PRIMARY KEY ASC,
            forbotresid INTEGER,
            FOREIGN KEY(forbotresid) REFERENCES botresponse(botresid) ON DELETE CASCAD,
            forbotquesid INTEGER,
            FOREIGN KEY(forbotquesid) REFERENCES botquestion(botquesid) ON DELETE CASCAD
        );
        INSERT INTO botquesres VALUES(1,1,4);
        INSERT INTO botquesres VALUES(2,2,2);
        INSERT INTO botquesres VALUES(3,2,3);
        """)
        #TODO more   
    
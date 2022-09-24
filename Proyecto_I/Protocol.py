from re import search
from Cache import Cache
from CacheBlock import *
from Memory import Memory
from Controller import *
#https://www.youtube.com/watch?v=ndyKrPMUqwE&ab_channel=ERAIngenier%C3%ADa
class Bus:
    def __init__(self,controller_list, memory):
        self.CONTROLLER_LIST=controller_list
        self.CACHE_LIST=self.__get_cache_list(self.CONTROLLER_LIST)
        self.MEMORY=memory
        self.WRITE_MISS=[0,0,0,0]
        self.READ_MISS=[0,0,0,0]

    def __get_cache_list(self,controller_list):
        cash_list=[]
        for cont in controller_list:
            cash_list+=[cont.CACHE]
        return cash_list
    
    def __copies(self,address):
        n_copies=0
        for cache in self.CACHE_LIST:
            if(cache.exists(address)):
                n_copies+=1
        #print("COPIES: "+str(n_copies))
        return n_copies

    # Search cache by ID
    def search_cache(self,ID):
        pos=0
        for cache in self.CACHE_LIST:
            if(cache.ID==ID):
                return pos
            pos+=1
        return -1
    
    def __search_modified(self, address):
        cache_pos=0
        for cache in self.CACHE_LIST:
            set_block=cache.get_block_id(address)
            if(set_block!=-1 and cache.BLOCKS[set_block].STATE=='M'):
                return cache_pos,set_block
            pos+=1
        return -1, -1
    
    def __search_exclusive(self, address):
        cache_pos=0
        for cache in self.CACHE_LIST:
            set_block=cache.get_block_id(address)
            if(set_block!=-1 and cache.BLOCKS[set_block].STATE=='E'):
                return cache_pos,set_block
            cache_pos+=1
        return -1, -1

    def __search_state(self, address,state):
        cache_pos=0
        for cache in self.CACHE_LIST:
            set_block=cache.get_block_id(address)
            if(set_block!=-1 and cache.BLOCKS[set_block].STATE==state):
                return cache_pos,set_block
            cache_pos+=1
        return -1, -1

    def __search_shared(self, address):
        cache_pos=0
        for cache in self.CACHE_LIST:
            set_block=cache.get_block_id(address)
            if(set_block!=-1 and cache.BLOCKS[set_block].STATE=='S'):
                return cache_pos,set_block
            cache_pos+=1
        return -1, -1

    def __update2share(self,address,data):
        for cache in self.CACHE_LIST:
            set_block=cache.get_block_id(address)
            
            if(set_block!=-1):
                cache.BLOCKS[set_block].STATE='S'
                cache.BLOCKS[set_block].DATA=data
      
    
    def __write_mem(self, address, data):
        return self.MEMORY.write(address, data)

    def read(self, ID, address):
        #STATE: EXCLUSIVE

        #No existe en Caché
        ind = self.search_cache(ID)
        exists=self.CACHE_LIST[ind].exists(address) 
        set_block=self.CACHE_LIST[ind].get_block_id(address)
        state=self.CACHE_LIST[ind].BLOCKS[set_block].STATE
        #Existe en la actual Caché y es Exclusived
        #Existe en la actual Caché y es Modified
        #Existe en la actual Caché y es Shared
        condition= (state=='E') and (state=='M') and (state=='S')
        #No existe en memoria
        if(0==self.__copies(address)):
            self.__set_is_modified(ID,address)
            self.__read_exclusive(ID, address)
            self.READ_MISS[ind]+=1
            print("READ MISS")
        
        #Existe en la actual Caché y es E || M || S
        elif(exists and condition):
            print("NO hacer nada")
        
        #Existe en la actual Caché y es I
        elif(exists and not(condition)):
            print("READ MISS")
            self.READ_MISS[ind]+=1
            cache_pos,set_block=self.__search_state(address,'M')
            data=self.CACHE_LIST[cache_pos].BLOCKS[set_block].DATA
            print("WB")
            self.__write_mem(address,data)
            self.__update2share(address,data)
      
        #No existe en la actual pero existen copias en otras caché
        elif(not(exists) and 0<self.__copies(address)):
            print("READ MISS")
            self.READ_MISS[ind]+=1
            mod_pos,set_mod=self.__search_state(address,'M')
            exc_pos, set_exc=self.__search_state(address,'E')
            sha_pos, set_sha=self.__search_state(address,'S')
            self.__set_is_modified(ID,address)
            if(mod_pos!=-1):
                data=self.CACHE_LIST[mod_pos].BLOCKS[set_mod].DATA
                print("WB")
                self.__write_mem(address,data)
                self.__update2share(address,data)
                #Load to ca$h
                self.CONTROLLER_LIST[ind].load(address,data,'S')
            elif(exc_pos!=-1):
               
                data=self.CACHE_LIST[exc_pos].BLOCKS[set_exc].DATA
                self.__update2share(address,data)
                #Load to ca$h
                self.CONTROLLER_LIST[ind].load(address,data,'S')
            elif(sha_pos!=-1):
                data=self.CACHE_LIST[sha_pos].BLOCKS[set_sha].DATA
                #Load to ca$h
                self.CONTROLLER_LIST[ind].load(address,data,'S')

    def __set_is_modified(self,ID,new_address):
        ind = self.search_cache(ID)
        set_block=self.CONTROLLER_LIST[ind].get_set_address(new_address)
        state=self.CACHE_LIST[ind].BLOCKS[set_block].STATE
        
        #Si esta ocupada y es Modified
        if((-1!=set_block) and ('M'==state)):
            data=self.CACHE_LIST[ind].BLOCKS[set_block].DATA
            old_address=self.CACHE_LIST[ind].BLOCKS[set_block].TAG
            self.__write_mem(old_address,data)
            self.__update2share(old_address,data)

            


    def __read_exclusive(self, ID, address):
        # STATE: Exclusive
        # Read from memory
        ind = self.search_cache(ID)
        mem_pos=self.MEMORY.getMemory(address)
        if(-1!=mem_pos):
            #set=self.CONTROLLER_LIST[ind].get_set(mem_pos)
            #self.CACHE_LIST[ind].BLOCKS[set].STATE='E'
            mem=self.MEMORY.read(address)
            #self.CACHE_LIST[ind].BLOCKS[set].TAG=address
            #self.CACHE_LIST[ind].BLOCKS[set].DATA=mem.DATA
            self.CONTROLLER_LIST[ind].load(address,mem.DATA,'E')

    
    
    
    def __search_data_other_cache(self,ID, address):
        pos=0
        positions_list=[]
        for cache in self.CACHE_LIST:
            if(cache.ID!=ID):
                if(cache.exists(address)):
                    positions_list+=[pos]
            pos+=1
        return positions_list

    def __read_shared(self, ID, address):
        # STATE: Shared
        positions_list = self.__search_data_other_cache(ID,address)
        ind = self.search_cache(ID)
        for pos in positions_list:
            set=self.CACHE_LIST[pos].get_block_id(address)
            self.CACHE_LIST[pos].BLOCKS[set].STATE='S'
            self.CACHE_LIST[pos].BLOCKS[set].TAG=address
            data=self.CACHE_LIST[pos].BLOCKS[set].DATA
        set=self.CACHE_LIST[ind].get_block_id(address)
        self.CACHE_LIST[ind].BLOCKS[set].STATE='S'
        self.CACHE_LIST[ind].BLOCKS[set].DATA=data
        self.CACHE_LIST[ind].BLOCKS[set].TAG=address

    def write(self, ID, address,data):
        #STATE: EXCLUSIVE
        #No existe en Caché
        ind = self.search_cache(ID)
        exists=self.CACHE_LIST[ind].exists(address) 
        set_block=self.CACHE_LIST[ind].get_block_id(address)
        state=self.CACHE_LIST[ind].BLOCKS[set_block].STATE
        #Existe en la actual Caché y es Exclusived
        #Existe en la actual Caché y es Modified
        #Existe en la actual Caché y es Shared
        condition= (state=='E') and (state=='M') and (state=='S')
        #No existe en memoria
        if(0==self.__copies(address)):
            self.__set_is_modified(ID,address)
            self.__read_exclusive(ID, address)
            print("WRITE MISS")
            self.WRITE_MISS[ind]+=1
            self.__write_modified(ID, address,data) #Update modified
        
        #Existe en la actual Caché y es M
        elif(exists and (state=='M')):
            print("write Modified")
            self.__write_modified(ID, address,data)

        #Existe en la actual Caché y es S 
        elif(exists and (state=='S')):
            print("write Modified")
            self.__write_modified(ID, address,data)

        #Existe en la actual Caché y es I 
        elif(exists and (state=='I')):
            print("Write MISS")
            self.WRITE_MISS[ind]+=1
            cache_pos,set_block=self.__search_state(address,'M')
            data_temp=self.CACHE_LIST[cache_pos].BLOCKS[set_block].DATA
            print("WB")
            self.__write_mem(address,data_temp) #Escribir en memoria
            self.__write_modified(ID,address,data)
  
        #No existe en la actual pero existen copias en otras caché
        elif(not(exists) and 0<self.__copies(address)):
            print("Write MISS")
            self.WRITE_MISS[ind]+=1
            mod_pos,set_mod=self.__search_state(address,'M')
            exc_pos, set_exc=self.__search_state(address,'E')
            sha_pos, set_sha=self.__search_state(address,'S')
            self.__set_is_modified(ID,address)
            if(mod_pos!=-1):
                data_temp=self.CACHE_LIST[mod_pos].BLOCKS[set_mod].DATA
                print("WB")
                self.__write_mem(address,data_temp)
                self.__update2share(address,data_temp)
                #Modified data
                self.__write_modified(ID,address,data)

            elif(exc_pos!=-1):
                #Modified data
                self.__write_modified(ID,address,data)

            elif(sha_pos!=-1):
                #Modified data
                self.__write_modified(ID,address,data)


    def __write_modified(self, ID, address,data):
        # STATE: Modified
        #Search in all caches where store mem address input
        positions_list = self.__search_data_other_cache(ID,address)
        ind = self.search_cache(ID)
        for pos in positions_list:
            set=self.CONTROLLER_LIST[pos].get_set_address(address)
            self.CACHE_LIST[pos].BLOCKS[set].STATE='I'

        set=self.CONTROLLER_LIST[ind].get_set_address(address)
        self.CACHE_LIST[ind].BLOCKS[set].STATE='M'
        self.CACHE_LIST[ind].BLOCKS[set].DATA=data
        self.CACHE_LIST[ind].BLOCKS[set].TAG=address
        
 

"""


ID1="CPU@01"
ID2="CPU@02"
ID3="CPU@03"
ID4="CPU@04"
mem= Memory(0)
controller_list=[Controller(ID1,mem,Cache(ID1)),Controller(ID2,mem,Cache(ID2)),Controller(ID3,mem,Cache(ID3)),Controller(ID4,mem,Cache(ID4))]
print("***************#1**********************************")
mem.write('0000',0x999)
mem.write('0010',0x560)
mem.write('0100',0x382)
mem.write('1000',0x258)
#mem.iprint()
#cache_list=[Cache(ID1),Cache(ID2),Cache(ID3),Cache(ID4)]
bus= Bus(controller_list,mem)
#bus.read(ID1,'0000')
bus.write(ID1,'0000',0x111)
bus.CACHE_LIST[0].iprint()
bus.CACHE_LIST[1].iprint()


print("***************#2**********************************")
#bus.read(ID2,'0100')
bus.write(ID2,'1000',0x777)

bus.CACHE_LIST[0].iprint()
bus.CACHE_LIST[1].iprint()

bus.write(ID1,'1000',0x222)
print("***************#3**********************************")
bus.CACHE_LIST[0].iprint()
bus.CACHE_LIST[1].iprint()
bus.CACHE_LIST[2].iprint()




"""
from re import search
from Cache import Cache
from CacheBlock import *
from Memory import Memory
#https://www.youtube.com/watch?v=ndyKrPMUqwE&ab_channel=ERAIngenier%C3%ADa
class Bus:
    def __init__(self,controller_list, memory):
        self.CONTROLLER_LIST=controller_list
        self.CACHE_LIST=self.__get_cache_list(self.CONTROLLER_LIST)
        self.MEMORY=memory

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
        print("COPIES: "+str(n_copies))
        return n_copies

    # Search cache by ID
    def __search_cache(self,ID):
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
            pos+=1
        return -1, -1

    def __search_state(self, address,state):
        cache_pos=0
        for cache in self.CACHE_LIST:
            set_block=cache.get_block_id(address)
            if(set_block!=-1 and cache.BLOCKS[set_block].STATE==state):
                return cache_pos,set_block
            pos+=1
        return -1, -1

    def __search_shared(self, address):
        cache_pos=0
        for cache in self.CACHE_LIST:
            set_block=cache.get_block_id(address)
            if(set_block!=-1 and cache.BLOCKS[set_block].STATE=='S'):
                return cache_pos,set_block
            pos+=1
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
        ind = self.__search_cache(ID)
        exists=self.CACHE_LIST[ind].exists(address) 
        state=self.CACHE_LIST[ind].STATE
        #Existe en la actual Caché y es Exclusived
        #Existe en la actual Caché y es Modified
        #Existe en la actual Caché y es Shared
        condition= (state=='E') and (state=='M') and (state=='S')
        #No existe en memoria
        if(0==self.__copies(address)):
            self.__read_exclusive(ID, address)
            print("READ MISS")
        
        #Existe en la actual Caché y es E || M || S
        elif(exists and condition):
            print("NO hacer nada")
        
        #Existe en la actual Caché y es I
        elif(exists and not(condition)):
            print("READ MISS")
            cache_pos,set_block=self.__search_state(address,'M')
            data=self.CACHE_LIST[cache_pos].BLOCKS[set_block].DATA
            print("WB")
            self.__write_mem(address,data)
            self.__update2share(address,data)
      
        #No existe en la actual pero existen copias en otras caché
        elif(not(exists) and 0<self.__copies(address)):
            print("READ MISS")
            mod_pos,set_mod=self.__search_state(address,'M')
            exc_pos, set_exc=self.__search_state(address,'E')
            sha_pos, set_sha=self.__search_state(address,'S')
            if(mod_pos!=-1):
                data=self.CACHE_LIST[mod_pos].BLOCKS[set_mod].DATA
                print("WB")
                self.__write_mem(address,data)
                self.__update2share(address,data)
                #Load to ca$h
                self.CONTROLLER_LIST[mod_pos].load(address,data,'S')
            elif(exc_pos!=-1):
                data=self.CACHE_LIST[exc_pos].BLOCKS[set_exc].DATA
                self.__update2share(address,data)
                #Load to ca$h
                self.CONTROLLER_LIST[exc_pos].load(address,data,'S')
            elif(sha_pos!=-1):
                data=self.CACHE_LIST[sha_pos].BLOCKS[set_sha].DATA
                #Load to ca$h
                self.CONTROLLER_LIST[exc_pos].load(address,data,'S')


    def __read_exclusive(self, ID, address):
        # STATE: Exclusive
        # Read from memory
        ind = self.__search_cache(ID)
        mem_pos=self.MEMORY.getMemory(address)
        if(False!=mem_pos):
            set=self.CONTROLLER_LIST[ind].get_set(mem_pos)
            self.CACHE_LIST[ind].BLOCKS[set].STATE='E'
            mem=self.MEMORY.read(address)
            self.CACHE_LIST[ind].BLOCKS[set].TAG=address
            self.CACHE_LIST[ind].BLOCKS[set].DATA=mem.DATA
    
    
    
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
        ind = self.__search_cache(ID)
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
        ind = self.__search_cache(ID)
        exists=self.CACHE_LIST[ind].exists(address) 
        state=self.CACHE_LIST[ind].STATE
        #Existe en la actual Caché y es Exclusived
        #Existe en la actual Caché y es Modified
        #Existe en la actual Caché y es Shared
        condition= (state=='E') and (state=='M') and (state=='S')
        #No existe en memoria
        if(0==self.__copies(address)):
            self.__read_exclusive(ID, address)
            print("READ MISS")
            self.__write_modified() #Update modified
        
        #Existe en la actual Caché y es M
        elif(exists and (state=='M')):
            print("write Modified")
            #writemodified
        
        #Existe en la actual Caché y es I
        elif(exists and not(condition)):
            print("READ MISS")
            cache_pos,set_block=self.__search_state(address,'M')
            data=self.CACHE_LIST[cache_pos].BLOCKS[set_block].DATA
            print("WB")
            self.__write_mem(address,data)
            self.__update2share(address,data)
      
        #No existe en la actual pero existen copias en otras caché
        elif(not(exists) and 0<self.__copies(address)):
            print("READ MISS")
            mod_pos,set_mod=self.__search_state(address,'M')
            exc_pos, set_exc=self.__search_state(address,'E')
            sha_pos, set_sha=self.__search_state(address,'S')
            if(mod_pos!=-1):
                data=self.CACHE_LIST[mod_pos].BLOCKS[set_mod].DATA
                print("WB")
                self.__write_mem(address,data)
                self.__update2share(address,data)
                #Load to ca$h
                self.CONTROLLER_LIST[mod_pos].load(address,data,'S')
            elif(exc_pos!=-1):
                data=self.CACHE_LIST[exc_pos].BLOCKS[set_exc].DATA
                self.__update2share(address,data)
                #Load to ca$h
                self.CONTROLLER_LIST[exc_pos].load(address,data,'S')
            elif(sha_pos!=-1):
                data=self.CACHE_LIST[sha_pos].BLOCKS[set_sha].DATA
                #Load to ca$h
                self.CONTROLLER_LIST[exc_pos].load(address,data,'S')

    def write(self, ID, address,data):
        self.__write_modified(ID, address,data)

    def __write_modified(self, ID, address,data):
        # STATE: Modified
        #Search in all caches where store mem address input
        positions_list = self.__search_data_other_cache(ID,address)
        ind = self.__search_cache(ID)
        for pos in positions_list:
            set=self.CACHE_LIST[pos].get_block_id(address)
            self.CACHE_LIST[pos].BLOCKS[set].STATE='I'

        set=self.CACHE_LIST[ind].get_block_id(address)
        self.CACHE_LIST[ind].BLOCKS[set].STATE='M'
        self.CACHE_LIST[ind].BLOCKS[set].DATA=data
        self.CACHE_LIST[ind].BLOCKS[set].TAG=address
        
        
        





mem= Memory(0)
mem.write('0100',0x58)
mem.write('0000',0x58)
#mem.iprint()
cache_list=[Cache("CPU@01"),Cache("CPU@02"),Cache("CPU@03"),Cache("CPU@04")]
bus= Bus(cache_list,mem)
bus.read("CPU@01",'0100')

bus.CACHE_LIST[0].iprint()
bus.CACHE_LIST[1].iprint()
print("***************#2**********************************")
bus.read("CPU@02",'0100')
bus.CACHE_LIST[0].iprint()
bus.CACHE_LIST[1].iprint()
bus.read("CPU@03",'0100')
print("***************#3**********************************")
bus.CACHE_LIST[0].iprint()
bus.CACHE_LIST[1].iprint()
bus.CACHE_LIST[2].iprint()
bus.write("CPU@03",'0100',0x200)
print("***************#4**********************************")
bus.CACHE_LIST[0].iprint()
bus.CACHE_LIST[1].iprint()
bus.CACHE_LIST[2].iprint()
#bus.copies('0000')

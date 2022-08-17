from enum import Enum
import string

class Operator():

    class __OperatorState(Enum):
        AVAIBLE = 'avaible'
        RINGING = 'ringing'
        BUSY = 'busy'
         
    __id: string
    __state: __OperatorState
    __call_id: string

    def __init__(self, id: string):
        self.__id = id
        self.__set_state(self.__OperatorState.AVAIBLE)

    def __set_state(self, state: __OperatorState) -> None:
        self.__state = state

    def receive_call(self, call_id: string) -> bool:
        if self.__state != self.__OperatorState.AVAIBLE:
            return False
        
        self.__set_state(self.__OperatorState.RINGING)
        self.__call_id = call_id
        return True

    def reject_call(self) -> bool:
        if self.__state != self.__OperatorState.RINGING:
            return False
        
        self.__set_state(self.__OperatorState.AVAIBLE) 
        self.__call_id = ""

        return True

    def answer_call(self) -> bool:
        if self.__state != self.__OperatorState.RINGING:
            return False
        
        self.__set_state(self.__OperatorState.BUSY)
        
        return True

    def finishe_call(self) -> bool:
        if self.__state == self.__OperatorState.AVAIBLE:
            return False

        self.__set_state(self.__OperatorState.AVAIBLE) 
        self.__call_id = ""

        return True

    def get_call_id(self) -> string:
        return self.__call_id

    def get_operator_id(self) -> string:
        return self.__id

    def get_operator_state(self) -> string:
        return self.__state.value
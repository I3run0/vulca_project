from lib2to3.pgen2.token import OP
from queue import Queue
from re import T
import string
from collections import deque
from typing import Deque 
from operator_call_center import Operator


class Manager():

    __received_calls: Queue = Queue()
    __operators_avaible: deque

    __delivered_calls: dict = {}
    __operators_unavailable: dict = {}

    def __init__(self) -> None:
        self.__operators_avaible = deque([Operator('A'), Operator('B')])

    def receive_call(self, call_id) -> None:    
        self.__received_calls.put(call_id)
        
        print(f'Call {call_id} received')


    def make_the_operator_answer(self, operator_id: string) -> None:    
        operator: Operator = self.__operators_unavailable[operator_id]

        operator.answer_call()

        print(f'Call {operator.get_call_id()} answered by operator {operator.get_operator_id()}')


    def finish_the_call(self, call_id: string) -> None:
        if call_id in self.__delivered_calls:   

            operator: Operator = self.__delivered_calls[call_id]

            if operator.get_operator_state() == 'busy':
                print(f'Call {call_id} finished and operator {operator.get_operator_id()} available')
            else:
                print(f'Call {call_id} missed')

            operator.finishe_call()

            del self.__operators_unavailable[operator.get_operator_id()]
            del self.__delivered_calls[call_id]
            self.__operators_avaible.appendleft(operator)

        else:
            print(f'Call {self.__delete_the_call_from_queue(call_id)} missed')

        self.__deliveri_waiting_calls()

    def reject_the_call(self, operator_id: string) -> None:
        operator: Operator = self.__operators_unavailable[operator_id]
        
        call_id: string = operator.get_call_id()
        operator_id: string = operator.get_operator_id()
        
        operator.reject_call()

        self.__received_calls.put(call_id)

        del self.__operators_unavailable[operator_id]

        self.__operators_avaible.appendleft(operator)

        print(f'Call {call_id} rejected by {operator_id}')

        self.__deliveri_waiting_calls()

    
    def __deliveri_waiting_calls(self) -> None:
        if not self.__received_calls.empty():
            self.__deliveri_calls()


    def __deliveri_calls(self) -> bool:
        if len(self.__operators_avaible) == 0 or self.__received_calls.empty():
            print(f'Call {call_id} waiting in queue')
            return False

        call_id: string = self.__received_calls.get() 
        operator: Operator = self.__operators_avaible.popleft()
        
        self.__delivered_calls[call_id] = operator
        self.__operators_unavailable[operator.get_operator_id()] = operator

        operator.receive_call(call_id)
        
        print(f'Call {call_id} ringing for operator {operator.get_operator_id()}')
        return True

    def __delete_the_call_from_queue(self, call_id: string) -> string:
        queue_withouto_call_delete: Queue = Queue()
        possible_call_to_delete = self.__received_calls.get()

        while possible_call_to_delete != call_id and not self.__received_calls.empty():
            queue_withouto_call_delete.put(possible_call_to_delete)
            possible_call_to_delete = self.__received_calls.get()
        
        while not self.__received_calls.empty():
            queue_withouto_call_delete.put(self.__received_calls.get())
        
        self.__received_calls = queue_withouto_call_delete

        return possible_call_to_delete
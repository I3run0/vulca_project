import cmd
from queue import Queue
from manager_call_center import Manager

class CMDSimulation(cmd.Cmd):
    
    manager_call_center: Manager = Manager()

    intro = '***************** WELCOME TO CALL CENTER *****************\n' +\
            '**********************************************************\n' +\
            'THIS IS A CALL CENTER SIMULATION. THANK YOU, FOR BE IN HERE\n' +\
            '**********************************************************\n'
    
    prompt = 'call_center: '

    def do_call(self, args) -> None:
        self.manager_call_center.receive_call(args)

    def do_answer(self, args) -> None:
        self.manager_call_center.make_the_operator_answer(args)
    
    def do_reject(self, args) -> None:
        self.manager_call_center.reject_the_call(args)

    def do_hangup(self, args) -> None:
        self.manager_call_center.finish_the_call(args)
    
    def do_exit() -> bool:
        return True 

if __name__ == '__main__':
    CMDSimulation().cmdloop()
 

# -*- coding: utf-8 -*-
#Import libraries
import random
from pyknow import AND,AS,DefFacts,EXISTS,Fact,KnowledgeEngine,MATCH,OR,Rule,TEST,watch
from methods import dialogMakeSale, dialogNoMakeSale, checkInt, dialogClientReq, dialog_consult_use, dialog_evaluate_budget, dialog_show_options, dialog_check_availability

#global variables
req = []
req_max = []
phone_recomendation_expert = []
budget = 0

#inputs 
class Client(Fact):
    pass

class Requeriments(Fact):
    pass

class Phones(Fact):
    pass

class Expert(Fact):
    pass

class SalePhone(Fact):
    pass

class Consult(Fact):
    pass

class expertMotor(KnowledgeEngine):  

    #------ First Rules ------
    #-------------------------
    #rule for decided client      
    @Rule(Client(typeClient=1))
    def determined_client(self):
        self.declare(SalePhone(make_sale=True))
    
    #rule for client that exposes requirements
    @Rule(Client(typeClient=2))
    def exposes_requirements(self):
        self.declare(Expert(consult_features=True))
         
    #rule for cliente undecided
    @Rule(OR( 
            Client(typeClient=3), 
            Client(clear_needs=False)))
    def consult_use(self):
        self.declare(Expert(define_features=False))

    #------ Rules for requirements and uses ------
    #------------------------------------
    #rule for cliente that consult features
    @Rule(Expert(consult_features=True))
    def consult_features(self):
        global req
        req = dialogClientReq()
        self.declare(Requeriments(memory=req[0],cam=req[1],storage=req[2],
                software=req[3],battery=req[4],color=req[5],screen=req[6],undecided=req[7]))

    #rule for client with clear needs    
    @Rule(Requeriments(undecided = MATCH.a), TEST(lambda a: a < 4))
    def clear_needs(self):
        self.declare(Client(clear_needs=True))
    
    #rule for client with NO clear needs
    @Rule(Requeriments(undecided = MATCH.a), TEST(lambda a: a >= 4))
    def no_clear_needs(self):
        self.declare(Client(clear_needs=False))

    #rule for check availability if clear needs or define features
    @Rule(AND(
                Client(clear_needs=True),
                Expert(consult_features=True))
            )
    def check_availability(self):
        global req
        global phone_recomendation_expert
        phone_recomendation_expert = dialog_check_availability(req)

        if len(phone_recomendation_expert) != 0:
            self.declare(Expert(show_options=True))
        else:
            self.declare(SalePhone(make_sale=False))

    #rule for show options
    @Rule(Expert(show_options=True))
    def show_options(self):
        dialog_show_options(phone_recomendation_expert)
        self.declare(Expert(evaluate_budget=True))

    #rule for evaluate budget
    @Rule(Expert(evaluate_budget=True))
    def evaluate_budget(self):
        global budget

        budget = dialog_evaluate_budget(phone_recomendation_expert)

        if budget == 1:
            self.declare(Consult(budget_OK=False))
        else:
            self.declare(Consult(budget_OK=True))
   
    #rule for budget OK
    @Rule(AND(
            Expert(evaluate_budget=True),
            Consult(budget_OK=True)))
    def budget_OK(self):
        self.declare(SalePhone(make_sale=True))
    
    #rule for budget no OK
    @Rule(AND( 
            Expert(evaluate_budget=True),
            Consult(budget_OK=False)))
    def budget_no_OK(self):
        print("Desea replantear su consulta?: ")
        print("1 - SI")
        print("2 - NO")

        budget_election = 0
        while budget_election < 1 or budget_election > 2:
            budget_election = checkInt("Elegir opcion: ")

        if budget_election == 1:
            self.declare(Consult(rethink_budget=True))
        else:
            self.declare(Consult(rethink_budget=False))

    #rule for define features
    @Rule(Expert(define_features=False))
    def define_features(self):
        #falta criterios para definir las caracteisticas
        global req_max
        global req_min
        use_requeriments = dialog_consult_use()
        req_min = use_requeriments[0]
        req_max = use_requeriments[1]
        self.declare(Expert(define_features=True))
    
    #rule for check availability if clear needs or define features
    @Rule(Expert(define_features=True))
    def check_availability_to_use(self):
        global req
        global phone_recomendation_expert
        phone_recomendation_expert = dialog_check_availability(req_min)
        phone_max = dialog_check_availability(req_max)

        for item in phone_max:
            bandera = True
            for items in phone_recomendation_expert:
                if item['ID'] == items['ID']:
                    bandera = False
            if bandera:
                phone_recomendation_expert.insert(len(phone_recomendation_expert),item)

        if len(phone_recomendation_expert) != 0:
            self.declare(Expert(show_options=True))
        else:
            self.declare(SalePhone(make_sale=False))

    #------ Rules for make sale or no make sale ------
    #-------------------------------------------------
    #rule for a sale made
    @Rule(SalePhone(make_sale=True))
    def make_sale(self):
        dialogMakeSale()
        
    #rule for a no sale made
    @Rule(OR(
            SalePhone(make_sale=False),
            Consult(rethink_budget=False)))
    def no_make_sale(self):
        dialogNoMakeSale()

    @Rule(Consult(rethink_budget=True))
    def rethink_budget(self):
        motor.reset()
        motor.declare(Client(typeClient=2))
        motor.run()
        motor.facts
        
motor = expertMotor()
#definition of type of client
def clientType(opt):
    #watch('RULES', 'FACTS')
    motor.reset()
    motor.declare(Client(typeClient=opt))
    motor.run()
    motor.facts

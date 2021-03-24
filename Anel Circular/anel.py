import threading
import time 

atualTh = 0
nThreads = 30

class multThread (threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def testUpper(self):
        global texto
        #verifica caracter minusculo na frase capturada
        for i in texto:
            if i.islower():
                return False
        return True

    def run(self):
        self.upper(self.name)

    def upper(self, threadName):
        global atualTh
        global texto
        global nThreads

        while True:

            if self.testUpper():
                break
            
            if atualTh == self.id:
                ## Se é a vez dessa thread fazer a tarefa, ela executará
                for i in range(len(texto)):

                    if texto[i].islower(): 
                      ## se o caracter for minusculo - modifica para maiusculo
                      texto = texto[:i] + texto[i].upper() + texto[i+1:]
                      time.sleep(1)
                      print(f"Thread {str(self.id)}:")
                      print(f"{texto}\n")
                      atualTh = (atualTh+1) % nThreads
                      break

if __name__ == "__main__":
    
    threads = []
    texto = input(':\n')

    for i in range(30):
      threads.append(multThread(i, "Thread-"+str(i)))
      threads[i].start()
    
    while True:
        if not threads[0].is_alive():
            time.sleep(1)
            break

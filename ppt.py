import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

led_vermelho = 8   
led_amarelo = 10   
led_verde = 12     

botao_pedra = 22   
botao_papel = 24   
botao_tesoura = 26 

GPIO.setup(led_vermelho, GPIO.OUT)
GPIO.setup(led_amarelo, GPIO.OUT)
GPIO.setup(led_verde, GPIO.OUT)

GPIO.setup(botao_pedra, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botao_papel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botao_tesoura, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        jogador_escolha = ''

        maquina_escolha = random.choice(["pedra", "papel", "tesoura"])
        print("A maquina escolheu: {}".format(maquina_escolha))
        print("Escolha: Pedra, Papel ou Tesoura")

        while jogador_escolha == '':
            if GPIO.input(botao_pedra) == GPIO.HIGH:
                jogador_escolha = "pedra"
            elif GPIO.input(botao_papel) == GPIO.HIGH:
                jogador_escolha = "papel"
            elif GPIO.input(botao_tesoura) == GPIO.HIGH:
                jogador_escolha = "tesoura"
            time.sleep(0.1)

        print("Você escolheu: {}".format(jogador_escolha))

        if jogador_escolha == maquina_escolha:
            GPIO.output(led_amarelo, GPIO.HIGH)
            time.sleep(4)
            GPIO.output(led_amarelo, GPIO.LOW)
            print("Empate!")
        elif jogador_escolha == "pedra":
            if maquina_escolha == "tesoura":
                GPIO.output(led_verde, GPIO.HIGH)
                time.sleep(4)
                GPIO.output(led_verde, GPIO.LOW)
                print("Você venceu!")
            else:
                GPIO.output(led_vermelho, GPIO.HIGH)            
                time.sleep(4)
                GPIO.output(led_vermelho, GPIO.LOW)
                print("Você perdeu!")
        elif jogador_escolha == "papel":
            if maquina_escolha == "pedra":
                GPIO.output(led_verde, GPIO.HIGH)
                time.sleep(4)
                GPIO.output(led_verde, GPIO.LOW)
                print("Você venceu!")
            else:
                GPIO.output(led_vermelho, GPIO.HIGH)
                time.sleep(4)
                GPIO.output(led_vermelho, GPIO.LOW)
                print("Você perdeu!")
        elif jogador_escolha == "tesoura":
            if maquina_escolha == "papel":
                GPIO.output(led_verde, GPIO.HIGH)
                time.sleep(4)
                GPIO.output(led_verde, GPIO.LOW)
                print("Você venceu!")
            else:
                GPIO.output(led_vermelho, GPIO.HIGH)
                time.sleep(4)
                GPIO.output(led_vermelho, GPIO.LOW)
                print("Você perdeu!")

        time.sleep(1)  

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
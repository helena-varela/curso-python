import pyautogui
import time

# Espera 5 segundos antes de começar (tempo para você focar na janela do navegador)
time.sleep(5)

n = 0
# Loop que recarrega a página a cada 5 segundos
while True:
    pyautogui.press('f5')  # Pressiona F5 para recarregar a página
    n += 1
    print(f"Página recarregada!, {n}")
    time.sleep(10)
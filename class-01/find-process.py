import psutil

# Listar os primeiros 10 processos ativos
for proc in psutil.process_iter(['pid', 'name', 'status']):
    try:
        print(f"PID: {proc.info['pid']}, Nome: {proc.info['name']}, Status: {proc.info['status']}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

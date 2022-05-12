import subprocess
import sys
import datetime

dt = datetime.datetime.now()
dt_string = dt.strftime("%d-%m-%Y-%H:%M")
files = (sys.stdout, open(f"{dt_string}", "w"))

ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).communicate()[0]
#ps = "USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND\nroot 1 0.0 0.3 5748 3512 pts/0 Ss 07:29 0:00 sh space\nagr 51 0.0 0.2 5748 3592 pts/1 Ss+ 07:34 0:00 bash\nroot 65 0.0 0.1 9388 2896 pts/0 R+ 09:18 0:00 ps aux"
processes = ps.decode().split("\n")
nfields = len(processes[0].split()) - 1
processes_running = []
CPU, MEM, NAME_CPU_MAX, NAME_MEM_MAX, users, list_process = 0, 0, None, None, [], []
CPU_MAX = 0.0
MEM_MAX = 0.0
for row in processes[1:]:
    process = row.split(None, nfields)
    list_process.append(process)
    try:
        if process[0] not in users:
            users.append(process[0])
    except IndexError:
        break
    processes_running.append(process[1])
    CPU = CPU + float(process[2])
    MEM = MEM + float(process[3])
    if float(process[2]) >= float(CPU_MAX):
        CPU_MAX = process[2]
        NAME_CPU_MAX = process[0]
    if float(process[3]) >= float(MEM_MAX):
        MEM_MAX = process[3]
        NAME_MEM_MAX = process[0]
    name_process_max_mem = "pass"

for f in files:
    print("Отчёт о состоянии системы:", file=f)
    print(f"Пользователи системы: '{', '.join(users)}'", file=f)
    print(f"Процессов запущено: {len(processes_running)}", file=f)
    print("Пользовательских процессов:", file=f)
    for i in range(len(users)):
        total_len_user_process = 0
        for j in range(len(list_process)):
            try:
                total_len_user_process = total_len_user_process + 1 if users[i] == list_process[j][0] else total_len_user_process + 0
            except IndexError:
                break
        print(users[i], ":", total_len_user_process, file=f)
    print(f"Всего памяти используется: {round(MEM, 1)}%", file=f)
    print(f"Всего CPU используется: {round(CPU, 1)}%", file=f)
    print(f"Больше всего памяти использует: {str(NAME_CPU_MAX)[:20]}", file=f)
    print(f"Больше всего CPU использует: {str(NAME_MEM_MAX)[:20]}", file=f)

sys.stdout.close()

class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task_exist = False
        for task in self.tasks:
            if task['description'] == description: task_exist = True
        if task_exist:
            print(f'Задача "{description}" уже есть в списке, срок выполнения: {task['deadline']}')
        else:
            self.tasks.append({'description':description, 'deadline':deadline, 'status':'in_progress'})
            print(f'Задача "{description}" добавлена в список. Срок выполнения - {deadline}')

    def task_done(self, description):
        task_exist = False
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = 'done'
                task_exist = True
        if task_exist: print(f'Задача "{description}" выполнена!')
        else: print(f'Задача "{description}" не найдена')

    def show_tasks(self):
        print('Текущие задачи:')
        for task in self.tasks:
            if task['status'] == 'in_progress': print(f'{task['description']}: срок выполнения - {task['deadline']}')

task = Task()
task.add_task('Попрыгать на одной ноге', '25.06.24')
task.add_task('Попрыгать на одной ноге', '26.06.24')
task.task_done('Попрыгать на другой ноге')
task.add_task('Попрыгать на другой ноге', '26.06.24')
task.add_task('Отдохнуть', '27.06.24')
task.task_done('Попрыгать на одной ноге')
task.task_done('Попрыгать на другой ноге')
task.show_tasks()
import inspect

class Object():
	def __init__(self, name):
		self.name = name


class Folder(Object):
	def __init__(self, name, parent):
		Object.__init__(self, name)
		self.__listdir = ['.', '..']
		self.__listfile = []
		self.__parent = parent

	def ls(self):
		print (' '.join(self.__listdir) + ' ' + ' '.join(self.__listfile))

	def mkdir(self, *args):
		if len(args) == 0:
			print('Не указано имя папки!')
			return True
		dir_name = args[0]
		if (dir_name in self.__listdir):
			print ('Папка с таким именем уже существует!')
		else:
			self.__listdir.append(dir_name)
			list_folder.append(Folder(dir_name, self.name))

	def touch(self, *args):
		if len(args) == 0:
			print('Не указано имя файла!')
			return True
		file_name = args[0]
		if (file_name in self.__listfile):
			print('Файл с таким именем уже существует!')
		else:
			self.__listdir.append(file_name)
			list_file.append(File(file_name, self.name))



class File(Object):
	def __init__(self, name, parent):
		Object.__init__(self, name)
		self.owner = ""
		self.content = ""
		self.__parent = parent


def help_com(*arg):
	print ("Команды, поддерживаемые на текущий момент:")
	for i in command_list:
		print ("   {}".format(i))
	return True

def ls(*args):
	current_folder.ls()
	return True

def mkdir(*args):
	current_folder.mkdir(*args[0])
	return True

def touch(*args):
	current_folder.touch(*args[0])
	return True

current_folder = root = Folder('','//')
command_list = {'help': help_com, 'exit': 'exit', 'ls': ls, 'mkdir': mkdir, 'touch': touch}
list_folder = []
list_file = []

def main():
	list_folder = [root]
	print("Добро пожаловать в testOS! Введите желаемую команду, или 'help' для получения перечня всех команд.")
	while (True):
		command_arr = input("~~ ").split()
		user_command = command_arr[0]
		if user_command == "exit":
			print("До свидания!")
			break
		else:
			if not user_command in command_list:
				print("Данная команда в настоящий момент не поддерживается. Для вывода всех команд напишите help.")
			else:
				exec_command = command_list[user_command]
				result = exec_command(command_arr[1:])
				if not result:
					print("Произошла проблема при выполнении команды.")



if __name__ == "__main__":
	main()

#try:
#    module = __import__(command)
#    result = getattr(module, command)(command_arr[1:])
#except ModuleNotFoundError:
#    print("Данная команда в настоящий момент не поддерживается.")
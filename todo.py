class Todo:
    todoList = []
    user = [{"name": "Admin", "email": "admin@admin.com", "password": "1234567890A"}]
    login_sets = {"admin@admin.com": 0}
    todo_sets = {0, 0}
    _todo_count = 0
    _login_count = 0

    def __init__(self, todo):
        self.todoList.append(todo)
        print("\n\n")
        print(
            " ---------------------------------------------------------------------------------------------------------------------"
        )
        print("| ############\t\t\t\t\tWELCOME AT TODOS\t\t\t\t\t############  |")
        print(
            " ---------------------------------------------------------------------------------------------------------------------"
        )
        self.crud_todo()

    def user_response(self, response):
        return input(response)

    def login(self):
        email = self.user_response("Enter you Email: -> [ ")
        auth_idx = self.login_sets[email]

        if (self.user[auth_idx]["email"]) and (self.user[auth_idx]["password"]):
            return True
        else:
            print("")
            return False

    def create_account(self):
        _full_name = self.user_response("Enter you Fullname: -> [ ")
        _email = self.user_response("Enter your Email: -> [ ")
        _password = self.user_response("Enter strong Password: -> [ ")
        self._login_count += 1
        self.login_sets[_email] = self._login_count
        self.user.append({"name": _full_name, "email": _email, "password": _password})

    def crud_todo(self):
        user_auth = self.user_response(
            "Are you a new User? (Type *N* for 'No' & *Y* for 'Yes' -> [ "
        ).upper()

        if user_auth == "Y":
            self.create_account()
        else:
            is_user = self.login()
            if not is_user:
                log_try = input(
                    "Invalid Credentials! Want to try again! *Y* for 'Yes' *N* for 'No' -> [ "
                )
                if log_try == "N":
                    self.create_account()
                else:
                    is_user = self.login()
                    if not is_user:
                        print(
                            "Sorry! Invalid Credentials! Create new account?\nThank you!!"
                        )
                        exit(1)

        while True:
            res = self.user_response(
                'Enter "Y" to Start \nEnter "N" to Stop -> ['
            ).upper()

            if res == "N":
                break

            job_res = int(
                input(
                    "\n\t\t(Pick)\n1. Show To-do List\n2. Add To-do List\n3. Delete To-do List\n4. Update To-do List\t(Here you will Enter your response) -> ["
                )
            )

            if job_res == 1:
                self.showTodo()
                continue
            elif job_res == 2:
                self.addTodo()
            elif job_res == 3:
                self.removeTodo()
            elif job_res == 4:
                self.updateTodo()

        print("Thank you for visiting...")

    def addTodo(self):
        todo = input("Enter Todo task -> [ ")
        mode = input("Enter task mode (stop, progress, completed) -> [ ")
        self._todo_count += 1
        self.todo_sets.add(
            self._todo_count,
        )
        self.todoList.append({"id": self._todo_count, "todo": todo, "mode": mode})
        print(self.todo_sets)
        print(self.todoList)

    def find_largest_string(self, todos):
        todos["todo"] = str(todos["todo"]).ljust(70)
        return todos["todo"]

    def updateTodo(self):
        print("\n")
        self.showTodo()
        up_idx = int(input("\nPick the column you want to update? -> [ "))
        up_key = input("\n(todo) or (mode) you want to change?  -> [ ")
        up_item = input("\nEnter the Updated data -> [ ")
        self.todoList[up_idx - 1]

    def removeTodo(self):
        self.showTodo()
        r_todo = int(input("\n\nPick the delete todos number -> [ "))
        self.todoList.pop(r_todo)
        print("\nRemove Todo is Successful!\n")
        self.showTodo()

    def showTodo(self):
        print("\n\n\t\t\t\t\t############ TODO LIST ############\n")
        for todos in self.todoList:
            print(
                str(todos["id"])
                + "\t"
                + self.find_largest_string(todos)
                + todos["mode"]
            )


td = Todo(
    {"id": 0, "todo": "Solve 1 leetcode problem, array : easy", "mode": "progress"}
)

# td.addTodo({"id": 2, "todo": "style create-post component", "mode": "progress"})
# td.addTodo(
#     {
#         "id": 3,
#         "todo": "add the element and style it to public the post",
#         "mode": "progress",
#     }
# )
# td.addTodo(
#     {"id": 4, "todo": "Spend time on mdn-doc read about HTML API's", "mode": "progress"}
# )
# td.addTodo("style create-post component")
# td.addTodo("add the element and style it to public the post")
# td.addTodo("Spend time on mdn-doc read about HTML API's")
# td.addTodo("Read 10pages of Discrete mathematics book")

# td.showTodo()

from lib.todo_list import TodoList 
from lib.todo import Todo 

def test_todo_list_initializes():
    todo_list = TodoList()
    todo = Todo("Walk the dog")
    todo_list.add(todo)
    assert todo_list._todos == [todo]

#unit test the incomplete method

def test_incomplete_returns_all_todos_when_none_complete():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Buy the gorceries")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    assert todo_list.incomplete() == [todo_1, todo_2]

def test_give_up_marks_all_todos_complete():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Buy groceries")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.give_up()
    assert todo_1.complete == True
    assert todo_2.complete == True
    assert todo_list.incomplete() == []
    assert todo_list.complete() == [todo_1, todo_2] 


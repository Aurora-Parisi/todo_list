from lib.todo_list import TodoList
from lib.todo import Todo 

def test_todo_list_integration():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Buy groceries")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    assert todo_list.incomplete() == [todo_1, todo_2]
    todo_1.mark_complete()
    #assert incomplete after mark_complete (red phase)
    assert todo_list.incomplete() == [todo_2] 
    assert todo_list.complete() == [todo_1] 
    todo_list.give_up()
    assert todo_list.complete() == [todo_1, todo_2]
    assert todo_list.incomplete() == []


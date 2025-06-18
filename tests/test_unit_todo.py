from lib.todo import Todo
from lib.todo_list import TodoList

def test_todo_initializes_with_the_task_and_incomplete():
    todo = Todo("Walk the dog")
    assert todo.task == "Walk the dog"
    assert todo.complete == False 

#test for the mark_complete

def test_mark_complete_sets_complete_to_true():
    todo = Todo("Walk the dog")
    todo.mark_complete()
    assert todo.complete == True 

def complete_returns_completed_todos():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Buy the groceries")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_1.mark_complete()
    assert todo_list.complete() == [todo_1]
